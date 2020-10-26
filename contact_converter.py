

import os
import json
import csv 

DIR = os.path.dirname(os.path.realpath(__file__))

cjson = {}
with open(os.path.join(DIR,'contacts.json'),'r',encoding='utf-8') as file:
    cjson = json.load(file)

my_list = [
    [
    'Name',
    'Given Name',
    'Additional Name',
    'Family Name',
    'Nickname',
    'Notes',
    'Phone 1 - Type',
    'Phone 1 - Value',
    'Phone 2 - Type',
    'Phone 2 - Value',
    'E-mail 1 - Type',
    'E-mail 1 - Value',
    'E-mail 2 - Type',
    'E-mail 2 - Value',
    'Organization 1 - Name'
    ]
]

for c in cjson['contacts']:
    print(c)
    il = []
    il.append(c.get('firstName',None))
    il.append(c.get('firstName',None))
    il.append(c.get('lastName',None))
    il.append(c.get('lastName',None))
    il.append(c.get('nickName',None))
    il.append(c.get('notes',None))

    try:
        il.append(c.get('phones',None)[0]['label'])
        il.append(c.get('phones',None)[0]['field'])
    except:
        il.append('')
        il.append('')
    try:
        il.append(c.get('phones',None)[1]['label'])
        il.append(c.get('phones',None)[1]['field'])
    except:
        il.append('')
        il.append('')

    try:
        il.append(c.get('emailAddresses',None)[0]['label'])
        il.append(c.get('emailAddresses',None)[0]['field'])
    except:
        il.append('')
        il.append('')
    try:
        il.append(c.get('emailAddresses',None)[1]['label'])
        il.append(c.get('emailAddresses',None)[1]['field'])
    except:
        il.append('')
        il.append('')

    try:
        il.append(c.get('companyName',None))
    except:
        il.append('')

    my_list.append(il)


with open(os.path.join(DIR,"contacts.csv"), "w", newline="") as outfile:
    writer = csv.writer(outfile)
    for l in my_list:
        writer.writerow(l)
