from wagtail import blocks
from wagtail.blocks import (
    CharBlock,
    TextBlock,
    StructBlock,
    ListBlock,
    URLBlock
)
# from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock
from wagtail.templatetags.wagtailcore_tags import richtext


class CustomBlock(StructBlock):
    """Cards with image and text and button(s)."""

    # title = CharBlock(required=True, help_text="Add your title")

    cards = ListBlock(
        StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", CharBlock(required=True, max_length=40)),
                ("name", TextBlock(required=True, max_length=200)),
                # ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "whatsApp",
                    URLBlock(
                        required=False,
                        help_text="Enter the link to whatsApp.",  # noqa
                    ),
                ), (
                "instagram",
                URLBlock(
                    required=False,
                    help_text="Enter link to instagram",  # noqa
                ),
            ), (
                "linkedin",
                URLBlock(
                    required=False,
                    help_text="Enter link to linkedin",  # noqa
                ),
            ), (
                "x",
                URLBlock(
                    required=False,
                    help_text="Enter link to x",  # noqa
                ),
            ),
            ]
        )
    )

    # <a href=""><i class="bi bi-twitter-x"></i></a>
    #               <a href=""><i class="bi bi-facebook"></i></a>
    #               <a href=""><i class="bi bi-instagram"></i></a>
    #               <a href=""><i class="bi bi-linkedin"></i></a>

    class Meta:  # noqa
        template = "streams/staff_card.html"
        icon = "placeholder"
        label = "Staff Cards"


class CustomImageBlock(StructBlock):
    """Cards with image and text and button(s)."""

    # title = CharBlock(required=True, help_text="Add your title")

    photos = ListBlock(
        StructBlock(
            [
                ("image", ImageChooserBlock(required=False)),

            ]
        )
    )

    #
    class Meta:  # noqa
        template = "streams/image.html"
        icon = "placeholder"
        label = "Project photo"


class TestimonialBlock(StructBlock):
    """Testimonial with image and text and button(s)."""

    clients_testimony = ListBlock(
        StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", CharBlock(required=True, max_length=40)),
                ("name", TextBlock(required=True, max_length=200)),
                ("testimony", TextBlock(required=True, max_length=200)),

            ]
        )
    )

    # <a href=""><i class="bi bi-twitter-x"></i></a>
    #               <a href=""><i class="bi bi-facebook"></i></a>
    #               <a href=""><i class="bi bi-instagram"></i></a>
    #               <a href=""><i class="bi bi-linkedin"></i></a>

    class Meta:  # noqa
        template = "streams/testimonials.html"
        icon = "placeholder"
        label = "Staff Cards"


class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    def get_api_representation(self, value, context=None):
        return richtext(value.source)

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = " Details"
