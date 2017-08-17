import tweepy

consumer_key = 'xxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

#認証のためにリダイレクトするURLを発行
try:
    redirect_url = auth.get_authorization_url()
    print("Redirect URL: " + redirect_url)
except tweepy.TweepError:
    print("Error! Failed to get request token.")

# Example w/o callback (desktop)
verifier = input("Verifier: ")

# Get access token
auth.get_access_token(verifier)

key = auth.access_token
print("OAuth access token (key): " + key)
secret = auth.access_token_secret
print("OAuth access token (secret): " + secret)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
api.update_status('test tweet')
