import simplejson as json
import httplib2

url = "https://api.nuggad.net/flights/1/impressions"

h = httplib2.Http(".cache")
h.add_credentials('RHutton', 'RHutton01')
resp, content = h.request("https://api.nuggad.net/flights/1/impressions")
data = json.loads(content)

for item in data:
 impressions = item.get('impressions')

#print impressions




