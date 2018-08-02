import requests
import lxml.html
import sys
import codecs

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

print(titles)
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
for var in enumerate(output):
    print(var)

"""
html = requests.get('https://www.tijd.be')
doc = lxml.html.fromstring(html.content)

new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]

titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')

tags = [tag.text_content() for tag in new_releases.xpath('.//div[@class="tab_item_top_tags"]')]
tags = [tag.split(', ') for tag in tags]

platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []

for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)

output = []
for info in zip(titles, prices, tags, total_platforms):
    resp = {}
    resp['title'] = info[0]
    resp['price'] = info[1]
    resp['tags'] = info[2]
    resp['platforms'] = info[3]
    output.append(resp)
for var in enumerate(output):
    print(var)
"""
