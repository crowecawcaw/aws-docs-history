

# Change a protection configuration association in AWS End User Messaging SMS
<a name="protect-configuration-edit-association"></a>

To use the country rules contained in a protect configuration, you need to associate the protect configuration as the *account default* to a configuration set, or use it directly with a message send. If you only have one message sending use case, using an *account default* is the simplest option. If you have several use cases, you can use configuration sets to control which countries AWS End User Messaging SMS sends to, and for the most control, you can associate a protect configuration directly in a message send. To change a protect configuration's association, you can use the AWS End User Messaging SMS console, the `AssociateProtectConfiguration` or `SetAccountDefaultProtectConfiguration` action in the AWS End User Messaging SMS and voice v2 API, or the `aws sms-voice associate-protect-configuration` or `aws sms-voice set-account-default-protect-configuration` commands in the AWS CLI. This section shows how to change a protect configuration’s association using the AWS End User Messaging SMS console and the AWS CLI.

The selection process for the *effective* protection configuration for a sending request is as follows:

1. *ProtectConfigurationId* – If a protection configuration is specified in the API request parameters, it will be used.

1. *ConfigurationSetName* – If no protection configuration is specified in the API request parameters, but a configuration set is specified and it has an associated protection configuration, then the protection configuration associated with this configuration set will be used.

1. *Account default* – If a protection configuration is not specified or available from 1 or 2, the *account default* protection configuration will be used.

1. *None* – The protect configuration will only be used if specified in a `SendTextMessage` API request.

A protect configuration can be associated to multiple configuration sets, while a configuration set can only be associated with one protect configuration. There can only be one *account default* protect configuration.

------
#### [ Edit a protect configuration association (Console) ]

To edit a protect configuration using the AWS End User Messaging SMS console, follow these steps:

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Protect**, choose **Protect configuration**.

1. On the **Protect configurations** page, choose a protect configuration.

1. Choose the **Associations** tab.

1. Choose **Edit settings**.

1. On the **Edit setting** page, choose one of the following options:
   + **Account default** – Use the protect configuration as your *account default* protect configuration. This replaces the current *account default* protect configuration.
   + **Configuration set** – Associate the protect configuration with one or more configuration sets. 
     + In **Configuration sets available for association** check one or more configuration sets that do not already have a protect configuration association. 
   + **No association** – The protect configuration is not associated with the *account default* or a configuration set.

1. Choose **Save changes**.

------
#### [ Edit a protect configuration association (AWS CLI) ]

You can use the associate-protect-configuration command to associate the protect configuration with a configuration set. To change the *account default* protect configuration use the set-account-defult-protect-configuration command.

To change a configuration sets association to a protect configuration at the command line, enter the following command:

```
$ aws pinpoint-sms-voice-v2 associate-protect-configuration --configuration-set-name {{ConfigurationSetName}} --protect-configuration-id {{ProtectConfigurationID}}
```

In the preceding command, make the following changes:
+ Replace {{ConfigurationSetName}} with the name of the configuration set.
+ Replace {{ProtectConfigurationID}} with the unique identifier of the protect configuration.

To change the account default protect configuration at the command line, enter the following command:

```
$ aws pinpoint-sms-voice-v2 set-account-default-protect-configuration --protect-configuration-id {{ProtectConfigurationID}}
```

In the preceding command, make the following changes:
+ Replace {{ProtectConfigurationID}} with the unique identifier of the protect configuration.

------
#### [ Disassociate a protect configuration (AWS CLI) ]

You can use the disassociate-protect-configuration command to disassociate the protect configuration with a configuration set. To remove the *account default* protect configuration use the delete-account-defult-protect-configuration command.

To remove a configuration sets association to a protect configuration at the command line, enter the following command:

```
$ aws pinpoint-sms-voice-v2 disassociate-protect-configuration --configuration-set-name {{ConfigurationSetName}} --protect-configuration-id {{ProtectConfigurationID}}
```

In the preceding command, make the following changes:
+ Replace {{ConfigurationSetName}} with the name of the configuration set.
+ Replace {{ProtectConfigurationID}} with the unique identifier of the protect configuration.

To remove the *account default* protect configuration at the command line, enter the following command:

```
$ aws pinpoint-sms-voice-v2 delete-account-default-protect-configuration
```

------