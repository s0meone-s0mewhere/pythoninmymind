import markdown
from main.markdown_extensions import SlugFieldExtension, ImgStyleExtension, TablesExtension
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
@stringfilter
def render_markdown(value):
    md = markdown.Markdown(extensions=["fenced_code", SlugFieldExtension(), ImgStyleExtension(), TablesExtension(),])
    return mark_safe(md.convert(value))