name = input("What is the member name: ")
club = input("What is the member club name: ")

member_number = 8
points = 9.5
is_active = True

print("Member Number:", member_number, "type:", type(member_number))
print("Points:", points, "type:", type(points))
print("Active Status:", is_active, "type:", type(is_active))

print("Member:" + name)

print(name[0:3])
print(club[-1])
print(str(member_number))

print("===== CLUB BADGE =====")

print(name , "," , club , "," , member_number , "," , points , "," , is_active)



# ================================
# SCHOOL CLUB MEMBER BADGE
# ================================

# ---------- PART 1: member details ----------
# YOUR CODE HERE
# Ask for the member name and the club name with input().
# Save each answer in its own variable.

# ---------- PART 2: data types ----------
# YOUR CODE HERE
# Make member_number = 8, points = 9.5 and is_active = True.
# Print each one with its data type, using type().

# ---------- PART 3: badge code ----------
# YOUR CODE HERE
# Join: the first 3 letters of the name,
#       the last letter of the club,
#       and the member number turned into text.
# Save it in badge_code and print it.

# ---------- PART 4: final badge ----------
#print("===== CLUB BADGE =====")
# YOUR CODE HERE
# Print four lines: Member, Club, Code and Points | Active.
# Join the words and the values with +.
