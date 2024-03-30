import markdown
import re
from django.urls import reverse
from markdown.inlinepatterns import LinkInlineProcessor, LINK_RE, ImageInlineProcessor, IMAGE_LINK_RE 
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import xml.etree.ElementTree as etree



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
    
