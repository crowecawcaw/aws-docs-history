# Key stores

A _key store_ is a secure location for storing and using
cryptographic keys. The default key store in AWS KMS also supports methods for generating and
managing the keys that it stores. By default, the cryptographic key material for the
AWS KMS keys that you create in AWS KMS is generated in and protected by hardware security
modules (HSMs) that are [FIPS 140-3 Cryptographic Module Validation
Program](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4884 "https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4884"). Key material for your KMS keys never leave the
HSMs unencrypted.

AWS KMS supports several types of key stores to protect your key material when using AWS KMS
to create and manage your encryption keys. All of the key store options supplied by AWS KMS are
continually validated under FIPS 140-3 at Security Level 3 and are designed to prevent anyone,
including AWS operators, from accessing your plaintext keys or using them without your
permission.

## AWS KMS standard key store

By default, a KMS key is created using the standard AWS KMS HSM. This HSM type can be
thought of as a multi-tenant fleet of HSMs that allows for the most scalable, lowest cost and
easiest key store to manage from your perspective. If you are creating a KMS key for use
within one or more AWS services so that service can encrypt your data on your behalf, you
will create a symmetric key. If you are using a KMS key for your own application design, you
may choose to create a symmetric encryption key, asymmetric key, or HMAC key.

In the standard key store option, AWS KMS creates your key, then encrypts it under keys that
the service manages internally. Multiple copies of encrypted versions of your keys are then
stored in systems that are designed for durability. Generating and protecting your key
material in the standard key store type lets you take full advantage of the scalability,
availability, and durability of AWS KMS with the lowest operational burden and cost of the AWS
key stores.

## AWS KMS standard key store with imported key

material

Instead of asking AWS KMS to both generate and store the only copies of a given key, you can
choose to import key material into AWS KMS, allowing you to generate your own 256-bit symmetric
encryption key, RSA or elliptic curve (ECC) key, or Hash-Based Message Authentication Code
(HMAC) key, and apply it to a KMS key identifier (keyId). This is sometimes referred to as
_bring your own key_ (BYOK). Imported key material from
your local key management system must be protected by using a public key issued by AWS KMS, a
supported cryptographic wrapping algorithm, and a time-based import token provided by AWS KMS.
This process verifies that your encrypted, imported key can only ever be decrypted by an AWS KMS
HSM once it has left your environment.

Imported key material may be useful if you have specific requirements around the system
that generates keys, or want a copy of your key outside of AWS as a backup. Note that you
are responsible for an imported key material's overall availability and durability. While
AWS KMS has a copy of your imported key and will keep highly available while you need it,
imported keys offer a special API for deletion – DeleteImportedKeyMaterial. This API will
immediately delete all copies of the imported key material that AWS KMS has, with no option for
AWS to recover the key. In addition, you can set an expiration time on an imported key,
after which the key will be unusable. To make the key useful again in AWS KMS, you will have to
reimport the key material and assign it to the same keyId. This deletion action for imported
keys is different than standard keys that AWS KMS generates and stored for you on your behalf.
In the standard case, the key deletion process has a mandatory waiting period where a key
scheduled for deletion is first blocked from usage. This action allows you to see access
denied errors in logs from any application or AWS service that might need that key to access
data. If you see such access requests, you can choose to cancel the scheduled deletion and
re-enable the key. After a configurable waiting period (between 7 and 30 days), only then will
KMS actually delete the key material, the keyID and all metadata associated with the key. For
more information about availability and durability, see [Protecting imported key material](import-keys-protect.md "import-keys-protect.md") in the _AWS KMS Developer
Guide_.

