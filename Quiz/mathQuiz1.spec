# -*- mode: python -*-

block_cipher = None


a = Analysis(['mathQuiz1.py'],
             pathex=['D:\\01_Paul\\00_Projcets\\PythonLearning\\mathQuiz'],
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
          name='mathQuiz1',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
