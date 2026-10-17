# Problem 02: The Caption's room
# HackerRank Link : https://www.hackerrank.com/challenges/py-the-captains-room/problem


k = int(input())
rooms = list(map(int, input().split()))

unique_rooms = set(rooms)

captain_room = (sum(unique_rooms) * k - sum(rooms)) // (k - 1)

print(captain_room)
