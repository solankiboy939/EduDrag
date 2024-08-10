# Define the file path
file_path = 'its.txt'

# Define the text to search for and the text to replace it with
search_text = ']'
replace_text = '}'

# Read the contents of the file
with open(file_path, 'r') as file:
    file_contents = file.read()

# Replace the old text with the new text
file_contents = file_contents.replace(search_text, replace_text)

# Write the updated contents back to the file
with open(file_path, 'w') as file:
    file.write(file_contents)
