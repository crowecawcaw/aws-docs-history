# Create an HMAC KMS key

You can create HMAC KMS keys in the AWS KMS console, by using the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") API, or by using
the [AWS::KMS::Key CloudFormation
template](../../../AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.md").

When you create an HMAC KMS key, you must select a key spec. AWS KMS supports multiple
[key specs for HMAC KMS keys](symm-asymm-choose-key-spec.md#hmac-key-specs "symm-asymm-choose-key-spec.md#hmac-key-specs"). The key spec that
you select might be determined by regulatory, security, or business requirements. In
general, longer keys are more resistant to brute-force attacks.

For information about the permissions required to create KMS keys, see [Permissions for creating KMS keys](create-keys.md#create-key-permissions "create-keys.md#create-key-permissions").

You can use the AWS Management Console to create HMAC KMS keys. HMAC KMS keys are symmetric
keys with a key usage of **Generate and verify MAC**. You can also
create multi-Region HMAC keys.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**.
4. Choose **Create key**.
5. For **Key type**, choose
   **Symmetric**.

HMAC KMS keys are symmetric. You use the same key to generate and verify
HMAC tags. 6. For **Key usage**, choose **Generate
and verify MAC**.

Generate and verify MAC is the only valid key usage for HMAC
KMS keys.

###### Note

**Key usage** is displayed for symmetric keys only
when HMAC KMS keys are supported in your selected Region. 7. Select a specification (**Key spec**) for your HMAC
KMS key.

The key spec that you select can be determined by regulatory, security, or
business requirements. In general, longer keys are more secure. 8. To create a [multi-Region](multi-region-keys-overview.md "multi-region-keys-overview.md")
_primary_ HMAC key, in **Advanced
options**, choose **Multi-Region key**. The
[shared properties](multi-region-keys-overview.md#mrk-sync-properties "multi-region-keys-overview.md#mrk-sync-properties") that you
define for this KMS key, such as its key type and key usage, will be
shared with its replica keys.

You cannot use this procedure to create a replica key. To create a
multi-Region _replica_ HMAC key, follow the
[instructions for creating a
replica key](multi-region-keys-replicate.md "multi-region-keys-replicate.md"). 9. Choose **Next**. 10. Enter an [alias](kms-alias.md "kms-alias.md") for the KMS key. The
alias name cannot begin with `aws/`. The
`aws/` prefix is reserved by Amazon Web Services to represent
AWS managed keys in your account.

We recommend that you use an alias that identifies the KMS key as an
HMAC key, such as `HMAC/test-key`. This will make it easier for
you to identify your HMAC keys in the AWS KMS console where you can sort and
filter keys by tags and aliases, but not by key spec or key usage.

Aliases are required when you create a KMS key in the AWS Management Console. You
cannot specify an alias when you use the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation, but
you can use the console or the [CreateAlias](../APIReference/API_CreateAlias.md "../APIReference/API_CreateAlias.md") operation to
create an alias for an existing KMS key. For details, see [Aliases in AWS KMS](kms-alias.md "kms-alias.md"). 11. (Optional) Enter a description for the KMS key.

Enter a description that explains the type of data you plan to protect or
the application you plan to use with the KMS key.

You can add a description now or update it any time unless the [key state](key-state.md "key-state.md") is `Pending Deletion` or
`Pending Replica Deletion`. To add, change, or delete the
description of an existing customer managed key, edit the description on the details
page for the KMS key in the AWS Management Console in the AWS Management Console or use the [UpdateKeyDescription](../APIReference/API_UpdateKeyDescription.md "../APIReference/API_UpdateKeyDescription.md") operation. 12. (Optional) Enter a tag key and an optional tag value. To add more than one
tag to the KMS key, choose **Add tag**.

Consider adding a tag that identifies the key as an HMAC key, such as
`Type=HMAC`. This will make it easier for you to identify
your HMAC keys in the AWS KMS console where you can sort and filter keys by
tags and aliases, but not by key spec or key usage.

When you add tags to your AWS resources, AWS generates a cost allocation
report with usage and costs aggregated by tags. Tags can also be used to control access to a KMS key. For information about tagging KMS keys,
see [Tags in AWS KMS](tagging-keys.md "tagging-keys.md") and [ABAC for AWS KMS](abac.md "abac.md"). 13. Choose **Next**. 14. Select the IAM users and roles that can administer the KMS key.

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
impact how the console displays updates that you make to the statement. 15. (Optional) To prevent the selected IAM users and roles from deleting
this KMS key, in the **Key deletion** section at the
bottom of the page, clear the **Allow key administrators to delete
this key** check box. 16. Choose **Next**. 17. Select the IAM users and roles that can use the KMS key for [cryptographic
operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations").

###### Notes

IAM best practices discourage the use of IAM users with long-term credentials. Whenever
possible, use IAM roles, which provide temporary credentials. For details,
see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

The AWS KMS console adds key users to the key policy under the statement identifiers `"Allow use of the key"` and `"Allow 
 attachment of persistent resources"`. Modifying these statement identifiers might
impact how the console displays updates that you make to the statement. 18. (Optional) You can allow other AWS accounts to use this KMS key for
cryptographic operations. To do so, in the **Other
AWS accounts** section at the bottom of the page, choose
**Add another AWS account** and enter the
AWS account identification number of an external account. To add multiple
external accounts, repeat this step.

###### Note

To allow principals in the external accounts to use the KMS key,
Administrators of the external account must create IAM policies that
provide these permissions. For more information, see [Allowing users in other accounts to
use a KMS key](key-policy-modifying-external-accounts.md "key-policy-modifying-external-accounts.md"). 19. Choose **Next**. 20. Review the key policy statements for the key. To make changes to the key policy,
select **Edit**. 21. Choose **Next**. 22. Review the key settings that you chose. You can still go back and change
all settings. 23. Choose **Finish** to create the HMAC KMS key.
You can use the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md")
operation to create an HMAC KMS key. These examples use the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any
supported programming language.

When you create an HMAC KMS key, you must specify the `KeySpec`
parameter, which determines the type of the KMS key. Also, you must specify a
`KeyUsage` value of GENERATE_VERIFY_MAC, even though it's the only
valid key usage value for HMAC keys. To create a [multi-Region](multi-region-keys-overview.md "multi-region-keys-overview.md") HMAC KMS key, add the
`MultiRegion` parameter with a value of `true`. You cannot
change these properties after the KMS key is created.

The `CreateKey` operation doesn't let you specify an alias, but you can
use the [CreateAlias](../APIReference/API_CreateAlias.md "../APIReference/API_CreateAlias.md") operation
to create an alias for your new KMS key. We recommend that you use an alias that
identifies the KMS key as an HMAC key, such as `HMAC/test-key`. This
will make it easier for you to identify your HMAC keys in the AWS KMS console where
you can sort and filter keys by alias, but not by key spec or key usage.

If you try to create an HMAC KMS key in an AWS Region in which HMAC keys are
not supported, the `CreateKey` operation returns an
`UnsupportedOperationException`

The following example uses the `CreateKey` operation to create a
512-bit HMAC KMS key.

```
`$` `aws kms create-key --key-spec HMAC_512 --key-usage GENERATE_VERIFY_MAC`
`{
 "KeyMetadata": {
 "KeyState": "Enabled",
 "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
 "KeyManager": "CUSTOMER",
 "Description": "",
 "Arn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
 "CreationDate": 1669973196.214,
 "MultiRegion": false,
 "KeySpec": "HMAC_512",
 "CustomerMasterKeySpec": "HMAC_512",
 "KeyUsage": "GENERATE_VERIFY_MAC",
 "MacAlgorithms": [
 "HMAC_SHA_512"
 ],
 "AWSAccountId": "111122223333",
 "Origin": "AWS_KMS",
 "Enabled": true
 }
}`
```
