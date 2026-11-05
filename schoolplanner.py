print("Smart School Planner")
print("Answer 3 quick questions and I will plan your day!")

day = input("What day is it?(Mon-Sun").strip().capitalize()
weather = input("What weather is it?(sunny/rainy/cloudy").strip().lower()
homework = input("Is your homework done? (yes/no)").strip().lower()

print(f"==== Your plan for the {day}===")

print("-"* 35)

if day in ("Saturday", "Sunday"):
    print("Day type:         Weekend  - Enjoy your free time!")
elif day == "Monday":
    print("Day type:         First day of the week  - Pack your weekly planner")
elif day == "Friday":
    print("Day type:         Last school day  - Return library books today.")
elif day == ("Tuesday", "Wednesday", "Thursday"):
    print("Day type:         Regular school day  - Stay focused!")
else:
    print("Day type:         Day not recognized. Please check the spelling.")

if weather == "sunny" and homework == "yes":
    print("After school: Head to the park- great weather and homework is done.")


if weather == "rainy" or weather == "cloudy":
    print("Weather tip: Pack your umbrella, it may get wet outside.")

if not(homework == "yes"):
    print("Homework:     Not done yet, finish before going out.")

if weather == "rainy" and not(homework == "yes"):
    print("Best plan:   Stay in, finish homework, then watch your favorite show.")

elif weather == "sunny" and homework == "yes" and not(day in ("Saturday", "Sunday")):
    print("Best plan:   All set for a great school day! You are prepared.")

elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan:  Perfect weekend weather, head outside and have fun!")
else:
    print("Best plan:  Take it one step at a time, you got this!")

print("Plan complete! Have a wonderful day!")
    