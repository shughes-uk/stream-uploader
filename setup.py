from distutils.core import setup
import py2exe

setup(console=['streamuploader.py'],
	zipfile = None,
	options = {
	'py2exe': {
	'includes': ['BaseHTTPServer'],
	'bundle_files' : 1,
	'compressed': True,
	}
	})