# mylist_wrapper.py
import ctypes

class MyList:
    def __init__(self):
        self.mylist = ctypes.CDLL('./mylist.so')

        self.mylist.create_list.restype = ctypes.POINTER(ctypes.c_void_p)
        self.mylist.destroy_list.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
        self.mylist.get_length.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
        self.mylist.get_length.restype = ctypes.c_int
        self.mylist.get_item.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_int]
        self.mylist.get_item.restype = ctypes.c_int
        self.mylist.append_item.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_int]

        self.list_ptr = self.mylist.create_list()

    def __del__(self):
        self.mylist.destroy_list(self.list_ptr)

    def get_length(self):
        return self.mylist.get_length(self.list_ptr)

    def get_item(self, index):
        return self.mylist.get_item(self.list_ptr, index)

    def append_item(self, item):
        self.mylist.append_item(self.list_ptr, item)