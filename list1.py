import facebook
import requests

token = "EAACEdEose0cBAKxCY6NFoDEhMpiiBEn8bgClZCtDlMvsD5N5Lq2TKsHGRCQ0bBC4Eozw9uCJNPYL4WM2ZBTvhRvVBuc1eU2OzjkzvWLZALIoU3ZAQcarTIfVAXl33I1ypo9qzen0yHo9AXVCyv8GiITT4T6lV0b4zUwAUnfwdfEJdNaZC43TQ7dUqAPfkoZAQZD"
graph = facebook.GraphAPI(token)
profile = graph.get_object("140216402663925")
posts = graph.get_connections(profile['id'], "posts")

for post in posts['data']:
    try:
        graph.put_object(post['id'], "likes")
        print("Liking the post : " +post['message'])

    except:
        continue