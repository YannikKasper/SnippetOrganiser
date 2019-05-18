# -*- mode: python -*-

block_cipher = None


a = Analysis(['snippetOrganiser.py'],
             pathex=['C:\\Users\\Frozzy\\Desktop\\SnippetOrganiser'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas += [ ('pic.png', '.\\pic.png', 'DATA')]
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='snippetOrganiser',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\Frozzy\\Downloads\\puzzle-piece-silhouette.ico')
