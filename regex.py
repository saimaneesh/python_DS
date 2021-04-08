import re
def removeZeros(ip):
    print(re.match(r'\d0+',ip).group())
    new_ip = re.sub(r'0+(\d)', r'\1', ip)
    return new_ip
# driver code
# example1
ip ="100.020.003.400"
print(removeZeros(ip))

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print(match.group()) ## 'b@google'
t="this is is is is is 0 85 89 2 6 8"


m=re.findall("..",t)
print(m)