frappe.ui.form.on("IS Event", {
    refresh(frm) {

        frappe.call("frappe.geo.country_info.get_country_timezone_info").then(({ message }) => {
            frm.fields_dict.time_zone.set_data(message.all_timezones);
        });

        const button_label = frm.doc.is_published ? __("Unpublished") : __("Publish");

        frm.add_custom_button(button_label, () => {
            frm.set_value("is_published", !frm.doc.is_published);
            frm.save();
        });


        // frm.set_query("track", "schedules", (doc, cdt,cdn)=>{
        //     console.log(doc.name);
        //     return{
        //         filters:{
        //             event :doc.name
        //         }
        //     }
        // })

        




        frm.add_custom_button(__("Start Check In"), () => {

            frappe.prompt(
                [
                    {
                        label: "Track",
                        fieldname: "track",
                        fieldtype: "Link",
                        options: "Event Track",
                    }
                ],
                (values) => {

                    const track = values.track;

                    new frappe.ui.Scanner({
                        dialog: true,
                        multiple: false,

                        on_scan(data) {

                            const ticket_id = data.decodedText;

                            frm.call("check_in", {
                                ticket_id,
                                track
                            }).then(() => {
                                frappe.show_alert(__("Check In Complete!"));
                                frm.refresh();
                            });

                        }
                    });

                }
            );

        });

    }
});