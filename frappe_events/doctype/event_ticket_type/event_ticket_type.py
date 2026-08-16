# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class EventTicketType(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		auto_unpublished_after: DF.Date | None
		currency: DF.Link
		event: DF.Link
		max_tickets: DF.Int
		name: DF.Int | None
		price: DF.Currency
		published: DF.Check
		title: DF.Data
	# end: auto-generated types

	pass
