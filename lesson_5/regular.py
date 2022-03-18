import re

text = 'Hello! my name is Jack!'

result = re.search('!', text)

print(text[result.start()])

result = re.findall('m', text)

print(result)




