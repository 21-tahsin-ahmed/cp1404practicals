name_to_age = {"Bill": 21, "Jane": 4, "Sven": 56}
key = input("Enter new name: ")
value = input("Enter new age: ")
name_to_age[key] = value
for key, value in name_to_age.items():
    print(f"{key}     -     {value}")
