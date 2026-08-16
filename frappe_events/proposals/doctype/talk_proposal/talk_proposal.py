# Copyright (c) 2026, ismayil and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TalkProposal(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe_events.proposals.doctype.proposal_speaker.proposal_speaker import ProposalSpeaker
		from frappe.types import DF

		event: DF.Link
		speakers: DF.Table[ProposalSpeaker]
		status: DF.Literal["Review Pending", "Approved", "Rejected", "Short Listed"]
		submitted_by: DF.Link | None
		talk_description: DF.TextEditor | None
		title: DF.Data
	# end: auto-generated types

	pass
