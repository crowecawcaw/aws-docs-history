# Removing tags from Amazon Personalize resources

You can remove tags from Amazon Personalize resources with the Amazon Personalize console or the [UntagResource](API_UntagResource.md "API_UntagResource.md") API operation with the AWS Command Line Interface (AWS CLI) or AWS SDKs. The following examples show
how to remove a tag from an Amazon Personalize dataset group. You can remove tags from other Amazon Personalize resources in the same way.

###### Topics

- [Removing tags (console)](#remove-tag-console "#remove-tag-console")
- [Removing tags (AWS CLI)](#remove-tag-cli "#remove-tag-cli")
- [Removing tags (AWS SDKs)](#remove-tag-sdks "#remove-tag-sdks")

## Removing tags (console)

After you add tags to a resource in Amazon Personalize, you can remove the tags with the Amazon Personalize console. The following example
removes a tag from a dataset group

###### To remove tags from a dataset group

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to your account.
2. Choose your dataset group.
3. At the bottom of the page, choose the **Tags** tab and choose **Manage
   tags**.
4. For each tag that you want to remove, choose **Remove**.
5. Choose **Save** to remove the tags.

## Removing tags (AWS CLI)

To remove tags from an existing resource with the AWS CLI, use the following `untag-resource` command.
For `resource-arn`, specify the
Amazon Resource Name (ARN) of the resource. For `tag-keys`, specify the keys of the tags to be removed.

```
aws personalize untag-resource \
--resource-arn `resource ARN` \
--tag-keys `key1` `key2`
```

## Removing tags (AWS SDKs)

To remove tags from an existing Amazon Personalize resource with the AWS SDKs, use the [UntagResource](API_UntagResource.md "API_UntagResource.md") API operation.
The following code shows how to remove multiple tags from a dataset group with the SDK for Python (Boto3). For `resourceArn`, specify the
Amazon Resource Name (ARN) of the resource. For `tagKeys`, specify the keys of the tags to be removed.

```
import boto3

personalize = boto3.client('personalize')

response = personalize.untag_resource(
    resourceArn="`Resource ARN`",
    tagKeys=["`tag1Key`", "`tag2Key`"]
)
```
