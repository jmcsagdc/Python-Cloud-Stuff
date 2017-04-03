# This requires the user to have exported a json
# key to the machine running this and add to .bashrc
# export GOOGLE_APPLICATION_CREDENTIALS=<path_to_file>
# Remember that this will require the user to restart
# the terminal to pick it up.

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
        permissions=tags.get('items', 'No additional permissions')
    
    # build a single row
    row.append(str(name))
    row.append(str(status))
    row.append(str(myNetwork['value']))
    row.append(str(myType['value']))
    row.append(tags['fingerprint'])
    row.append(permissions)
    # add the row to the table
    myTable.append(row)
    #for thing in instance:
        #print thing
        #print(thing, instance[thing])
print tabulate(myTable, headers=["name","status","network","type","fingerprint","permissions"])
