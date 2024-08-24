
#
# class SecretKeyGenerator(object):
#     @classmethod
#     def decryptKey(cls,key:str):
#
#         org_key=list()
#         st_key=""
#
#         for i in key:
#             if i.isdigit():
#                 org_key.append(int(i)+7)
#             if i.isalnum():
#                 org_key.append(chr(ord(i)+7))
#
#         for j in org_key:
#             st_key+=str(j)
#         return st_key

import cryptocode

# Encrypt a string
# str_encoded = cryptocode.encrypt("3e584c002b4a3eded2ecc0434764449e0e1940962b7a6b16958cb81bbca02a59", "wow")

# Decrypt the string
str_decoded = cryptocode.decrypt("8ilZnahVlSIItn8Kbgd5m+zLw1rr/0airDevriF1DxfYPj1PzgO4tghsF9U12CC2TX9YcvoiN8DjIraCate1SQ==*i5ait7ALK9q5jEjBLGMzrw==*CBHmIKgCUp9GZcm+onae+A==*JxRzM2raQaPL8sgEGentcg==", "wow")

# print(f"Encrypted: {str_encoded}")
print(f"Decrypted: {str_decoded}")

# if __name__=="__main__":
#     obj = SecretKeyGenerator()
#     key = "3e584c002b4a3eded2ecc0434764449e0e1940962b7a6b16958cb81bbca02a59"
#     print(obj.decryptKey(key))