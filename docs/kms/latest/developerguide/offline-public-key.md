# Perform offline operations with public keys

In an asymmetric KMS key, the private key is created in AWS KMS and never leaves AWS KMS
unencrypted. To use the private key, you must call AWS KMS. You can use the public key within
AWS KMS by calling the AWS KMS API operations. Or, you can [download the public key](download-public-key.md "download-public-key.md") and share for use outside of AWS KMS.

You might share a public key to let others encrypt data outside of AWS KMS that you can
decrypt only with your private key. Or, to allow others to verify a digital signature outside of
AWS KMS that you have generated with your private key. Or, to share your public key with a peer to
derive a shared secret.

When you use the public key in your asymmetric KMS key within AWS KMS, you benefit from the
authentication, authorization, and logging that are part of every AWS KMS operation. You also
reduce of risk of encrypting data that cannot be decrypted. These features are not effective
outside of AWS KMS. For details, see [Special considerations for downloading
public keys](#download-public-key-considerations "#download-public-key-considerations").

###### Tip

Looking for data keys or SSH keys? This topic explains how to manage asymmetric keys in
AWS Key Management Service, where the private key is not exportable. For exportable data key pairs where the
private key is protected by a symmetric encryption KMS key, see [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md"). For help with
downloading the public key associated with an Amazon EC2 instance, see _Retrieving the public key_ in the [Amazon EC2 User Guide](../../../AWSEC2/latest/UserGuide/describe-keys.md#retrieving-the-public-key "../../../AWSEC2/latest/UserGuide/describe-keys.md#retrieving-the-public-key")
and [Amazon EC2 User Guide](../../../AWSEC2/latest/WindowsGuide/describe-keys.md#retrieving-the-public-key "../../../AWSEC2/latest/WindowsGuide/describe-keys.md#retrieving-the-public-key").

###### Topics

- [Special considerations for downloading
  public keys](#download-public-key-considerations "#download-public-key-considerations")
- [Download public key](download-public-key.md "download-public-key.md")
- [Example offline operations](offline-operations.md "offline-operations.md")

## Special considerations for downloading

public keys

To protect your KMS keys, AWS KMS provides access controls, authenticated encryption, and
detailed logs of every operation. AWS KMS also allows you to prevent the use of KMS keys,
temporarily or permanently. Finally, AWS KMS operations are designed to minimize of risk of
encrypting data that cannot be decrypted. These features are not available when you use
downloaded public keys outside of AWS KMS.

**Authorization**

[Key policies](key-policies.md "key-policies.md") and [IAM policies](iam-policies.md "iam-policies.md") that control access to the KMS key within AWS KMS have no
effect on operations performed outside of AWS. Any user who can get the public key can
use it outside of AWS KMS even if they don't have permission to encrypt data or verify
signatures with the KMS key.

**Key usage restrictions**

Key usage restrictions are not effective outside of AWS KMS. If you call the [Encrypt](../APIReference/API_Encrypt.md "../APIReference/API_Encrypt.md") operation with a KMS key that
has a `KeyUsage` of `SIGN_VERIFY`, the AWS KMS operation fails. But
if you encrypt data outside of AWS KMS with a public key from a KMS key with a
`KeyUsage` of `SIGN_VERIFY` or `KEY_AGREEMENT`, the
data cannot be decrypted.

**Algorithm restrictions**

Restrictions on the encryption and signing algorithms that AWS KMS supports are not
effective outside of AWS KMS. If you encrypt data with the public key from a KMS key
outside of AWS KMS, and use an encryption algorithm that AWS KMS does not support, the data
cannot be decrypted.

**Disabling and deleting KMS keys**

Actions that you can take to prevent the use of KMS key in a cryptographic
operation within AWS KMS do not prevent anyone from using the public key outside of AWS KMS.
For example, disabling a KMS key, scheduling deletion of a KMS key, deleting a
KMS key, or deleting the key material from a KMS key have no effect on a public key
outside of AWS KMS. If you delete an asymmetric KMS key or delete or lose its key
material, data that you encrypt with a public key outside of AWS KMS is
unrecoverable.

**Logging**

AWS CloudTrail logs that record every AWS KMS operation, including the request, response,
date, time, and authorized user, do not record the use of the public key outside of
AWS KMS.

**Offline verification with SM2 key pairs (China Regions only)**

To verify a signature outside of AWS KMS with an SM2 public key, you must specify the
distinguishing ID. By default, AWS KMS uses `1234567812345678` as the
distinguishing ID. For more information, see [Offline verification with SM2 key pairs
(China Regions only).](offline-operations.md#key-spec-sm-offline-verification "offline-operations.md#key-spec-sm-offline-verification")
