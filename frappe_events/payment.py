import frappe
from frappe.ticketing.doctype.event_booking.event_booking import EventBooking
from payments.utils import get_payment_gateway_controller

def get_payment_gateway_for_event(event: str):
    return frappe.get_cached_value("IS Event", event, "payment_gateway")

def get_controller(payment_gateway):
    return get_payment_gateway_controller(payment_gateway)


def validate_currency(payment_gateway, currency):
    controller = get_controller(payment_gateway)
    controller().validate_transaction_currency(currency)







@frappe.whitelist()
def get_payment_link_for_booking(booking_id:str) -> str:
    booking_doc:"EventBooking"= frappe.get_cached_doc("Event Booking",booking_id)
    payment_gateway = get_payment_gateway_for_event(booking_doc.event)
    event_title = frappe.get_cached_value("IS Event", booking_doc.event, "title")
    user_full_name = frappe.get_cached_value("User", frappe.session.user, "full_name" )

   
    # amount_with_gst = total_amount if total_amount != amount else 0

    payment = record_payment(
        booking_id,
        booking_doc.total_amount,
        booking_doc.currency,
        payment_gateway,
        
       
    )

    controller = get_controller(payment_gateway)


    # TODO
    redirect_to = "/app"


    payment_details = {
        "amount": booking_doc.total_amount,
        "title": f"Payment for {event_title}",
        "description": f"{user_full_name}'s payment for booking #{booking_id}",
        "reference_doctype": "Event Booking",
        "reference_docname": booking_id,
        "payer_email": frappe.session.user,
        "payer_name": user_full_name,
        "currency": booking_doc.currency,
        "payment_gateway": payment_gateway,
        "redirect_to": redirect_to,
        "payment": payment.name,
    }


    if payment_gateway== "razorpay":
        order=controller.create_order(**payment_details)
        payment_details.update({"order_id": order.get("id")})




    url = controller.get_payment_url(**payment_details)

    return url


def record_payment( booking_id: str, amount: float, currency:str, payment_gateway:str|None=None ):
   
    payment_doc = frappe.new_doc("Event Payment")

    payment_doc.update(
        {
            "user": frappe.session.user,
            "amount": amount,
            "currency": currency,
            "reference_doctype": "Event Booking",
            "reference_docname": booking_id,
            "payment_gateway": payment_gateway,
        }
    )

    payment_doc.save(ignore_permissions=True)

    return payment_doc



# def save_address(address):
#     filters = {"email_id": frappe.session.user}
#     exists = frappe.db.exists("Address", filters)

#     if exists:
#         address_doc = frappe.get_last_doc("Address", filters=filters)
#     else:
#         address_doc = frappe.new_doc("Address")

#     address_doc.update(address)

#     address_doc.update(
#         {
#             "address_title": frappe.db.get_value(
#                 "User",
#                 frappe.session.user,
#                 "full_name",
#             ),
#             "address_type": "Billing",
#             "is_primary_address": 1,
#             "email_id": frappe.session.user,
#         }
#     )

#     address_doc.save(ignore_permissions=True)

#     return address_doc.name