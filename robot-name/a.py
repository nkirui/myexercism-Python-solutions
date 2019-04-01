import re

wood = 'hello 42 I\'m a 32 string 30'
print(re.findall(r'\d$', wood))