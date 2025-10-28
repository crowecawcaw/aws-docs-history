# Create a KMS key with imported key

material

Imported key material lets you protect your AWS resources under cryptographic keys that
you generate. The following overview explains how to import your key material into AWS KMS.
For more details about each step in the process, see the corresponding topics.

1. [Create a KMS key with no key
   material](importing-keys-create-cmk.md "importing-keys-create-cmk.md") – The origin must be `EXTERNAL`. A key origin
   of `EXTERNAL` indicates that the key is designed for imported key
   material and prevents AWS KMS from generating key material for the KMS key. In a
   later step you will import your own key material into this KMS key.

The key material that you import must be compatible with the key spec of the
associated AWS KMS key. For more information about compatibility, see [Requirements for imported key
material](#importing-keys-material-requirements "#importing-keys-material-requirements"). 2. [Download the wrapping
public key and import token](importing-keys-get-public-key-and-token.md "importing-keys-get-public-key-and-token.md") – After completing step 1, download a
wrapping public key and an import token. These items protect your key material while
it's imported to AWS KMS.

In this step, you choose the type ("key spec") of the RSA wrapping key and the
wrapping algorithm that you'll use to encrypt your data in transit to AWS KMS. You can
choose a different wrapping key spec and wrapping key algorithm each time you import
or reimport the same key material. 3. [Encrypt the key
material](importing-keys-encrypt-key-material.md "importing-keys-encrypt-key-material.md") – Use the wrapping public key that you downloaded in step
2 to encrypt the key material that you created on your own system. 4. [Import the key material](importing-keys-import-key-material.md "importing-keys-import-key-material.md")
– Upload the encrypted key material that you created in step 3 and the import
token that you downloaded in step 2.

