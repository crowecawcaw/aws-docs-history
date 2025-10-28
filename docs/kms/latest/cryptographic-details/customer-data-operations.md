# Customer data operations

After you have established a KMS key, it can be used to perform cryptographic operations.
Whenever data is encrypted under a KMS key, the resulting object is a customer ciphertext. The
ciphertext contains two sections: an unencrypted header (or cleartext) portion, protected by the
authenticated encryption scheme as the additional authenticated data, and an encrypted portion.
The cleartext portion includes the HBK identifier (HBKID). These two immutable fields of the
ciphertext value help ensure that AWS KMS can decrypt the object in the future.

###### Topics

- [Generating data keys](generating-data-keys.md "generating-data-keys.md")
- [Encrypt](encrypt-operation.md "encrypt-operation.md")
- [Decrypt](decrypt-operation.md "decrypt-operation.md")
- [Reencrypting an encrypted object](reencrypting-an-encrypted-object.md "reencrypting-an-encrypted-object.md")
