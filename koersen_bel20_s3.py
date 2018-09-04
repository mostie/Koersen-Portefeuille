import requests
import lxml.html
import sys
import codecs
import xlsxwriter
import openpyxl
from openpyxl import load_workbook
import datetime

from datetime import datetime
import os

from apscheduler.schedulers.blocking import BlockingScheduler

import boto3
import csv

# input : UU:MM => YYYY/MM/DD UU:00:00
def convert_time_to_date_time(etime):
    etime_array = etime.split(":")
    #print(etime_array[0])
    #print(etime_array[1])
    etime = etime_array[0] + ":" + "00"
    #print(etime)
    etime += ':00'
    current_datetime = str(datetime.datetime.now())[0:10]
    current_datetime = current_datetime + " " + etime
    #print(current_datetime)
    return current_datetime

    #rcurrent_datetime.strftime('%x %X')

def csv_writer(output, path):

    """

    Write output to a CSV file path

    """

    with open(path, "w") as csv_file:

        writer = csv.writer(csv_file, delimiter=',')

        #print(writer)

        #writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

        for line in output:

            writer.writerow(line)
            


def write_bel20_to_amazon_s3():


    print('test')
    

    # zorgt ervoor dat speciale karakters geprint worden : vb. Chinese karakters
    #sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)



    html = requests.get('https://www.beursduivel.be/Koersen/Aandelen.aspx')
    doc = lxml.html.fromstring(html.content)

    Issue_Default = doc.xpath('//div[@class="IssueDefault"]')[0]
    titles = Issue_Default.xpath('.//td[@class="TitleCell DateTimeCell"]/a/text()')
    lastprices = Issue_Default.xpath('.//td[@class="ValueCell"][1]/span/text()')
    highprices = Issue_Default.xpath('.//td[@class="ValueCell"][4]/span/text()')
    lowprices = Issue_Default.xpath('.//td[@class="ValueCell"][5]/span/text()')
    finals = Issue_Default.xpath('.//td[@class="ValueCell"][6]/span/text()')
    #times = Issue_Default.xpath('.//td[@class="ValueCell"][7]/span/text()')


    output = []
    #for info in zip(titles, lastprices, highprices, lowprices,finals,times):
    for info in zip(titles, lastprices, highprices, lowprices,finals):        
        resp = {}
        resp['title'] = info[0]
        resp['price'] = info[1]
        resp['high'] = info[2]
        resp['low'] = info[3]
        resp['final'] = info[4]
        #resp['time'] = convert_time_to_date_time(info[5])
        output.append(resp)
        #for var in enumerate(output):
        #    print(var)


    row = 0

    for j in output:
            row +=1
            col = 0
            for k in j:
                col += 1
                print(j[k])
                print(row)
                print(col)

    path = "d:\data\it\python\koersen.csv"

    csv_writer(output, path)

    # Create an S3 client
    s3 = boto3.client('s3')

    filename = "d:\data\it\python\koersen.csv"
    bucket_name = 'mostie-algemeen'

    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.
    s3.upload_file(filename, bucket_name, filename)    



if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(write_bel20_to_amazon_s3, 'interval', seconds=5)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

#write_bel20_to_amazon_s3()