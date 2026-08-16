import frappe


@frappe.whitelist(allow_guest=True)
def test_connection():
    return {
        "success": True,
        "message": "Frontend connected to Frappe!",
        "user": frappe.session.user,
    }


@frappe.whitelist(allow_guest=True)
def get_events():
    events = frappe.get_all(
        "IS Event",
        fields=[
            "name",
            "title",
            "description",
            "start_date",
            "end_date",
            "time_zone",
            "is_published",
        ],
    )

    return events