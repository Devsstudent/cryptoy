from cryptography.hazmat.primitives.ciphers.aead import (
    AESGCM,
)


def encrypt(msg: bytes, key: bytes, nonce: bytes) -> bytes:
    pass


def decrypt(msg: bytes, key: bytes, nonce: bytes) -> bytes:
    pass
