// Copyright (c) 2026, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.query_reports["Event Overview"] = {
	filters: [
		{
			"fieldname": "event",
			"label": __("Event"),
			"fieldtype": "Link",
			"options": "IS Event",
			"reqd": 1,
		},
	],
};