There are some additional limitations with imported key material to be aware of. Since
AWS KMS cannot generate new key material, there is no way to configure automatic rotation of
imported keys. You will need to create a new KMS key with a new keyId, then import new key
material to achieve an effective rotation. Also, ciphertexts created in AWS KMS under an
imported symmetric key cannot be easily decrypted using your local copy of the key outside of
AWS. This is because the authenticated encryption format used by AWS KMS appends additional
metadata to the ciphertext to provide assurances during the decryption operation that the
ciphertext was created by the expected KMS key under a previous encrypt operation. Most
external cryptographic systems won’t understand how to parse this metadata to gain access to
the raw ciphertext to be able to use their copy of a symmetric key. Ciphertexts created under
imported asymmetric keys (e.g. RSA or ECC) can be used outside of AWS KMS with the matching
(public or private) portion of the key because there is no additional metadata added by AWS KMS
to the ciphertext.

## AWS KMS custom key stores

However, if you require even more control of the HSMs, you can create a custom key
store.

A _custom key store_ is a key store within AWS KMS that is
backed by a key manager outside of AWS KMS, which you own and manage. Custom key stores combine
the convenient and comprehensive key management interface of AWS KMS with the ability to own and
control the key material and cryptographic operations. When you use a KMS key in a custom
key store, the cryptographic operations are performed by your key manager using your
cryptographic keys. As a result, you assume more responsibility for the availability and
durability of cryptographic keys, and for the operation of the HSMs.

Owning your HSMs may be useful to help meet certain regulatory requirements that don’t yet
allow multi-tenant web services like the standard KMS key store to hold your cryptographic
keys. Custom key stores are not more secure than KMS key store that use AWS-managed HSMs,
but they have different (and higher) management and cost implications. As a result, you assume
more responsibility for the availability and durability of cryptographic keys and for the
operation of the HSMs. Regardless of whether you use the standard key store with AWS KMS HSMs or
a custom key store, the service is designed so that no one, including AWS employees, can
retrieve your plaintext keys or use them without your permission. AWS KMS supports two types of
custom key stores, AWS CloudHSM key stores and external key stores.

**Unsupported features**

AWS KMS does not support the following features in custom key stores.

- [Asymmetric KMS keys](symmetric-asymmetric.md "symmetric-asymmetric.md")
- [HMAC KMS keys](hmac.md "hmac.md")
- [KMS keys with imported key material](importing-keys.md "importing-keys.md")
- [Automatic key rotation](rotate-keys.md "rotate-keys.md")
- [Multi-Region keys](multi-region-keys-overview.md "multi-region-keys-overview.md")

### AWS CloudHSM key store

You can create a KMS key in an [AWS CloudHSM](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/") key
store, where root user keys are generated, stored and used in a AWS CloudHSM cluster that you
own and manage. Requests to AWS KMS to use a key for some cryptographic operation are
forwarded to your AWS CloudHSM cluster to perform the operation. While a AWS CloudHSM cluster is
hosted by AWS, it is a single-tenant solution that is directly managed and operated by
you. You own much of the availability and performance of KMS keys in a AWS CloudHSM cluster. To
see if a AWS CloudHSM custom key store is a good fit for your requirements, read [Are AWS KMS
custom key stores right for you?](https://aws.amazon.com/blogs/security/are-kms-custom-key-stores-right-for-you/ "https://aws.amazon.com/blogs/security/are-kms-custom-key-stores-right-for-you/") on the AWS security blog.

### External key store

You can configure AWS KMS to use an External Key Store (XKS), where root user keys are
generated, stored and used in a key management system outside the AWS Cloud. Requests to
AWS KMS to use a key for some cryptographic operation are forwarded to your externally hosted
system to perform the operation. Specifically, requests are forwarded to an XKS Proxy in
your network, which then forwards the request to whichever cryptographic system you use. The
XKS Proxy is an open-source specification that anyone can integrate with. Many commercial
key management vendors support the XKS Proxy specification. Because an External Key Store is
hosted by you or some third party, you own all of the availability, durability, and
performance of the keys in the system. To see if an External Key Store is a good fit for
your requirements, read [Announcing
AWS KMS External Key Store (XKS)](https://aws.amazon.com/blogs/aws/announcing-aws-kms-external-key-store-xks/ "https://aws.amazon.com/blogs/aws/announcing-aws-kms-external-key-store-xks/") on the AWS News blog.
