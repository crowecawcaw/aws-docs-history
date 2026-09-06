

# Tagging S3 Files resources
<a name="s3-files-tagging"></a>

To help you manage your S3 Files resources, you can assign your own metadata to each resource in the form of tags. With tags, you can categorize your AWS resources in different ways, for example, by purpose, owner, or environment. This categorization is useful when you have many resources of the same type as you can quickly identify a specific resource based on the tags that you've assigned to it. You can tag S3 file system and access point resources that already exist in your account. This topic describes tags and shows you how to create them.

## Tag restrictions
<a name="s3-files-tagging-restrictions"></a>

The following basic restrictions apply to tags:
+ Maximum number of tags per resource – 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length – 128 Unicode characters in UTF-8
+ Maximum value length – 256 Unicode characters in UTF-8
+ The allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: `+ - = . _ : / @`.
+ Tag keys and values are case-sensitive.
+ The `aws:` prefix is reserved for AWS use. If a tag has a tag key with this prefix, then you can't edit or delete the tag's key or value. Tags with the `aws:` prefix do not count against your tags per resource limit.

You can't update or delete a resource based solely on its tags; you must specify the resource identifier. For example, to delete file systems that you tagged with a tag key called `DeleteMe`, you must use the `DeleteFileSystem` action with the resource identifiers of the file system, such as the file system ID.

When you tag public or shared resources, the tags that you assign are available only to your AWS account. No other AWS account will have access to those tags. For tag-based access control to shared resources, each AWS account must assign its own set of tags to control access to the resource.

## Using the S3 console
<a name="s3-files-tagging-console"></a>

You can use the S3 Files console to manage tags on your resources.
+ Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).
+ In the navigation bar, verify you are in your desired AWS Region.
+ In the left navigation pane, choose **File systems**.
+ You can specify tags for a resource when you create the resource, such as an S3 file system or an access point. Or, you can add, modify, or delete tags after creation by going to the properties of the resource.

## Using the AWS CLI
<a name="s3-files-tagging-cli"></a>

If you're using the S3 Files API, the AWS CLI, or an AWS SDK, you can use the `TagResource` S3 Files API action to apply tags to existing resources. Additionally, some resource-creating actions enable you to specify tags for a resource when the resource is created, such as when you create a file system.

The AWS CLI commands for managing tags, and the equivalent S3 Files API actions, are listed in the following table.


| CLI command | Description | Equivalent API operation | 
| --- | --- | --- | 
| tag-resource | Add new tags or update existing tags | TagResource | 
| list-tags-for-resource | Retrieve existing tags | ListTagsForResource | 
| untag-resource | Delete existing tags | UntagResource | 