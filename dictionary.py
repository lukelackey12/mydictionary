# Create the initial student dictionary
student = {
    "name": 'Luke Lackey',
    "age": 22,
    "major": "MIS",
    "hobbies": ["Basketball", "Photography", "Reading"]
}

# Add the state of residence
student["State"] = "Texas"

# Update age to current age + 1
student["age"] += 1

# Loop to print key-value pairs
for topic in student:
    answer = student[topic]
    print(f"{topic}: {answer}")

