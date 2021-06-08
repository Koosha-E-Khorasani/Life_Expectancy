import abc


class FileReader:
    def __init__(self, address, name="-"):
        self._name = name
        self._address = address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name
    @property
    def address(self):
        return self._address
    @address.setter
    def address(self,ad):
        self._address = ad
    @abc.abstractmethod
    def read_data(self):
        return
