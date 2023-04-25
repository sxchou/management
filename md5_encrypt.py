import hashlib

SECRET_KEY = 'django-insecure-l3=cr9v31ptrp@$(b+-()-@tgs^@s2&*#%(id)gg^cb=%gb=5-'


def md5(data_string):
    obj = hashlib.md5(SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()


v = md5("123")
print(v)
