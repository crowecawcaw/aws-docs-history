

# Delete a configuration set in AWS End User Messaging
<a name="nx-features-configuration-sets-delete"></a>

Use the AWS End User Messaging console or AWS CLI to delete a configuration set.

------
#### [ Deleting a configuration set (Console) ]

To delete a configuration set using the AWS End User Messaging console, follow these steps:

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Configuration sets**.

1. Select the **Configuration set** you want to delete and then choose **Delete**.

------
#### [ Deleting a configuration set (AWS CLI) ]

You can use the [delete-configuration-set](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/delete-configuration-set.html) command to delete a configuration set.

```
$ aws pinpoint-sms-voice-v2 delete-configuration-set \
> --configuration-set-name {{configurationSet}}
```

In the preceding command, replace {{configurationSet}} with the name of the configuration set that you want to delete.

------