from abc import ABC
from manager import Manager

class BaseClass(ABC):

    objects_list=None
    manager=None

    def __init__(self):
        self.add(self)


    @classmethod
    def add(cls,obj):
        if cls.objects_list is None:
            cls.objects_list=list()

        cls.objects_list.append(obj)

    @classmethod
    def add_manager(cls):
        if cls.manager is None:
            cls.manager=Manager(cls)

