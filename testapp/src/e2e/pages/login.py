from .common import PageObject


class Form(PageObject):

    def submit(self):
        self.page.get_by_role('button', name='Login').click()

    def enter_email(self, email):
        self.page.get_by_role('input', name='Text field for the login email').fill(email)

    def enter_password(self, password):
        self.page.get_by_role('input', name='Text field for the login password').fill(password)
