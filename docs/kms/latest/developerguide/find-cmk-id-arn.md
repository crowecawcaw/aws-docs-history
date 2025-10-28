# Find the key ID and key ARN

To identify an AWS KMS key, you can use the [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id")
or the Amazon Resource Name ([key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN")). In [cryptographic operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations"), you can also use the
[alias name](concepts.md#key-id-alias-name "concepts.md#key-id-alias-name") or [alias ARN](concepts.md#key-id-alias-ARN "concepts.md#key-id-alias-ARN").

You can use the [AWS KMS console](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms") or the [ListKeys](../APIReference/API_ListKeys.md "../APIReference/API_ListKeys.md") operation to identify the key ID
and key ARN of each KMS key in your account and Region.

For detailed information about the KMS key identifiers supported by AWS KMS, see [Key identifiers (KeyId)](concepts.md#key-id "concepts.md#key-id"). For help finding an alias name and alias ARN,
see [Find the alias name and alias ARN for a KMS key](alias-view.md "alias-view.md").

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. To view the keys in your account that you create and manage, in the navigation
   pane choose **Customer managed keys**. To view the keys in your account that AWS creates and manages for you, in the navigation pane, choose **AWS managed keys**.
4. To find the [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id") for a KMS key,
   see the row that begins with the KMS key alias.

The **Key ID** column appears in the tables by default.
If the Key ID column doesn't appear in your table, use the procedure
described in [Customize your console view](viewing-console-customize.md "viewing-console-customize.md") to restore it. You
can also view the key ID of a KMS key on its details page.

![Customer managed keys table showing Key ID for a single key-test alias.](images/find-key-id-new.png) 5. To find the Amazon Resource Name (ARN) of the KMS key, choose the key ID
or alias. The [key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN") appears in the
**General Configuration** section.

![General configuration section showing key alias, status, and ARN details.](images/find-key-arn.png)
To find the [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id") and [key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN") of an AWS KMS key, use the [ListKeys](../APIReference/API_ListKeys.md "../APIReference/API_ListKeys.md") operation.

The `ListKeys` operation returns the key ID and Amazon Resource Name
(ARN) of all KMS keys in the caller's account and Region.

For example, this call to the `ListKeys` operation returns the ID and
ARN of each KMS key in this fictitious account. For examples in multiple
programming languages, see [Use ListKeys with an AWS SDK or CLI](example_kms_ListKeys_section.md "example_kms_ListKeys_section.md").

```
`$` `aws kms list-keys`
`{
 "Keys": [
 {
 "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
 "KeyArn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
 },
 {
 "KeyId": "0987dcba-09fe-87dc-65ba-ab0987654321",
 "KeyArn": "arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321"
 }
 ]
}`
```
