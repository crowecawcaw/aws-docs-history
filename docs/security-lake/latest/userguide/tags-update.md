# Editing tags for Amazon Security Lake resources

To edit the tags (tag keys or tag values) for an Amazon Security Lake resource, you can use the
Security Lake console or the Security Lake API.

###### Important

Editing the tags for a resource can affect access to the resource. Before you edit
a tag key or value for a resource, review any AWS Identity and Access Management (IAM) policies that might
use the tag to control access to resources.

Console
Follow these steps to edit a resource's tags by using the Security Lake
console.

###### To edit the tags for a resource

1.  Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2.  Depending on the type of resource whose tags you want to edit, do one of the
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

3.  Choose **Edit**.
4.  Expand the **Tags** section. The **Tags** section
    lists all the tags that are currently assigned to the
    resource.
5.  Do any of the following:

        * To add a tag value to an existing tag key, enter the value in the
         **Value** box next to the tag
         key.
        * To change an existing tag key, choose **Remove** next to the tag.
         Then choose **Add new tag**. In the
         **Key** box that appears, enter the new
         tag key. Optionally enter an associated tag value in the
         **Value** box.
        * To change an existing tag value, choose
         **X** in the **Value**
         box that contains the value. Then enter the new tag value in
         the **Value** box.
        * To remove an existing tag value, choose
         **X** in the **Value**
         box that contains the value.
        * To remove an existing tag (both the tag key and tag
         value), choose **Remove** next to the
         tag.

    A resource can have as many as 50 tags. A tag key can contain as
    many as 128 characters. A tag value can contain as many as 256
    characters. The characters can be letters, numbers, spaces, or the
    following symbols: \_ . : / = + - @

6.  When you finish editing the tags, choose **Save**.

API
When you edit a tag for a resource programmatically, you overwrite the
existing tag with new values. Therefore, the best way to edit a tag depends
on whether you want to edit a tag key, a tag value, or both. To edit a tag
key, [remove the current tag](tags-remove.md "tags-remove.md") and [add a new tag](tags-add.md "tags-add.md").

To edit or remove only the tag value that's associated with a tag key, overwrite the
existing value by using the [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") operation of the Security Lake API. If you're using the
AWS Command Line Interface (AWS CLI), run the [tag-resource](../../../cli/latest/reference/securitylake/tag-resource.md "../../../cli/latest/reference/securitylake/tag-resource.md") command. In your request, specify the Amazon
Resource Name (ARN) of the resource whose tag value you want to edit or
remove.

To edit a tag value, use the `tags` parameter to specify the tag key whose tag
value you want to change. Also specify the new tag value for the key. For
example, the following AWS CLI command changes the tag value from
`Cloud` to `On-Premises` for the
`Environment` tag key that's assigned to the specified
subscriber. This example is formatted for Linux, macOS, or Unix, and it uses
the backslash (\) line-continuation character to improve readability.

```
`$` `aws securitylake tag-resource \
--resource-arn `arn:aws:securitylake:us-east-1:123456789012:subscriber/1234abcd-12ab-34cd-56ef-1234567890ab` \
--tags key=`Environment`,value=`On-Premises``
```

Where:

- `resource-arn` specifies the ARN of the subscriber.
- `Environment` is the tag key
  that's associated with the tag value to change.
- `On-Premises` is the new tag
  value for the specified tag key
  (`Environment`).

To remove a tag value from a tag key, don’t specify a value for the `value`
argument of the key in the `tags` parameter. For example:

```
`$` `aws securitylake tag-resource \
--resource-arn `arn:aws:securitylake:us-east-1:123456789012:subscriber/1234abcd-12ab-34cd-56ef-1234567890ab` \
--tags key=`Owner`,value=`
```

If the operation succeeds, Security Lake returns an empty HTTP 200 response. Otherwise,
Security Lake returns an HTTP 4*xx* or 500
response that indicates why the operation failed.

## Reviewing tags for Amazon Security Lake resources

You can review the tags (both tag keys and tag values) for an Amazon Security Lake resource by
using the Security Lake console or the Security Lake API.

Console
Follow these steps to review a resource's tags by using the Security Lake
console.

###### To review the tags for a resource

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. Depending on the type of resource whose tags you want to review,
   do one of the following:
   - For a data lake configuration, choose **Regions** in the navigation
     pane. In the **Regions** table, select the
     Region, and then choose **Edit**. Then
     expand the **Tags** section.
   - For a subscriber, choose **Subscribers** in the navigation pane.
     Then, in the **My subscribers** table,
     choose the subscriber's name.

   If the subscriber doesn't appear in the table, use the
   AWS Region selector in the upper-right corner of the page
   to select the Region where you created the subscriber. The
   table lists existing subscribers only for the current
   Region.

The **Tags** section lists all the tags that are currently assigned to
the resource.

API
To retrieve and review the tags for an existing resource programmatically, use the [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") operation of the Security Lake API. In your
request, use the `resourceArn` parameter to specify the Amazon
Resource Name (ARN) of the resource.

If you're using the AWS Command Line Interface (AWS CLI), run the [list-tags-for-resource](../../../cli/latest/reference/securitylake/list-tags-for-resource.md "../../../cli/latest/reference/securitylake/list-tags-for-resource.md") command and use the
`resource-arn` parameter to specify the ARN of the resource.
For example:

```
`$` `aws securitylake list-tags-for-resource --resource-arn `arn:aws:securitylake:us-east-1:123456789012:subscriber/1234abcd-12ab-34cd-56ef-1234567890ab``
```

In the preceding example, `arn:aws:securitylake:us-east-1:123456789012:subscriber/1234abcd-12ab-34cd-56ef-1234567890ab` is the ARN of an
existing subscriber.

If the operation succeeds, Security Lake returns a `tags` array. Each object in
the array specifies a tag (both the tag key and tag value) that's currently
assigned to the resource. For example:

```
`{
 "tags": [
 {
 "key": "Environment",
 "value": "Cloud"
 },
 {
 "key": "CostCenter",
 "value": "12345"
 },
 {
 "key": "Owner",
 "value": ""
 }
 ]
}`
```

Where `Environment`, `CostCenter`, and
`Owner` are the tag keys that are assigned to the resource.
`Cloud` is the tag value that's associated with the
`Environment` tag key. `12345` is the tag value
that's associated with the `CostCenter` tag key. The
`Owner` tag key doesn't have an associated tag value.
