from .common import PageObject


class Form(PageObject):

    @property
    def submit_button(self):
        self.page.get_by_role('button', name='Login')

    def enter_email(self, email):
        self.page.get_by_role('input', name='Text field for the login email').fill(email)

    def enter_password(self, password):
        self.page.get_by_role('input', name='Text field for the login password').fill(password)
