import random
import sys

# Number of pokemon you can choose from in each round of a draft
DRAFT_OPTION_COUNT = 4

# Number of rounds in a draft
DRAFT_ROUNDS = 8

# Number of random pokemon to generate when using "random"
RANDOM_COUNT = 18

# Filepath to database
DATABASE = "databases/fully_evolved_no_restricted.txt"

def main():
	if (len(sys.argv) != 2):
		print("Usage: python random_poke.py format")
		exit(1)

	pokemon = []

	# Parse player format
	if (sys.argv[1] == "d" or sys.argv[1] == "draft"):
		pokemon = draft(DRAFT_OPTION_COUNT, DRAFT_ROUNDS)

	elif (sys.argv[1] == "r" or sys.argv[1] == "rand" or sys.argv[1] == "random"):
		pokemon = random_pokemon(RANDOM_COUNT)

	else:
		print("Please specify a valid format.")
		exit(1)

	print("Your Pokémon:\n")

	for mon in pokemon:
		print(mon)

	print("\nGood luck!")


def draft(options, rounds):
	"""Lefts the player draft, then returns a list containing the name of the drafted pokemon."""

	print("===================================\n")

	picks = []

	for i in range(rounds):
		options = random_pokemon(4)

		# Print options
		print(f"Pick {i + 1}:")
		print(f"A. {options[0]}")
		print(f"B. {options[1]}")
		print(f"C. {options[2]}")
		print(f"D. {options[3]}")
		print()

		choice = ""

		# Get player input
		while (True):
			choice = input("Choose one to draft: ")

			if (choice == "A" or choice == "B" or choice == "C" or choice == "D"):
				break

			print("Please enter A, B, C, or D.")

		# Add player choice to list
		if (choice == "A"):
			picks.append(options[0])
			print(f"You drafted {options[0]}!")
		elif (choice == "B"):
			picks.append(options[1])
			print(f"You drafted {options[1]}!")
		elif (choice == "C"):
			picks.append(options[2])
			print(f"You drafted {options[2]}!")
		elif (choice == "D"):
			picks.append(options[3])
			print(f"You drafted {options[3]}!")

		print()

	print("===================================\n")

	return picks


def random_pokemon(count):
	"""Returns a list containing the names of random pokemon."""

	pokemon = []
	line_count = 0

	# Open database into a list
	with open(DATABASE) as database:
		for line in database:
			pokemon.append(line.strip())
			line_count += 1

	if count >= line_count:
		print(f"Error: {count} random Pokémon requested, but only {line_count} exist in database")
		exit(1)

	ids = []

	# Get list of unique, random integers
	for i in range(count):
		while True:
			rand_id = random.randint(0, line_count - 1)

			if not rand_id in ids:
				ids.append(rand_id)
				break

	ids.sort()
	out = []

	# Turn random numbers into pokemon names, and add them to the output array
	for i in range(count):
		out.append(pokemon[ids[i]])

	return out

main()