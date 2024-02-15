class PageObject:
  
    def __init__(self, page):
        self.page = page


class Header(PageObject):

    @property
    def basket(self):
        pass

    def toggle_account_modal(self):
        self.page.get_by_role('button', name='Show/hide account menu').click()


class AccountModal(PageObject):

    @property
    def login_button(self):
        self.page.get_by_role('menuitem', name='Go to login page')

    @property
    def logout_button(self):
        pass


class WelcomeModal(PageObject):

    def dismiss(self):
        self.page.get_by_role('button', name='Close Welcome Banner').click()
