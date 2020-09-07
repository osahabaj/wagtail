from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from .blocks import *

class HomePage(Page):

    template = 'home/home_page.html'


class BlogPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title", default='Add you content here')),
        ('cardPost', CardPostBlock()),
        ('image', ImageBlock()),
        ('link', LinkBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]


class PostPage(Page):
    body = StreamField([
        ('Post', PostBlock()),
        ('image', ImageBlock()),
        ('link', LinkBlock()),
        ('text', TextBlock()),
        ('image_list', blocks.ListBlock(blocks.StructBlock([
            ('image', ImageBlock()),
        ]), form_classname='image-list', template='blocks/image_list_block.html'))
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]