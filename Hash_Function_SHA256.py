# import sha256
from hashlib import sha256
# text to hash
text = "I am excited to learn about blockchain!"

"""Since Python 3.0, strings are stored as Unicode, i.e. each character in the string is represented by a code point.\
So, each string is just a sequence of Unicode code points. For efficient storage of these strings, the sequence of code\
points are converted into set of bytes. The process is known as encoding."""

hash_result = sha256(text.encode())
res = hash_result.hexdigest()
# print result
#print (hash_result)
print(res)
