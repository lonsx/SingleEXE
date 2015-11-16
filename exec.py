#!/usr/bin/python
# coding:utf-8

__version__ = '1.0'
__author__ = "wstchql@gmail.com"

import sys
import os
import struct


dirname = os.path.dirname(os.path.abspath(__file__))#make dirname
if dirname.endswith('.zip'):
	dirname = os.path.dirname(dirname)
os.chdir(dirname)#change dir
#os.path.abspath = os.path.dirname + os.path.basename 

python_dll = "python%d%d.dll" % sys.version_info[:2]#define python_dll

arcname = os.path.join(dirname, 'python27.zip')#define zipfile's path
assert os.path.isfile(arcname), u'%s not exists!' % arcname

def ensure_unicode(text):
    if isinstance(text, unicode):
        return text
    return text.decode("mbcs")

from py2exe_util import add_resource

exe_path = os.path.join(dirname, 'python27.exe')
# add the pythondll as resource
# bundle pythonxy.dll
dll_path = os.path.join(dirname, python_dll)
bytes = open(dll_path, "rb").read()
# image, bytes, lpName, lpType

print "Adding %s as resource to %s" % (python_dll, exe_path)
add_resource(ensure_unicode(exe_path), bytes,
             # for some reason, the 3. argument MUST BE UPPER CASE,
             # otherwise the resource will not be found.
             ensure_unicode(python_dll).upper(), 1, False)

zip_data = open(arcname, "rb").read()
open(exe_path, "a+b").write(zip_data)

print "Success!"