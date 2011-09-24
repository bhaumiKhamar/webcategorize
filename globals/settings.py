# -*- coding: utf-8 -*-
import os
from PyQt4 import QtCore
from globals import global_imports

class Settings(QtCore.QObject):

	date_format = "dd-MM-yyyy"
	date_time_format = "dd-MM-yyyy HH:mm"
	opts = None

	def __init__(self):
		QtCore.QObject.__init__(self)
		self.qSettings = QtCore.QSettings("arduino-pyqt", "arduino-pyqt-1")

	#################################################
	## Pass<>Thru for QSettings class
	#################################################
	def value(self, ki, as_string=True):
		v = self.qSettings.value( ki )
		if v.isNull():
			return None
		if as_string:
			return v.toString()
		return v

	def setValue(self, ki, valu ):
		return self.qSettings.setValue( ki, QtCore.QVariant(valu) )

	def remove(self, ki):
		self.qSettings.remove(ki)


	#################################################
	## Window Save/Restore
	#################################################
	def save_window(self, windowName, window):
		self.qSettings.setValue( "window/%s/geometry" % windowName, QtCore.QVariant(window.saveGeometry()) )

	def restore_window(self, windowName, window):
		geo = self.qSettings.value( "window/%s/geometry" % windowName )
		window.restoreGeometry( geo.toByteArray() )


	#########################################################
	## Paths
	#########################################################
	def check_path(self, file_path):
		"""Checks file/path exists or return none"""
		d = QtCore.QFileInfo(file_path)
		if d.exists():
			return file_path
		return None

	def all_paths(self):
		"""Returns all paths as a dict - exlcuding superfilous"""
		ret = []
		ret.append(['Arduino', self.arduino_path()])
		ret.append(['arduino-pyqt', self.app_path()])
		ret.append(['Arduino svn/trunk', self.arduino_svn_path()])
		ret.append(['Help', self.help_path()])
		ret.append(['Examples', self.examples_path()])
		ret.append(['Sketchbooks', self.sketchbooks_path()])
		ret.append(['Hardware', self.hardware_path()])
		ret.append(['API', self.api_def_path()])
		return ret


	## App Path - directory of parent dir
	def app_path(self, cd_to=None):
		path = QtCore.QDir(__file__)
		path.cd('../../')
		if cd_to:
			path.cd(cd_to)
		return path


	## Arduino Path = ARDUINO_DIR in arduino_make.sh
	def arduino_path(self, cd_to=None):
		string_path = self.value("path/arduino_path")
		if not string_path:
			string_path = os.path.join(os.path.dirname(__file__))
		path = QtCore.QDir(string_path)
		if cd_to:
			path.cd(cd_to)
		return path

	## Arduino HTML files
	def html_ref_path(self):
		ard =  self.arduino_path()
		if ard:
			return ard.absoluteFilePath('reference/')
		return None

	## Arduino SVN trunk
	def arduino_svn_path(self, cd_to=None):
		path = QtCore.QDir(self.value("path/arduino_svn_path"))
		if cd_to:
			path.cd(cd_to)
		return path


	## Sketches Path - Path to the sketchbook
	def sketches_path(self, cd_to=None):
		pth = self.value("path/sketchbooks_path")
		if not pth:
			pth = os.path.dirname(__file__)
		path = QtCore.QDir(pth)
		if cd_to:
			path.cd(cd_to)
		return path	

	## API Info Path - directory to yaml
	def api_define_path(self):
		return self.app_path('etc/api_define')

	## Icons Dir
	def icons_path(self):
		return self.app_path('images/icons')
		
	## Aarduino Hardware Dir
	def hardware_path(self):
		return self.arduino_path('hardware')

	## Help HTML files
	def html_pages_path(self):
		return self.app_path('etc/html_pages')

	## Exmaples Dir
	def examples_path(self):
		return self.arduino_path('examples')
	
	def version(self):
		return global_imports.__version__
		

settings = Settings()
