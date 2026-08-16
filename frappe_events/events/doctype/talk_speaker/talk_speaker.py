# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TalkSpeaker(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.events.doctype.social_media_link.social_media_link import SocialMediaLink
		from frappe.types import DF

		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		social_media_links: DF.Table[SocialMediaLink]
		speaker: DF.Link
	# end: auto-generated types

	pass
