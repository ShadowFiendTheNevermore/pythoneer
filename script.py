# -*- coding: utf-8 -*-
import pycurl
import json
import sys
from StringIO import StringIO
print u'Введите число от 1 до 56'

limit = int(sys.stdin.readline().strip())

url = 'http://icomms.ru/inf/meteo.php?tid=21'

buffer = StringIO();
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()

jsonData = json.loads(body)

for i,item in enumerate(jsonData):
	if i == limit:
		break;
	print u'Дата(в периоде): %s | Температура воздуха(в градусах по цельсию) = %s | Ветер: %s' % (item['date'], item['temp'], item['wind'])


