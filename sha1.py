import hashlib
yigit= "paluk-sifre"

print(hashlib.sha256(yigit.encode()).hexdigest())