from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()
from googleapiclient.discovery import build
service = build('compute', 'v1', credentials=credentials)
result = service.instances().list(project='jason-v', zone='us-central1-c').execute()

# This needs to be installed via:
# pip install tabulate

from tabulate import tabulate

# Take a look at what you get back. It's a lot.
#print result

# Process that mess into something useful.
row=[]
myTable=[]
items=result['items']

for instance in items:
    # for each row, start clean
    row=[]
    status=instance['status']
    name=instance['name']
    metadata=instance['metadata']
    items_l=metadata['items']
    myNetwork=items_l[1]
    myType=items_l[0]
    tags=instance['tags']
    if 'desktop' not in myType:
        if 'items' in tags.keys():
            permissions=tags['items']
        else:
            permissions='none'

# build a single row
    row.append(str(name))
    row.append(str(status))
    row.append(str(myNetwork['value']))
    row.append(str(myType['value']))
    row.append(tags['fingerprint'])
    row.append(permissions)
    # add the row to the table
    myTable.append(row)

print tabulate(myTable, headers=["name","status","network","type","fingerprint","permissions"])
