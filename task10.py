import requests
from time import sleep

VK_TOKEN = "TOKEN_HERE"
VK_URL = "https://api.vk.com/method/"
VK_API_VER = 5.131


class VKUser:
    def __init__(self, user_id):
        self.user_id = str(user_id)

    def __str__(self):
        return "https://vk.com/id" + self.user_id

    def get_username(self):
        sleep(0.4)
        url = VK_URL + 'users.get?v=' + str(VK_API_VER) + '&access_token=' + VK_TOKEN + '&user_id=' + self.user_id
        req = requests.get(url)
        if req.status_code != 200:
            return ""
        else:
            user_base = req.json()['response'][0]
            return f"{user_base['first_name']} {user_base['last_name']}"

    def get_friends_ids(self):
        sleep(0.4)
        url = VK_URL + 'friends.get?v=' + str(VK_API_VER) + '&access_token=' + VK_TOKEN + '&user_id=' + self.user_id
        req = requests.get(url)
        if req.status_code != 200:
            return []
        else:
            return [elem for elem in req.json()['response']['items']]

    def __and__(self, other):
        common_fiends = list(set(self.get_friends_ids()).intersection(set(other.get_friends_ids())))
        return [VKUser(friend) for friend in common_fiends]


if __name__ == '__main__':

    user1 = VKUser("user1_id")
    user2 = VKUser("user2_id")
    print('Наши пользователи:')
    print(f"{user1.get_username()} - {user1}")
    print(f"{user2.get_username()} - {user2}")
    common_friends = user1 & user2
    if len(common_friends) == 0:
        print('У них нет общих друзей')
    else:
        print('Их общие друзья:')
        print(*list(f.get_username() for f in common_friends), sep='\n')
