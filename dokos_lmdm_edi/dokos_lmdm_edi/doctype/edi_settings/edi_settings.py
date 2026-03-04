# Copyright (c) 2026, SKwireL and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
import requests


class EDISettings(Document):
	"""EDI Settings - Single DocType for EDI configuration"""
	
	def validate(self):
		"""Validate EDI Settings before saving"""
		self.validate_babelway_url()
	
	def validate_babelway_url(self):
		"""Validate Babelway Base API URL format"""
		if self.babelway_base_api:
			# Remove trailing slash
			self.babelway_base_api = self.babelway_base_api.rstrip('/')
			
			# Check if it's a valid URL
			if not self.babelway_base_api.startswith(('http://', 'https://')):
				frappe.throw(_("Babelway Base API URL must start with http:// or https://"))
	
	def on_update(self):
		"""Actions after saving settings"""
		# Clear cache when settings are updated
		frappe.cache().delete_value('edi_settings')
		frappe.msgprint(_("EDI Settings updated successfully"), alert=True)


@frappe.whitelist()
def test_babelway_connection():
	"""Test connection to Babelway API"""
	settings = frappe.get_single("EDI Settings")
	
	if not settings.babelway_base_api:
		frappe.throw(_("Please configure Babelway Base API URL first"))
	
	try:
		# Try to ping a common health endpoint (adjust based on Babelway API)
		url = f"{settings.babelway_base_api}/health"
		headers = {}
		
		if settings.babelway_api_key:
			headers["Authorization"] = f"Bearer {settings.get_password('babelway_api_key')}"
		
		timeout = settings.timeout or 30
		
		response = requests.get(url, headers=headers, timeout=timeout)
		
		if response.status_code == 200:
			frappe.msgprint(
				_("Connection to Babelway API successful!"),
				title=_("Success"),
				indicator="green"
			)
		else:
			frappe.msgprint(
				_("Connection failed. Status code: {0}").format(response.status_code),
				title=_("Connection Error"),
				indicator="orange"
			)
	
	except requests.exceptions.Timeout:
		frappe.throw(_("Connection timeout. Please check your timeout settings."))
	except requests.exceptions.ConnectionError:
		frappe.throw(_("Could not connect to Babelway API. Please check the URL."))
	except Exception as e:
		frappe.throw(_("Error testing connection: {0}").format(str(e)))


@frappe.whitelist()
def get_edi_settings():
	"""Get EDI Settings (cached)"""
	cached = frappe.cache().get_value('edi_settings')
	
	if cached:
		return cached
	
	settings = frappe.get_single("EDI Settings")
	settings_dict = settings.as_dict()
	
	# Don't cache the password
	if 'babelway_api_key' in settings_dict:
		settings_dict.pop('babelway_api_key')
	
	frappe.cache().set_value('edi_settings', settings_dict, expires_in_sec=300)  # 5 min cache
	
	return settings_dict
