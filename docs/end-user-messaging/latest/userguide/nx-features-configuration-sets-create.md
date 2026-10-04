

# Create a configuration set in AWS End User Messaging
<a name="nx-features-configuration-sets-create"></a>

Use the AWS End User Messaging console or AWS CLI to create a configuration set. After you have created a configuration set you should add an [Event destinations in AWS End User Messaging](nx-features-configuration-sets-event-destinations.md) and protect configuration.

------
#### [ Creating a configuration set (Console) ]

To create a configuration set using the AWS End User Messaging console, follow these steps:

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Configuration sets** and then **Create configuration set**.

1. For **Configuration set name** enter a descriptive name for the configuration set.

1. Choose **Create configuration set**.

------
#### [ Creating a configuration set (AWS CLI) ]

You can use the [create-configuration-set](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/create-configuration-set.html) command to create a new configuration set.

```
$ aws pinpoint-sms-voice-v2 create-configuration-set \
> --configuration-set-name {{configurationSet}}
```

In the preceding command, replace {{configurationSet}} with the name of the configuration set that you want to create.

------