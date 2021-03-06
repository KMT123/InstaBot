import requests

from get_user_id import get_user_id
from constants import APP_ACCESS_TOKEN, BASE_URL
from clint.textui import colored


def get_post_id(insta_username):
    user_id = get_user_id(insta_username)

    if user_id == None:
        print colored.red('Username does not exist')
        exit()

    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print colored.yellow('GET request url : %s' % (request_url))
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:

        # extract post id
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print colored.red('Post does not exist')
    else:
        print user_media
        print colored.red('Status code received is other than 200')
        exit()