At this stage, you can [set an optional
expiration time](importing-keys-import-key-material.md#importing-keys-expiration "importing-keys-import-key-material.md#importing-keys-expiration"). When imported key material expires, AWS KMS deletes it,
and the KMS key becomes unusable. To continue to use the KMS key, you must
reimport the **same** key material.

When the import operation completes successfully, the key state of the KMS key
changes from `PendingImport` to `Enabled`. You can now use the
KMS key in cryptographic operations.
AWS KMS records an entry in your AWS CloudTrail log when you [create
the KMS key](ct-createkey.md "ct-createkey.md"), [download the wrapping
public key and import token](ct-getparametersforimport.md "ct-getparametersforimport.md"), and [import the
key material](ct-importkeymaterial.md "ct-importkeymaterial.md"). AWS KMS also records an entry when you delete imported key material
or when AWS KMS [deletes expired key
material](ct-deleteexpiredkeymaterial.md "ct-deleteexpiredkeymaterial.md").

## Permissions for importing key

material

To create and manage KMS keys with imported key material, the user needs permission
for the operations in this process. You can provide the
`kms:GetParametersForImport`, `kms:ImportKeyMaterial`, and
`kms:DeleteImportedKeyMaterial` permissions in the key policy when you
create the KMS key. In the AWS KMS console, these permissions are added automatically
for key administrators when you create a key with an **External** key
material origin.

To create KMS keys with imported key material, the principal needs the following
permissions.

- [kms:CreateKey](customer-managed-policies.md#iam-policy-example-create-key "customer-managed-policies.md#iam-policy-example-create-key") (IAM
  policy)
  - To limit this permission to KMS keys with imported key material, use
    the [kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin "conditions-kms.md#conditions-kms-key-origin")
    policy condition with a value of `EXTERNAL`.

  ```
  {
    "Sid": "CreateKMSKeysWithoutKeyMaterial",
    "Effect": "Allow",
    "Resource": "*",
    "Action": "kms:CreateKey",
    "Condition": {
      "StringEquals": {
        "kms:KeyOrigin": "EXTERNAL"
      }
    }
  }
  ```

- [kms:GetParametersForImport](../APIReference/API_GetParametersForImport.md "../APIReference/API_GetParametersForImport.md") (Key policy or IAM policy)
  - To limit this permission to requests that use a particular wrapping
    algorithm and wrapping key spec, use the [kms:WrappingAlgorithm](conditions-kms.md#conditions-kms-wrapping-algorithm "conditions-kms.md#conditions-kms-wrapping-algorithm") and [kms:WrappingKeySpec](conditions-kms.md#conditions-kms-wrapping-key-spec "conditions-kms.md#conditions-kms-wrapping-key-spec") policy conditions.

- [kms:ImportKeyMaterial](../APIReference/API_ImportKeyMaterial.md "../APIReference/API_ImportKeyMaterial.md") (Key policy or IAM policy)
  - To allow or prohibit key material that expires and control the
    expiration date, use the [kms:ExpirationModel](conditions-kms.md#conditions-kms-expiration-model "conditions-kms.md#conditions-kms-expiration-model") and [kms:ValidTo](conditions-kms.md#conditions-kms-valid-to "conditions-kms.md#conditions-kms-valid-to") policy
    conditions.

To reimport imported key material, the principal needs the [kms:GetParametersForImport](../APIReference/API_GetParametersForImport.md "../APIReference/API_GetParametersForImport.md") and [kms:ImportKeyMaterial](../APIReference/API_ImportKeyMaterial.md "../APIReference/API_ImportKeyMaterial.md")
permissions.

To delete imported key material, the principal needs [kms:DeleteImportedKeyMaterial](../APIReference/API_DeleteImportedKeyMaterial.md "../APIReference/API_DeleteImportedKeyMaterial.md") permission.

For example, to give the example `KMSAdminRole` permission to manage all
aspects of a KMS key with imported key material, include a key policy statement like
the following one in the key policy of the KMS key.

```
{
  "Sid": "Manage KMS keys with imported key material",
  "Effect": "Allow",
  "Resource": "*",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/KMSAdminRole"
  },
  "Action": [
    "kms:GetParametersForImport",
    "kms:ImportKeyMaterial",
    "kms:DeleteImportedKeyMaterial"
  ]
}
```

## Requirements for imported key

material

The key material that you import must be compatible with the [key spec](create-keys.md#key-spec "create-keys.md#key-spec") of the associated KMS key. For asymmetric key pairs, import only
the private key of the pair. AWS KMS derives the public key from the private key.

AWS KMS supports the following key specs for KMS keys with imported key
material.

- **Symmetric encryption keys**
  - **Key spec:**
    - SYMMETRIC_DEFAULT.

  - **Requirements:**
    - 256-bits (32 bytes) of binary data.
    - In China Regions, it must be a 128-bits (16 bytes) of binary
      data.

- **HMAC keys**
  - **Key specs:**
    - HMAC_224
    - HMAC_256
    - HMAC_384
    - HMAC_512

  - **Requirements:**
    - HMAC key material must conform to [RFC
      2104](https://datatracker.ietf.org/doc/html/rfc2104 "https://datatracker.ietf.org/doc/html/rfc2104").
    - The key length must be at least the same length specified by
      the key spec. The maximum key length is 1024-bits.
    - If your key material exceeds 1024 bits, you can hash the key
      material and import the hash output. The hashing algorithm must
      match the key spec of the HMAC KMS key you're creating.

  - **Example:**
    - To import 2048 bits of key material into an HMAC_256 key,
      first compute the SHA-256 hash of the 2048-bit key material,
      then import the resulting 256-bit hash output into the
      KMS key.

  - **Valid key lengths:**
    - HMAC_224: 224–1024 bits
    - HMAC_256: 256–1024 bits
    - HMAC_384: 384–1024 bits
    - HMAC_512: 512–1024 bits

- **RSA asymmetric private key**
  - **Key specs:**
    - RSA_2048
    - RSA_3072
    - RSA_4096

  - **Requirements:**
    - The RSA asymmetric private key that you import must be part of
      a key pair that conforms to [RFC
      3447](https://datatracker.ietf.org/doc/html/rfc3447/ "https://datatracker.ietf.org/doc/html/rfc3447/").
    - **Modulus:** 2048 bits, 3072 bits
      or 4096 bits
    - **Number of primes:** 2
      (multi-prime RSA keys are not supported)
    - Asymmetric key material must be BER-encoded or DER-encoded in
      Public-Key Cryptography Standards (PKCS) #8 format that complies
      with [RFC 5208](https://datatracker.ietf.org/doc/html/rfc5208 "https://datatracker.ietf.org/doc/html/rfc5208").

- **Elliptic curve asymmetric private key**
  - **Key specs:**
    - ECC_NIST_P256 (secp256r1)
    - ECC_NIST_P384 (secp384r1)
    - ECC_NIST_P521 (secp521r1)
    - ECC_SECG_P256K1 (secp256k1)

  - **Requirements:**
    - The ECC asymmetric private key that you import must be part of
      a key pair that conforms to [RFC
      5915](https://datatracker.ietf.org/doc/html/rfc5915/ "https://datatracker.ietf.org/doc/html/rfc5915/").
    - **Curve:** NIST P-256, NIST
      P-384, NIST P-521, or Secp256k1.
    - **Parameters:** Named curves only
      (ECC keys with explicit parameters are rejected).
    - **Public point coordinates:** May
      be compressed, uncompressed, or projective.
    - Asymmetric key material must be BER-encoded or DER-encoded in
      Public-Key Cryptography Standards (PKCS) #8 format that complies
      with [RFC 5208](https://datatracker.ietf.org/doc/html/rfc5208 "https://datatracker.ietf.org/doc/html/rfc5208").

- **ML-DSA key**
  - **Key specs:**
    - ML_DSA_44
    - ML_DSA_65
    - ML_DSA_87

###### Important

Importing ML-DSA keys is not supported.

- **SM2 asymmetric private key** (China Regions
  only)
  - **Requirements:**
    - The SM2 asymmetric private key that you import must be part of
      a key pair that conforms to GM/T 0003.
    - **Curve:** SM2.
    - **Parameters:** Named curve only
      (SM2 keys with explicit parameters are rejected).
    - **Public point coordinates:** May
      be compressed, uncompressed, or projective.
    - Asymmetric key material must be BER-encoded or DER-encoded in
      Public-Key Cryptography Standards (PKCS) #8 format that complies
      with [RFC 5208](https://datatracker.ietf.org/doc/html/rfc5208 "https://datatracker.ietf.org/doc/html/rfc5208").
