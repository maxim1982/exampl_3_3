import requests

VERSION = '5.60'
APP_ID = 5869677
common_friend = {'друг': 0}

access_token = '00b912605fa5a4232f30039cf3acbba106bb8ff34e56de46cf0759246adc370f9140bcfa3b2a2949b....' # здесь нужен свой токен
params = {'access_token': access_token, 'v': VERSION}

# все друзья в контакте...
response = requests.get('https://api.vk.com/method/friends.get', params)

# пробую с онлайн друзьями
#response = requests.get('https://api.vk.com/method/friends.getOnline', params)

i = 0
print('my_friend:')
for user_id in response.json()['response']['items']:
    i += 1
    get_friend = requests.get('https://api.vk.com/method/users.get', {'user_id': user_id})
    # Получим список всех своих друзей(в контакте):
    print(i, get_friend.json()['response'][0])

    # внесем в словарь друзей
    if user_id in common_friend:
        common_friend[user_id] += 1
    else:
        common_friend[user_id] = 1

i = 0
for user_id in response.json()['response']['items']:
    i += 1
    get_friend_friends = requests.get('https://api.vk.com/method/friends.get',
                                      {'access_token': access_token, 'v': VERSION, 'user_id': user_id})
    # Для каждого своего друга получим список его друзей:
    print(i, 'friend: ', user_id, '\nfriend_friends: ', get_friend_friends.json())

    # внесем в словарь друзей
    if user_id in common_friend:
        common_friend[user_id] += 1
    else:
        common_friend[user_id] = 1

print('common friends :')

for key in sorted(common_friend, key=common_friend.get, reverse=True):
    if common_friend[key] > 1:
        print(key, common_friend[key])



