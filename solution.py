# Write a function that takes a list of words and a dictionary where keys are the words and values are the number of occurrences of the word

def word_freq(words):
  # Create an empty dictionary to count the occurrences
  word_dict = {}
  
  #For each word in the word list:
    # If the word is already in the dictionary, increment the value by 1
    # If the word is new to the dictionary, add the word as a key with the value of 1
  
  for word in words:
    if word in word_dict:
      word_dict[word] += 1
    else:
      word_dict[word] = 1

  return word_dict

# Test function
words = ["cat", "dog", "pig", "dog", "dog", "cat"]

print(word_freq(words))