from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class PostBlock(blocks.StructBlock):
    author = blocks.CharBlock(default='Add your author here')
    date_posted = blocks.DateBlock()
    image = ImageChooserBlock(required=False)
    text = blocks.RichTextBlock(default='Add your content here')
    class Meta:
        icon = 'user'
        template = 'blocks/post_block.html'


class TextBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(default='Контент суда')

    class Meta:
        template = 'blocks/text_block.html'

class TextBlock2(blocks.StructBlock):
    text = blocks.RichTextBlock(default='Контент сюда')

    class Meta:
        template = 'blocks/text_block.html'



class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()

    class Meta:
        template = 'blocks/image_block.html'


# class EmbedBlock(blocks.StructBlock):
#     image = blocks.EmbedBlock()

#     class Meta:
#         template = 'home/embed_block.html'


class QuoteBlock(blocks.StructBlock):
    quote = blocks.BlockQuoteBlock()

    class Meta:
        template = 'blocks/quote_block.html'


class CardPostBlock(blocks.StructBlock):
    author = blocks.CharBlock(max_lengrth=100, default='Add you content here')
    date_posted = blocks.DateBlock()

    class Meta:
        template = 'blocks/card_post_block.html'


class LinkBlock(blocks.StructBlock):
    url = blocks.URLBlock()

    class Meta:
        template = 'blocks/url_block.html'