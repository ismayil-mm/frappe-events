// Copyright (c) 2026, Frappe Technologies and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Attendee Ticket Add-on", {
// 	refresh(frm) {

// 	},
// });




frappe.ui.form.on('Ticket Add-on Value', {
    add_on(frm, cdt, cdn) {
        const doc = frappe.get_doc(cdt, cdn);

        frappe.db.get_value("Ticket Add-on", doc.add_on, "options")
            .then(({ message }) => {
                if (message && message.options) {
                    const options = message.options.trim().split("\n");

                    const grid = frm.fields_dict.add_ons.grid;
                    const row = grid.grid_rows_by_docname[cdn];

                    row.on_grid_fields_dict.value.set_data(options);
                }
            });
    }
});