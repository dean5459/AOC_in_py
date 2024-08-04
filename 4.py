import hashlib

index = 0
secret_code = 'ckczppom'

while index < 99000000:
    hash_check = secret_code + str(index)
    result = hashlib.md5(hash_check.encode()).hexdigest()
    
    if result[0:6] == '000000':
        break
    else:
        index = index + 1

print(index)