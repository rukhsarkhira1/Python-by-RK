s1="   Extra space is removed from the beginnig"
print(s1.strip())

s2="UPPER CASE TO LOWER CASE"
print(s2.lower())
print(s2.casefold())

s3="lower case to upper case"
print(s3.upper())

s4='first letter is capitalized'
print(s4.capitalize())

s5='Counts all the characters in a string'
print(len(s5))

s6='counts only given character/word/whitespace'
print(s6.count('o'))

s7='Replace given character/word/whitespace'
print(s7.replace('Replace','Replaces'))
print(s7.replace(' ','-'))

s8_a="Concat"
s8_b="ination"
print(s8_a+s8_b)

s9='25'
str="Hi , I'm Alice , I'm {}."

print(str.format(s9))       #OR
print(f"Hi , I'm David , I'm {s9}.") 


s10="Checks if it really ends with given character."
print(s10.endswith('.'))
print(s10.startswith('c'))

s11="find() and index() works similarly which returns index of a given character/word"
print(s11.find('returns'))
print(s11.index('given'))

s12="first character is capitalized of each string"
print(s12.title())

s13="string splitting example"
print(len(s13))
print(s13.split('t'))
print(s13.split(' '))
print(s13[5:])
print(s13[:25])
print(s13[:])

s14="hello"
print(s14.isalnum())
print(s14.isdigit())
print(s14.istitle())



