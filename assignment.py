'''import random

# Generate a random integer between 1 and 10 (inclusive)
random_number = random.randint(1, 10)

print("Random Number:", random_number)

# Generate a random floating-point number between 0 and 1
random_float = random.random()

print("Random Float:", random_float)

# Shuffle a list randomly
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)

print("Shuffled List:", my_list)'''

import os

# Specify the directory path
directory_path = '/path/to/your/directory'

# Check if the directory exists
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    # Get a list of files in the directory
    file_list = os.listdir(directory_path)

    # Print the list of files
    print(f"Files in {directory_path}:")
    for file in file_list:
        print(file)
else:
    print(f"The directory {directory_path} does not exist.")

