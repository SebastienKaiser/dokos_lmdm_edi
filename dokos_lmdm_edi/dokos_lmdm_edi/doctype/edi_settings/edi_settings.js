// Copyright (c) 2026, SKwireL and contributors
// For license information, please see license.txt

frappe.ui.form.on('EDI Settings', {
	refresh: function(frm) {
		// Add Test Connection button
		frm.add_custom_button(__('Test Babelway Connection'), function() {
			frappe.call({
				method: 'dokos_lmdm_edi.dokos_lmdm_edi.doctype.edi_settings.edi_settings.test_babelway_connection',
				callback: function(r) {
					frm.reload_doc();
				}
			});
		}, __('Actions'));
		
		// Add icon for visual feedback
		if (frm.doc.babelway_base_api) {
			frm.set_df_property('babelway_base_api', 'description', 
				'<i class="fa fa-check-circle text-success"></i> API URL configured');
		}
	},
	
	babelway_base_api: function(frm) {
		// Auto-format URL (remove trailing slash)
		if (frm.doc.babelway_base_api) {
			frm.set_value('babelway_base_api', frm.doc.babelway_base_api.trim().replace(/\/$/, ''));
		}
	},
	
	babelway_test_connection: function(frm) {
		// Trigger test connection when button clicked
		frappe.call({
			method: 'dokos_lmdm_edi.dokos_lmdm_edi.doctype.edi_settings.edi_settings.test_babelway_connection',
			callback: function(r) {
				frm.reload_doc();
			}
		});
	}
});
