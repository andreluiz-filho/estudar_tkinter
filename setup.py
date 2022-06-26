from sys import platform
from cx_Freeze import setup, Executable

base = None

if platform == 'win32':
    base = 'Win32Gui'
setup(
    name='tradutor_andre',
    version='1.0',
    description='Tradutor da Livee de Python',
    options={
        'build_exe':{
            'includes': ['tkinter']
        }
    },
    executables=[
        Executable('tradutor.py', base=base)
    ],
)