classone = 15
classtwo = 12
classthree = 27
classfour = 23
classfive = 11

total = classone + classtwo + classthree+ classfour + classfive
average = total/5

print(average)

stars_per_point = 7
reward_stars = total * stars_per_point
print("total reward stars: ", reward_stars)

boxes = reward_stars//25
leftover = reward_stars % 25

print("Full boxes packed: ", boxes)
print("Leftover stars:", leftover)

last_week = 450

print("better than last week?", total > last_week)

print("same as last week?", total == last_week)

print("at least as good?", total >= last_week)

total += 30

print("after some bonus points:", total)

total -= 15
print("after missed tasks:", total)

#bonus for more understanding
total * 2
print("after doing twice tasks: ", total)

reward_stars = total * stars_per_point
boxes = reward_stars//25
print("Final boxes packed:", boxes)
