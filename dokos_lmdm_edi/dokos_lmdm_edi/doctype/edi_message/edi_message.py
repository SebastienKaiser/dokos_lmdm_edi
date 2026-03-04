# Copyright (c) 2026, SKwireL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EDIMessage(Document):
	"""EDI Message DocType - Simple test DocType"""
	
	def validate(self):
		"""Validate the EDI Message before saving"""
		if not self.message_type:
			frappe.throw("Message Type is required")
	
	def before_save(self):
		"""Actions before saving"""
		# Auto-generate title if not provided
		if not self.title:
			self.title = f"{self.message_type} - {self.message_id or 'New'}"
