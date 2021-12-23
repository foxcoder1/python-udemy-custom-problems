# Read file contents
with open('input.txt', mode='r') as myfile:
    data = myfile.readlines()

#myfile = open('input.txt')
#data = myfile.readlines()
#myfile.close()
print(data)

# Convert list items to int
intList = [int(i) for i in data]
print(intList)

# Multiply data
print(intList[0])
print(intList[1])
number = intList[0] * intList[1]
print('The product is: ', number)

# Output to a new file
print(type(number))
converted_number = str(number)
print(type(converted_number))
with open('output.txt', mode='w') as f:
    f.write(converted_number)
