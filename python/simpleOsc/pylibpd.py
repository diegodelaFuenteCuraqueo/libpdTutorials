# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _pylibpd
else:
    import _pylibpd

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def libpd_clear_search_path():
    return _pylibpd.libpd_clear_search_path()

def libpd_add_to_search_path(path):
    return _pylibpd.libpd_add_to_search_path(path)

def __libpd_openfile(name, dir):
    return _pylibpd.__libpd_openfile(name, dir)

def __libpd_closefile(p):
    return _pylibpd.__libpd_closefile(p)

def __libpd_getdollarzero(p):
    return _pylibpd.__libpd_getdollarzero(p)

def libpd_blocksize():
    return _pylibpd.libpd_blocksize()

def libpd_init_audio(inChannels, outChannels, sampleRate):
    return _pylibpd.libpd_init_audio(inChannels, outChannels, sampleRate)

def libpd_process_float(ticks, inBuffer, outBuffer):
    return _pylibpd.libpd_process_float(ticks, inBuffer, outBuffer)

def libpd_process_short(ticks, inBuffer, outBuffer):
    return _pylibpd.libpd_process_short(ticks, inBuffer, outBuffer)

def libpd_process_double(ticks, inBuffer, outBuffer):
    return _pylibpd.libpd_process_double(ticks, inBuffer, outBuffer)

def libpd_process_raw(inBuffer, outBuffer):
    return _pylibpd.libpd_process_raw(inBuffer, outBuffer)

def libpd_process_raw_short(inBuffer, outBuffer):
    return _pylibpd.libpd_process_raw_short(inBuffer, outBuffer)

def libpd_process_raw_double(inBuffer, outBuffer):
    return _pylibpd.libpd_process_raw_double(inBuffer, outBuffer)

def libpd_arraysize(name):
    return _pylibpd.libpd_arraysize(name)

def libpd_resize_array(name, size):
    return _pylibpd.libpd_resize_array(name, size)

def libpd_read_array(outBuffer, name, offset, n):
    return _pylibpd.libpd_read_array(outBuffer, name, offset, n)

def libpd_write_array(name, offset, inBuffer, n):
    return _pylibpd.libpd_write_array(name, offset, inBuffer, n)

def libpd_bang(recv):
    return _pylibpd.libpd_bang(recv)

def libpd_float(recv, x):
    return _pylibpd.libpd_float(recv, x)

def libpd_symbol(recv, symbol):
    return _pylibpd.libpd_symbol(recv, symbol)

def __libpd_start_message(maxlen):
    return _pylibpd.__libpd_start_message(maxlen)

def __libpd_add_float(x):
    return _pylibpd.__libpd_add_float(x)

def __libpd_add_symbol(symbol):
    return _pylibpd.__libpd_add_symbol(symbol)

def __libpd_finish_list(recv):
    return _pylibpd.__libpd_finish_list(recv)

def __libpd_finish_message(recv, msg):
    return _pylibpd.__libpd_finish_message(recv, msg)

def __libpd_bind(recv):
    return _pylibpd.__libpd_bind(recv)

def __libpd_unbind(p):
    return _pylibpd.__libpd_unbind(p)

def libpd_exists(recv):
    return _pylibpd.libpd_exists(recv)

def libpd_set_print_callback(callback):
    return _pylibpd.libpd_set_print_callback(callback)

def libpd_set_bang_callback(callback):
    return _pylibpd.libpd_set_bang_callback(callback)

def libpd_set_float_callback(callback):
    return _pylibpd.libpd_set_float_callback(callback)

def libpd_set_symbol_callback(callback):
    return _pylibpd.libpd_set_symbol_callback(callback)

def libpd_set_list_callback(callback):
    return _pylibpd.libpd_set_list_callback(callback)

def libpd_set_message_callback(callback):
    return _pylibpd.libpd_set_message_callback(callback)

def libpd_noteon(channel, pitch, velocity):
    return _pylibpd.libpd_noteon(channel, pitch, velocity)

def libpd_controlchange(channel, controller, value):
    return _pylibpd.libpd_controlchange(channel, controller, value)

