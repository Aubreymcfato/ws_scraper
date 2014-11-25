#!/usr/bin/env python

import wikipedia
from bs4 import BeautifulSoup
import unicodecsv


wikipedia.set_lang("it")
out = unicodecsv.writer(open("listametadati.csv", "wb"), encoding="utf-8")
head = ("TITLE", "TYPE", "URL", "CCE", "SUBJECT", "CREATOR", "CONTRIBUTOR", "DESCRIPTION", "PUBLISHER", "DATE", "FORMAT", "SOURCE", "LANGUAGE", "RELATION", "COVERAGE", "RIGHTS", "IMMAGINE", "IMMAGINE ED.")
out.writerow(head)

def get_cover(page, data_indice):
    #page = wikipedia.page(book)
    page_cover = wikipedia.page(data_indice)
    #"Indice:"+unicode(title)+".djvu"
    soup_cover = BeautifulSoup(page_cover.html())
    cover_line=soup_cover.find("img", { "class" : "thumbimage" })
    #print cover_line
    if cover_line is not None:
        cover_semiurl = cover_line['src']
        cover_url = "http:" + str(cover_semiurl)
    else:
        cover_url = ""  
    #print cover_url
    return cover_url    
    

def get_bookmetadata(book):
    page = wikipedia.page(book)
    soup = BeautifulSoup(page.html())#non capisco bene che fa, dato che l'HTML e lo stesso... ma lo rendo un oggetto 
    data = soup.find("span", { "id" : "dati" })
    #print data
    data_argomento =data['data-argomento']
    data_indice = data['data-urldellaversionecartaceaafronte'] 
    print data_indice
    try:
        titles = soup.find ('span', attrs={"id" : "ws-title"}) #se vede titoli troppo lunghi, prende quello della pagina in ns0 e non quello con l'a capo
        authors = soup.find ('span', attrs={"id" : "ws-author"})
        publishers = soup.find ('span', attrs={"id" : "ws-publisher"})
        dates = soup.find ('span', attrs={"id" : "ws-year"})
        places = soup.find ('span', attrs={"id" : "ws-place"})
    except HTMLParser.HTMLParseError:
        title = ""
        author = ""
        publishe = ""
        date = ""
        place = ""
    
    if titles is not None:
        title=titles.text#.encode('ascii', 'ignore')
    if authors is not None:
        author=authors.text#.encode('ascii', 'ignore')
    if publishers is not None:
        publisher=publishers.text#.encode('ascii', 'ignore')
    if dates is not None:
        date=dates.text#.encode('ascii', 'ignore')
    if places is not None:
        place=places.text#.encode('ascii', 'ignore')
    
    if data_indice is not None:
        cover_url=get_cover(page, data_indice)
    else: 
        cover_url=""        
                    #"TITLE", "TYPE", "URL", "CCE", "SUBJECT", "CREATOR", "CONTRIBUTOR", "DESCRIPTION", "PUBLISHER", "DATE", "FORMAT", "SOURCE", "LANGUAGE", "RELATION", "COVERAGE", "RIGHTS", "IMMAGINE", "IMMAGINE ED.")
        
    out.writerow([unicode(title), "E-book Open", u"http://it.wikisource.org/wiki/"+ unicode(book[0]) + u" | " +u"http://wsexport.wmflabs.org/tool/book.php?lang=it&format=epub&page=" + unicode(book[0]), None, unicode(data_argomento), unicode(author), None, None, u"Wikisource, la biblioteca libera. <it.wikisource.org>", None, u"HTML | EPUB", unicode(date) + " | " + unicode(publisher)  + " | " + unicode(place), u"Italiano", None, None, u"Pubblico dominio", unicode(cover_url), u"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/229px-Wikisource-logo.svg.png"])

books=unicodecsv.reader(open("listalibri.csv"), encoding="utf-8")
for book in books:
    get_bookmetadata(book)

print "everything is ok"
