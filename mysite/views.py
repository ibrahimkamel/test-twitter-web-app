import twitter
from django.http import JsonResponse
from django.shortcuts import render_to_response
import json
def home(request):
    return render_to_response("index.html")
def latest_tweets(request,username):

    api = twitter.Api(consumer_key='7aIQWprw7qXr4TOLVRtndgVBK',
                      consumer_secret='giElC1SDGLqQr64wjTp2bOdP6jbPAef3ApdSNP2m1FB8Uc9xTJ',
                      access_token_key='64526899-v7J7LaNDQF09HOzbvP5FBC5H7tr3ifQxZRUTEbyjh',
                      access_token_secret='NfUf9zNgFUTpY7JVZHXvUSS7ZM0q7k0X6ZbIXTGpQEDoo')
    # test if user exists
    try:
        api.GetUser(screen_name=username)
    except:
        return JsonResponse({"message": "Invalid UserName"},status="404")
    statuses = api.GetUserTimeline(screen_name=username)[:5]
    latest_statuses = []
    for status in statuses:
        latest_statuses.append(status.text)
    return JsonResponse({"latest_statuses": latest_statuses})
