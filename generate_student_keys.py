from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096
)

# Serialize private key
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Serialize public key
public_pem = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save private key
with open("student_keys/student_private_key.pem", "wb") as f:
    f.write(private_pem)

# Save public key
with open("student_keys/student_public_key.pem", "wb") as f:
    f.write(public_pem)

print("✔ RSA 4096-bit student keys generated successfully!")
