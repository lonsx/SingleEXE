#SingleEXE
This script is like DLLinZIP.  
When you run py2exe to build Windows executable programs from Python scripts `eg. xyz.py` with `bundle_files=1` & `zipfile=None`,  
and replace the file build\_exe.py in C:\Pyt~ckages\py2exe\ with the one I supply before,  
or just modify the build\_exe.py in `line 847` to:  
~~~~{python}
if self.distribution.zipfile is not None:#add not
            relative_arcname = ""
~~~~
This will Interrupt py2exe building process.  
Then you will get three files in the dist\_dir:  

1. xyz.exe(with the 'PYTHONSCRIPT' mean bundling all into single)
2. library.zip
3. python-dll

Now you can modify the zipfile as you like .  
After that,you can use the script to join the three files into one single exec.  
Just does what py2exe do with bundle\_files=1 and zipfile=None.  
The source code was from build\_exe.py in C:\Python27\Lib\site-packages\py2exe\.  
--------Remember to replace the zipfile&exefile name in arc.py in your case--------  

				********Run with Python\_x86 Installed on win32 with py2exe\_x86**********

##Note:It just work when installing python\_x86 ,py2exe\_x86 on windows x86,because bundle-files 1 not yet supported on win64.  
IMPORTANT:You should replace the file build\_exe.py in C:\Pyt~ckages\py2exe\ with the one I supply,  
before getting the three files (exefile,zipfile,Python27.dll) using py2exe.  
And then,you can run this script to create single-file executables.
