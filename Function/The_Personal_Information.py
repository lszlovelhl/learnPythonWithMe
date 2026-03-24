def personal_info(name, age=18, city="BeiJing"):
    return f"My name is {name}, I am {age} years old, and I live in {city}."

# Example usage:
print(personal_info("Alice"))
print(personal_info("Bob", 25))
print(personal_info("Charlie", city="Shanghai"))