# Manage tags for a protect configuration in AWS End User Messaging SMS

Tags are pairs of keys and values that you can optionally apply to your AWS resources to
control access or usage. Adding a tag to a resource can help you categorize and manage resources in different ways, such as by
purpose, owner, environment, or other criteria. You can use tags to easily find existing resources, or to
control which users can access specific resources.

To manage tags for a protect configuration, you can use the AWS End User Messaging SMS console, the
`TagResource` and `UnTagResource` actions in the AWS End User Messaging SMS and voice v2 API, or the `aws
 sms-voice tag-resource` and `aws
 sms-voice untag-resource` commands in the AWS CLI. This section shows how to
tag and untag a protect configuration using the AWS End User Messaging SMS console and the AWS CLI.

Manage tags (Console)
Use the AWS End User Messaging SMS console to add, edit or delete a Tag.

###### Manage tags (Console)

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Protect**,
   choose **Protect configurations**.
3. On the **Protect configurations** page, choose the protect configurations
   to add a tag to.
4. On the **Tags** tab, choose **Manage
   tags**.
   - **Add a tag** – In
     **Manage tags**, choose **Add new
     tag** to create a new blank key/value pair.
   - **Delete a tag** – In
     **Manage tags**, choose
     **Remove** next to the key/value
     pair.
   - **Edit a tag** – In
     **Manage tags**, choose the
     **Key** or **Value** and
     edit the text.

5. Choose **Save changes**.

Manage tags (AWS CLI)
Use the AWS CLI to add or edit a Tag.

```
`$` aws pinpoint-sms-voice-v2 tag-resource \
  --resource-arn `resource-arn` \
  --tags tags={`key1`=`value1`,`key2`=`value2`}
```

In the preceding example, do the following:

- Replace `resource-arn` with the Amazon Resource Name (ARN) that you
  want to add the tags to.
- Replace `key1` and
  `key2` with the keys of the tags that you
  want to add to the resource.
- Replace `value1` and
  `value2` with the values of the tags that
  you want to add for the respective keys.

Use the AWS CLI to delete a Tag.

```
`$` aws pinpoint-sms-voice-v2 untag-resource \
  --resource-arn `resource-arn` \
  --tag-keys tags={`key1`=`value1`,`key2`=`value2`}
```

In the preceding example, do the following:

- Replace `resource-arn` with the Amazon Resource Name (ARN) that you
  want to remove the tag from.
- Replace `key1` and
  `key2` with the keys of the tags that you
  want to remove.
- Replace `value1` and
  `value2` with the values of the tags that
  you want to remove.
