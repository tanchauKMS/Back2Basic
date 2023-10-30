# mydict_wrapper.py
import ctypes

class MyDict:
    def __init__(self):
        self.mydict = ctypes.CDLL('./mydictionary.so')

        self.mydict.create_dict.restype = ctypes.POINTER(ctypes.c_void_p)
        self.mydict.destroy_dict.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
        self.mydict.get_size.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
        self.mydict.get_size.restype = ctypes.c_int
        self.mydict.get_value.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p]
        self.mydict.get_value.restype = ctypes.c_int
        self.mydict.set_value.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p, ctypes.c_int]

        self.dict_ptr = self.mydict.create_dict()

    def __del__(self):
        self.mydict.destroy_dict(self.dict_ptr)

    def get_size(self):
        return self.mydict.get_size(self.dict_ptr)

    def get_value(self, key):
        return self.mydict.get_value(self.dict_ptr, key.encode())

    def set_value(self, key, value):
        self.mydict.set_value(self.dict_ptr, key.encode(), value)