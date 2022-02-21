# formatted Strings

first = 'john'
last = 'smith'

#john [smith] is a coder

message = first+ '['+ last + '] is a coder'

#this is not a good idea,, so we use formatted strings

msg = f'{first}[{last}] is a coder'
# in this method we use f as a prefix for string statement and insert variables inside curly braces

print(message)
print(msg)