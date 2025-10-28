# Create a symmetric encryption KMS key

This topic explains how to create the basic KMS key, a [symmetric encryption KMS key](symm-asymm-choose-key-spec.md#symmetric-cmks "symm-asymm-choose-key-spec.md#symmetric-cmks") for a single Region with key material from AWS KMS. You
can use this KMS key to protect your resources in an AWS service.

You can create symmetric encryption KMS keys in the AWS KMS console, by using the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") API, or by using the [AWS::KMS::Key AWS CloudFormation template](../../../AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.md").

The default key spec, [SYMMETRIC_DEFAULT](symm-asymm-choose-key-spec.md#symmetric-cmks "symm-asymm-choose-key-spec.md#symmetric-cmks"), is the key
spec for symmetric encryption KMS keys. When you select the **Symmetric**
key type and the **Encrypt and decrypt** key usage in the AWS KMS console, it
selects the `SYMMETRIC_DEFAULT` key spec. In the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation, if you don't specify a
`KeySpec` value, SYMMETRIC_DEFAULT is selected. If you don't have a reason to use
a different key spec, SYMMETRIC_DEFAULT is a good choice.

For information about quotas that apply to KMS keys, see [Quotas](limits.md "limits.md").

You can use the AWS Management Console to create AWS KMS keys (KMS keys).

###### Important

Do not include confidential or sensitive information in the alias, description, or tags. These fields may appear in plain text in CloudTrail logs and other output.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**.
4. Choose **Create key**.
5. To create a symmetric encryption KMS key, for **Key
   type** choose **Symmetric**.
6. In **Key usage**, the **Encrypt and decrypt**
   option is selected for you.
7. Choose **Next**.
8. Type an alias for the KMS key. The alias name cannot begin with
   `aws/`. The `aws/` prefix is reserved by
   Amazon Web Services to represent AWS managed keys in your account.

###### Note

Adding, deleting, or updating an alias can allow or deny permission to the KMS key. For details, see [ABAC for AWS KMS](abac.md "abac.md") and [Use aliases to control access to KMS keys](alias-authorization.md "alias-authorization.md").

An alias is a display name that you can use to identify the KMS key. We
recommend that you choose an alias that indicates the type of data you plan to protect
or the application you plan to use with the KMS key.

Aliases are required when you create a KMS key in the AWS Management Console. They are
optional when you use the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation. 9. (Optional) Type a description for the KMS key.

You can add a description now or update it any time unless the [key state](key-state.md "key-state.md") is `Pending Deletion` or
`Pending Replica Deletion`. To add, change, or delete the description of
an existing customer managed key, edit the description on the details page for the KMS key in
the AWS Management Console or use the [UpdateKeyDescription](../APIReference/API_UpdateKeyDescription.md "../APIReference/API_UpdateKeyDescription.md") operation. 10. (Optional) Type a tag key and an optional tag value. To add more than one tag to
the KMS key, choose **Add tag**.

###### Note

Tagging or untagging a KMS key can allow or deny permission to the
KMS key. For details, see [ABAC for AWS KMS](abac.md "abac.md") and [Use tags to control access to KMS keys](tag-authorization.md "tag-authorization.md").

When you add tags to your AWS resources, AWS generates a cost allocation
report with usage and costs aggregated by tags. Tags can also be used to control access to a KMS key. For information about tagging KMS keys,
see [Tags in AWS KMS](tagging-keys.md "tagging-keys.md") and [ABAC for AWS KMS](abac.md "abac.md"). 11. Choose **Next**. 12. Select the IAM users and roles that can administer the KMS key.

###### Notes

This key policy gives the AWS account full control of this KMS key. It
allows account administrators to use IAM policies to give other principals
permission to manage the KMS key. For details, see [Default key policy](key-policy-default.md "key-policy-default.md").

IAM best practices discourage the use of IAM users with long-term credentials. Whenever
possible, use IAM roles, which provide temporary credentials. For details,
see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

The AWS KMS console adds key administrators to the key policy under the statement identifier
`"Allow access for Key Administrators"`. Modifying this statement identifier might
impact how the console displays updates that you make to the statement. 13. (Optional) To prevent the selected IAM users and roles from deleting this
KMS key, in the **Key deletion** section at the bottom of the page,
clear the **Allow key administrators to delete this key** check
box. 14. Choose **Next**. 15. Select the IAM users and roles that can use the key in [cryptographic operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations")

###### Notes

IAM best practices discourage the use of IAM users with long-term credentials. Whenever
possible, use IAM roles, which provide temporary credentials. For details,
see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

The AWS KMS console adds key users to the key policy under the statement identifiers `"Allow use of the key"` and `"Allow 
 attachment of persistent resources"`. Modifying these statement identifiers might
impact how the console displays updates that you make to the statement. 16. (Optional) You can allow other AWS accounts to use this KMS key for
cryptographic operations. To do so, in the **Other AWS accounts**
section at the bottom of the page, choose **Add another
AWS account** and enter the AWS account identification number of an
external account. To add multiple external accounts, repeat this step.

###### Note

To allow principals in the external accounts to use the KMS key,
Administrators of the external account must create IAM policies that provide these
permissions. For more information, see [Allowing users in other accounts to
use a KMS key](key-policy-modifying-external-accounts.md "key-policy-modifying-external-accounts.md"). 17. Choose **Next**. 18. Review the key policy statements for the key. To make changes to the key policy,
select **Edit**. 19. Choose **Next**. 20. Review the key settings that you chose. You can still go back and change all
settings. 21. Choose **Finish** to create the KMS key.
You can use the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md")
operation to create AWS KMS keys of all types. These examples use the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"). For examples in multiple
programming languages, see [Use CreateKey with an AWS SDK or CLI](example_kms_CreateKey_section.md "example_kms_CreateKey_section.md").

###### Important

Do not include confidential or sensitive information in the `Description` or `Tags` fields. These fields may appear in plain text in CloudTrail logs and other output.

The following operation creates a symmetric encryption key in a single Region backed
by key material generated by AWS KMS. This operation has no required parameters. However,
you might also want to use the `Policy` parameter to specify a key policy. You
can change the key policy ([PutKeyPolicy](../APIReference/API_PutKeyPolicy.md "../APIReference/API_PutKeyPolicy.md")) and add optional elements, such as a [description](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md") and [tags](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") at any time. You can also create
[asymmetric keys](asymm-create-key.md#create-asymmetric-keys-api "asymm-create-key.md#create-asymmetric-keys-api"), [multi-Region keys](create-primary-keys.md "create-primary-keys.md"), keys with [imported key material](importing-keys-create-cmk.md#importing-keys-create-cmk-api "importing-keys-create-cmk.md#importing-keys-create-cmk-api"), and keys in [custom key stores](create-cmk-keystore.md#create-cmk-keystore-api "create-cmk-keystore.md#create-cmk-keystore-api"). To create data keys for
client-side encryption, use the [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") operation.

The `CreateKey` operation doesn't let you specify an alias, but you can use
the [CreateAlias](../APIReference/API_CreateAlias.md "../APIReference/API_CreateAlias.md") operation to create
an alias for your new KMS key.

The following is an example of a call to the `CreateKey` operation with no
parameters. This command uses all of the default values. It creates a symmetric encryption
KMS key with key material generated by AWS KMS.

```
`$` `aws kms create-key`
`{
 "KeyMetadata": {
 "Origin": "AWS_KMS",
 "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
 "Description": "",
 "KeyManager": "CUSTOMER",
 "Enabled": true,
 "KeySpec": "SYMMETRIC_DEFAULT",
 "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
 "KeyUsage": "ENCRYPT_DECRYPT",
 "KeyState": "Enabled",
 "CreationDate": 1502910355.475,
 "Arn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
 "AWSAccountId": "111122223333",
 "MultiRegion": false
 "EncryptionAlgorithms": [
 "SYMMETRIC_DEFAULT"
 ],
 }
}`
```

If you do not specify a key policy for your new KMS key, the [default key policy](key-policy-default.md "key-policy-default.md") that `CreateKey`
applies differs from the default key policy that the console applies when you use it to
create a new KMS key.

For example, this call to the [GetKeyPolicy](../APIReference/API_GetKeyPolicy.md "../APIReference/API_GetKeyPolicy.md") operation returns the key policy that `CreateKey`
applies. It gives the AWS account access to the KMS key and allows it to create
AWS Identity and Access Management (IAM) policies for the KMS key. For detailed information about IAM
policies and key policies for KMS keys, see [KMS key access and permissions](control-access.md "control-access.md")

```
`$` `aws kms get-key-policy --key-id 1234abcd-12ab-34cd-56ef-1234567890ab --policy-name default --output text`
```

JSON

```
`{
 "Version":"2012-10-17",
 "Id" : "key-default-1",
 "Statement" : [ {
 "Sid" : "EnableIAMUserPermissions",
 "Effect" : "Allow",
 "Principal" : {
 "AWS" : "arn:aws:iam::`111122223333`:root"
 },
 "Action" : "kms:*",
 "Resource" : "*"
 } ]
}`

```
