import requests
import time
import hashlib

def hash_password(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1[:5], sha1[5:]

def check_pwned_password(password):
    first5, tail = hash_password(password)
    url = f"https://api.pwnedpasswords.com/range/{first5}"
    response = requests.get(url)
    if response.status_code != 200:
        return False, "Request failed to API", None
    hashes = (line.split(':') for line in response.text.splitlines())
    for suffix, count in hashes:
        if suffix == tail:
            return True, "Success.", int(count)
    return True, "Success.", None

