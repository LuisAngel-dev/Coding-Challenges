def word_counter():
    # Open the file
    try:
      with open('example.txt', 'r') as file:
          # Read the file and then split the contents into a list of words
          words = file.read().split()
          # Print the number of words
          print("The file has {} words.".format(len(words)))
    except FileNotFoundError:
        print("The file does not exist.")

word_counter()