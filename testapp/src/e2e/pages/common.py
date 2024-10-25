class PageObject:
  
    def __init__(self, page):
        self.page = page


class Header(PageObject):

    def view_basket(self):
        pass

    def toggle_account_modal(self):
        self.page.get_by_role('button', name='Show/hide account menu').click()


class AccountModal(PageObject):

    def login(self):
        self.page.get_by_role('menuitem', name='Go to login page').click()

    def logout(self):
        pass


class WelcomeModal(PageObject):

    def dismiss(self):
        self.page.get_by_role('button', name='Close Welcome Banner').click()
