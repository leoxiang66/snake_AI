from setuptools import setup

APP = ['snake_human.py']
DATA_FILES = [
    ('', ['snake.png']),
    ('', ['berry.png']),
    ('', ['wall.png']),
    ('', ['map.txt'])
]
OPTIONS = {
    'argv_emulation': False,
    # 'iconfile': 'icon.icns',
    'plist': {
        'CFBundleShortVersionString': '0.1.0',
        'CFBundleVersion': '0.1.0'
    },

    
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)


