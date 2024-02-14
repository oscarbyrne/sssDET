from .common import PageObject


class Item(PageObject):

    @property
    def name(self):
        pass

    def add_to_basket(self):
        pass


class List(PageObject):

    @property
    def items(self):
        pass