def libpd_programchange(channel, value):
    return _pylibpd.libpd_programchange(channel, value)

def libpd_pitchbend(channel, value):
    return _pylibpd.libpd_pitchbend(channel, value)

def libpd_aftertouch(channel, value):
    return _pylibpd.libpd_aftertouch(channel, value)

def libpd_polyaftertouch(channel, pitch, value):
    return _pylibpd.libpd_polyaftertouch(channel, pitch, value)

def libpd_midibyte(port, byte):
    return _pylibpd.libpd_midibyte(port, byte)

def libpd_sysex(port, byte):
    return _pylibpd.libpd_sysex(port, byte)

def libpd_sysrealtime(port, byte):
    return _pylibpd.libpd_sysrealtime(port, byte)

def libpd_set_noteon_callback(callback):
    return _pylibpd.libpd_set_noteon_callback(callback)

def libpd_set_controlchange_callback(callback):
    return _pylibpd.libpd_set_controlchange_callback(callback)

def libpd_set_programchange_callback(callback):
    return _pylibpd.libpd_set_programchange_callback(callback)

def libpd_set_pitchbend_callback(callback):
    return _pylibpd.libpd_set_pitchbend_callback(callback)

def libpd_set_aftertouch_callback(callback):
    return _pylibpd.libpd_set_aftertouch_callback(callback)

def libpd_set_polyaftertouch_callback(callback):
    return _pylibpd.libpd_set_polyaftertouch_callback(callback)

def libpd_set_midibyte_callback(callback):
    return _pylibpd.libpd_set_midibyte_callback(callback)

def libpd_start_gui(path):
    return _pylibpd.libpd_start_gui(path)

def libpd_stop_gui():
    return _pylibpd.libpd_stop_gui()

def libpd_poll_gui():
    return _pylibpd.libpd_poll_gui()

def libpd_set_verbose(verbose):
    return _pylibpd.libpd_set_verbose(verbose)

def libpd_get_verbose():
    return _pylibpd.libpd_get_verbose()

import array

def __process_args(args):
  if __libpd_start_message(len(args)): return -2
  for arg in args:
      if isinstance(arg, str):
        __libpd_add_symbol(arg)
      else:
        if isinstance(arg, int) or isinstance(arg, float):
          __libpd_add_float(arg)
        else:
          return -1
  return 0

def libpd_list(recv, *args):
  return __process_args(args) or __libpd_finish_list(recv)

def libpd_message(recv, symbol, *args):
  return __process_args(args) or __libpd_finish_message(recv, symbol)

__libpd_patches = {}

def libpd_open_patch(patchannel, dir = '.'):
  ptr = __libpd_openfile(patchannel, dir)
  if not ptr:
    raise IOError("unable to open patch: %s/%s" % (dir, patch))
  dz = __libpd_getdollarzero(ptr)
  __libpd_patches[dz] = ptr
  return dz

def libpd_close_patch(dz):
  __libpd_closefile(__libpd_patches[dz])
  del __libpd_patches[dz]

__libpd_subscriptions = {}

def libpd_subscribe(recv):
  if recv not in __libpd_subscriptions:
    __libpd_subscriptions[recv] = __libpd_bind(recv)

def libpd_unsubscribe(recv):
  __libpd_unbind(__libpd_subscriptions[recv])
  del __libpd_subscriptions[recv]

def libpd_compute_audio(flag):
  libpd_message('pd', 'dsp', flag)

def libpd_release():
  for p in __libpd_patches.values():
    __libpd_closefile(p)
  __libpd_patches.clear()
  for p in __libpd_subscriptions.values():
    __libpd_unbind(p)
  __libpd_subscriptions.clear()

class PdManager:
  def __init__(self, inChannels, outChannels, sampleRate, ticks):
    self.__ticks = ticks
    self.__outbuf = array.array('b', '\x00\x00'.encode() * outChannels * libpd_blocksize())
    libpd_compute_audio(1)
    libpd_init_audio(inChannels, outChannels, sampleRate)
  def process(self, inBuffer):
    libpd_process_short(self.__ticks, inBuffer, self.__outbuf)
    return self.__outbuf


