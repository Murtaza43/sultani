#Regex
#1
import re
pattern = r'ab*'
string = "abbb"
if re.fullmatch(pattern, string):
    print("Match")
else:
    print("Not match")
#2
import re
pattern = r'ab{2,3}'
string = "abbb"
if re.fullmatch(pattern, string):
    print("Match")
else:
    print("Not match")
#3
import re
text = "hello_world abc_def ghi"
matches = re.findall(r'[a-z]+_[a-z]+', text)
print(matches)
#4
import re
text = "Hello there AreYouFine GoodDay"
matches = re.findall(r'[A-Z][a-z]+', text)
print(matches)
#5
import re
pattern = r'a.*b'
string = "aXYZb"
if re.fullmatch(pattern, string):
    print("Match")
else:
    print("Not match")
#6
import re
text = "Hello, how are you. I am fine"
result = re.sub(r'[ ,.]', ':', text)
print(result)
#7
def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])
print(snake_to_camel("my_variable_name"))
#8
import re
text = "SplitAtUpperCaseLetters"
result = re.findall(r'[A-Z][a-z]*', text)
print(result)
#9
import re
text = "ThisIsCamelCaseText"
result = re.sub(r'([A-Z])', r' \1', text).strip()
print(result)
#10
import re
def camel_to_snake(name):
    return re.sub(r'([A-Z])', r'_\1', name).lower()
print(camel_to_snake("camelCaseToSnake"))