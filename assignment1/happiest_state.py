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


def get_sentiment(senti_dict, line):
    sentiment_score = 0
    non_sentiment_words = []
    for word in line.split(' '):
        if word in sentiment_dict:
            sentiment_score += sentiment_dict[word]
        else:
            non_sentiment_words.append(word)
    return sentiment_score, non_sentiment_words


def geo_info(tweet):
    try:
        if tweet['place']['country_code'] == 'US':
            state = tweet['place']['full_name'][-2:]
            return True, state
        else:
            return False, ''
    except:
        pass
    return False, ''


def main():
    sentiment_dict = construct_dict(sys.argv[1])
    tweet_file = open(sys.argv[2])
    state_happiness_index = defaultdict()
    total_tweet_count = 0

    for line in tweet_file:
        tweet = json.loads(line.encode('utf8'))
        try:
            if tweet['lang'] == 'en':
                if 'text' in tweet.keys():
                    normalized_tweet = normalize_word(
                        tweet['text'].encode('utf8'))
                    is_US, state = geo_info(d)
                    if is_US:
                        total_tweet_count += 1
                        sentiment_score = get_senti(sentiment_dict,
                                                    normalized_tweet)
                        if state in state_happiness_index:
                            state_happiness_index[state] += sentiment_score
                        else:
                            state_happiness_index[state] = sentiment_score
        except:
            pass

    happiest_state = 'XX'
    happiness_score = -1

    for state, score in state_happiness_index.items():
        if score > happiness_score:
            happiness_score = score
            happiest_state = state
    print happiest_state


if __name__ == '__main__':
    main()
