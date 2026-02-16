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
