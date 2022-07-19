from abc import ABC

from base.search import Manager

class BaseClass(ABC):

    objects_list=None
    manager=None

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.add(self)
        self.add_manager()

    @classmethod
    def add(cls,obj):
        if cls.objects_list is None:
            cls.objects_list=list()

        cls.objects_list.append(obj)

    @classmethod
    def add_manager(cls):
        if cls.manager is None:
            cls.manager = Manager(cls)

