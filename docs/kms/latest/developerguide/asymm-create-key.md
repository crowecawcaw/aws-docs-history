# Create an asymmetric KMS key

You can create [asymmetric KMS keys](symmetric-asymmetric.md "symmetric-asymmetric.md") in the
AWS KMS console, by using the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md")
API, or by using the [AWS::KMS::Key CloudFormation
template](../../../AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.md"). An asymmetric KMS key represents a public and private key pair that
can be used for encryption, signing, or deriving shared secrets. The private key remains
within AWS KMS. To download the public key for use outside of AWS KMS, see [Download public key](download-public-key.md "download-public-key.md").

When you create an asymmetric KMS key, you must select a key spec. Often the key spec
that you select is determined by regulatory, security, or business requirements. It might
also be influenced by the size of messages that you need to encrypt or sign. In general,
longer encryption keys are more resistant to brute-force attacks. For a detailed description
of all supported key specs, see [Key spec reference](symm-asymm-choose-key-spec.md "symm-asymm-choose-key-spec.md").

AWS services that integrate with AWS KMS do not support asymmetric KMS keys. If you want
to create a KMS key that encrypts data that you store or manage in an AWS service, [create a symmetric encryption KMS key](create-symmetric-cmk.md "create-symmetric-cmk.md").

For information about the permissions required to create KMS keys, see [Permissions for creating KMS keys](create-keys.md#create-key-permissions "create-keys.md#create-key-permissions").

You can use the AWS Management Console to create asymmetric AWS KMS keys (KMS keys). Each
asymmetric KMS key represents a public and private key pair.

###### Important

Do not include confidential or sensitive information in the alias, description, or tags. These fields may appear in plain text in CloudTrail logs and other output.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**.
4. Choose **Create key**.
5. To create an asymmetric KMS key, in **Key
   type,** choose **Asymmetric**.
6. To create an asymmetric KMS key for public key encryption, in **Key usage**, choose **Encrypt and
   decrypt**.

To create an asymmetric KMS key for signing messages and verifying
signatures, in **Key usage**, choose
**Sign and verify**.

To create an asymmetric KMS key for deriving shared secrets, in
**Key usage**, choose **Key
agreement**.

For help choosing a key usage value, see [Choosing what type of KMS key to create](create-keys.md#symm-asymm-choose "create-keys.md#symm-asymm-choose"). 7. Select a specification (**Key spec**) for your asymmetric
KMS key. 8. Choose **Next**. 9. Type an [alias](kms-alias.md "kms-alias.md") for the KMS key. The
alias name cannot begin with `aws/`. The
`aws/` prefix is reserved by Amazon Web Services to represent
AWS managed keys in your account.

An _alias_ is a friendly name that you
can use to identify the KMS key in the console and in some AWS KMS APIs.
We recommend that you choose an alias
that indicates the type of data you plan to protect or the application you
plan to use with the KMS key.

Aliases are required when you create a KMS key in the AWS Management Console. You
cannot specify an alias when you use the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation, but
you can use the console or the [CreateAlias](../APIReference/API_CreateAlias.md "../APIReference/API_CreateAlias.md") operation to
create an alias for an existing KMS key. For details, see [Aliases in AWS KMS](kms-alias.md "kms-alias.md"). 10. (Optional) Type a description for the KMS key.

Enter a description that explains the type of data you plan to protect or
the application you plan to use with the KMS key.

You can add a description now or update it any time unless the [key state](key-state.md "key-state.md") is `Pending Deletion` or
`Pending Replica Deletion`. To add, change, or delete the
description of an existing customer managed key, edit the description on the details
page for the KMS key in the AWS Management Console or use the [UpdateKeyDescription](../APIReference/API_UpdateKeyDescription.md "../APIReference/API_UpdateKeyDescription.md") operation. 11. (Optional) Type a tag key and an optional tag value. To add more than one
tag to the KMS key, choose **Add tag**.

When you add tags to your AWS resources, AWS generates a cost allocation
report with usage and costs aggregated by tags. Tags can also be used to control access to a KMS key. For information about tagging KMS keys,
see [Tags in AWS KMS](tagging-keys.md "tagging-keys.md") and [ABAC for AWS KMS](abac.md "abac.md"). 12. Choose **Next**. 13. Select the IAM users and roles that can administer the KMS key.

###### Notes

This key policy gives the AWS account full control of this
KMS key. It allows account administrators to use IAM policies to
give other principals permission to manage the KMS key. For details,
see [Default key policy](key-policy-default.md "key-policy-default.md").

IAM best practices discourage the use of IAM users with long-term credentials. Whenever
possible, use IAM roles, which provide temporary credentials. For details,
see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

The AWS KMS console adds key administrators to the key policy under the statement identifier
`"Allow access for Key Administrators"`. Modifying this statement identifier might
impact how the console displays updates that you make to the statement. 14. (Optional) To prevent the selected IAM users and roles from deleting
this KMS key, in the **Key deletion** section at the
bottom of the page, clear the **Allow key administrators to delete
this key** check box. 15. Choose **Next**. 16. Select the IAM users and roles that can use the KMS key for [cryptographic
operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations").

###### Notes

IAM best practices discourage the use of IAM users with long-term credentials. Whenever
possible, use IAM roles, which provide temporary credentials. For details,
see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

The AWS KMS console adds key users to the key policy under the statement identifiers `"Allow use of the key"` and `"Allow 
 attachment of persistent resources"`. Modifying these statement identifiers might
impact how the console displays updates that you make to the statement. 17. (Optional) You can allow other AWS accounts to use this KMS key for
cryptographic operations. To do so, in the **Other
AWS accounts** section at the bottom of the page, choose
**Add another AWS account** and enter the
AWS account identification number of an external account. To add multiple
external accounts, repeat this step.

###### Note

To allow principals in the external accounts to use the KMS key,
administrators of the external account must create IAM policies that
provide these permissions. For more information, see [Allowing users in other accounts to
use a KMS key](key-policy-modifying-external-accounts.md "key-policy-modifying-external-accounts.md"). 18. Choose **Next**. 19. Review the key policy statements for the key. To make changes to the key policy,
select **Edit**. 20. Choose **Next**. 21. Review the key settings that you chose. You can still go back and change
all settings. 22. Choose **Finish** to create the KMS key.
You can use the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md")
operation to create an asymmetric AWS KMS key. These examples use the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any
supported programming language.

When you create an asymmetric KMS key, you must specify the `KeySpec`
parameter, which determines the type of keys you create. Also, you must specify a
`KeyUsage` value of ENCRYPT_DECRYPT, SIGN_VERIFY, or KEY_AGREEMENT.
You cannot change these properties after the KMS key is created.

The `CreateKey` operation doesn't let you specify an alias, but you can
use the [CreateAlias](../APIReference/API_CreateAlias.md "../APIReference/API_CreateAlias.md") operation
to create an alias for your new KMS key.

###### Important

Do not include confidential or sensitive information in the `Description` or `Tags` fields. These fields may appear in plain text in CloudTrail logs and other output.

###### Create an asymmetric KMS key pair for public encryption

The following example uses the `CreateKey` operation to create an
asymmetric KMS key of 4096-bit RSA keys designed for public key
encryption.

```
`$` `aws kms create-key --key-spec RSA_4096 --key-usage ENCRYPT_DECRYPT`
`{
 "KeyMetadata": {
 "KeyState": "Enabled",
 "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
 "KeyManager": "CUSTOMER",
 "Description": "",
 "Arn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
 "CreationDate": 1569973196.214,
 "MultiRegion": false,
 "KeySpec": "RSA_4096",
 "CustomerMasterKeySpec": "RSA_4096",
 "KeyUsage": "ENCRYPT_DECRYPT",
 "EncryptionAlgorithms": [
 "RSAES_OAEP_SHA_1",
 "RSAES_OAEP_SHA_256"
 ],
 "AWSAccountId": "111122223333",
 "Origin": "AWS_KMS",
 "Enabled": true
 }
}`
```

###### Create an asymmetric KMS key pair for signing and verification

The following example command creates an asymmetric KMS key that represents
a pair of ECC keys used for signing and verification. You cannot create an
elliptic curve key pair for encryption and decryption.

```
`$` `aws kms create-key --key-spec ECC_NIST_P521 --key-usage SIGN_VERIFY`
`{
 "KeyMetadata": {
 "KeyState": "Enabled",
 "KeyId": "0987dcba-09fe-87dc-65ba-ab0987654321",
 "CreationDate": 1570824817.837,
 "Origin": "AWS_KMS",
 "SigningAlgorithms": [
 "ECDSA_SHA_512"
 ],
 "Arn": "arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321",
 "AWSAccountId": "111122223333",
 "KeySpec": "ECC_NIST_P521",
 "CustomerMasterKeySpec": "ECC_NIST_P521",
 "KeyManager": "CUSTOMER",
 "Description": "",
 "Enabled": true,
 "MultiRegion": false,
 "KeyUsage": "SIGN_VERIFY"
 }
}`
```

###### Create an asymmetric KMS key pair for deriving shared secrets

The following example command creates an asymmetric KMS key that represents
a pair of ECDH keys used for deriving shared secrets. You cannot create an
elliptic curve key pair for encryption and decryption.

```
`$` `aws kms create-key --key-spec ECC_NIST_P256 --key-usage KEY_AGREEMENT`
`{
 "KeyMetadata": {
 "AWSAccountId": "111122223333",
 "KeyId": "0987dcba-09fe-87dc-65ba-ab0987654321",
 "Arn": "arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321",
 "CreationDate": "2023-12-27T19:10:15.063000+00:00",
 "Enabled": true,
 "Description": "",
 "KeyUsage": "KEY_AGREEMENT",
 "KeyState": "Enabled",
 "Origin": "AWS_KMS",
 "KeyManager": "CUSTOMER",
 "CustomerMasterKeySpec": "ECC_NIST_P256",
 "KeySpec": "ECC_NIST_P256",
 "KeyAgreementAlgorithms": [
 "ECDH"
 ],
 "MultiRegion": false
 }
}`
```
