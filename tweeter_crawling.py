import tweepy
from textblob import TextBlob
import os
import json

path = os.getcwd()
secret_file = os.path.join(path, 'secrets.json')  # secrets.json 파일 위치를 명시
print(secret_file)
# API 키를 입력합니다.
with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)


API_KEY = get_secret("API_KEY")
API_SECRET = get_secret("API_SECRET")
ACCESS_TOKEN = get_secret("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = get_secret("ACCESS_TOKEN_SECRET")

# 트위터로 부터 Access 권한을 받습니다.
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# API를 연결하고 Novak Djokovic와 관련된 트윗들을 다운받습니다.
api = tweepy.API(auth)

tweets = api.search('Novak Djokovic')
polarity = 0
subjectivity = 0
i = 0

# 개별 트윗을 분석하여 심리 점수와, 주관적 점수를 받습니다.
for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    polarity += analysis.sentiment[0]
    subjectivity += analysis.sentiment[1]
    i += 1

# 평균값을 통해 점수를 산출하여 보여줍니다.
print("Sentiment : " + str(polarity/i))
print("subjectivity : " + str(subjectivity/i))
