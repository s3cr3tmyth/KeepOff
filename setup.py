from setuptools import setup

APP = ['keepOffMacApp.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon',
    'plist': {
        'CFBundleShortVersionString': '0.1.0',
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    name='KeepOff',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps']
)
