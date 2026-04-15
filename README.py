# --------------------------
# PART 1: IDENTIFY & CREATE
# --------------------------

# 1. A tuple of 5 favorite fruits
fruits = ("apple", "banana", "mango", "grapes", "orange")
print("Tuple:", fruits)

# 2. A list of 5 daily tasks
tasks = ["Wake up", "Eat breakfast", "Study", "Exercise", "Sleep"]
print("List:", tasks)

# 3. A set of unique numbers from [1, 2, 2, 3, 4, 4, 5]
numbers = {1, 2, 2, 3, 4, 4, 5}
# Or using set(): numbers = set([1, 2, 2, 3, 4, 4, 5])
print("Set:", numbers)

# 4. A dictionary with keys: "name", "age", "course"
student = {
    "name": "John Ramiel",
    "age": 19,
    "course": "BSIT"
}
print("Dictionary:", student)
print("\n" + "-"*40 + "\n")

# --------------------------
# PART 2: MANIPULATION CHALLENGE
# --------------------------

# --- LIST TASKS ---
print("--- LIST OPERATIONS ---")
print("Original:", tasks)

# Add a new task
tasks.append("Read book")
print("After adding:", tasks)

# Remove one task
tasks.remove("Exercise")
print("After removing:", tasks)

# Sort the list
tasks.sort()
print("After sorting:", tasks)
print("\n")

# --- TUPLE TASKS ---
print("--- TUPLE OPERATIONS ---")
try:
    # Trying to change a value
    fruits[0] = "pineapple"
except TypeError as e:
    print("Error:", e)
    print("Explanation: Tuples are immutable, meaning their values cannot be changed once created.")
print("\n")

# --- SET TASKS ---
print("--- SET OPERATIONS ---")
print("Original:", numbers)

# Add a number
numbers.add(6)
print("After adding 6:", numbers)

# Remove a number
numbers.discard(3)
print("After removing 3:", numbers)

# Show how duplicates are removed
test_list = [1, 2, 2, 3, 3, 3]
test_set = set(test_list)
print(f"List with duplicates: {test_list}")
print(f"Converted to Set: {test_set}  (Duplicates are automatically removed)")
print("\n")

# --- DICTIONARY TASKS ---
print("--- DICTIONARY OPERATIONS ---")
print("Original:", student)

# Add a new key "grade"
student["grade"] = "A"

# Update "age"
student["age"] = 21

# Print all keys and values
print("Updated Dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")
