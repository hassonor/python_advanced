import abc

class Immutable(abc.ABC):
    __slots__ = ('__attrs__',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__attrs__ = frozenset()

    def __setattr__(self, name, value):
        if name == '__attrs__':
            super().__setattr__(name, value)
            return

        if name in self.__attrs__:
            raise AttributeError(f"Attempt to modify immutable attribute \'{name}\'")
        else:
            super().__setattr__(name, value)
            self.__attrs__ |= {name}

    def __delattr__(self, name):
        if name in self.__attrs__:
            raise AttributeError(f"Attempt to delete immutable attribute \'{name}\'")
        else:
            raise AttributeError(name)
