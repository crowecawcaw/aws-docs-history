# Adding tags to Amazon Security Lake resources

To add tags to an Amazon Security Lake resource, you can use the Security Lake console or the Security Lake
API.

###### Important

Adding tags to a resource can affect access to the resource. Before you add a tag
to a resource, review any AWS Identity and Access Management (IAM) policies that might use tags to control
access to resources.

Console
When you enable Security Lake for an AWS Region or create a subscriber, the Security Lake
console provides options for adding tags to the resource—the data
lake configuration for the Region or the subscriber. Follow the instructions
on the console to add tags to the resource when you create the resource.

To add one or more tags to an existing resource by using the Security Lake console, follow
these steps.

###### To add a tag to a resource

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. Depending on the type of resource that you want to add a tag to, do one of the
   following:
   - For a data lake configuration, choose **Regions** in the navigation
     pane. Then, in the **Regions** table,
     select the Region.
   - For a subscriber, choose **Subscribers** in the navigation pane.
     Then, in the **My subscribers** table,
     select the subscriber.

   If the subscriber doesn't appear in the table, use the
   AWS Region selector in the upper-right corner of the page
   to select the Region where you created the subscriber. The
   table lists existing subscribers only for the current
   Region.

3. Choose **Edit**.
4. Expand the **Tags** section. This section lists all the tags that are
   currently assigned to the resource.
5. In the **Tags** section, choose **Add new
   tag**.
6. In the **Key** box, enter the tag key for the tag
   to add to the resource. Then, in the **Value** box,
   optionally enter a tag value for the key.

A tag key can contain as many as 128 characters. A tag value can
contain as many as 256 characters. The characters can be letters,
numbers, spaces, or the following symbols: \_ . : / = + - @ 7. To add another tag to the resource, choose **Add new tag**, and then
repeat the preceding step. You can assign as many as 50 tags to a
resource. 8. When you finish adding tags, choose **Save**.

API
To create a resource and add one or more tags to it programmatically, use
the appropriate `Create` operation for the type of resource that
you want to create:

- Data lake configuration – Use the [CreateDataLake](../APIReference/API_CreateDataLake.md "../APIReference/API_CreateDataLake.md") operation or, if you're using the
  AWS Command Line Interface (AWS CLI), run the [create-data-lake](../../../cli/latest/reference/securitylake/create-data-lake.md "../../../cli/latest/reference/securitylake/create-data-lake.md") command.
- Subscriber – Use the [CreateSubscriber](../APIReference/API_CreateSubscriber.md "../APIReference/API_CreateSubscriber.md") operation or, if you're using the
  AWS CLI, run the [create-subscriber](../../../cli/latest/reference/securitylake/create-subscriber.md "../../../cli/latest/reference/securitylake/create-subscriber.md") command.

In your request, use the `tags` parameter to specify the tag key
(`key`) and optional tag value (`value`) for each
tag to add to the resource. The `tags` parameter specifies an
array of objects. Each object specifies a tag key and its associated tag
value.

To add one or more tags to an existing resource, use the [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") operation of the Security Lake API or, if you're using
the AWS CLI, run the [tag-resource](../../../cli/latest/reference/securitylake/tag-resource.md "../../../cli/latest/reference/securitylake/tag-resource.md") command. In your request, specify the Amazon
Resource Name (ARN) of the resource that you want to add a tag to. Use the
`tags` parameter to specify the tag key (`key`)
and optional tag value (`value`) for each tag to add. As is the
case for `Create` operations and commands, the `tags`
parameter specifies an array of objects, one object for each tag key and its
associated tag value.

For example, the following AWS CLI command adds an `Environment` tag key with a
`Cloud` tag value to the specified subscriber. This example
is formatted for Linux, macOS, or Unix, and it uses the backslash (\)
line-continuation character to improve readability.

```
`$` `aws securitylake tag-resource \
--resource-arn `arn:aws:securitylake:us-east-1:123456789012:subscriber/1234abcd-12ab-34cd-56ef-1234567890ab` \
--tags key=`Environment`,value=`Cloud``
```

Where:

- `resource-arn` specifies the ARN of the subscriber to
  add a tag to.
- `Environment` is the tag key
  of the tag to add to the subscriber.
- `Cloud` is the tag value for
  the specified tag key
  (`Environment`).

In the following example, the command adds several tags to the subscriber.

```
`$` `aws securitylake tag-resource \
--resource-arn `arn:aws:securitylake:us-east-1:123456789012:subscriber/1234abcd-12ab-34cd-56ef-1234567890ab` \
--tags key=`Environment`,value=`Cloud` key=`CostCenter`,value=`12345` key=`Owner`,value=`jane-doe``
```

For each object in a `tags` array, both the `key` and
`value` arguments are required. However, the value for the
`value` argument can be an empty string. If you don’t want to
associate a tag value with a tag key, don't specify a value for the
`value` argument. For example, the following command adds an
`Owner` tag key with no associated tag value:

```
`$` `aws securitylake tag-resource \
--resource-arn `arn:aws:securitylake:us-east-1:123456789012:subscriber/1234abcd-12ab-34cd-56ef-1234567890ab` \
--tags key=`Owner`,value=`
```

If a tagging operation succeeds, Security Lake returns an empty HTTP 200 response. Otherwise,
Security Lake returns an HTTP 4*xx* or 500
response that indicates why the operation failed.
