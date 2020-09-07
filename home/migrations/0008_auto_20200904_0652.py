# Generated by Django 3.1.1 on 2020-09-04 06:52

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200904_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpage',
            name='body',
            field=wagtail.core.fields.StreamField([('Post', wagtail.core.blocks.StructBlock([('author', wagtail.core.blocks.CharBlock(default='Add your author here')), ('date_posted', wagtail.core.blocks.DateBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(default='Add your content here'))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('link', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock())])), ('text', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(default='Контент суда'))])), ('image_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock())]))]), form_classname='image-list'))]),
        ),
    ]
