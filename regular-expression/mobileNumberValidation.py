# 10 digit or 11 digit or 12 digit or 13 also
# ==============================================
# 10: 6 to 9, 9 digits
# 11: the first digit shoule be 0
# 12: the first 2 digits should be 91
# 13: the first 3 digits should be +91

import re
mobileNumber = input("Enter Mobile number to validation: ")
lengthOfNumber = len(mobileNumber)
regexPattern = None

if (lengthOfNumber == 10):
    regexPattern = re.findall(r'[6-9]\d{9}', mobileNumber)
elif (lengthOfNumber == 11):
    regexPattern = re.findall(r'0[6-9]\d{9}', mobileNumber)
elif (lengthOfNumber == 12):
    regexPattern = re.findall(r'91[6-9]\d{9}', mobileNumber)
elif (lengthOfNumber == 13):
    regexPattern = re.findall(r'[+91][6-9]\d{9}', mobileNumber)

if regexPattern:
    print(regexPattern[0])
else:
    print(f'{mobileNumber} not valid')
