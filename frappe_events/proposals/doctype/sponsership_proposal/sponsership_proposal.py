# Copyright (c) 2026, ismayil and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SponsershipProposal(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		company_logo: DF.AttachImage
		event: DF.Link
		status: DF.Literal["Review", "Pending", "Approve", "Accepted", "Rejected"]
		tier: DF.Link
	# end: auto-generated types

	pass
