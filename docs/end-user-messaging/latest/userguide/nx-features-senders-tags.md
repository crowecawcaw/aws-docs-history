

# Manage tags for a sender ID
<a name="nx-features-senders-tags"></a>

Tags are pairs of keys and values that you can optionally apply to your AWS resources to control access or usage. Adding a tag to a resource can help you categorize and manage resources by purpose, owner, environment, or other criteria.

------
#### [ Manage tags (Console) ]

Use the AWS End User Messaging console to add, edit, or delete a tag.

**Manage tags (Console)**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Sender IDs**.

1. On the **Sender IDs** page, choose the sender ID to add a tag to.

1. On the **Tags** tab, choose **Manage tags**.
   + **Add a tag** – choose **Add new tag** to create a new blank key/value pair.
   + **Delete a tag** – choose **Remove** next to the key/value pair.
   + **Edit a tag** – choose the **Key** or **Value** and edit the text.

1. Choose **Save changes**.

------
#### [ Manage tags (AWS CLI) ]

Use the AWS CLI to add or edit a tag.

```
$ aws pinpoint-sms-voice-v2 tag-resource \
  --resource-arn {{resource-arn}} \
  --tags tags={{{key1}}={{value1}}}
```

Use the AWS CLI to delete a tag.

```
$ aws pinpoint-sms-voice-v2 untag-resource \
  --resource-arn {{resource-arn}} \
  --tag-keys {{key1}}
```

In the preceding commands, replace {{resource-arn}} with the Amazon Resource Name (ARN) of the sender ID, and {{key1}}/{{value1}} with your tag keys and values.

------