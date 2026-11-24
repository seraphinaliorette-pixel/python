Camera = 1
microphone = 2
storage = 4

approved_apps = ["coding app", "math app", "reading app", "science app",]
restricted_apps = ["gaming app", "shopping app", "social media app"]

requested_app = input("enter the app you want to access:")

print("\n -----  identity operator check--")
student_age = 11

if type(student_age) is int:
    print("the student age is stored as a number.")
    if type(student_age) is not str:
        print("the student age is not stored as text")

print("\n----  membership operator check--")
if requested_app is in approved_apps:
    print(<app> "is an approved student app.")
else:
    print(<app> "is not an approved student app.")
if requested_app is not in restricted_apps:
    prunt("the app is not in the restricted list.")
else:
    print("access denied because app restricted.")


print("\n--- app permission settings")
student_permissions = 0

print("permission bits:",
bin(student_permissions))
if student_permissions and Camera is not 0:
    print("camera permission: enabled")
if student_permissions and microphone is not 0:
    print("microphone permission: enabled")
if storage == "on":
    print("storage permission: enabled")
else:
    print("storage permission: disabled")
print("\n --- bit shift demonstration")
print("after left shift:") and bin(Camera << 1)

print("camera bit:", bin(Camera))

print("storage bit:", bin(storage))
print("after right shift:") and bin(storage >> 1)

print("\n -- final access result")
if requested_app is in approved_apps and not in restricted_apps:
    print("acess granted to", <app>)
else:
    print("access denied to", <app>)

