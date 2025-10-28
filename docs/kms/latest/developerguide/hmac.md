# HMAC keys in AWS KMS

Hash-Based Message Authentication Code (HMAC) KMS keys are symmetric keys that you use
to generate and verify HMACs within AWS KMS. The unique key material associated with each HMAC
KMS key provides the secret key that HMAC algorithms require. You can use an HMAC
KMS key with the `GenerateMac` and [`VerifyMac`](../APIReference/API_VerifyMac.md "../APIReference/API_VerifyMac.md") operations to verify the integrity and authenticity
of data within AWS KMS.

HMAC algorithms combine a cryptographic hash function and a shared secret key. They take a
message and a secret key, such as the key material in an HMAC KMS key, and return a
unique, fixed-size code or _tag_. If even one character of
the message changes, or if the secret key is not identical, the resulting tag is entirely
different. By requiring a secret key, HMAC also provides authenticity; it is impossible to
generate an identical HMAC tag without the secret key. HMACs are sometimes called _symmetric signatures_, because they work like digital
signatures, but use a single key for both signing and verification.

HMAC KMS keys and the HMAC algorithms that AWS KMS uses conform to industry standards
defined in [RFC 2104](https://datatracker.ietf.org/doc/html/rfc2104 "https://datatracker.ietf.org/doc/html/rfc2104"). The
AWS KMS [GenerateMac](../APIReference/API_GenerateMac.md "../APIReference/API_GenerateMac.md") operation generates
standard HMAC tags. HMAC KMS keys are generated in AWS KMS hardware security modules that
are certified under the [FIPS 140-3 Cryptographic Module
Validation Program](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4884 "https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4884") (except in China (Beijing) and China (Ningxia)
Regions) and never leave AWS KMS unencrypted. To use an HMAC KMS key, you must call
AWS KMS.

You can use HMAC KMS keys to determine the authenticity of a message, such as a JSON Web
Token (JWT), tokenized credit card information, or a submitted password. They can also be
used as secure Key Derivation Functions (KDFs), especially in applications that require
deterministic keys.

HMAC KMS keys provide an advantage over HMACs from application software because the key
material is generated and used entirely within AWS KMS, subject to the access controls that
you set on the key.

###### Tip

Best practices recommend that you limit the time during which any signing mechanism,
including an HMAC, is effective. This deters an attack where the actor uses a signed
message to establish validity repeatedly or long after the message is superseded. HMAC
tags do not include a timestamp, but you can include a timestamp in the token or message
to help you detect when its time to refresh the HMAC.

**Supported cryptographic operations**

HMAC KMS keys support only the [`GenerateMac`](../APIReference/API_GenerateMac.md "../APIReference/API_GenerateMac.md") and
[`VerifyMac`](../APIReference/API_VerifyMac.md "../APIReference/API_VerifyMac.md")
cryptographic operations. You cannot use HMAC KMS keys to encrypt data or sign
messages, or use any other type of KMS key in HMAC operations. When you use
the `GenerateMac` operation, you supply a message of up to 4,096
bytes, an HMAC KMS key, and the MAC algorithm that is compatible with the HMAC
key spec, and `GenerateMac` computes the HMAC tag. To verify an HMAC
tag, you must supply the HMAC tag, and the same message, HMAC KMS key, and MAC
algorithm that `GenerateMac` used to compute the original HMAC tag.
The `VerifyMac` operation computes the HMAC tag and verifies that it
is identical to the supplied HMAC tag. If the input and computed HMAC tags are
not identical, verification fails.

HMAC KMS keys _do not_ support [automatic key rotation](rotate-keys.md "rotate-keys.md") and you cannot create an
HMAC KMS key in a [custom key
store](key-store-overview.md#custom-key-store-overview "key-store-overview.md#custom-key-store-overview").

If you are creating a KMS key to encrypt data in an AWS service, use a
symmetric encryption key. You cannot use an HMAC KMS key.

**Regions**

HMAC KMS keys are supported in all AWS Regions that AWS KMS supports.

**Learn more**

- To create HMAC KMS keys, see [Create an HMAC KMS key](hmac-create-key.md "hmac-create-key.md").
- To create multi-Region HMAC KMS keys, see [Multi-Region keys in AWS KMS](multi-region-keys-overview.md "multi-region-keys-overview.md").
- To examine the difference in the default key policy that the AWS KMS console sets
  for HMAC KMS keys, see [Allows key users to use a KMS key for
  cryptographic operations](key-policy-default.md#key-policy-users-crypto "key-policy-default.md#key-policy-users-crypto").
- To identify and view HMAC KMS keys, see [Identify HMAC KMS keys](identify-key-types.md#hmac-view "identify-key-types.md#hmac-view").
- To learn about using HMACs to create JSON web tokens, see [How to
  protect HMACs inside AWS KMS](https://aws.amazon.com/blogs/security/how-to-protect-hmacs-inside-aws-kms/ "https://aws.amazon.com/blogs/security/how-to-protect-hmacs-inside-aws-kms/") in the _AWS Security
  Blog_.
- Listen to a podcast: [Introducing HMACs for AWS Key Management Service](https://aws.amazon.com/podcasts/introducing-hmacs-apis-in-aws-key-management-service "https://aws.amazon.com/podcasts/introducing-hmacs-apis-in-aws-key-management-service") on _The Official
  AWS Podcast_.
