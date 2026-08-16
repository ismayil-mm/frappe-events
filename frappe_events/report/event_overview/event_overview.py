# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = get_data(filters)

	return columns, data


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Event"),
			"fieldname": "event",
			"fieldtype": "Link",
			"options":"IS Event",
			"width": 200
		},
		{
			"label": _("Number of Tickets Sold"),
			"fieldname": "num_tickets_sold",
			"fieldtype": "Int",
				},
		{
			"label": _("Number of Add Ons Sold"),
			"fieldname": "num_add_ons_sold",
			"fieldtype": "Int",
		},
		{
			"label": _("Ticket Sales"),
			"fieldname": "sales",
			"fieldtype": "currency",
				},
	]


def get_data(filters: dict) -> list[dict]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""

	event= filters.get("event")

	if event:
		return [get_summary_for_event(event)]


	data=[]
	events = frappe.db.get_all("IS Event",  pluck= "name")
	for event in events:
		summary = get_summary_for_event(event)
		summary["event"]= event
		data.append(summary)


	return data



def get_summary_for_event (event:str) -> dict:
	"""return summary data for event

	this function is used to get a summary for the event, such as total ticket sold,
	total add-ons sold, total sales
	
	"""

	event_tickets= frappe.db.get_all("Event Ticket", filters={"event": event,"docstatus":1 },pluck= "name")

	num_tickets_sold = len(event_tickets)
	sales_result=  frappe.db.get_all(
		"Event Booking",
		filters={"event": event, "docstatus": 1},
		fields=[{"SUM": "total_amount", "as": "sales"}],
	)
	sales =  sales_result[0]["sales"] if sales_result else 0
	
	num_add_ons_sold = frappe.db.get_all("Ticket Add-on Value", filters= { 
			"parenttype": "Event Ticket",
			"parentfield":"add_ons" ,
			"parent":["in", event_tickets]}, 
			  fields=[{"COUNT": "*", "as": "num_add_ons_sold"}])[0]["num_add_ons_sold"] or 0
	
	
	return {"event":event,"num_tickets_sold": num_tickets_sold,"num_add_ons_sold":num_add_ons_sold, "sales":sales}
			
		
	


