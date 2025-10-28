# Calling CreateKey

An AWS KMS key is generated as a result of a call to the [`CreateKey`](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") API call.

The following is a subset of the [`CreateKey` request syntax](../APIReference/API_CreateKey.md#API_CreateKey_RequestSyntax "../APIReference/API_CreateKey.md#API_CreateKey_RequestSyntax").

```
{
  "Description": "string",
  "KeySpec": "string",
  "KeyUsage": "string",
  "Origin": "string";
  "Policy": "string"
}
```

The request accepts the following data in JSON format.

**Description**
(Optional) Description of the key. We recommend that you choose a description that helps you
decide whether the key is appropriate for a task.

**KeySpec**
Specifies the type of KMS key to create. The default value, SYMMETRIC_DEFAULT, creates a
symmetric encryption KMS key. This parameter is optional for symmetric encryption
keys, and is required for all other key specs.

**KeyUsage**
Speciﬁes the use of the key. Valid values are `ENCRYPT_DECRYPT`,
`SIGN_VERIFY`, or `GENERATE_VERIFY_MAC`. The default value is
`ENCRYPT_DECRYPT`. This parameter is optional for symmetric encryption
keys, and is required for all other key specs.

**Origin**
(Optional) Specifies the source of the key material for the KMS key. The default value is
`AWS_KMS`, which indicates that AWS KMS generates and manages the key
material for the KMS key. Other valid values include `EXTERNAL`, which
represents a KMS key created without key material for [imported key material](../developerguide/importing-keys.md "../developerguide/importing-keys.md"), and
`AWS_CLOUDHSM` which creates a KMS key in a [custom key store](../developerguide/custom-key-store-overview.md "../developerguide/custom-key-store-overview.md") backed by
an AWS CloudHSM cluster that you control.

**Policy**
(Optional) Policy to attach to the key. If the policy is omitted, the key is created with the
default policy (following) that allows the root account and IAM principals with AWS KMS
permissions to manage it.

For details on the policy, see [Key policies in
AWS KMS](../developerguide/key-policies.md "../developerguide/key-policies.md") and [Default key
policy](../developerguide/key-policy-default.md "../developerguide/key-policy-default.md") in the _AWS Key Management Service Developer Guide_.

The `CreateKey` request returns a [response](../APIReference/API_CreateKey.md#API_CreateKey_ResponseSyntax "../APIReference/API_CreateKey.md#API_CreateKey_ResponseSyntax") that
includes a key ARN.

```
arn:`<partition>`:kms:`<region>`:`<account-id>`:key/`<key-id>`
```

If the `Origin` is `AWS_KMS`, after the ARN is created, a request to an
AWS KMS HSM is made over an authenticated session to provision a hardware security module (HSM)
backing key (HBK). The HBK is a 256-bit key that is associated with this key ID of the
KMS key. It can be generated only on an HSM and is designed never to be exported outside of
the HSM boundary in cleartext. The HBK is encrypted under the current domain key,
DK0. These encrypted HBKs are referred to as encrypted key tokens
(EKTs). Although the HSMs can be configured to use a variety of key wrapping methods, the
current implementation uses AES-256 in Galois Counter Mode (GCM), an authenticated encryption
scheme. This authenticated encryption mode allows us to protect some cleartext exported key
token metadata.

This is stylistically represented as:

```
EKT = Encrypt(DK0, HBK)
```

Two fundamental forms of protection are provided to your KMS keys and the subsequent HBKs:
authorization policies set on your KMS keys and the cryptographic protections on your
associated HBKs. The remaining sections describe the cryptographic protections and the
security of the management functions in AWS KMS.

In addition to the ARN, you can create a user-friendly name and associate it with the
KMS key by creating an _alias_ for the key. Once an alias
has been associated with a KMS key, the alias can be used to identify the KMS key in
cryptographic operations. For detailed information, see [Using aliases](../developerguide/kms-alias.md "../developerguide/kms-alias.md") in the _AWS Key Management Service Developer Guide_.

Multiple levels of authorizations surround the use of KMS keys. AWS KMS enables separate
authorization policies between the encrypted content and the KMS key. For instance, an AWS KMS
envelope-encrypted Amazon Simple Storage Service (Amazon S3) object inherits the policy on the Amazon S3 bucket. However,
access to the necessary encryption key is determined by the access policy on the KMS key.
For information about authorization of KMS keys, see [Authentication and access control for AWS KMS](../developerguide/control-access.md "../developerguide/control-access.md")
in the _AWS Key Management Service Developer Guide_.
