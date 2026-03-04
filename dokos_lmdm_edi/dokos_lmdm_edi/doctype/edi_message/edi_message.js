// Copyright (c) 2026, SKwireL and contributors
// For license information, please see license.txt

frappe.ui.form.on('EDI Message', {
	refresh: function(frm) {
		// Add custom button
		if (frm.doc.status === 'Draft') {
			frm.add_custom_button(__('Process Message'), function() {
				frm.set_value('status', 'Processing');
				frm.save();
			});
		}
	},
	
	message_type: function(frm) {
		// Auto-update title when message type changes
		if (frm.doc.message_type && !frm.doc.title) {
			frm.set_value('title', frm.doc.message_type + ' Message');
		}
	}
});
