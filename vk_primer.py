import requests

VERSION = '5.60'
APP_ID = 5869677

access_token = 'bf0a786cb1fda3452856f0cb340f1fe239f6ac62a82bd20be090f26c6d7b3afc1a27a4107fc7930b959..' # здесь нужен свой токен
params = {'access_token': access_token, 'v': VERSION}

#response = requests.get('https://api.vk.com/method/friends.get', params)
#print(response.json()['response']['items'])
#for user_id in response.json()['response']['items']:

response = requests.get('https://api.vk.com/method/friends.getOnline', params)
i = 0
for user_id in response.json()['response']:
    i += 1
    get_friend = requests.get('https://api.vk.com/method/users.get', {'user_id': user_id})
    # Получим список всех своих друзей:
    print(i, 'friend:', get_friend.json()['response'])

i = 0
for user_id in response.json()['response']:
    i += 1
    get_friend_friends = requests.get('https://api.vk.com/method/friends.get',
                                      {'access_token': access_token, 'v': VERSION,'user_id': user_id})
    # Для каждого своего друга получим список его друзей:
    print(i, 'friend: ', user_id, '\nfriend_friends: ', get_friend_friends.json()['response']['items'])


