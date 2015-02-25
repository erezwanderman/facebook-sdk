import facebook
import json
import requests

access_token = "YOUR_ACCESS_TOKEN"
group_id = "YOUR_GROUP_ID"

graph = GraphAPI(access_token)
#graph = facebook.GraphAPI("**********FILL ME*****************")


# https://facepy.readthedocs.org/en/latest/usage/graph-api.html
data = graph.get_object(group_id + "/feed")


with open('group_dump.json', 'w') as outfile:
    while True:
        try:
            # Perform some action on each post in the collection we receive from
            # Facebook.
            json.dump(data, outfile, indent = 4)
            # Attempt to make a request to the next page of data, if it exists.
            data = requests.get(data['paging']['next']).json()
        except KeyError:
            # When there are no more pages (['paging']['next']), break from the
            # loop and end the script.
            break


