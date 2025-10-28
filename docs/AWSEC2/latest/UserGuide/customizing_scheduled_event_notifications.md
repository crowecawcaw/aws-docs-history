# Customize scheduled

event notifications for your EC2 instances

You can customize scheduled event notifications to include tags in the email
notification. This makes it easier to identify the affected resource (instances or
Dedicated Hosts) and to prioritize actions for the upcoming event.

When you customize event notifications to include tags, you can choose to
include:

- All of the tags that are associated with the affected resource
- Only specific tags that are associated with the affected resource
  For example, suppose that you assign `application`,
  `costcenter`, `project`, and `owner` tags to
  all of your instances. You can choose to include all of the tags in event
  notifications. Alternatively, if you'd like to see only the `owner` and
  `project` tags in event notifications, then you can choose to include
  only those tags.

After you select the tags to include, the event notifications will include the
resource ID (instance ID or Dedicated Host ID) and the tag key and value pairs that are
associated with the affected resource.

###### Tasks

- [Include tags in event notifications](#register-tags "#register-tags")
- [Remove tags from event notifications](#deregister-tags "#deregister-tags")
- [View the tags to be included in event
  notifications](#view-tags "#view-tags")

## Include tags in event notifications

The tags that you choose to include apply to all resources (instances and
Dedicated Hosts) in the selected Region. To customize event notifications in other
Regions, first select the required Region and then perform the following
steps.

Console

###### To include tags in event notifications

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Events**.
3. Choose **Actions**, **Manage
   event notifications**.
4. Turn on **Include tags in event
   notifications**.
5. Do one of the following, depending on the tags that you
   want to include in event notifications:
   - To include all tags associated with the affected
     instance or Dedicated Host, select **Include all
     tags**.
   - To select the tags to include, select
     **Choose the tags to include**
     and then select or enter the tag keys.

6. Choose **Save**.

AWS CLI

###### To include all tags in event notifications

Use the [register-instance-event-notification-attributes](../../../cli/latest/reference/ec2/register-instance-event-notification-attributes.md "../../../cli/latest/reference/ec2/register-instance-event-notification-attributes.md")
command and set the `IncludeAllTagsOfInstance`
parameter to `true`.

```
aws ec2 register-instance-event-notification-attributes \
    --instance-tag-attribute "IncludeAllTagsOfInstance=true"
```

###### To include specific tags in event notifications

Use the [register-instance-event-notification-attributes](../../../cli/latest/reference/ec2/register-instance-event-notification-attributes.md "../../../cli/latest/reference/ec2/register-instance-event-notification-attributes.md")
command and specify the tags to include by using the
`InstanceTagKeys` parameter.

```
aws ec2 register-instance-event-notification-attributes \
    --instance-tag-attribute 'InstanceTagKeys=["`tag_key_1`", "`tag_key_2`", "`tag_key_3`"]'
```

PowerShell

###### To include all tags in event notifications

Use the [Register-EC2InstanceEventNotificationAttribute](../../../powershell/latest/reference/items/Register-EC2InstanceEventNotificationAttribute.md "../../../powershell/latest/reference/items/Register-EC2InstanceEventNotificationAttribute.md")
cmdlet.

```
Register-EC2InstanceEventNotificationAttribute `
    -InstanceTagAttribute_IncludeAllTagsOfInstance $true
```

###### To include specific tags in event notifications

Use the [Register-EC2InstanceEventNotificationAttribute](../../../powershell/latest/reference/items/Register-EC2InstanceEventNotificationAttribute.md "../../../powershell/latest/reference/items/Register-EC2InstanceEventNotificationAttribute.md")
cmdlet.

```
Register-EC2InstanceEventNotificationAttribute `
    -InstanceTagAttribute_InstanceTagKey `tag_key_1`, `tag_key_2`, `tag_key_3`
```

## Remove tags from event notifications

You can remove tags from event notifications.

Console

###### To remove tags from event notifications

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Events**.
3. Choose **Actions**, **Manage
   event notifications**.
4. To remove all tags from event notifications, turn off
   **Include tags in event
   notifications**.
5. To remove specific tags from event notifications, choose
   the **X**) for the corresponding tag
   keys.
6. Choose **Save**.

AWS CLI

###### To remove all tags from event notifications

Use the [deregister-instance-event-notification-attributes](../../../cli/latest/reference/ec2/deregister-instance-event-notification-attributes.md "../../../cli/latest/reference/ec2/deregister-instance-event-notification-attributes.md")
command and set the `IncludeAllTagsOfInstance`
parameter to `false`.

```
aws ec2 deregister-instance-event-notification-attributes \
    --instance-tag-attribute "IncludeAllTagsOfInstance=false"
```

###### To remove a tag from event notifications

Use the [deregister-instance-event-notification-attributes](../../../cli/latest/reference/ec2/deregister-instance-event-notification-attributes.md "../../../cli/latest/reference/ec2/deregister-instance-event-notification-attributes.md")
command and specify the tags to remove by using the
`InstanceTagKeys` parameter.

```
aws ec2 deregister-instance-event-notification-attributes \
    --instance-tag-attribute 'InstanceTagKeys=["`tag_key_3`"]'
```

PowerShell

###### To remove all tags from event notifications

Use the [Unregister-EC2InstanceEventNotificationAttribute](../../../powershell/latest/reference/items/Unregister-EC2InstanceEventNotificationAttribute.md "../../../powershell/latest/reference/items/Unregister-EC2InstanceEventNotificationAttribute.md") cmdlet.

```
Unregister-EC2InstanceEventNotificationAttribute `
    -InstanceTagAttribute_IncludeAllTagsOfInstance $false
```

###### To remove a tag from event notifications

Use the [Unregister-EC2InstanceEventNotificationAttribute](../../../powershell/latest/reference/items/Unregister-EC2InstanceEventNotificationAttribute.md "../../../powershell/latest/reference/items/Unregister-EC2InstanceEventNotificationAttribute.md") cmdlet.

```
Unregister-EC2InstanceEventNotificationAttribute `
    -InstanceTagAttribute_InstanceTagKey `tag_key_3`
```

## View the tags to be included in event

notifications

You can view the tags that are to be included in event notifications.

Console

###### To view the tags that are to be included in event

notifications

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Events**.
3. Choose **Actions**, **Manage
   event notifications**.

AWS CLI

###### To view the tags to be included in event notifications

Use the [describe-instance-event-notification-attributes](../../../cli/latest/reference/ec2/describe-instance-event-notification-attributes.md "../../../cli/latest/reference/ec2/describe-instance-event-notification-attributes.md")
command.

```
aws ec2 describe-instance-event-notification-attributes
```

PowerShell

###### To view the tags to be included in event notifications

Use the [Get-EC2InstanceEventNotificationAttribute](../../../powershell/latest/reference/items/Get-EC2InstanceEventNotificationAttribute.md "../../../powershell/latest/reference/items/Get-EC2InstanceEventNotificationAttribute.md")
cmdlet.

```
Get-EC2InstanceEventNotificationAttribute
```
