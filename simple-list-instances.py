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


# The following line failed because instances was not defined.
# Syntax examples on cloud.google.com are inconsitent and don't
# build on the prior snippet...
#instances = list_instances(compute, project='jason-v', zone='us-central1-c')

# Take a look at what you get back. It's a lot.
print result

# Process that mess into something useful.

items=result['items']

for instance in items:
    status=instance['status']
    name=instance['name']
    print name, status

# Prints something like this:
'''
desktop1-troz RUNNING
desktop2-troz RUNNING
server-django1-troz RUNNING
server-django2-troz RUNNING
server-django3-troz RUNNING
server-ldap-troz RUNNING
server-nfs-troz RUNNING
server-plain-troz RUNNING
server-rsyslog-troz RUNNING
server-sql1-troz RUNNING
server-sql2-troz RUNNING
server-sql3-troz RUNNING
'''
