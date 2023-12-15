import sys
import json

# Global variables
input_text = ""
words = []

# Function to combine command-line arguments into input_text
def get_input():
    global input_text

    for i, arg in enumerate(sys.argv):
        if i != 0:
            input_text += arg + " "

# Main function to get keywords
def get_keywords(loc_data_set):
    global input_text
    global words

    # Read data from the file and split using "|"
    unformatted_data = open(loc_data_set).read().replace("&", "e").split("\n")

    # Split using "$" and remove newline characters from each key
    unformatted_data_keys = unformatted_data[0].split("$")
    unformatted_data_keys = [key.replace("\n", "") for key in unformatted_data_keys]

    # Split using "$" and remove newline characters from each length
    unformatted_data_len = unformatted_data[1].split("$")
    unformatted_data_len = [length.replace("\n", "") for length in unformatted_data_len]

    # Remove the last item from the lists
    unformatted_data_keys = unformatted_data_keys[:-1]
    unformatted_data_len = unformatted_data_len[:-1]

    # Process the keys: split by ">" and convert the last part to a float
    data_keys = {key.split(">")[:-1][0]: float(key.split(">")[-1]) for key in unformatted_data_keys}

    # Process the lengths: split by ">" and convert the first part to an int
    # and the last part to a float
    data_len = {length.split(">")[0]: float(length.split(">")[1]) for length in unformatted_data_len}

    get_input()

    # Calculate the average value for missing keys in data_keys
    average_data_keys = sum(data_keys.values()) / len(data_keys) / 2

    # Process input_text
    input_text = input_text.replace("'", " ").replace(",", "").replace(".", "")
    words = input_text.split(" ")
    words = words[:-1]

    word_values = []
    keywords = []

    try:
        anz_keywords = round(data_len[str(len(input_text))])
    except:
        data_len[str(len(input_text))] = sum(data_len.values()) / len(data_len)
        anz_keywords = round(data_len[str(len(input_text))])

    # Populate word_values with rounded values of data_keys
    for w in words:
        try:
            word_values.append([round(data_keys.get(w, average_data_keys), 2), w])
        except:
            word_values.append([round(average_data_keys, 2), w])

    rel_val = 100

    # Generate keywords based on rel_val threshold
    while len(keywords) < anz_keywords:
        for word_id in range(len(word_values)):
            if word_values[word_id][0] >= rel_val and word_values[word_id][1] not in keywords:
                keywords.append(word_values[word_id][1])

        rel_val -= 0.01
    
    new_data = ""

    word_values.sort(reverse= True)

    # Prepare a string with the updated word_values
    for w in word_values:
        new_data += str(w[1]) + ">" + str(w[0]) + "$"

    new_data += "\n"

    # Prepare a string with the updated data_len
    for l in data_len:
        new_data += str(l) + ">" + str(round(data_len[l], 2)) + "$"

    # Store data_keys and data_len back into the file
    open("keywords.gpt", "w").write(new_data.replace("e", "&"))
    return keywords

# Call the function and print the result
print(get_keywords("keywords.gpt"))
