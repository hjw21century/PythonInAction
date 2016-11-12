#pythonsheets.com code snippet 

#Encode: unicode code point to bytes
s = u'咖啡'
print(type(s.encode('utf-8')))

#Decode: bytes to unicode code point
s2 = bytes('咖啡', encoding = 'utf-8')
print(s2.decode('utf-8'))

#Get unicode code Point
s3 = u'咖啡 coffee'
for _c in s3: print('U+%04x' % ord(_c))

#python2 str is equivalent to byte string
#python3 str is equivalent to unicode string
print(len(s3))
bs = bytes(s3, encoding='utf-8')
print(bs)
print(len(bs))

#unicode normalization
u1 = 'Café'
u2 = 'Cafe\u0301'
print(len(u1))
print(len(u2))
from unicodedata import normalize
s1 = normalize('NFC', u1)
s2 = normalize('NFC', u2)
print(s1 == s2)
