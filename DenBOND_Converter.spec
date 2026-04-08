# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import copy_metadata

datas = [('/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/moviepy', 'moviepy')]
hiddenimports = ['moviepy.editor']
datas += copy_metadata('imageio')
datas += copy_metadata('imageio-ffmpeg')
hiddenimports += collect_submodules('moviepy')


a = Analysis(
    ['DenBOND_Converter.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='DenBOND_Converter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
app = BUNDLE(
    exe,
    name='DenBOND_Converter.app',
    icon=None,
    bundle_identifier=None,
)
