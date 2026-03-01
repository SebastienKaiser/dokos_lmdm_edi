"""
Frappe hooks for EDI Integration App
"""

app_name = "dokos_lmdm_edi"
app_title = "EDI Integration (LMDM)"
app_publisher = "Your Company"
app_description = "EDI data synchronization and integration with external systems"
app_icon = "octicon octicon-sync"
app_color = "#FF6B6B"
app_email = "your@email.com"
app_license = "MIT"
app_version = "1.0.0"

# Requires
required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = []
app_include_js = []

# include js, css files in header of web template
web_include_css = []
web_include_js = []

# include custom scss in every page
# app_include_scss = "edi/public/scss/index.scss"

# Includes in <body>
# ---------------------

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}

# include js in form
# form_js = {"doctype" : "public/js/form.js"}

# provide settings in customize form
# customize_form = {"doctype": "settings", "fieldname": "custom_settings", "template": "form"}

# ET Events
# ----------

# Trigger on document events
# doc_events = {
# 	"*": {
# 		"on_update": "edi.event_handlers.on_update"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"cron": {
# 		"0/15 * * * *": [
# 			"edi.tasks.sync_edi_data"
# 		]
# 	},
# 	"daily": [
# 		"edi.tasks.daily_sync"
# 	]
# }

# Fixtures (auto-install)
# ----------

# fixtures = ["Custom Field"]

# Migrate
# -------

# migrate_from_version changes
# migrate_from_version = "0.0.1"

# before_migrate,after_migrate

# Testing
# -------

# before_tests deprecated_function in tests/__init__.py

# Website
# -------

# auto_route = False

# webpage_route_rules = [
# 	{
# 		"from_route": "/blog/<blog_post_name>",
# 		"to_route": "Blog Post/<blog_post_name>"
# 	}
# ]

# Workspace
# ---------

# Custom workspaces
has_website_permission = {}

# On desk page trigger
on_session_creation = []

# Export to users
export_python_type_annotations = True

# Workspaces (for Desk sidebar navigation)
# Automatically loaded from workspace/ directory

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"edi.auth.validate"
# ]

# Translation
# -----------

# After translation, the app/locale folder should have a list of all
# pages, doctype, reports etc. for which a translation(_) function was called.
# OR use babel with edi/public/js as input
