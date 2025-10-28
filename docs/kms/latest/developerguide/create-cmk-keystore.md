# Create a KMS key in an AWS CloudHSM key store

After you have created an AWS CloudHSM key store, you can create AWS KMS keys in your key store. They must be [symmetric encryption KMS keys](symm-asymm-choose-key-spec.md#symmetric-cmks "symm-asymm-choose-key-spec.md#symmetric-cmks") with key material that AWS KMS generates. You cannot
create [asymmetric KMS keys](symmetric-asymmetric.md "symmetric-asymmetric.md"), [HMAC KMS keys](hmac.md "hmac.md") or KMS keys with [imported key
material](importing-keys.md "importing-keys.md") in a custom key store. Also, you cannot use symmetric encryption KMS keys in
a custom key store to generate asymmetric data key pairs. KMS cannot communicate over IPv6 with AWS CloudHSM key stores.

To create a KMS key in an AWS CloudHSM key store, the AWS CloudHSM key store must be [connected to the associated AWS CloudHSM cluster](connect-keystore.md "connect-keystore.md") and the cluster
must contain at least two active HSMs in different Availability Zones. To find the connection
state and number of HSMs, view the [AWS CloudHSM key stores
page](view-keystore.md#view-keystore-console "view-keystore.md#view-keystore-console") in the AWS Management Console. When using the API operations, use the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md") operation
to verify that the AWS CloudHSM key store is connected. To verify the number of active HSMs in the
cluster and their Availability Zones, use the AWS CloudHSM [DescribeClusters](../../../cloudhsm/latest/APIReference/API_DescribeClusters.md "../../../cloudhsm/latest/APIReference/API_DescribeClusters.md") operation.

When you create a KMS key in your AWS CloudHSM key store, AWS KMS creates the KMS key in AWS KMS.
But, it creates the key material for the KMS key in the associated AWS CloudHSM cluster.
Specifically, AWS KMS signs into the cluster as the [kmsuser CU that you created](create-keystore.md#before-keystore "create-keystore.md#before-keystore"). Then it creates a persistent,
non-extractable, 256-bit Advanced Encryption Standard (AES) symmetric key in the cluster. AWS KMS
sets the value of the [key label
attribute](../../../cloudhsm/latest/userguide/cloudhsm_cli-key-attributes.md "../../../cloudhsm/latest/userguide/cloudhsm_cli-key-attributes.md"), which is visible only in the cluster, to Amazon Resource Name (ARN) of the
KMS key.

When the command succeeds, the [key state](key-state.md "key-state.md") of the new
KMS key is `Enabled` and its origin is `AWS_CLOUDHSM`. You cannot change
the origin of any KMS key after you create it. When you view a KMS key in an AWS CloudHSM key store
in the AWS KMS console or by using the [DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md") operation, you can see typical properties, like its key ID, key state,
and creation date. But you can also see the custom key store ID and (optionally) the AWS CloudHSM
cluster ID.

If your attempt to create a KMS key in your AWS CloudHSM key store fails, use the error message
to help you determine the cause. It might indicate that the AWS CloudHSM key store is not connected
(`CustomKeyStoreInvalidStateException`) or the associated AWS CloudHSM cluster doesn't
have the two active HSMs that are required for this operation
(`CloudHsmClusterInvalidConfigurationException`). For help see [Troubleshooting a custom key store](fix-keystore.md "fix-keystore.md").

For an example of the AWS CloudTrail log of the operation that creates a KMS key in an AWS CloudHSM key
store, see [CreateKey](ct-createkey.md "ct-createkey.md").

## Create a new KMS key in your CloudHSM key

store

You can create a symmetric encryption KMS key in your AWS CloudHSM key store in the AWS KMS
console or by using the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md")
operation.

Use the following procedure to create a symmetric encryption KMS key in an AWS CloudHSM key
store.

###### Note

Do not include confidential or sensitive information in the alias, description, or tags. These fields may appear in plain text in CloudTrail logs and other output.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**.
4. Choose **Create key**.
5. Choose **Symmetric**.
6. In **Key usage**, the **Encrypt and decrypt**
   option is selected for you. Do not change it.
7. Choose **Advanced options**.
8. For **Key material origin**, choose **AWS CloudHSM key
   store**.

You cannot create a multi-Region key in an AWS CloudHSM key store. 9. Choose **Next**. 10. Select an AWS CloudHSM key store for your new KMS key. To create a new AWS CloudHSM key store,
choose **Create custom key store**.

The AWS CloudHSM key store that you select must have a status of
**Connected**. Its associated AWS CloudHSM cluster must be active and
contain at least two active HSMs in different Availability Zones.

For help with connecting an AWS CloudHSM key store, see [Disconnect an AWS CloudHSM key store](connect-keystore.md "connect-keystore.md"). For help with adding HSMs, see [Adding an HSM](../../../cloudhsm/latest/userguide/add-remove-hsm.md#add-hsm "../../../cloudhsm/latest/userguide/add-remove-hsm.md#add-hsm") in the _AWS CloudHSM User Guide_. 11. Choose **Next**. 12. Type an alias and an optional description for the KMS key. 13. (Optional). On the **Add Tags** page, add tags that identify or
categorize your KMS key.

When you add tags to your AWS resources, AWS generates a cost allocation
report with usage and costs aggregated by tags. Tags can also be used to control access to a KMS key. For information about tagging KMS keys,
see [Tags in AWS KMS](tagging-keys.md "tagging-keys.md") and [ABAC for AWS KMS](abac.md "abac.md"). 14. Choose **Next**. 15. In the **Key Administrators** section, select the IAM users and
roles who can manage the KMS key. For more information, see [Allows key administrators to
administer the KMS key](key-policy-default.md#key-policy-default-allow-administrators "key-policy-default.md#key-policy-default-allow-administrators").

###### Notes

IAM policies can give other IAM users and roles permission to use the
KMS key.

IAM best practices discourage the use of IAM users with long-term credentials. Whenever
possible, use IAM roles, which provide temporary credentials. For details,
see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

The AWS KMS console adds key administrators to the key policy under the statement identifier
`"Allow access for Key Administrators"`. Modifying this statement identifier might
impact how the console displays updates that you make to the statement. 16. (Optional) To prevent these key administrators from deleting this KMS key, clear
the box at the bottom of the page for **Allow key administrators to delete this
key.** 17. Choose **Next**. 18. In the **This account** section, select the IAM users and roles in
this AWS account that can use the KMS key in [cryptographic operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations"). For more
information, see [Allows key users to use
the KMS key](key-policy-default.md#key-policy-default-allow-users "key-policy-default.md#key-policy-default-allow-users").

###### Notes

IAM best practices discourage the use of IAM users with long-term credentials. Whenever
possible, use IAM roles, which provide temporary credentials. For details,
see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

The AWS KMS console adds key users to the key policy under the statement identifiers `"Allow use of the key"` and `"Allow 
 attachment of persistent resources"`. Modifying these statement identifiers might
impact how the console displays updates that you make to the statement. 19. (Optional) You can allow other AWS accounts to use this KMS key for
cryptographic operations. To do so, in the **Other AWS accounts**
section at the bottom of the page, choose **Add another AWS account**
and enter the AWS account ID of an external account. To add multiple external
accounts, repeat this step.

###### Note

Administrators of the other AWS accounts must also allow access to the KMS key
by creating IAM policies for their users. For more information, see [Allowing users in other accounts to
use a KMS key](key-policy-modifying-external-accounts.md "key-policy-modifying-external-accounts.md"). 20. Choose **Next**. 21. Review the key policy statements for the key. To make changes to the key policy,
select **Edit**. 22. Choose **Next**. 23. Review the key settings that you chose. You can still go back and change all
settings. 24. When you're done, choose **Finish** to create the key.
When the procedure succeeds, the display shows the new KMS key in the AWS CloudHSM key store
that you chose. When you choose the name or alias of the new KMS key, the
**Cryptographic configuration** tab on its detail page displays the
origin of the KMS key (**AWS CloudHSM**), the name, ID, and type of the custom
key store, and the ID of the AWS CloudHSM cluster. If the procedure fails, an error message appears
that describes the failure.

###### Tip

To make it easier to identify KMS keys in a custom key store, on the
**Customer managed keys** page, add the **Custom key store
ID** column to the display. Click the gear icon in the upper-right and select
**Custom key store ID**. For details, see [Customize your console view](viewing-console-customize.md "viewing-console-customize.md").

To create a new AWS KMS key (KMS key) in your AWS CloudHSM
key store, use the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation.
Use the `CustomKeyStoreId` parameter to identify your custom key store and
specify an `Origin` value of `AWS_CLOUDHSM`.

You might also want to use the `Policy` parameter to specify a key policy.
You can change the key policy ([PutKeyPolicy](../APIReference/API_PutKeyPolicy.md "../APIReference/API_PutKeyPolicy.md")) and add optional elements, such as a [description](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md") and [tags](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") at any time.

The examples in this section use the [AWS Command Line Interface
(AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported programming language.

The following example begins with a call to the [DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md")
operation to verify that the AWS CloudHSM key store is connected to its associated AWS CloudHSM cluster.
By default, this operation returns all custom keys stores in your account and Region. To
describe only a particular AWS CloudHSM key store, use its `CustomKeyStoreId` or
`CustomKeyStoreName` parameter (but not both).

Before running this command, replace the example custom key store ID with a valid
ID.

###### Note

Do not include confidential or sensitive information in the `Description` or `Tags` fields. These fields may appear in plain text in CloudTrail logs and other output.

```
`$` `aws kms describe-custom-key-stores --custom-key-store-id `cks-1234567890abcdef0``
`{
 "CustomKeyStores": [
 "CustomKeyStoreId": "cks-1234567890abcdef0",
 "CustomKeyStoreName": "ExampleKeyStore",
 "CustomKeyStoreType": "AWS CloudHSM key store",
 "CloudHsmClusterId": "cluster-1a23b4cdefg",
 "TrustAnchorCertificate": "`<certificate string appears here>`",
 "CreationDate": "1.499288695918E9",
 **"ConnectionState": "CONNECTED"**
 ],
}`
```

The next example command uses the [DescribeClusters](../../../cloudhsm/latest/APIReference/API_DescribeClusters.md "../../../cloudhsm/latest/APIReference/API_DescribeClusters.md") operation to verify that the AWS CloudHSM cluster that is associated
with the `ExampleKeyStore` (cluster-1a23b4cdefg) has at least two active
HSMs. If the cluster has fewer than two HSMs, the `CreateKey` operation
fails.

```
`$` `aws cloudhsmv2 describe-clusters`
`{
 "Clusters": [
 {
 "SubnetMapping": {
 ...
 },
 "CreateTimestamp": 1507133412.351,
 "ClusterId": "cluster-1a23b4cdefg",
 "SecurityGroup": "sg-865af2fb",
 "HsmType": "hsm1.medium",
 "VpcId": "vpc-1a2b3c4d",
 "BackupPolicy": "DEFAULT",
 "Certificates": {
 "ClusterCertificate": "-----BEGIN CERTIFICATE-----\...\n-----END CERTIFICATE-----\n"
 },
 "Hsms": [
 {
 "AvailabilityZone": "us-west-2a",
 "EniIp": "10.0.1.11",
 "ClusterId": "cluster-1a23b4cdefg",
 "EniId": "eni-ea8647e1",
 "StateMessage": "HSM created.",
 "SubnetId": "subnet-a6b10bd1",
 "HsmId": "hsm-abcdefghijk",
 *"State": "ACTIVE"*
 },
 {
 "AvailabilityZone": "us-west-2b",
 "EniIp": "10.0.0.2",
 "ClusterId": "cluster-1a23b4cdefg",
 "EniId": "eni-ea8647e1",
 "StateMessage": "HSM created.",
 "SubnetId": "subnet-b6b10bd2",
 "HsmId": "hsm-zyxwvutsrqp",
 *"State": "ACTIVE"*
 },
 ],
 "State": "ACTIVE"
 }
 ]
}`
```

This example command uses the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation to create a KMS key in an AWS CloudHSM key store. To create a
KMS key in an AWS CloudHSM key store, you must provide the custom key store ID of the AWS CloudHSM key
store and specify an `Origin` value of `AWS_CLOUDHSM`.

The response includes the IDs of the custom key store and the AWS CloudHSM cluster.

Before running this command, replace the example custom key store ID with a valid
ID.

```
`$` `aws kms create-key --origin AWS_CLOUDHSM --custom-key-store-id `cks-1234567890abcdef0``
`{
 "KeyMetadata": {
 "AWSAccountId": "111122223333",
 "Arn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
 "CreationDate": 1.499288695918E9,
 "Description": "Example key",
 "Enabled": true,
 "MultiRegion": false,
 "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
 "KeyManager": "CUSTOMER",
 "KeyState": "Enabled",
 "KeyUsage": "ENCRYPT_DECRYPT",
 "Origin": "AWS_CLOUDHSM"
 "CloudHsmClusterId": "cluster-1a23b4cdefg",
 "CustomKeyStoreId": "cks-1234567890abcdef0"
 "KeySpec": "SYMMETRIC_DEFAULT",
 "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
 "EncryptionAlgorithms": [
 "SYMMETRIC_DEFAULT"
 ]
 }
}`
```
