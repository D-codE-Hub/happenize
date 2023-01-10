// Copyright (c) 2023, D-codE and contributors
// For license information, please see license.txt

frappe.ui.form.on('Smart Search', {
	
	search: function(frm) {
		frappe.call({
			method: "read_excel",
			doc: frm.doc,
			callback: (r) => {
				frappe.msgprint(r.message)
				$.each(r.message || [], function(i, v){
					var d = frappe.model.add_child(frm.doc, "Smart Search Table", "sales_order");
					d.sales_order = v;
				});
				frm.refresh_field("sales_order");
			}
		});
	}
});
