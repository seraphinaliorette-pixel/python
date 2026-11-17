print("=== SWIMMING POOL ENTRY CHECKER =====")
age = int(input("How old are you?"))
can_swim = input("Can you swim 25 metres?yes/no: ").strip().lower()
adult_here = input("is an adult with you?yes/no: ").strip().lower()

print()
print("entry decision")
print("-" * 32)

if age < 4:
    print("age group : toddler")
elif age < 12:
    print("age group: child")
elif age < 18:
    print("age group: teen")
else:
    print("age group: adult")

    if can_swim == "yes" and adult_here == "yes":
        print("deep pool: allowed- you can swim and an adult is with you.")
        if age < 12 or can_swim == "no":
            print("shallow end: stay in the shallow end today.")

            if not (adult_here == "yes"):
                print("reminder: no adult with you- tell the lifeguard.")
