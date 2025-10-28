# Removing tags from Security Hub CSPM resources

If you add tags to an AWS Security Hub CSPM resource, you can subsequently remove one or more of
them. A _tag_ is a label that you define and assign to
AWS resources, including certain types of Security Hub CSPM resources. You can add, edit, and
remove tags from the following types of Security Hub CSPM resources: automation rules, configuration policies, and
the `Hub` resource.

To remove tags from an individual AWS Security Hub CSPM resource, you can use the
Security Hub CSPM API. The Security Hub CSPM console currently doesn't support tag removal.

To remove tags from multiple Security Hub CSPM resources at the same time, use the tagging operations of the [AWS Resource Groups Tagging API](../../../resourcegroupstagging/latest/APIReference/overview.md "../../../resourcegroupstagging/latest/APIReference/overview.md").

###### Important

Removing tags from a resource can affect access to the resource. Before you remove
a tag, review any AWS Identity and Access Management (IAM) policies that might use the tag to control
access to resources.

Security Hub CSPM API
**To remove tags from a Security Hub CSPM resource (API)**

To remove one or more tags from a resource programmatically, use the [UntagResource](../../1.0/APIReference/API_UntagResource.md "../../1.0/APIReference/API_UntagResource.md") operation of the Security Hub CSPM API. In your request,
use the `resourceArn` parameter to specify the Amazon Resource
Name (ARN) of the resource to remove a tag from. Use the
`tagKeys` parameter to specify the tag key of the tag to
remove. To remove multiple tags, append the `tagKeys` parameter
and argument for each tag to remove, separated by an ampersand
(&)—for example,
`tagKeys=`key1`&tagKeys=`key2``.
To remove only a specific tag value (not a tag key) from a resource, [edit the tag](tags-update.md "tags-update.md") instead of removing the
tag.

If you're using the AWS CLI, run the [untag-resource](../../../cli/latest/reference/securityhub/untag-resource.md "../../../cli/latest/reference/securityhub/untag-resource.md") command to remove one or more tags from a
resource. For the `resource-arn` parameter, specify the ARN of
the resource to remove a tag from. Use the `tag-keys` parameter
to specify the tag key of the tag to remove. For example, the following
command removes the `Environment` tag (both the tag key and tag
value) from the specified configuration policy:

```
`$` `aws securityhub untag-resource \
--resource-arn `arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` \
--tag-keys `Environment``
```

Where `resource-arn` specifies the ARN of the configuration policy to
remove a tag from, and `Environment`
is the tag key of the tag to remove.

To remove multiple tags from a resource, add each additional tag key as an
argument for the `tag-keys` parameter. For example:

```
`$` `aws securityhub untag-resource \
--resource-arn `arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` \
--tag-keys `Environment` `Owner``
```

If the operation succeeds, Security Hub CSPM returns an empty HTTP 200 response. Otherwise,
Security Hub CSPM returns an HTTP 4*xx* or 500
response that indicates why the operation failed.
