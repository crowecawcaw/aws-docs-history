# Encrypt, Decrypt and Re-encrypt data

Encryption and Decryption methods can be used to encrypt or decrypt data using a variety of symmetric and asymmetric techniques
including TDES, AES and RSA. These methods also support keys derived using [DUKPT](terminology.md#terms.dukpt "terminology.md#terms.dukpt") and [EMV](terminology.md#terms.emv "terminology.md#terms.emv") techniques.
For use cases where you wish to secure data under a new key without exposing the underlying data, the ReEncrypt command can also be used.

###### Note

When using the encrypt/decrypt functions, all inputs are assumed to be in hexBinary - for instance a value of 1 will be input as 31 (hex) and a lower case t is represented as 74 (hex).
All outputs are in hexBinary as well.

For details on all available options, please consult the API Guide for [Encrypt](../DataAPIReference/API_EncryptData.md "../DataAPIReference/API_EncryptData.md"),
[Decrypt](../DataAPIReference/API_DecryptData.md "../DataAPIReference/API_DecryptData.md"),
and [Re-Encrypt](../DataAPIReference/API_ReEncryptData.md "../DataAPIReference/API_ReEncryptData.md").

###### Topics

- [Encrypt data](encrypt-data.md "encrypt-data.md")
- [Decrypt data](decrypt-data.md "decrypt-data.md")
