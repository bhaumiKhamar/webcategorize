# -*- coding: utf-8 -*-
import os
from PyQt4 import QtCore, QtGui
from globals.settings import settings

class Icon(QtGui.QIcon):
    """
        An Icon helper
    """
    def __init__(self, file_name):
        QtGui.QIcon.__init__(self, settings.icons_path().absoluteFilePath(file_name))

# TODO: Banish this! (said nick)
# TODO: seems to work at the moment for pedro.. later maybe this would be ina resource file ?


class Icons:

    Webcategorize = 'arduino.png'

    ## General
    Add = 'add.png'
    Delete = 'delete.png'
    Remove = 'delete.png'
    Cancel = 'bullet_black.png'
    Save = 'accept.png'
    Refresh = 'refresh.gif'

    Up = 'arrow_up.png'
    Down = 'arrow_down.png'

    Green = 'bullet_green.png'
    Blue = 'bullet_blue.png'
    Black = 'bullet_black.png'
    Yellow = 'bullet_yellow.png'
    Pink = 'bullet_ping.png'

    Large = 'bullet_green.png'
    Medium = 'bullet_orange.png'
    Small = 'bullet_purple.png'



    BootLoaderBurn = 'transmit_go.png'
    BootLoaders = 'transmit_blue.png'
    BootLoader = 'transmit.png'

    Board = 'brick.png'
    Boards = 'bricks.png'

    SerialPort = 'joystick.png'

    ## sketch Related
    Projects = 'book_open.png'
    Project = 'page.png'


    ## Compile related
    Upload = 'arrow_up.png'
    Compile = 'arrow_right.png'
    CompileUpload = 'arrow_merge.png'
    CompileError = 'exclamation.png'
    CompileOk = 'accept.png'

    ## Directories
    FileSystemBrowser = 'chart_organisation.png'
    Folder = 'folder.png'
    FolderAdd = 'folder_add.png'
    FolderEdit = 'folder_edit.png'
    FolderDelete = 'folder_delete.png'

    
    # Api and help
    Functions = 'ruby.png'
    Function = 'ruby.png'
    FunctionAdd = 'ruby_add.png'
    FunctionEdit = 'ruby.png'
    FunctionDelete = 'ruby_delete.png'
    FunctionReturn = 'bullet_go.png'
    FunctionParam = 'bullet_green.png'
    FunctionSub = 'bullet_red.png'

    Keyword = 'page_white.png'
    Help = 'help.png'
    HelpDoc = 'page_white.png'
    Html = 'page_white.png'

    Back = 'arrow_left.png'
    Forward = 'arrow_right.png'
    WebPage = 'page_world.png'

    
    

    WriteFile = 'book_next.png'

    Settings = 'cog.png'
    Exit  = 'delete.png'
# XX: Remove this hack once Ico is out of use
Ico = Icons
