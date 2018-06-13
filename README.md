# Find deleted memberships in Webex Teams

This capabilities of this Python script allow for a report to be created for space membership delete events across a period of time. For example, if a user was accidentally deleted from Cisco Webex Teams, they will lose all memberships to spaces they were joined to. Cisco cannot restore these objects unfortunately, so the customer is left trying to figure out what spaces the user was a member of, and who the moderator of those spaces might be (in order to invite them back...).

## Pre-requisites

- This script was written with python 3.6, it should work on any version of Python greater than 3.5. Python can be installed [here](https://www.python.org/downloads/)
- Cisco spark API package should be installed via `pip install ciscosparkapi`
- Requests library is required to access the Webex Teams Event API and can be installed via `pip install requests`
- Alternatively, all dependent libraries can be installed via one command `pip install -r requirements.txt`

## Steps to Run the script

1.  Populate the deleteduserlist.csv to include the email address (aka user id) of the users.
2.  The API used to access the Events API is privileged information and requires to be run from a user with "Compliance Admin" role in Webex Teams
3.  This script requires a developer token for the Teams application. It can be retrieved [here](https://developer.webex.com/getting-started.html)
4.  Update the token and data range you need to investigate
    ![alt text](/media/deleted-membership-modify-prerequisites.png "Script Prerequisites")
5.  Run the script by typing "python find-deleted-memberships.py"

The output returned will show the Space name, list of current active memberships, and who the active moderators are
![alt text](/media/deleted-membership-ouput.png "Script Output")

Hopefully this script will be helpful in situations where restoring memberships of spaces is critical.

Enjoy!
