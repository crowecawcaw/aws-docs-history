# Manage tags for a configuration set in AWS End User Messaging SMS

Tags are pairs of keys and values that you can optionally apply to your AWS resources to
control access or usage. Adding a tag to a resource can help you categorize and manage resources in different ways, such as by
purpose, owner, environment, or other criteria. You can use tags to easily find existing resources, or to
control which users can access specific resources.

Manage tags (Console)
Use the AWS End User Messaging SMS console to add, edit or delete a Tag.

###### Add a Tag (Console)

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**,
   choose **Configuration sets**.
3. On the **Configuration sets** page, choose the configuration set
   to add a tag to.
4. On the **Tags** tab, choose **Manage
   tags**.
5. - **Add a tag** – In
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
6. Choose **Save changes**.

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
