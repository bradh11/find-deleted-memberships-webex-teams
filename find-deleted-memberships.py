from ciscosparkapi import CiscoSparkAPI
import json
import requests

# list of email addresses of users who were deleted.  No header required, put all users in one column.
csvfile = open('deleteduserlist.csv')
userList = []
for line in csvfile:
    row_data = line.strip("\n").split()
    userList.append(row_data[0])

# user token must have compliance officer role 
token ='< insert admin token here >'
api = CiscoSparkAPI(access_token=token)

# change dates below to the time where users were deleted
eventParams = {
    'resource':'memberships',
    'type':'deleted',
    'from':'2018-03-07T00:00:00.939Z',
    'to':'2018-03-08T10:00:00.939Z',
    'max':'1000'}
headers = {
    'Authorization': "Bearer " + token,
    'Content-Type': "application/json",
    }

events = requests.get('https://api.ciscospark.com/v1/events', headers=headers ,params=eventParams)
events = json.loads(events.text)

# print(events['items'])
for event in events['items']:
    # print(event['data'])
    if 'machine.' not in event['data']['personEmail'] and event['data']['personEmail'] in userList:
        # print (event)
        roomId = event['data']['roomId']
        email = event['data']['personEmail']
        try:
            memberships = api.memberships.list(roomId=roomId)
            room = api.rooms.get(roomId=roomId)
            print ('*'*75)
            print (room.title + ':  Add missing user - ' + email) 
            for membership in memberships:
                if membership.isModerator:
                    print (membership.personEmail + ' is moderator')
                else:
                    print(membership.personEmail)
        except:
            pass