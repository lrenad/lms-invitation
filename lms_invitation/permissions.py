# lms_invitation/permissions.py

def invitation_code_permission_query(user):
    if "LMS Instructor" in frappe.get_roles(user):
        return f"""
            `tabInvitation Code`.course in (
                select name
                from `tabCourse`
                where owner = '{user}'
            )
        """

    return ""