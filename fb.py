import facebook
import urllib3
import requests

token = 'EAAfYrlZBZBizYBAN7b9jORDMZACd7tVjdzvpWOC3shpdLGUg8LsAOvpTK2UNIY3S1qZC7O4uNRym232rSBDoVEY7gwpZAyq2STSWZBAFtMOfyz131UdEpg4ZChhLh8SLug6pUaLpQ3ZBkuHfTaH2ZBO3ZABBcJK5Rb9xBVOpJzHo40zTihgw8H9DJd'

graph = facebook.GraphAPI(access_token=token, version = 2.8)
#events = graph.request('me/id')
thisid = graph.get_object(id = 'me?fields=id,name,email,gender,posts')
print "User Name :", thisid['name']
print "User ID :", thisid['id']
print "User Email :", thisid['email']
print "User Gender :", thisid['gender']
print "User Post :", thisid['posts']['data'][0]['message']
print "User Post :", thisid['posts']['data'][1]['message']
