import ctypes
import os
from datetime import time

_file = 'adder.so';

_path = os.path.join(*(os.path.split(__file__)[:-1] + (_file,)))

# _mod = ctypes.cdll.LoadLibrary(_path)

# _add = _mod.add_int
# _add.argtypes = (ctypes.c_int, ctypes.c_int)
# _add.restype = ctypes.c_int
# print(_add(1,2))

# print(os.path.join(*(os.path.split(__file__)[:-1] + (_file,))));

_file2 = 'libuart.so'
_path = os.path.join(*(os.path.split(__file__)[:-1] + (_file2,)))

_mod = ctypes.cdll.LoadLibrary(_path)
_openFile = _mod.OpenFile
_openFile.argtypes = (ctypes.c_ubyte)
_openFile.restype = ctypes.c_int

_send = _mod.Send
_send.argtypes = (ctypes.c_int, ctypes.c_char, ctypes.c_uint)

_receive = _mod.Receive
_receive.argtypes = (ctypes.c_int, ctypes.c_char, ctypes.c_uint)

_close = _mod.close_uart
_close.argtypes = (ctypes.c_int)

# print(__file__)
# print(os.path.split(__file__)[:-1])

if __name__ == '__main__':
    count = 1
    fd = _openFile(3)
    while True:
        _send(fd, "s", 4)
        time.sleep(1)
        if count == 10:
            break
        count += 1
    _close(fd)