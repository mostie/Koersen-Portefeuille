import requests
import lxml.html
import sys
import codecs
import xlsxwriter

# zorgt ervoor dat speciale karakters geprint worden : vb. Chinese karakters
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)


html = requests.get('https://www.beursduivel.be/Koersen/Aandelen.aspx')
doc = lxml.html.fromstring(html.content)

Issue_Default = doc.xpath('//div[@class="IssueDefault"]')[0]
titles = Issue_Default.xpath('.//td[@class="TitleCell DateTimeCell"]/a/text()')
lastprices = Issue_Default.xpath('.//td[@class="ValueCell"][1]/span/text()')
highprices = Issue_Default.xpath('.//td[@class="ValueCell"][4]/span/text()')
lowprices = Issue_Default.xpath('.//td[@class="ValueCell"][5]/span/text()')
finals = Issue_Default.xpath('.//td[@class="ValueCell"][6]/span/text()')
times = Issue_Default.xpath('.//td[@class="ValueCell"][7]/span/text()')

#print(titles)
#print(prices)


output = []
for info in zip(titles, lastprices, highprices, lowprices,finals,times):
    resp = {}
    resp['title'] = info[0]
    resp['price'] = info[1]
    resp['high'] = info[2]
    resp['low'] = info[3]
    resp['final'] = info[4]
    resp['time'] = info[5]
    output.append(resp)
#for var in enumerate(output):
#    print(var)

workbook = xlsxwriter.Workbook('d:\data\it\python\koersen.xlsx')
worksheet = workbook.add_worksheet()

row = -1

for j in output:
        #print(j)
        row += 1
        col = -1
        for k in j:
            col += 1
            print("{}:{}".format(k,j[k]))
            worksheet.write(row,col,j[k] )


workbook.close()
