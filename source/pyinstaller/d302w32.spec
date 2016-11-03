# -*- mode: python -*-

block_cipher = None


a = Analysis(['..\\d302.py'],
             pathex=['pyinstaller'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=True,
             win_private_assemblies=True,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='d302w32',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='d302.ico')
