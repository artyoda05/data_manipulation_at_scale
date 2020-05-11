import sys
import json
import string
from collections import defaultdict
import operator


def normalize_word(word):
    exclude = set(string.punctuation)
    word = ''.join(ch for ch in word.lower() if ch not in exclude)
    return word


def update_dict(hashtags, dict):
    for hashtag in hashtags:
        if hashtag in dict:
            dict[hashtag] += 1
        else:
            dict[hashtag] = 1


def main():
    tweet_file = open(sys.argv[1])
    h_dict = defaultdict()
    for line in tweet_file:
        tweet = json.loads(line.encode('utf8'))
        hashtags = tweet['entities']['hashtags']
        tags = []
        for tag in hashtags:
            tags.append(normalize_word(tag['text'].encode('utf8')))
        update_dict(tags, h_dict)
    h_dict = sorted(h_dict.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(10):
        print h_dict[i][0], h_dict[i][1]


if __name__ == '__main__':
    main()
