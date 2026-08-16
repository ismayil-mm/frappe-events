# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document


class ISEvent(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.events.doctype.schedule_item.schedule_item import ScheduleItem
		from frappe.types import DF

		about: DF.TextEditor | None
		banner_image: DF.Attach | None
		category: DF.Link
		end_date: DF.Date
		end_time: DF.Time | None
		external_registration_page: DF.Check
		host: DF.Link
		medium: DF.Literal["In Person", "Online"]
		payment_gateway: DF.Link | None
		registration_url: DF.Data | None
		route: DF.Link | None
		schedules: DF.Table[ScheduleItem]
		short_description: DF.SmallText | None
		start_date: DF.Date
		start_time: DF.Time | None
		time_zone: DF.Autocomplete | None
		title: DF.Data
		venue: DF.Link | None
	# end: auto-generated types

	def validate(self):
		self.validate_route()



	def validate_route(self):
		if not self.route:
			self.route = frappe.website.utils.cleanup_page_name(self.title).replace("_", "-")	

	@frappe.whitelist()
	def check_in(
		self,
		ticket_id: str,
		track: str | None = None
	):
		check_in = frappe.get_doc({
			"doctype": "Event Check In",
			"ticket": ticket_id,
			"track": track
		})

		check_in.insert()
		check_in.submit()

		return check_in.name