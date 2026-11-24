total_chores = 4
og_count = total_chores

print(f"you have {og_count} chores to finish today!\n")

completed_count = 0
chore_num = 1

while chore_num <= total_chores:

    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    elif chore_num == 3: next_chore = "take out the trash"
    else: next_chore == "wash the dishes"

    answer = input(f"have u finished: {next_chore}? (yes/no)")

    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("great job chore completed")
    else:
        print("okay finish it and check again")

    print("chores remaining:", total_chores, completed_count)
    print()

print("=== all chores complete==== ")   
print("great work finishing ur enitre checklist today\n")

print("now lets safely peek at an infinite loop")
test_value = 0
safety_counter = 0 
while test_value <= 0:
    print("this condition never changes so this would run forever")
    safety_counter += 1
    if safety_counter == 3:
        print("stopping here on purpose - a real inifinite loop nvr stops on its own")
        break
print("\n ==chore checklist summary ==")
print("chores assigned today:", og_count)
print('chores completed:', completed_count)
print("chores remaining:", total_chores - completed_count)