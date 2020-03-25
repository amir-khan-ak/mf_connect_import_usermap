import json
import sys
import pandas as pd
import requests
import xml.etree.ElementTree as ET

# define variables for accessing octane rest api



import base64

credentials = sys.argv[2] #"Administrator:Administraror:Micro Focus Connect" 
message_bytes = credentials.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_credentials = base64_bytes.decode('ascii')

#print(base64_credentials)



url = sys.argv[1]
ContentType = {'Content-Type': 'application/json'}
excel_path = sys.argv[3]
headers= {"Accept":"*",
        "Content-type": "application/json",
       "Credentials":base64_credentials}

data_xls = pd.read_excel(excel_path)
print(data_xls)
print('Total Rows in Excel: ' + str(data_xls.shape[0]))
payload_usermap=''
for i in range(data_xls.shape[0]):

    # read excel and build usermap json

    payload_usermap = payload_usermap + '{"name":"' + data_xls.UserMapName[i] + '",' \
                                '"User":[{"name":"'+ data_xls.UsernameMaster[i] + '",' \
                                '"type":"DATA_SOURCE","value":"'+ data_xls.SystemMaster[i] + '"},' \
                                '{"name":"' + data_xls.UsernameTarget[i] + '",' \
                                '"type":"DATA_SOURCE","value":"'+ data_xls.SystemTarget[i] + '"}]},'



payload_begin = '{"UserMap":['
payload_end = ']}'
payload_um = payload_begin + payload_usermap[:-1] + payload_end
#print(url.endswith("/"))
if url.endswith("/"):
    url=url[:-1]

# Login to MF Connect
resource = 'connectRest/rest/users/logon'
print('Login URL: ' + url + '/' + resource)
resp = requests.get(url + '/' + resource,
                    headers=headers)

print('Login: ' + str(resp.status_code))
responseXml = ET.fromstring(resp.content)
sessionid = responseXml.find('sessionId')
#print(sessionid.text)
#print(resp.content)

headersum= {"Accept":"*",
        "Content-type": "application/json",
       "Credentials":credentials, "session-id":sessionid.text}
# import user map
resource = 'connectRest/rest/connect/userMaps'
resp = requests.put(url + '/' + resource, data=payload_um, headers=headersum)
print('Import Usermap URL: ' +url + '/' + resource)
print('Import of usermap in progress: ' + str(resp.status_code))
#print(resp.content)

print('Importing finished')
