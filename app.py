# Print built-in functions
print("Hello World!😍")
print("*" * 10)
print("Hello World!")

# variables formatting
x = 1
y = 2
unit_price = 10

# Variables
student_count = 1000
print(student_count)

# Strings
course = "Python Programming"

print(len(course))

print(course[0])

print(course[-2])

print(course[0:3])

# backsplash is used to escape the special characters
# text = "Python \"Programming" # double quotes
# text = "Python \nProgramming" # new line
text = "Python \tProgramming" # tab
# text = "Python \rProgramming" # carriage return
# text = "Python \bProgramming" # backspace
# text = "Python \fProgramming" # form feed
# text = "Python \nProgramming" # new line
# text = "Python \rProgramming" # carriage return
# text = "Python \bProgramming" # backspace
# text = "Python \fProgramming" # form feed
print(text)

print(text.upper()) # convert to uppercase
print(text.lower()) # convert to lowercase
print(text.title()) # convert to title case
print(text.strip()) # remove whitespace
print(text.find("P")) # find the index of the first occurrence of the substring
print(text.replace("P", "J")) # replace the first occurrence of the substring
print("Python" in text) # check if the substring is in the string
print("swift" not in text) # check if the substring is not in the string

# Formatting strings(concatenation)
first = "John"
last = "Smith"
full = first + " " + last
print(full)

