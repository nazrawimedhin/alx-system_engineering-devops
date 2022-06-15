#!/usr/bin/python3
"""contains a function that parses the title of all hot articles,
and prints a sorted count of given keywords"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """returns top tens"""
    headers = {
        'User-agent': 'cli:api_advanced:v1.0.0 (by /u/dereje77'
    }
    if after is None:
        return hot_list

    r = requests.get('https://www.reddit.com/r/{}/hot.json'.format(subreddit),
                     params={'limit': 100, 'after': after},
                     headers=headers,
                     allow_redirects=False)
    if r.status_code != 200:
        return None
    json = r.json()
    for post in json['data']['children']:
        hot_list.append(post['data']['title'])
    return recurse(subreddit, hot_list, json['data']['after'])


def count_words(subreddit, word_list):
    """parses the title of all hot articles, and prints a sorted count
    of given keywords"""
    word_list = list(map(str.lower, word_list))
    result = {}
    titles = recurse(subreddit)
    for title in titles:
        for word in word_list:
            if word in title:
                if result.get(word) is None:
                    result[word] = 0
                result[word] += 1
    result = [(k, v) for k, v in result.items()]
    result.sort(key=lambda x: x[1], reverse=True)
    for k, v in result:
        print('{}: {}'.format(k, v))
