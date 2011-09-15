from DBInterface import *

class Company:
    def __init__(self, id=-1, name="", base_url="", crawled=0):
        self.id = id
        self.name = name
        self.base_url = base_url
        self.crawled = crawled
        self.url_list = []
        
    def addUrl(self, url):
        ''' url: URL Object '''
        self.url_list.append(url)
        
class URL:
    def __init__(self, id=0, address="", content="", analyzed=""):
        self.id = id
        self.address = address
        self.content = content
        self.analyzed = analyzed

class UrlInterface:
    def __init__(self, db):
        self.db = db
    
    def crawlingComplete(self, company_name):
        self.db.update('Company', "crawling", 1, "name", company_name)
        
        
    def uncrawledCompanies(self):
        result = self.db.query("Company", ["id", "name", "base_url", "crawled"], "crawled", 1)
        
        companies = []
        for r in result:
            c = Company(r.id, r.name, r.base_url, r.crawled)
            companies.append(c)
            
        return companies
    
    def urlAnalyzed(self, url):
        ''' url: String '''
        self.db.update('URL', 'analyzed', 1, 'address', url)
        
    def addURL(self, company, url):
        ''' company: Company class object
            url: URL class object '''
        if (company.id < 0):
            company.id, company.name = self.db.query("Company", ["name"], "name", company.name)
        
        self.db.insert('URL', ["address", "content", "analyzed", "company_index"], 
                       [url.address, url.content, url.analyzed, url.company_index])