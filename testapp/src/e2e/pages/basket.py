from .common import PageObject


class Item(PageObject):

    @property
    def name(self):
        pass

    def delete(self):
        pass


class List(PageObject):

    @property
    def items(self):
        pass
