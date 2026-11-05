# 氏名と生年月日を入力
name = input("氏名：")
birthday = input("生年月日：")

year, month, day = birthday.split("/")

name_length = 0
for char in name:
    if char.isalnum():
        name_length += 1

total = int(year) + int(month) + int(day) + name_length

if total % 6 == 0:
    fortune = "大吉"
elif total % 3 == 0:
    fortune = "中吉"
elif total % 2 == 0:
    fortune = "吉"
else:
    fortune = "凶"

print(f"{name}さんの運勢: {fortune}")
