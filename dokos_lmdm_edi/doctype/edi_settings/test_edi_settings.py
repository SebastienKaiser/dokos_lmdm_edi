# Copyright (c) 2026, Your Company and Contributors
# See license.txt

import frappe
import unittest


class TestEDISettings(unittest.TestCase):
	"""Test EDI Settings"""
	
	def test_api_endpoint_validation(self):
		"""Test API endpoint must start with http:// or https://"""
		settings = frappe.get_doc({
			"doctype": "EDI Settings",
			"api_endpoint": "invalid-url"
		})
		
		with self.assertRaises(frappe.ValidationError):
			settings.validate()
	
	def test_sync_interval_validation(self):
		"""Test sync interval must be at least 1 minute"""
		settings = frappe.get_doc({
			"doctype": "EDI Settings",
			"enable_auto_sync": 1,
			"sync_interval": 0
		})
		
		with self.assertRaises(frappe.ValidationError):
			settings.validate()
