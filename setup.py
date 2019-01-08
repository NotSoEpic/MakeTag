from cx_Freeze import setup, Executable

base = None    

executables = [Executable("maketag.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "maketag",
    options = options,
    version = "1",
    description = 'makes tags',
    executables = executables
)
