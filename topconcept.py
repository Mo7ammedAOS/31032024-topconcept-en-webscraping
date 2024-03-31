from bs4 import BeautifulSoup as Bs
import requests
import csv
import pandas as pd

url = 'https://topconcept.ae/our-team/'
html_concept = requests.get(url).text
soup = Bs(html_concept,'html5lib')
# print(soup.prettify())
file = 'topconcept.csv'
csv_file = open(file,'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Employee Name','POSITION'])

employees = soup.findAll('div',class_ = 'edgtf-team-title-holder')

for person in employees:
    name = person.find('h4').a.text
    position = person.find('h6').text
    csv_writer.writerow([name,position])
    # print(name , position)

csv_file.close()

topconcept = pd.read_csv(file)

print(topconcept.head())