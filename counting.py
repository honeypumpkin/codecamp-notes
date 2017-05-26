test_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."

def count_chars(mess):
    
    # need to make dictionary
    counts = {}

    # loop over string
    for char in mess:
       
        # for each character, increment a counter in dictionary 
        # handle the situation where we're seeing a char for first time
        # existing_count = counts.get(char, 0) # reading something from the dictionary
        # print(counts[char]) can also use to read as well
        # counts[char] = existing_count + 1 # assigning a value to a key in the dictionary
        # OR
        counts[char] = counts.get(char, 0) + 1

        return counts

# print out results using a for loop
test_counts = count_chars(test_string)

#method 1
#for char, count in text_counts.items():

#method 2
#for char in test_counts.keys():
 #   count = test_counts[char]

#method 3
for char in test_counts:
    count = test_counts[char]
    print(char + " : ", count)
