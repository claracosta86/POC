
with open('classes_interface.txt', 'r') as file:
      data = file.readlines()

single_line_code = ' '.join(line.strip() for line in data)
print(single_line_code)