import re
import requests

docpattern = re.compile("(Dockey=)((\w)*)")
docFile = open("docKey.txt", 'w')
linkFile = open("links.txt", 'w')

dataSite = requests.get("https://nepis.epa.gov/EPA/html/pubs/pubtitle.html").text
matches = docpattern.findall(dataSite)
for match in matches:
    a = match[1]
    fileLink = "https://nepis.epa.gov/Exe/ZyPDF.cgi/" +a + ".PDF?Dockey=" + a + ".pdf"
    docFile.write(a)
    linkFile.write(fileLink)
    linkFile.write("\n")
    docFile.write("\n")
docFile.close()
linkFile.close()
