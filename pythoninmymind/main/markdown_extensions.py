import markdown
import re
from django.urls import reverse
from markdown.inlinepatterns import LinkInlineProcessor, LINK_RE, ImageInlineProcessor, IMAGE_LINK_RE
from markdown.extensions.tables import TableProcessor
import xml.etree.ElementTree as etree
from typing import Sequence



class SlugFieldLinkInlineProcessor(LinkInlineProcessor):
    def getLink(self, data, index):
        href, title, index, handled = super().getLink(data, index)
        if href.startswith("slug"):
            slug = href.split(":")[1]
            relative_url = reverse("article", args=[slug])
            href = relative_url
        return href, title, index, handled

class SlugFieldExtension(markdown.Extension):
    def extendMarkdown(self, md, *args, **kwargs):
        md.inlinePatterns.register(
            SlugFieldLinkInlineProcessor(LINK_RE, md), "link", 160
        )


class ImgStyleProcessor(ImageInlineProcessor):
    def handleMatch(self, m, data):
        text, index, handled = self.getText(data, m.end(0))    
        if not handled:
            return None, None, None

        src, title, index, handled = self.getLink(data, index)
        if not handled:
            return None, None, None

        el = etree.Element("img")

        el.set("src", src)
        el.set("class", "img-fluid")

        if title is not None:
            el.set("title", title)

        el.set('alt', self.unescape(text))

        return el, m.start(0), index
    

class ImgStyleExtension(markdown.Extension):
    def extendMarkdown(self, md, *args, **kwargs):
        md.inlinePatterns.register(
            ImgStyleProcessor(IMAGE_LINK_RE, md), "image-style", 160
        )
    

class TablesProcessor(TableProcessor):
    def _build_row(self, row: str, parent: etree.Element, align: Sequence[str | None]) -> None:
            tr = etree.SubElement(parent, 'tr')
            tag = 'td'
            if parent.tag == 'thead':
                tag = 'th'
            cells = self._split_row(row)

            for i, a in enumerate(align):
                c = etree.SubElement(tr, tag)
                if tag == 'th':
                    c.set("class", "col")
                    
                try:
                    c.text = cells[i].strip(' ')
                except IndexError: 
                    c.text = ""
                if a:
                    if self.config['use_align_attribute']:
                        c.set('align', a)
                    else:
                        c.set('style', f'text-align: {a};')


    def run(self, parent: etree.Element, blocks: list[str]) -> None:
        block = blocks.pop(0).split('\n')
        header = block[0].strip(' ')
        rows = [] if len(block) < 3 else block[2:]

        align: list[str | None] = []
        for c in self.separator:
            c = c.strip(' ')
            if c.startswith(':') and c.endswith(':'):
                align.append('center')
            elif c.startswith(':'):
                align.append('left')
            elif c.endswith(':'):
                align.append('right')
            else:
                align.append(None)

        div = etree.SubElement(parent, 'div')
        div.set("class", "overflow-x-auto")
        table = etree.SubElement(div, 'table')
        table.set("class", "table")
        thead = etree.SubElement(table, 'thead')
        self._build_row(header, thead, align)
        tbody = etree.SubElement(table, 'tbody')
        if len(rows) == 0:
            self._build_empty_row(tbody, align)
        else:
            for row in rows:
                self._build_row(row.strip(' '), tbody, align)

class TablesExtension(markdown.Extension):
    def extendMarkdown(self, md):
        if '|' not in md.ESCAPED_CHARS:
            md.ESCAPED_CHARS.append('|')
        processor = TablesProcessor(md.parser, self.getConfigs())
        md.parser.blockprocessors.register(processor, 'table', 75)