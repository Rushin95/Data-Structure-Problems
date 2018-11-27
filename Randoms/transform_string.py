# Transform string to a new string where the if the alphabet is repeated you increase the alphabet value by the count of that alphabet till that point

input_string = 'cacaca'
output_string = ''
dict = {}
print 'input_string:',input_string
for letter in input_string:
  if letter not in dict:
    output_string+= letter
    dict[letter] = 1
  else:
    count = dict[letter]
    new_letter = chr((ord(letter) - ord('a') + count) % 26 + ord('a'))
    output_string += new_letter
    dict[letter]+=1
print 'output_string:',output_string
