import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import nowdate
import secrets


class InvitationCode(Document):

    def before_insert(self):
        self.generate_code()
        self.validate_valid_until()

    def generate_code(self):
        if not self.code:
            self.code = secrets.token_hex(4).upper()

    def validate_valid_until(self):
        if self.valid_until and self.valid_until < nowdate():
            frappe.throw(
                _("Valid Until cannot be in the past.")
            )