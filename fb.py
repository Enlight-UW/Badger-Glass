import facebook
import urllib3
import requests

token = 'EAAfYrlZBZBizYBAN7b9jORDMZACd7tVjdzvpWOC3shpdLGUg8LsAOvpTK2UNIY3S1qZC7O4uNRym232rSBDoVEY7gwpZAyq2STSWZBAFtMOfyz131UdEpg4ZChhLh8SLug6pUaLpQ3ZBkuHfTaH2ZBO3ZABBcJK5Rb9xBVOpJzHo40zTihgw8H9DJd'

graph = facebook.GraphAPI(access_token=token, version = 2.7)
events = graph.request(‘/search?q=Poetry&type=event&limit=10000’)
