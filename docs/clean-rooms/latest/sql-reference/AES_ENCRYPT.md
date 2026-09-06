

# AES\_ENCRYPT function
<a name="AES_ENCRYPT"></a>

The AES\_ENCRYPT function is used for encrypting data using the Advanced Encryption Standard (AES) algorithm.

## Syntax
<a name="AES_ENCRYPT-syntax"></a>

```
aes_encrypt(expr, key[, mode[, padding[, iv[, aad]]]])
```

## Arguments
<a name="AES_ENCRYPT-arguments"></a>

 *expr*   
The binary value to encrypt.

 *key*   
The passphrase to use to encrypt the data.  
Key lengths of 16, 24 and 32 bits are supported.

 *mode*   
Specifies which block cipher mode should be used to encrypt messages.   
Valid modes: ECB (Electronic CodeBook), GCM (Galois/Counter Mode), CBC (Cipher-Block Chaining).

 *padding*   
Specifies how to pad messages whose length isn't a multiple of the block size.   
Valid values: PKCS, NONE, DEFAULT.   
The DEFAULT padding means PKCS (Public Key Cryptography Standards) for ECB, NONE for GCM and PKCS for CBC.  
Supported combinations of (*mode*, *padding*) are ('ECB', 'PKCS'), ('GCM', 'NONE') and ('CBC', 'PKCS').

 *iv*   
Optional initialization vector (IV). Only supported for CBC and GCM modes.   
Valid values: 12-bytes long for GCM and 16 bytes for CBC.

 *aad*   
Optional additional authenticated data (AAD). Only supported for GCM mode. This can be any free-form input and must be provided for both encryption and decryption.

## Return type
<a name="AES_ENCRYPT-returm-type"></a>

The AES\_ENCRYPT function returns an encrypted value of *expr* using AES in given mode with the specified padding.

## Examples
<a name="AES_ENCRYPT-example"></a>

The following example demonstrates how to use the Spark SQL AES\_ENCRYPT function to securely encrypt a string of data (in this case, the word "Spark") using a specified encryption key. The resulting ciphertext is then Base64-encoded to make it easier to store or transmit.

```
SELECT base64(aes_encrypt('Spark', 'abcdefghijklmnop'));
  4A5jOAh9FNGwoMeuJukfllrLdHEZxA2DyuSQAWz77dfn
```

The following example demonstrates how to use the Spark SQL AES\_ENCRYPT function to securely encrypt a string of data (in this case, the word "Spark") using a specified encryption key. The resulting ciphertext is then represented in hexadecimal format, which can be useful for tasks such as data storage, transmission, or debugging.

```
SELECT hex(aes_encrypt('Spark', '0000111122223333'));
 83F16B2AA704794132802D248E6BFD4E380078182D1544813898AC97E709B28A94
```

The following example demonstrates how to use the Spark SQL AES\_ENCRYPT function to securely encrypt a string of data (in this case, "Spark SQL") using a specified encryption key, encryption mode, and padding mode. The resulting ciphertext is then Base64-encoded to make it easier to store or transmit.

```
SELECT base64(aes_encrypt('Spark SQL', '1234567890abcdef', 'ECB', 'PKCS'));
 3lmwu+Mw0H3fi5NDvcu9lg==
```