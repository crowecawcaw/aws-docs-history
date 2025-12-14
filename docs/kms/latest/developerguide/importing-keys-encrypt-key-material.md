# Step 3: Encrypt the

key material

After you [download the public key
and import token](importing-keys-get-public-key-and-token.md "importing-keys-get-public-key-and-token.md"), encrypt your key material using the public key that you downloaded
and the wrapping algorithm that you specified. If you need to replace the public key or import
token, or change the wrapping algorithm, you must download a new public key and import token.
For information about the public keys and wrapping algorithms that AWS KMS supports, see [Select a wrapping public key spec](importing-keys-get-public-key-and-token.md#select-wrapping-key-spec "importing-keys-get-public-key-and-token.md#select-wrapping-key-spec") and [Select a wrapping algorithm](importing-keys-get-public-key-and-token.md#select-wrapping-algorithm "importing-keys-get-public-key-and-token.md#select-wrapping-algorithm").

The key material must be in binary format. For detailed information, see [Requirements for imported key
material](importing-keys-conceptual.md#importing-keys-material-requirements "importing-keys-conceptual.md#importing-keys-material-requirements").

###### Note

For asymmetric key pairs, encrypt and import only the private key. AWS KMS derives the
public key from the private key.

The following combination is NOT supported: ECC_NIST_P521 key material, the RSA_2048 public wrapping key spec, and an RSAES_OAEP_SHA\_\* wrapping algorithm.

You cannot directly wrap ECC_NIST_P521 key material with a RSA_2048 public wrapping key. Use a larger wrapping key or an RSA_AES_KEY_WRAP_SHA\_\* wrapping algorithm.

The RSA_AES_KEY_WRAP_SHA_256 and RSA_AES_KEY_WRAP_SHA_1
wrapping algorithms are not supported in China Regions.

Typically, you encrypt your key material when you export it from your hardware security
module (HSM) or key management system. For information about how to export key material in
binary format, see the documentation for your HSM or key management system. You can also refer
to the following section that provides a proof of concept demonstration using OpenSSL.

When you encrypt your key material, use the same wrapping algorithm that you specified when
you [downloaded the public key and import
token](importing-keys-get-public-key-and-token.md "importing-keys-get-public-key-and-token.md"). To find the wrapping algorithm that you specified, see the CloudTrail log event for
the associated [GetParametersForImport](../APIReference/API_GetParametersForImport.md "../APIReference/API_GetParametersForImport.md") request.

## Generate key material for testing

The following OpenSSL commands generate key material of each supported type for testing.
These examples are provided only for testing and proof-of-concept demonstrations. For
production systems, use a more secure method to generate your key material, such as a hardware
security module or key management system.

To convert the private keys of asymmetric key pairs into DER-encoded format, pipe the key
material generation command to the following `openssl pkcs8` command. The
`topk8` parameter directs OpenSSL to take a private key as input and return a
PKCS#8 formatted key. (The default behavior is the opposite.)

```
openssl pkcs8 -topk8 -outform der -nocrypt
```

The following commands generate test key material for each of the supported key
types.

- Symmetric encryption key (32 bytes)

This command generates a 256-bit symmetric key (32-byte random string) and saves it
in the `PlaintextKeyMaterial.bin` file. You do not need to encode this key
material.

```
openssl rand -out PlaintextKeyMaterial.bin **32**
```

In China Regions only, you must generate a 128-bit symmetric key (16-byte random
string).

```
openssl rand -out PlaintextKeyMaterial.bin **16**
```

- HMAC keys

This command generates a random byte string of the specified size. You do not need
to encode this key material.

The length of your HMAC key must match the length defined by the key spec of the
KMS key. For example, if the KMS key is HMAC_384, you must import a 384-bit
(48-byte) key.

```
openssl rand -out HMAC_224_PlaintextKey.bin **28**

openssl rand -out HMAC_256_PlaintextKey.bin **32**

openssl rand -out HMAC_384_PlaintextKey.bin **48**

openssl rand -out HMAC_512_PlaintextKey.bin **64**
```

- RSA private keys

```
openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:**2048** | openssl pkcs8 -topk8 -outform der -nocrypt > RSA_2048_PrivateKey.der

openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:**3072** | openssl pkcs8 -topk8 -outform der -nocrypt > RSA_3072_PrivateKey.der

openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:**4096** | openssl pkcs8 -topk8 -outform der -nocrypt > RSA_4096_PrivateKey.der
```

- ECC private keys

```
openssl genpkey -algorithm ec -pkeyopt ec_paramgen_curve:**P-256** | openssl pkcs8 -topk8 -outform der -nocrypt > ECC_NIST_P256_PrivateKey.der

openssl genpkey -algorithm ec -pkeyopt ec_paramgen_curve:**P-384** | openssl pkcs8 -topk8 -outform der -nocrypt > ECC_NIST_P384_PrivateKey.der

openssl genpkey -algorithm ec -pkeyopt ec_paramgen_curve:**P-521** | openssl pkcs8 -topk8 -outform der -nocrypt > ECC_NIST_P521_PrivateKey.der

openssl genpkey -algorithm ec -pkeyopt ec_paramgen_curve:**secp256k1** | openssl pkcs8 -topk8 -outform der -nocrypt > ECC_SECG_P256K1_PrivateKey.der
```

- SM2 private keys (China Regions only)

```
openssl genpkey -algorithm ec -pkeyopt ec_paramgen_curve:**sm2** | openssl pkcs8 -topk8 -outform der -nocrypt > SM2_PrivateKey.der
```

[Show moreShow less](# "#")

## Examples of encrypting key

material with OpenSSL

The following examples show how to use [OpenSSL](https://openssl.org/ "https://openssl.org/")
to encrypt your key material with the public key that you downloaded. To encrypt your key
material using an SM2 public key (China Regions only), use the [SM2OfflineOperationHelper class](offline-operations.md#key-spec-sm-offline-helper "offline-operations.md#key-spec-sm-offline-helper"). For more information on the key material types that
each wrapping algorithm supports, see [Select a wrapping algorithm](importing-keys-get-public-key-and-token.md#select-wrapping-algorithm "importing-keys-get-public-key-and-token.md#select-wrapping-algorithm").

###### Important

These examples are a proof of concept demonstration only. For production systems, use a
more secure method (such as a commercial HSM or key management system) to generate and store
your key material.

The following combination is NOT supported: ECC_NIST_P521 key material, the RSA_2048 public wrapping key spec, and an RSAES_OAEP_SHA\_\* wrapping algorithm.

You cannot directly wrap ECC_NIST_P521 key material with a RSA_2048 public wrapping key. Use a larger wrapping key or an RSA_AES_KEY_WRAP_SHA\_\* wrapping algorithm.

RSAES_OAEP_SHA_1
AWS KMS supports the RSAES_OAEP_SHA_1 for symmetric encryption keys
(SYMMETRIC_DEFAULT), elliptic curve (ECC) private keys, SM2 private keys, and HMAC keys.

RSAES_OAEP_SHA_1 is not supported for RSA private keys. Also, you cannot use an
RSA_2048 public wrapping key with any RSAES_OAEP_SHA\_\* wrapping algorithm to wrap an
ECC_NIST_P521 (secp521r1) private key. You must use a larger public wrapping key or an
RSA_AES_KEY_WRAP wrapping algorithm.

The following example encrypts your key material with the [public key that you
downloaded](importing-keys-get-public-key-and-token.md "importing-keys-get-public-key-and-token.md") and the RSAES_OAEP_SHA_1 wrapping algorithm, and saves it in the
`EncryptedKeyMaterial.bin` file.

In this example:

- `WrappingPublicKey.bin` is the file that
  contains the downloaded wrapping public key.
- `PlaintextKeyMaterial.bin` is the file
  that contains the key material that you are encrypting, such as
  `PlaintextKeyMaterial.bin`, `HMAC_384_PlaintextKey.bin` or
  `ECC_NIST_P521_PrivateKey.der`.

```
`$` `openssl pkeyutl \
 -encrypt \
 -in `PlaintextKeyMaterial.bin` \
 -out EncryptedKeyMaterial.bin \
 -inkey `WrappingPublicKey.bin` \
 -keyform DER \
 -pubin \
 -pkeyopt rsa_padding_mode:oaep \
 -pkeyopt rsa_oaep_md:sha1`
```

RSAES_OAEP_SHA_256
AWS KMS supports the RSAES_OAEP_SHA_256 for symmetric encryption keys
(SYMMETRIC_DEFAULT), elliptic curve (ECC) private keys, SM2 private keys, and HMAC keys.

RSAES_OAEP_SHA_256 is not supported for RSA private keys. Also, you cannot use an
RSA_2048 public wrapping key with any RSAES_OAEP_SHA\_\* wrapping algorithm to wrap an
ECC_NIST_P521 (secp521r1) private key. You must use a larger public key or an
RSA_AES_KEY_WRAP wrapping algorithm.

The following example encrypts key material with the [public key that you
downloaded](importing-keys-get-public-key-and-token.md "importing-keys-get-public-key-and-token.md") and the RSAES_OAEP_SHA_256 wrapping algorithm, and saves it in the
`EncryptedKeyMaterial.bin` file.

In this example:

- `WrappingPublicKey.bin` is the file that
  contains the downloaded public wrapping key. If you downloaded the public key from
  the console, this file is named
  `wrappingKey_`KMS key*key_ID`*`timestamp``
(for example,
`wrappingKey_f44c4e20-f83c-48f4-adc6-a1ef38829760_0809092909`).
- `PlaintextKeyMaterial.bin` is the file
  that contains the key material that you are encrypting, such as
  `PlaintextKeyMaterial.bin`, `HMAC_384_PlaintextKey.bin`, or
  `ECC_NIST_P521_PrivateKey.der`.

```
`$` `openssl pkeyutl \
 -encrypt \
 -in `PlaintextKeyMaterial.bin` \
 -out EncryptedKeyMaterial.bin \
 -inkey `WrappingPublicKey.bin` \
 -keyform DER \
 -pubin \
 -pkeyopt rsa_padding_mode:oaep \
 -pkeyopt rsa_oaep_md:sha256 \
 -pkeyopt rsa_mgf1_md:sha256`
```

RSA_AES_KEY_WRAP_SHA_1
The RSA_AES_KEY_WRAP_SHA_1 wrapping algorithm involves two encryption
operations.

1. Encrypt your key material with an AES symmetric key that you generate and an AES
   symmetric encryption algorithm.
2. Encrypt the AES symmetric key that you used with the public key that you
   downloaded and the RSAES_OAEP_SHA_1 wrapping algorithm.

The RSA_AES_KEY_WRAP_SHA_1 wrapping algorithm requires OpenSSL version 3._x_ or later.

1. ###### Generate a 256-bit AES symmetric encryption key

This command generates an AES symmetric encryption key consisting of 256 random
bits, and saves it in the `aes-key.bin` file

```
# Generate a 32-byte AES symmetric encryption key
`$` `openssl rand -out aes-key.bin 32`
```

2. ###### Encrypt your key material with the AES symmetric encryption key

This command encrypts your key material with the AES symmetric encryption key
and saves the encrypted key material in the `key-material-wrapped.bin`
file.

In this example command:

    * ``PlaintextKeyMaterial.bin`` is the file
     that contains the key material that you are importing, such as
     `PlaintextKeyMaterial.bin`, `HMAC_384_PlaintextKey.bin`,
     `RSA_3072_PrivateKey.der`, or
     `ECC_NIST_P521_PrivateKey.der`.
    * ``aes-key.bin`` is the file that
     contains 256-bit AES symmetric encryption key that you generated in the previous
     command.

```
# Encrypt your key material with the AES symmetric encryption key
``$` openssl enc -id-aes256-wrap-pad \
 -K "$(xxd -p < `aes-key.bin` | tr -d '\n')" \
 -iv A65959A6 \
 -in `PlaintextKeyMaterial.bin`\
 -out key-material-wrapped.bin`
```

3. ###### Encrypt your AES symmetric encryption key with the public key

This command encrypts your AES symmetric encryption key with the public key that
you downloaded and the RSAES_OAEP_SHA_1 wrapping algorithm, DER-encodes it, and save
it in the `aes-key-wrapped.bin` file.

In this example command:

    * ``WrappingPublicKey.bin`` is the file
     that contains the downloaded public wrapping key. If you downloaded the public
     key from the console, this file is named
     `wrappingKey_`KMS key_key_ID`_`timestamp``
     (for example,
     `wrappingKey_f44c4e20-f83c-48f4-adc6-a1ef38829760_0809092909`
    * ``aes-key.bin`` is the file that
     contains 256-bit AES symmetric encryption key that you generated in the first
     command in this example sequence.

```
# Encrypt your AES symmetric encryption key with the downloaded public key
`$` `openssl pkeyutl \
 -encrypt \
 -in `aes-key.bin` \
 -out aes-key-wrapped.bin \
 -inkey `WrappingPublicKey.bin` \
 -keyform DER \
 -pubin \
 -pkeyopt rsa_padding_mode:oaep \
 -pkeyopt rsa_oaep_md:sha1 \
 -pkeyopt rsa_mgf1_md:sha1`
```

4. ###### Generate the file to import

Concatenate the file with the encrypted key material and the file with the
encrypted AES key. Save them in the `EncryptedKeyMaterial.bin` file,
which is the file that you'll import in the [Step 4: Import the key material](importing-keys-import-key-material.md "importing-keys-import-key-material.md").

In this example command:

    * ``key-material-wrapped.bin`` is the file
     that contains your encrypted key material.
    * ``aes-key-wrapped.bin`` is the file that
     contains the encrypted AES encryption key.

```
# Combine the encrypted AES key and encrypted key material in a file
`$` `cat `aes-key-wrapped.bin` `key-material-wrapped.bin` > `EncryptedKeyMaterial.bin``
```

RSA_AES_KEY_WRAP_SHA_256
The RSA_AES_KEY_WRAP_SHA_256 wrapping algorithm involves two encryption
operations.

1. Encrypt your key material with an AES symmetric key that you generate and an AES
   symmetric encryption algorithm.
2. Encrypt the AES symmetric key that you used with the public key that you
   downloaded and the RSAES_OAEP_SHA_256 wrapping algorithm.

The RSA_AES_KEY_WRAP_SHA_256 wrapping algorithm requires OpenSSL version 3._x_ or later.

1. ###### Generate a 256-bit AES symmetric encryption key

This command generates an AES symmetric encryption key consisting of 256 random
bits, and saves it in the `aes-key.bin` file

```
# Generate a 32-byte AES symmetric encryption key
`$` `openssl rand -out aes-key.bin 32`
```

2. ###### Encrypt your key material with the AES symmetric encryption key

This command encrypts your key material with the AES symmetric encryption key
and saves the encrypted key material in the `key-material-wrapped.bin`
file.

In this example command:

    * ``PlaintextKeyMaterial.bin`` is the file
     that contains the key material that you are importing, such as
     `PlaintextKeyMaterial.bin`, `HMAC_384_PlaintextKey.bin`,
     `RSA_3072_PrivateKey.der`, or
     `ECC_NIST_P521_PrivateKey.der`.
    * ``aes-key.bin`` is the file that
     contains 256-bit AES symmetric encryption key that you generated in the previous
     command.

```
# Encrypt your key material with the AES symmetric encryption key
``$` openssl enc -id-aes256-wrap-pad \
 -K "$(xxd -p < `aes-key.bin` | tr -d '\n')" \
 -iv A65959A6 \
 -in `PlaintextKeyMaterial.bin`\
 -out key-material-wrapped.bin`
```

3. ###### Encrypt your AES symmetric encryption key with the public key

This command encrypts your AES symmetric encryption key with the public key that
you downloaded and the RSAES_OAEP_SHA_256 wrapping algorithm, DER-encodes it, and
save it in the `aes-key-wrapped.bin` file.

In this example command:

    * ``WrappingPublicKey.bin`` is the file
     that contains the downloaded public wrapping key. If you downloaded the public
     key from the console, this file is named
     `wrappingKey_`KMS key_key_ID`_`timestamp``
     (for example,
     `wrappingKey_f44c4e20-f83c-48f4-adc6-a1ef38829760_0809092909`
    * ``aes-key.bin`` is the file that
     contains 256-bit AES symmetric encryption key that you generated in the first
     command in this example sequence.

```
# Encrypt your AES symmetric encryption key with the downloaded public key
`$` `openssl pkeyutl \
 -encrypt \
 -in `aes-key.bin` \
 -out aes-key-wrapped.bin \
 -inkey `WrappingPublicKey.bin` \
 -keyform DER \
 -pubin \
 -pkeyopt rsa_padding_mode:oaep \
 -pkeyopt rsa_oaep_md:sha256 \
 -pkeyopt rsa_mgf1_md:sha256`
```

4. ###### Generate the file to import

Concatenate the file with the encrypted key material and the file with the
encrypted AES key. Save them in the
`EncryptedKeyMaterial.bin` file, which is the file that
you'll import in the [Step 4: Import the key material](importing-keys-import-key-material.md "importing-keys-import-key-material.md").

In this example command:

    * ``key-material-wrapped.bin`` is the file
     that contains your encrypted key material.
    * ``aes-key-wrapped.bin`` is the file that
     contains the encrypted AES encryption key.

````
# Combine the encrypted AES key and encrypted key material in a file
`$` `cat `aes-key-wrapped.bin` `key-material-wrapped.bin` > ``EncryptedKeyMaterial.bin```
````

Proceed to [Step 4: Import the key material](importing-keys-import-key-material.md "importing-keys-import-key-material.md").
