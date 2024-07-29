from wagtail.blocks import (
    CharBlock,
    TextBlock,
    StructBlock,
    ListBlock,
    URLBlock
)
# from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock


class CardBlock(StructBlock):
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
                    "facebook",
                    URLBlock(
                        required=False,
                        help_text="Enter the link to facebook.",  # noqa
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


        
