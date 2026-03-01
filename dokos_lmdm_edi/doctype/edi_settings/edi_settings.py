# Copyright (c) 2026, Your Company and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EDISettings(Document):
	"""EDI Settings DocType for EDI Integration configuration"""
	
	def validate(self):
		"""Validate EDI Settings"""
		# Validate API endpoint format if provided
		if self.api_endpoint:
			if not (self.api_endpoint.startswith('http://') or self.api_endpoint.startswith('https://')):
				frappe.throw("API Endpoint must start with http:// or https://")
		
		# Validate sync interval
		if self.enable_auto_sync and self.sync_interval < 1:
			frappe.throw("Sync Interval must be at least 1 minute")
