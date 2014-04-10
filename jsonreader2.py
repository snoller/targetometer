import simplejson as json
import httplib2
from config import user,pw

url = "https://api.nuggad.net/info"
try:
 h = httplib2.Http()
 h.add_credentials(user, pw)
 resp, content = h.request(url)
 data = json.loads(content)
except:
 pass

flat=[]

for k in data:
 if isinstance(data[k],list):
  print "list\n" 
  for k2 in data[k]:
   if(data[k][k2] != ("" or False)):
    l1=str(k) + " " + str(k2)
    flat.append([l1,data[k][k2]])
 elif isinstance(data[k],dict):
  print "dict\n"
  for k3 in data[k]:
   if(data[k][k3] != ("" or False)):
    l2=str(k) + " " + str(k3) 
    flat.append([l2,data[k][k3]])
 else:
  print "str"
  if(data[k] != ("" or False)):
   flat.append([k,data[k]])

#print flat

for h in enumerate(flat):
 print h
print "\n"
print flat[1][0];
#flatstr = map(str,flat)

#print flatstr



