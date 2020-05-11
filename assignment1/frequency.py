import sys
import json
import string

from collections import defaultdict


def construct_dict(sentiment_score_file):
    sentiment_file = open(sentiment_score_file)
    scores = {}
    for line in sentiment_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores


def normalize_word(word):
    exclude = set(string.punctuation)
    word = ''.join(ch for ch in word.lower() if ch not in exclude)
    return word


def get_sentiment(sentiment_dict, line):
    sentiment_score = 0
    non_sentiment_words = []
    for word in line.split(' '):
        if word in sentiment_dict:
            sentiment_score += sentiment_dict[word]
        else:
            non_sentiment_words.append(word)
    return sentiment_score, non_sentiment_words


def update_dict(dict, tweet):
    for word in tweet.split():
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1


def main():
    dict = defaultdict()
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
        tweet = json.loads(line.encode('utf8'))
        if 'text' in tweet.keys():
            update_dict(dict, normalize_word(tweet['text'].encode('utf8')))
    all_occurances = sum(dict.values())
    for word in dict.keys():
        print word, dict[word]/float(all_occurances)


if __name__ == '__main__':
    main()
