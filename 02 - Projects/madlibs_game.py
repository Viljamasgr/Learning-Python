# Mad Libs Game
# A word game where the player fills in blanks with random words to create a fun story.

# Get user input for different word types
adjective1 = input("Enter an adjective (e.g., happy, smelly): ")  # Describes something
noun1 = input("Enter a noun (e.g., cat, house): ")  # A person, place, or thing
adjective2 = input("Enter another adjective (e.g., fuzzy, gigantic): ")  # Another description
verb1 = input("Enter a verb ending with 'ing' (e.g., running, jumping): ")  # Action in progress
adjective3 = input("Enter one more adjective (e.g., surprised, excited): ")  # Final description

# Print the completed story
print(f"\nToday I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}.")
print(f"The {noun1} was {adjective2} and {verb1}.")
print(f"I was {adjective3}!")

# The game dynamically inserts the user's words into a silly, creative story.