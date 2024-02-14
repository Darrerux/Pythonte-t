# User input
noun1 = input("Enter the first noun: ")
noun2 = input("Enter the second noun: ")
adjective1 = input("Enter the first adjective: ")
adjective2 = input("Enter the second adjective: ")

# Define tthe 1st stanza
poem_stanza = """
The stars, like diamonds scattered on the sky,
Glint and shimmer in the velvet night.
A world of mystery and wonder unfolds,
Sparkling secrets in the pale moonlight.
"""

# Replace the words with user input using string formatting
modified_stanza = f"""
The {noun1}, like {adjective1} jewels scattered on the sky,
Glint and shimmer in the {adjective2} night.
A world of mystery and wonder unfolds,
Sparkling secrets in the pale {noun2} light.
"""

# Print the original and modified stanzas
print("\nOriginal stanza:")
print(poem_stanza)

print("\nModified stanza:")
print(modified_stanza)