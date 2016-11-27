import hashlib

#defining hash functions that use string as input

def hash_md5(pw):    
    return hashlib.md5(pw.encode('utf-8')).hexdigest().upper()

def hash_sha1(pw):    
    return hashlib.sha1(pw.encode('utf-8')).hexdigest().upper()

def hash_sha224(pw):    
    return hashlib.sha224(pw.encode('utf-8')).hexdigest().upper()

def hash_sha256(pw):    
    return hashlib.sha256(pw.encode('utf-8')).hexdigest().upper()

def hash_sha384(pw):    
    return hashlib.sha384(pw.encode('utf-8')).hexdigest().upper()

def hash_sha512(pw):    
    return hashlib.sha512(pw.encode('utf-8')).hexdigest().upper()

#asking for a string input and printing various hash digests

print("Text to hash:")
hashInput=input()

dig_md5=hash_md5(hashInput)
dig_sha1=hash_sha1(hashInput)
dig_sha224=hash_sha224(hashInput)
dig_sha256=hash_sha256(hashInput)
dig_sha384=hash_sha384(hashInput)
dig_sha512=hash_sha512(hashInput)

print("MD5: "+dig_md5+"\n")
print("SHA1: "+dig_sha1+"\n")
print("SHA224: "+dig_sha224+"\n")
print("SHA256: "+dig_sha256+"\n")
print("SHA384: "+dig_sha384+"\n")
print("SHA512: "+dig_sha512)



