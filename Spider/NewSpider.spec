# -*- mode: python -*-

block_cipher = None


a = Analysis(['E:\\�����ļ�\\Python\\Spider01\\Spider\\NewSpider.py'],
             pathex=['E:\\�����ļ�\\Python\\Spider01\\Spider'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='NewSpider',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='E:\\�����ļ�\\Python\\Spider01\\1.ico')
