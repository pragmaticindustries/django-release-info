from django.conf import settings
import markdown
import os

from django.views.generic import TemplateView

from xml.etree.ElementTree import Element, SubElement
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

class CollapsibleSectionProcessor(Treeprocessor):
    def run(self, root):
        new_root = Element("div")
        current_tbody = None

        def extract_text(element):
            text = element.text if element.text else ""
            for child in list(element):
                text += extract_text(child)
            return text

        for element in list(root):
            # Version
            if element.tag == "h1":
                if current_tbody is not None:
                    new_root.append(current_tbody)
                current_tbody = Element("tbody")

                # Erstelle die zusammenklappbare Reihe
                tr_summary = SubElement(
                    current_tbody, "tr", {"class": "expandable-row"}
                )
                td_date = SubElement(tr_summary, "td")
                td_version = SubElement(tr_summary, "td")
                td_version.text = element.text.strip()  # Version

                # Erstelle die versteckte Detail-Reihe
                tr_hidden = SubElement(
                    current_tbody, "tr", {"class": "hidden detail-row"}
                )
                td_hidden = SubElement(tr_hidden, "td", {"colspan": "3"})
                detail_div = SubElement(td_hidden, "div")

            # Date
            elif element.tag == "blockquote":
                if current_tbody is not None:
                    date_text = extract_text(element)
                    td_date = current_tbody.find(".//td")
                    if td_date.text:
                        td_date.text += f"\n{date_text}"
                    else:
                        td_date.text = date_text

            # List
            elif element.tag == "ul" or element.tag == "ol":
                list_tag = SubElement(detail_div, element.tag)
                for list_item in element:
                    if list_item.tag == "li":
                        list_item_tag = SubElement(list_tag, "li")
                        list_item_tag.text = list_item.text.strip()

            # Everything else
            else:
                if current_tbody is not None and element.text:
                    detail_div = current_tbody.find(".//div")
                    if detail_div is not None:
                        detail_div.text = f"{element.text.strip()}"

        if current_tbody is not None:
            new_root.append(current_tbody)

        root.clear()
        for child in new_root:
            root.append(child)


class CustomHeaderExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(
            CollapsibleSectionProcessor(md), "collapsible_section", 10
        )


class ReleaseView(TemplateView):
    template_name = "release_info/release.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        # Get version and release date from env
        context_data["version"] = os.environ.get("VERSION", "0.0.0")
        context_data["release_date"] = os.environ.get("RELEASE_DATE", "01.01.1970")
        context_data["info"] = settings.RELEASE_INFO

        # Load changelog.md and put rendered markdown into context
        with open("CHANGELOG.md", "r", encoding="utf-8") as changelog:
            context_data["changelog"] = markdown.markdown(
                changelog.read(), extensions=[CustomHeaderExtension()]
            )

        return context_data
