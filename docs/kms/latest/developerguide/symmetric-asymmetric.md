# Asymmetric keys in AWS KMS

An _asymmetric KMS key_ represents a mathematically
related public key and private key pair. You can give the public key to anyone, even if they're
not trusted, but the private key must be kept secret.

In an asymmetric KMS key, the private key is created in AWS KMS and never leaves AWS KMS
unencrypted. To use the private key, you must call AWS KMS. You can use the public key within
AWS KMS by calling the AWS KMS API operations. Or, you can [download the public key](download-public-key.md "download-public-key.md") and use it outside of AWS KMS.

If your use case requires encryption outside of AWS by users who cannot call AWS KMS,
asymmetric KMS keys are a good choice. However, if you are creating a KMS key to encrypt the
data that you store or manage in an AWS service, use a symmetric encryption KMS key.
[AWS services that
are integrated with AWS KMS](https://aws.amazon.com/kms/features/#AWS_Service_Integration "https://aws.amazon.com/kms/features/#AWS_Service_Integration") use only symmetric encryption KMS keys to encrypt your data. These services do not support encryption with asymmetric KMS keys.

When signing messages larger than 4 KB with AWS KMS, you must hash the message outside of AWS KMS before signing.
AWS KMS provides three `MessageType` options for handling message input: `RAW` for plaintext messages
(where AWS KMS performs the hashing), `DIGEST` for pre-hashed messages (where AWS KMS skips the hashing step), and
`EXTERNAL_MU` specifically for ML-DSA KMS key specs where the input is a 64-byte representative μ value. For
large messages exceeding the 4 KB limit, hash the message externally and use [`MessageType:DIGEST`](../APIReference/API_Sign.md#KMS-Sign-request-MessageType "../APIReference/API_Sign.md#KMS-Sign-request-MessageType")
(or [`MessageType:EXTERNAL_MU`](../APIReference/API_Sign.md#KMS-Sign-request-MessageType "../APIReference/API_Sign.md#KMS-Sign-request-MessageType") for ML-DSA KMS keys) when calling AWS KMS [Sign](../APIReference/API_Sign.md "../APIReference/API_Sign.md") and AWS KMS [Verify](../APIReference/API_Verify.md "../APIReference/API_Verify.md") operations.

AWS KMS supports several types of asymmetric KMS keys.

**RSA KMS keys**

A KMS key with an RSA key pair for encryption and decryption or signing and
verification (but not both). AWS KMS supports several key lengths for different security
requirements.

For technical details about the encryption and signing algorithms that AWS KMS supports
for RSA KMS keys, see [RSA key specs](symm-asymm-choose-key-spec.md#key-spec-rsa "symm-asymm-choose-key-spec.md#key-spec-rsa").

**Elliptic Curve (ECC) KMS keys**

A KMS key with an elliptic curve key pair for signing and verification or deriving
shared secrets (but not both). AWS KMS supports several commonly-used curves.

For technical details about the signing algorithms that AWS KMS supports for ECC
KMS keys, see [Elliptic curve key specs](symm-asymm-choose-key-spec.md#key-spec-ecc "symm-asymm-choose-key-spec.md#key-spec-ecc").

**ML-DSA KMS keys**

A KMS key with an ML-DSA key pair for signing and verification. ML-DSA is a
post-quantum cryptography standard developed by the US National Institute of Standards and
Technology (NIST) to protect against the security threats posed by quantum computing.
ML-DSA is the recommended digital signature algorithm for organizations transitioning from
RSA or Elliptic Curve digital signature algorithms to post-quantum safe
cryptography.

AWS KMS supports several key lengths for different security requirements. For technical
details about the signing algorithms that AWS KMS supports for ML-DSA KMS keys, see [ML-DSA key spec](symm-asymm-choose-key-spec.md#key-spec-mldsa "symm-asymm-choose-key-spec.md#key-spec-mldsa").

**SM2 KMS keys (China Regions only)**

A KMS key with an SM2 key pair for encryption and decryption, signing and
verification, or deriving shared secrets (you must choose one [Key usage](create-keys.md#key-usage "create-keys.md#key-usage") type).

For technical details about the encryption and signing algorithms that AWS KMS supports
for SM2 KMS keys (China Regions only), see [SM2 key
spec](symm-asymm-choose-key-spec.md#key-spec-sm "symm-asymm-choose-key-spec.md#key-spec-sm").

For help choosing your asymmetric key configuration, see [Choosing what type of KMS key to create](create-keys.md#symm-asymm-choose "create-keys.md#symm-asymm-choose").

**Regions**

Asymmetric KMS keys and asymmetric data key pairs are supported in all AWS Regions that AWS KMS supports.

**Learn more**

- To create asymmetric KMS keys, see [Create an asymmetric KMS key](asymm-create-key.md "asymm-create-key.md").
- To create multi-Region asymmetric KMS keys, see [Create multi-Region primary keys](create-primary-keys.md "create-primary-keys.md").
- To learn how to sign messages and verify signatures with asymmetric KMS keys, see
  [Digital
  signing with the new asymmetric keys feature of AWS KMS](https://aws.amazon.com/blogs/security/digital-signing-asymmetric-keys-aws-kms/ "https://aws.amazon.com/blogs/security/digital-signing-asymmetric-keys-aws-kms/") in the _AWS Security Blog_.
- To learn about special considerations for deleting asymmetric KMS keys, see [Deleting asymmetric KMS keys](deleting-keys.md#deleting-asymmetric-cmks "deleting-keys.md#deleting-asymmetric-cmks").
- To identify and view asymmetric KMS keys, see [Identify asymmetric KMS keys](identify-key-types.md#identify-asymm-keys "identify-key-types.md#identify-asymm-keys").
