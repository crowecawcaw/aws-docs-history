# Create aliases

You can create aliases in the AWS KMS console or by using AWS KMS API operations.

The alias must be string of 1–256 characters. It can contain only alphanumeric
characters, forward slashes (/), underscores (\_), and dashes (-). The alias name for a [customer managed key](concepts.md#customer-mgn-key "concepts.md#customer-mgn-key") cannot begin with `alias/aws/`. The
`alias/aws/` prefix is reserved for [AWS managed key](concepts.md#aws-managed-key "concepts.md#aws-managed-key").

You can create an alias for a new KMS key or for an existing KMS key. You might add an
alias so that a particular KMS key is used in a project or application.

You can also use a AWS CloudFormation template to create an alias for a KMS key. For more
information, see [AWS::KMS::Alias](../../../AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.md") in the _AWS CloudFormation User Guide_.

When you [create a KMS key](create-keys.md "create-keys.md") in the AWS KMS console,
you must create an alias for the new KMS key. To create an alias for an existing
KMS key, use the **Aliases** tab on the detail page for the
KMS key.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**. You cannot manage aliases for AWS managed keys or
   AWS owned keys.
4. In the table, choose the key ID or alias of the KMS key. Then, on the KMS key
   detail page, choose the **Aliases** tab.

If a KMS key has multiple aliases, the **Aliases** column in
the table displays one alias and an alias summary, such as **(+_n_ more)**. Choosing the alias summary takes you
directly to the **Aliases** tab on the KMS key detail page. 5. On the **Aliases** tab, choose **Create alias**.
Enter an alias name and choose **Create alias**.

###### Important

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

###### Note

Do not add the `alias/` prefix. The console automatically adds it for
you. If you enter `alias/ExampleAlias`, the actual alias name will be
`alias/alias/ExampleAlias`.
To create an alias, use the [CreateAlias](../APIReference/API_CreateAlias.md "../APIReference/API_CreateAlias.md") operation. Unlike the process of creating KMS keys in the
console, the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation
doesn't create an alias for a new KMS key.

###### Important

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

You can use the `CreateAlias` operation to create an alias for a new
KMS key with no alias. You can also use the `CreateAlias` operation to add an
alias to any existing KMS key or to recreate an alias that was accidentally deleted.

In the AWS KMS API operations, the alias name must begin with `alias/`
followed by a name, such as `alias/ExampleAlias`. The alias must be unique in
the account and Region. To find the alias names that are already in use, use the [ListAliases](../APIReference/API_ListAliases.md "../APIReference/API_ListAliases.md") operation. The alias name is
case sensitive.

The `TargetKeyId` can be any [customer managed key](concepts.md#customer-mgn-key "concepts.md#customer-mgn-key")
in the same AWS Region. To identify the KMS key, use its [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id") or [key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN"). You cannot use another
alias.

The following example creates the `example-key` alias and associates it
with the specified KMS key. These examples use the AWS Command Line Interface (AWS CLI). For examples in
multiple programming languages, see [Use CreateAlias with an AWS SDK or CLI](example_kms_CreateAlias_section.md "example_kms_CreateAlias_section.md").

```
`$` `aws kms create-alias \
 --alias-name alias/example-key \
 --target-key-id 1234abcd-12ab-34cd-56ef-1234567890ab`
```

`CreateAlias` does not return any output. To see the new alias, use the
`ListAliases` operation. For details, see [Using the AWS KMS API](alias-view.md#alias-view-api "alias-view.md#alias-view-api").
