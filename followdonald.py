import urllib
import twurl
import json

outfile = open('donalddata.json', 'w')
wrap_list=[] #since I need to make a twitter API call repeatedly I will wrap the JSON info into a list

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
acct = 'realdonaldtrump'
twittercount=200 #pull 200 tweets at a time (the max)
url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': str(twittercount)} )
connection = urllib.urlopen(url)
data = connection.read()
js = json.loads(data)
wrap_list.append(js)
print(0, js[0]['text'], js[0]['id']) #print most recent tweet



count=1
old_max_id=0
max_id=js[len(js) - 1]['id']

while old_max_id!=max_id:
     old_max_id=max_id
     TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
     url = twurl.augment(TWITTER_URL, {'screen_name': acct,'count': str(twittercount),'max_id': str(max_id) } )
     connection = urllib.urlopen(url)
     data = connection.read()
     js = json.loads(data)
     print(count, js[0]['text'], js[0]['id']) #print one every 200 tweets
     max_id=js[len(js) - 1]['id']
     wrap_list.append(js)
     count=count+1


json.dump(wrap_list, outfile)
outfile.close()