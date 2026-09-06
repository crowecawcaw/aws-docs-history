

# Create multi-Region primary keys
<a name="create-primary-keys"></a>

You can create a [multi-Region primary key](multi-region-keys-overview.md#mrk-primary-key) in the AWS KMS console or by using the AWS KMS API. You can create the primary key in any AWS Region where AWS KMS supports multi-Region keys.

To create a multi-Region primary key, the principal needs the [same permissions](create-keys.md#create-key-permissions) that they need to create any KMS key, including the [kms:CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html) permission in an IAM policy. The principal also needs the [iam:CreateServiceLinkedRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceLinkedRole.html) permission. You can use the [kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type) condition key to allow or deny permission to create multi-Region primary keys.

**Note**  
When creating your multi-Region primary key, carefully consider the IAM users and roles that you select to administer and use the key. IAM policies can give other IAM users and roles permission to manage the KMS key.  
IAM best practices discourage the use of IAM users with long-term credentials. Whenever possible, use IAM roles, which provide temporary credentials. For details, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Using the AWS KMS console
<a name="create-primary-console"></a>

To create a multi-Region primary key in the AWS KMS console, use the same process that you would use to create any KMS key.. You select a multi-Region key in **Advanced options**. For complete instructions, see [Create a KMS key](create-keys.md).

**Important**  
Do not include confidential or sensitive information in the alias, description, or tags. These fields may appear in plain text in CloudTrail logs and other output.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. To change the AWS Region, use the Region selector in the upper-right corner of the page.

1. In the navigation pane, choose **Customer managed keys**.

1. Choose **Create key**.

1. Select a [symmetric or asymmetric](symmetric-asymmetric.md) key type. Symmetric keys are the default.

   You can create multi-Region symmetric and asymmetric keys, including multi-Region HMAC KMS keys, which are symmetric. 

1. Select your key usage. **Encrypt and decrypt** is the default.

   For help, see [Create a KMS key](create-keys.md), [Create an asymmetric KMS key](asymm-create-key.md), or [Create an HMAC KMS key](hmac-create-key.md).

1. Expand **Advanced options**.

1. Under **Key material origin**, to have AWS KMS generate the key material that your primary and replica keys will share, choose **KMS**. If you are [importing key material](importing-keys-create-cmk.md) into the primary and replica keys, choose **External (Import key material)**. 

1. Under **Regionality**, choose **Multi-Region key**.

   You can't change this setting after you create the KMS key. 

1. Type an [alias](kms-alias.md) for the primary key. 

   Aliases are not a shared property of multi-Region keys. You can give your multi-Region primary key and its replicas the same alias or different aliases. AWS KMS does not synchronize the aliases of multi-Region keys.
**Note**  
Adding, deleting, or updating an alias can allow or deny permission to the KMS key. For details, see [ABAC for AWS KMS](abac.md) and [Use aliases to control access to KMS keys](alias-authorization.md).

1. (Optional) Type a description of the primary key.

   Descriptions are not a shared property of multi-Region keys. You can give your multi-Region primary key and its replicas the same description or different descriptions. AWS KMS does not synchronize the key descriptions of multi-Region keys.

1. (Optional) Type a tag key and an optional tag value. To assign more than one tag to the primary key, choose **Add tag**.

   Tags are not a shared property of multi-Region keys. You can give your multi-Region primary key and its replicas the same tags or different tags. AWS KMS does not synchronize the tags of multi-Region keys. You can change the tags on KMS keys at any time.
**Note**  
Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see [ABAC for AWS KMS](abac.md) and [Use tags to control access to KMS keys](tag-authorization.md).

1. Select the IAM users and roles that can administer the primary key.
**Notes**  
This step starts the process of creating a [key policy](key-policies.md) for the primary key. Key policies are not a shared property of multi-Region keys. You can give your multi-Region primary key and its replicas the same key policy or different key policies. AWS KMS does not synchronize the key policies of multi-Region keys. You can change the key policy of a KMS key at any time.
When creating a multi-Region primary key, consider using the [default key policy](key-policy-default.md) generated by the console. If you modify this policy, the console won't provide steps to select key administrators and users when creating replica keys, nor will it add the corresponding policy statements. As a result, you'll need to add these manually.
The AWS KMS console adds key administrators to the key policy under the statement identifier `"Allow access for Key Administrators"`. Modifying this statement identifier might impact how the console displays updates that you make to the statement.

1. (Optional) To prevent the selected IAM users and roles from deleting this KMS key, in the **Key deletion** section at the bottom of the page, clear the **Allow key administrators to delete this key** check box.

1. Choose **Next**.

1. Select the IAM users and roles that can use the KMS key for [cryptographic operations](kms-cryptography.md#cryptographic-operations).
**Notes**  
The AWS KMS console adds key users to the key policy under the statement identifiers `"Allow use of the key"` and `"Allow attachment of persistent resources"`. Modifying these statement identifiers might impact how the console displays updates that you make to the statement.

1. (Optional) You can allow other AWS accounts to use this KMS key for cryptographic operations. To do so, in the **Other AWS accounts** section at the bottom of the page, choose **Add another AWS account** and enter the AWS account identification number of an external account. To add multiple external accounts, repeat this step.
**Note**  
To allow principals in the external accounts to use the KMS key, Administrators of the external account must create IAM policies that provide these permissions. For more information, see [Allowing users in other accounts to use a KMS key](key-policy-modifying-external-accounts.md).

1. Choose **Next**.

1. Review the key policy statements for the key. To make changes to the key policy, select **Edit**.

1. Choose **Next**.

1. Review the key settings that you chose. You can still go back and change all settings.

1. Choose **Finish** to create the multi-Region primary key.

## Using the AWS KMS API
<a name="create-primary-api"></a>

To create a multi-Region primary key, use the [CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html) operation. Use the `MultiRegion` parameter with a value of `True`.

For example, the following command creates a multi-Region primary key in the caller's AWS Region (us-east-1). It accepts default values for all other properties, including the key policy. The default values for multi-Region primary keys are the same as the default values for all other KMS keys, including the [default key policy](key-policy-default.md). This procedure creates a symmetric encryption key, the default KMS key. 

The response includes the `MultiRegion` element and the `MultiRegionConfiguration` element with typical sub-elements and values for a multi-Region primary key with no replica keys. The [key ID](concepts.md#key-id-key-id) of a multi-Region key always begins with `mrk-`.

**Important**  
Do not include confidential or sensitive information in the `Description` or `Tags` fields. These fields may appear in plain text in CloudTrail logs and other output.

```
$ aws kms create-key --multi-region
{
    "KeyMetadata": {
        "Origin": "AWS_KMS",
        "KeyId": "mrk-1234abcd12ab34cd56ef1234567890ab",
        "Description": "",
        "KeyManager": "CUSTOMER",
        "Enabled": true,
        "KeySpec": "SYMMETRIC_DEFAULT",
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "KeyState": "Enabled",
        "CreationDate": 1606329032.475,
        "Arn": "arn:aws:kms:us-east-1:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab",
        "AWSAccountId": "111122223333",
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ],
        "MultiRegion": true,
        "MultiRegionConfiguration": { 
            "MultiRegionKeyType": "PRIMARY",
            "PrimaryKey": { 
                "Arn": "arn:aws:kms:us-east-1:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab",
                "Region": "us-east-1"
            },
            "ReplicaKeys": [ ]
      }
    }
}
```