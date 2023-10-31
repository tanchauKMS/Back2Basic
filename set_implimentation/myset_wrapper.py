# myset_wrapper.py
import ctypes

class MySet:
    def __init__(self):
        self.myset = ctypes.CDLL('./myset.so')

        self.myset.create_set.restype = ctypes.POINTER(ctypes.c_void_p)
        self.myset.handle_duplicate.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
        self.myset.destroy_set.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
        self.myset.get_size.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
        self.myset.get_size.restype = ctypes.c_int
        self.myset.get_values.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
        self.myset.get_values.restype = ctypes.POINTER(ctypes.c_char_p)
        self.myset.add.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_char_p]
        self.myset.add.restype = ctypes.POINTER(ctypes.c_void_p)

        self.set_ptr = self.myset.create_set()

    def __del__(self):
        self.myset.destroy_set(self.set_ptr)

    def handle_duplicate(self):
        self.myset.handle_duplicate(self.set_ptr)

    def get_size(self):
        return self.myset.get_size(self.set_ptr)

    def get_values(self):
        values_ptr = self.myset.get_values(self.set_ptr)
        values = []
        i = 0
        while values_ptr[i]:
            values.append(values_ptr[i].decode())
            i += 1
        return values

    def add(self, value):
        self.myset.add(self.set_ptr, value.encode())
        self.handle_duplicate()