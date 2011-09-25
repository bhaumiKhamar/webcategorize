import sys
import logging
import os
import sqlite3
from xlrd import open_workbook
import optparse
import sys
from string import *
from DB.alchemy import *
from types import *
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtSql
from DB import alchemy

urlDB = None
keywordDB = None

def getUrlDB():
    global urlDB
    # db_filename = 'sqlite_dbs/urls.db'
    db_filename = "urls"
    if (urlDB == None):
        urlDB = Alchemy(db_filename, alchemy.URLBase)
        
    _Session = sessionmaker(bind=urlDB.engine)
    session = _Session()
    urlDB.session = session        
    return urlDB

def getKeywordDB():
    global keywordDB
    # db_filename = 'sqlite_dbs/keywords.db'
    db_filename = "keywords"
    if (keywordDB == None):
        keywordDB = Alchemy(db_filename, alchemy.KeywordBase)

    _Session = sessionmaker(bind=keywordDB.engine)
    session = _Session()
    keywordDB.session = session        
    return keywordDB

def getCrawlerLogDB():
    db_filename = 'sqlite_dbs/crawlerLogs.db'
    return db_filename

def getHTMLParserLogDB():
    db_filename = 'sqlite_dbs/htmlParserLogs.db'
    return db_filename

def assertType(data, expected):
    if (type(data) != expected):
        msg = "Error: %s expected. Given %s" % (expected, type(data))
        raise(msg)
    
__version__ = "1.0"