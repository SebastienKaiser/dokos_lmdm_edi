import frappe


@frappe.whitelist()
def get_status():
    """Check if EDI app is running"""
    return {
        "status": "ok",
        "version": "1.0.0",
        "message": "EDI Integration App is running"
    }


@frappe.whitelist()
def sync_edi_data():
    """Main EDI synchronization endpoint"""
    # Placeholder for EDI sync logic
    return {
        "status": "success",
        "message": "EDI sync completed",
        "synced": 0
    }


@frappe.whitelist()
def get_edi_settings():
    """Get EDI Settings configuration"""
    if not frappe.db.exists("EDI Settings", "EDI Settings"):
        # Create default settings if they don't exist
        settings = frappe.get_doc({
            "doctype": "EDI Settings",
            "title": "EDI Configuration",
            "status": "Active"
        })
        settings.insert(ignore_permissions=True)
        frappe.db.commit()
    
    settings = frappe.get_doc("EDI Settings", "EDI Settings")
    return settings.as_dict()


@frappe.whitelist()
def update_edi_settings(api_endpoint=None, enable_auto_sync=None, sync_interval=None):
    """Update EDI Settings configuration"""
    frappe.only_for("System Manager")
    
    settings = frappe.get_doc("EDI Settings", "EDI Settings")
    
    if api_endpoint is not None:
        settings.api_endpoint = api_endpoint
    
    if enable_auto_sync is not None:
        settings.enable_auto_sync = int(enable_auto_sync)
    
    if sync_interval is not None:
        settings.sync_interval = int(sync_interval)
    
    settings.save()
    frappe.db.commit()
    
    return {
        "status": "success",
        "message": "EDI Settings updated successfully"
    }
