f = open("followers_1.json", "r")
data, followers = [], []
data = f.read().split('\n')
for follower in data:
    if follower[:15] == '        "href":':
        followers.append(follower[43:-2])
f.close()

f = open("following.json", "r")
data, followings = [], []
data = f.read().split('\n')
for following in data:
    if following[:18] == '          "value":':
        followings.append(following[20:-2])
f.close()

fakes = []
for following in followings:
    if following not in followers:
        fakes.append(following)

print("----- LIST OF FAKES -----")
for fake in fakes:
    print(fake)