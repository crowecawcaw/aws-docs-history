**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Tagging Your Amazon Glacier Vaults

You can assign your own metadata to Amazon Glacier vaults in the form of tags. A
_tag_ is a key-value pair that you define for a vault. For basic
information about tagging, including restrictions on tags, see [Tagging Amazon Glacier Resources](tagging.md "tagging.md").

The following topics describe how you can add, list, and remove tags for vaults.

###### Topics

- [Tagging Vaults by Using the Amazon Glacier Console](#tagging-console "#tagging-console")
- [Tagging Vaults by Using the AWS CLI](#tagging-cli "#tagging-cli")
- [Tagging Vaults by Using the Amazon Glacier API](#tagging-api "#tagging-api")
- [Related Sections](#related-sections-tagging-vaults "#related-sections-tagging-vaults")

## Tagging Vaults by Using the Amazon Glacier Console

You can add, list, and remove tags using the Amazon Glacier console, as described in the
following procedures.

###### To view the tags for a vault

1. Sign in to the AWS Management Console and open the Amazon Glacier console at [https://console.aws.amazon.com/glacier/home](https://console.aws.amazon.com/glacier/home "https://console.aws.amazon.com/glacier/home").
2. Under **Select a Region**, select an AWS Region from the Region
   selector.
3. In the left navigation pane, choose **Vaults**.
4. In the **Vaults** list, choose a vault.
5. Choose the **Vaults properties** tab. Scroll to the
   **Tags** section to view the tags associated with the vault.

###### To add a tag to a vault

You can associate up to 50 tags to a vault. Tags that are associated with a vault must
have unique tag keys.

For more information about tag restrictions, see [Tagging Amazon Glacier
Resources](tagging.md "tagging.md").

1. Sign in to the AWS Management Console and open the Amazon Glacier console at [https://console.aws.amazon.com/glacier/home](https://console.aws.amazon.com/glacier/home "https://console.aws.amazon.com/glacier/home").
2. Under **Select a Region**, select an AWS Region from the Region
   selector.
3. In the left navigation pane, choose **Vaults**.
4. In the **Vaults** list, choose the name of the vault that you want to
   add tags to.
5. Choose the **Vault properties** tab.
6. In the **Tags** section, choose **Add**. The
   **Add tags** page appears.
7. On the **Add tags** page, specify the tag key in the
   **Key** field, and optionally specify a tag value in the
   **Value** field.
8. Choose **Save changes**.

###### To edit a tag

1. Sign in to the AWS Management Console and open the Amazon Glacier console at [https://console.aws.amazon.com/glacier/home](https://console.aws.amazon.com/glacier/home "https://console.aws.amazon.com/glacier/home").
2. Under **Select a Region**, select an AWS Region from the Region
   selector.
3. In the left navigation pane, choose **Vaults**.
4. In the **Vaults** list, choose a vault name.
5. Choose the **Vault properties** tab, and then scroll down to the
   **Tags** section.
6. Under **Tags**, select the check box next to the tags that you want
   to change, then choose **Edit**. The **Edit tags** page
   appears.
7. Update the tag key in the **Key** field, and optionally update the
   tag value in the **Value** field.
8. Choose **Save changes**.

###### To remove a tag from a vault

1. Sign in to the AWS Management Console and open the Amazon Glacier console at [https://console.aws.amazon.com/glacier/home](https://console.aws.amazon.com/glacier/home "https://console.aws.amazon.com/glacier/home").
2. Under **Select a Region**, select an AWS Region from the Region
   selector.
3. In the left navigation pane, choose **Vaults**.
4. In the **Vaults** list, choose the name of the vault that you want to
   remove tags from.
5. Choose the **Vault properties** tab. Scroll down to the
   **Tags** section.
6. Under **Tags**, select the check box next to the tags that you want
   to remove, then choose **Delete**.
7. The **Delete tags** dialog box opens. To confirm that you want to
   delete the selected tags, choose **Delete**.

## Tagging Vaults by Using the AWS CLI

Follow these steps to add, list, or remove tags by using the AWS Command Line Interface (AWS CLI).

Each tag is composed of a key and a value. Each vault can have up to 50 tags.

1. To add tags to a vault, use the `add-tags-to-vault` command.

```
aws glacier add-tags-to-vault --vault-name `examplevault` --account-id `111122223333` --tags `id`=`1234`,`date`=`2020`
```

For more information on this vault operation, see [Add Tags To Vault](api-AddTagsToVault.md "api-AddTagsToVault.md") . 2. To list all the tags attached to a vault, use the `list-tags-for-vault`
command.

```
aws glacier list-tags-for-vault --vault-name `examplevault` --account-id `111122223333`
```

For more information on this vault operation, see [List Tags For Vault](api-ListTagsForVault.md "api-ListTagsForVault.md"). 3. To remove one or more tags from the set of tags attached to a vault, use the
`remove-tags-from-vault` command.

```
aws glacier remove-tags-from-vault --vault-name `examplevault` --account-id `111122223333` --tag-keys `date`
```

For more information on this vault operation, see [Remove Tags From Vault](api-RemoveTagsFromVault.md "api-RemoveTagsFromVault.md").

## Tagging Vaults by Using the Amazon Glacier API

You can add, list, and remove tags by using the Amazon Glacier API. For examples, see the
following documentation:

[Add Tags To Vault (POST tags add)](api-AddTagsToVault.md "api-AddTagsToVault.md")

Adds or updates tags for the specified vault.

[List Tags For Vault (GET tags)](api-ListTagsForVault.md "api-ListTagsForVault.md")

Lists the tags for the specified vault.

[Remove Tags From Vault (POST tags remove)](api-RemoveTagsFromVault.md "api-RemoveTagsFromVault.md")

Removes tags from the specified vault.

## Related Sections

- [Tagging Amazon Glacier Resources](tagging.md "tagging.md")
