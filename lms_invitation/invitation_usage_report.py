import frappe

def execute(filters=None):
    columns = [
        {"label": "Course", "fieldname": "course", "fieldtype": "Link", "options": "Course"},
        {"label": "Total Invitation Codes", "fieldname": "total", "fieldtype": "Int"},
        {"label": "Available Codes", "fieldname": "available", "fieldtype": "Int"},
        {"label": "Used Codes", "fieldname": "used", "fieldtype": "Int"},
        {"label": "Expired Codes", "fieldname": "expired", "fieldtype": "Int"},
    ]

    data = frappe.db.sql("""
        SELECT
            course,
            COUNT(*) as total,
            SUM(status='Available') as available,
            SUM(status='Used') as used,
            SUM(status='Expired') as expired
        FROM `tabInvitation Code`
        GROUP BY course
    """, as_dict=True)

    return columns, data