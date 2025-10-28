# Removing tags from Amazon Security Lake resources

To remove tags from an Amazon Security Lake resource, you can use the Security Lake console or the
Security Lake API.

###### Important

Removing tags from a resource can affect access to the resource. Before you remove
a tag, review any AWS Identity and Access Management (IAM) policies that might use the tag to control
access to resources.

Console
Follow these steps to remove one or more tags from a resource by using the
Security Lake console.

###### To remove a tag from a resource

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. Depending on the type of resource that you want to remove a tag from, do one of the
   following:
   - For a data lake configuration, choose
     **Regions** in the navigation pane.
     Then, in the **Regions** table, select the
     Region.
   - For a subscriber, choose **Subscribers**
     in the navigation pane. Then, in the **My
     subscribers** table, select the
     subscriber.

   If the subscriber doesn't appear in the table, use the
   AWS Region selector in the upper-right corner of the page
   to select the Region where you created the subscriber. The
   table lists existing subscribers only for the current
   Region.

3. Choose **Edit**.
4. Expand the **Tags** section. The **Tags** section
   lists all the tags that are currently assigned to the
   resource.
5. Do any of the following:
   - To remove only the tag value for a tag, choose
     **X** in the **Value**
     box that contains the value to remove.
   - To remove both the tag key and tag value (as a pair) for a
     tag, choose **Remove** next to the tag to
     remove.

6. To remove additional tags from the resource, repeat the preceding step for each
   additional tag to remove.
7. When you finish removing tags, choose **Save**.

API
To remove one or more tags from a resource programmatically, use the [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") operation of the Security Lake API. In your request,
use the `resourceArn` parameter to specify the Amazon Resource
Name (ARN) of the resource to remove a tag from. Use the
`tagKeys` parameter to specify the tag key of the tag to
remove. To remove multiple tags, append the `tagKeys` parameter
and argument for each tag to remove, separated by an ampersand
(&)—for example,
`tagKeys=`key1`&tagKeys=`key2``.
To remove only a specific tag value (not a tag key) from a resource, [edit the tag](tags-update.md "tags-update.md") instead of removing the
tag.

If you're using the AWS Command Line Interface (AWS CLI), run the [untag-resource](../../../cli/latest/reference/securitylake/untag-resource.md "../../../cli/latest/reference/securitylake/untag-resource.md") command to remove one or more tags from a
resource. For the `resource-arn` parameter, specify the ARN of
the resource to remove a tag from. Use the `tag-keys` parameter
to specify the tag key of the tag to remove. For example, the following
command removes the `Environment` tag (both the tag key and tag
value) from the specified subscriber:

```
`$` `aws securitylake untag-resource \
--resource-arn `arn:aws:securitylake:us-east-1:123456789012:subscriber/1234abcd-12ab-34cd-56ef-1234567890ab` \
--tag-keys `Environment``
```

Where `resource-arn` specifies the ARN of the subscriber to
remove a tag from, and `Environment`
is the tag key of the tag to remove.

To remove multiple tags from a resource, add each additional tag key as an
argument for the `tag-keys` parameter. For example:

```
`$` `aws securitylake untag-resource \
--resource-arn `arn:aws:securitylake:us-east-1:123456789012:subscriber/1234abcd-12ab-34cd-56ef-1234567890ab` \
--tag-keys `Environment` `Owner``
```

If the operation succeeds, Security Lake returns an empty HTTP 200 response. Otherwise,
Security Lake returns an HTTP 4*xx* or 500
response that indicates why the operation failed.
