from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, TEXT, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, backref

from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

KeywordBase = declarative_base()
URLBase = declarative_base()

class Alchemy:
    def __init__(self, filename, base, username="", password=""):
        self.filename = filename
        self.username = username
        self.password = password
        # self.engine = create_engine(('sqlite:///%s' % (filename)))
        self.engine = create_engine('mysql+mysqldb://root:blastoff@localhost/%s' % filename, pool_recycle=3600)
        self._Session = sessionmaker(bind=self.engine)
        self.session = self._Session()
        self.base = base
        
    def createTable(self):
        print "Creating Table"
        self.base.metadata.create_all(self.engine)
        
class ServiceLine(KeywordBase):
    __tablename__ = 'ServiceLine'
    
    id = Column(Integer, primary_key=True, nullable=False)
    serviceLine1 = Column(VARCHAR(255), nullable=False)
    serviceLine2 = Column(VARCHAR(255), nullable=False)
    serviceLine3 = Column(VARCHAR(255), nullable=False)
        
    def __init__(self, serviceLine1, serviceLine2, serviceLine3):
        self.serviceLine1 = serviceLine1
        self.serviceLine2 = serviceLine2
        self.serviceLine3 = serviceLine3

    @staticmethod
    def tableName():
        return ServiceLine.__tablename__

    def __repr__(self):
        return  "<Service Line: (%i,%s, %s, %s)>" % (self.id, self.serviceLine1, self.serviceLine2, self.serviceLine3)

class KeywordTable(KeywordBase):
    __tablename__ = 'KeywordTable'    
    
    id = Column(Integer, primary_key=True, nullable=False)
    keyword = Column(VARCHAR(255), nullable=False)
    serviceLine_index = Column(Integer, ForeignKey('ServiceLine.id'))
    
    serviceLine = relationship('ServiceLine', backref='keywords_list')
    
    def __init__(self, kwrd, sl3_id):
        self.keyword = kwrd
        self.serviceLine_index = sl3_id
    
    @staticmethod    
    def tableName():
        return KeywordTable.__tablename__
    
    def __repr__(self):
        return  "<Keyword Table: (%i,'%s')>" % (self.id, self.keyword)

class Company(URLBase):
    __tablename__ = 'Company'
    
    id = Column(Integer, primary_key=True)
    name = Column(TEXT, nullable=False)
    base_url = Column(TEXT, nullable=False)
    crawled = Column(Integer, default=0)
    
    def __init__(self, name, base_url, crawled=0):
        self.name = name
        self.base_url = base_url
        self.crawled = crawled

    @staticmethod        
    def tableName():
        return Company.__tablename__        

    def __repr__(self):
        return  "<Company: (%i,'%s','%s',%i)>" % (self.id, self.name, self.base_url,
                                                    self.crawled)
    
    
class URL(URLBase):
    __tablename__ = 'URL'
    
    id = Column(Integer, primary_key=True)
    address = Column(TEXT, unique=False, nullable=False)
    content = Column(TEXT)
    analyzed = Column(Integer, default=0)
    company_index = Column(Integer, ForeignKey('Company.id'))

    company = relationship("Company", backref=backref('urls', order_by=id))
    
    def __init__(self, address, content, analyzed, company_index):
        self.address = address
        self.content = content
        self.analyzed = analyzed
        self.company_index = company_index

    @staticmethod
    def tableName():
        return URL.__tablename__    

    def __repr__(self):
        return  "<Relationship: (%i,'%s','%s','%i','%i')>" % (self.id, self.address, self.content,
                                                              self.analyzed, self.company_index)

class TagStats(URLBase):
    __tablename__ = 'TagStats'
    
    id = Column(Integer, primary_key=True)
    tag = Column(TEXT, nullable=False)
    url_index = Column(Integer, ForeignKey('URL.id'))
    
    url = relationship("URL", backref=backref('tags'))
    
    def __init__(self, tag, url_id):
        self.tag = tag
        self.url_index = url_id
    
    @staticmethod
    def tableName():
        return TagStats.__tablename__        
    
    def __repr__(self):
        return "<Tag: (%i, %s)>" % (self.id, self.tag)
    
class KeywordStats(URLBase):
    __tablename__ = 'KeywordStats'
    
    id = Column(Integer, primary_key=True)
    keyword = Column(TEXT, nullable=False)
    count = Column(Integer, nullable=False, default=0)
    tagStat_index = Column(Integer, ForeignKey('TagStats.id'))
    keywordTable_index = Column(Integer, nullable=False)
    
    tag = relationship("TagStats", backref=backref('keywords', order_by=count))
    
    def __init__(self, keyword, count, tag_id, orig_keyword_id):
        self.keyword = keyword
        self.count = count
        self.tagStat_index = tag_id
        self.keywordTable_index = orig_keyword_id
    
    @staticmethod
    def tableName():
        return KeywordStats.__tablename__    
            
    def __repr__(self):
        return "<Keyword: (%i, %s, %i)>" % (self.id, self.keyword, self.count)