import urllib.request
import urllib.parse
import json
import requests

command = {
  "command": "broadcastTransactions",
  "trytes": ["P9KFSJVGSPLXAEBJSHWFZLGP ..."]
}

stringified = json.dumps(command)

headers = {
    'content-type': 'application/json',
    'X-IOTA-API-Version': '1'
}

url="http://ec2-54-147-37-156.compute-1.amazonaws.com:14265"

response = requests.get(url)
print(response.status_code)
#fo = urllib.parse.urlencode(command)
#fo = urllib2.urlunparse(command)
#fo = fo.encode('utf-8')
#print('encoded')
#request = urllib.request.Request(url, fo)
#print('requested')
#returnData = urllib.request.urlopen(request).read()
#print('url opened')

#jsonData = json.loads(returnData)

#print (jsonData)