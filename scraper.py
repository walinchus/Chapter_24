#import our libraries
import scraperwiki
import urllib2
import lxml.etree

#create a variable called 'url' and then read what's there
url = "http://www.staffssaferroads.co.uk/media/114997/03092012_forwebsite.pdf"
pdfdata = urllib2.urlopen(url).read()
print "The pdf file has %d bytes" % len(pdfdata)

 #convert to xml and print some info
xmldata = scraperwiki.pdftoxml(pdfdata)
print "After converting to xml it has %d bytes" % len(xmldata)
root = lxml.etree.fromstring(xmldata)

# this line uses xpath to find <text> tags
lines = root.findall('.//text[@font="5"])
print lines
for line in lines:
 print line.text

record = {}
for line in lines:
 if len(line.text)<5:
  code = line.text
  print record
  record["code"] = line.text
 if len(line.text)>4:
  print record
  record["locations"] = line.text
  scraperwiki.sqlite.save(['locations'], record)
