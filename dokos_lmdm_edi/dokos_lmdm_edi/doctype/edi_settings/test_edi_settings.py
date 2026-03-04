# Copyright (c) 2026, SKwireL and Contributors
# See license.txt

import frappe
import unittest


class TestEDISettings(unittest.TestCase):
	"""Test case for EDI Settings"""
	
	def setUp(self):
		"""Setup test environment"""
		# Create a test EDI Settings document
		if not frappe.db.exists("EDI Settings", "EDI Settings"):
			doc = frappe.get_doc({
				"doctype": "EDI Settings",
				"babelway_base_api": "https://test-api.babelway.com/v1",
				"enable_logging": 1,
				"log_level": "INFO",
				"retry_count": 3,
				"timeout": 30
			})
			doc.insert()
	
	def test_url_validation(self):
		"""Test that URL validation works"""
		settings = frappe.get_single("EDI Settings")
		
		# Test trailing slash removal
		settings.babelway_base_api = "https://api.babelway.com/v1/"
		settings.validate()
		self.assertEqual(settings.babelway_base_api, "https://api.babelway.com/v1")
		
		# Test invalid URL
		settings.babelway_base_api = "invalid-url"
		with self.assertRaises(frappe.ValidationError):
			settings.validate()
	
	def test_cache_clearing(self):
		"""Test that cache is cleared on update"""
		settings = frappe.get_single("EDI Settings")
		
		# Set cache
		frappe.cache().set_value('edi_settings', {'test': 'value'})
		
		# Update settings
		settings.babelway_base_api = "https://new-api.babelway.com/v1"
		settings.save()
		
		# Check cache is cleared
		cached = frappe.cache().get_value('edi_settings')
		self.assertIsNone(cached)
	
	def tearDown(self):
		"""Cleanup after tests"""
		frappe.db.delete("EDI Settings")
