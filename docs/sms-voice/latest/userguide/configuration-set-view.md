# View all configuration sets in AWS End User Messaging SMS

Use the AWS CLI to view your configuration sets.

List configuration sets (AWS CLI)You can use the [describe-configuration-sets](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-configuration-sets.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-configuration-sets.md") command to view information about the configuration
sets in your AWS End User Messaging SMS account.

###### To view a list of the configuration sets in your account using the AWS CLI

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 describe-configuration-sets
```

Describe a configuration set (AWS CLI)You can use the [describe-configuration-sets](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-configuration-sets.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-configuration-sets.md") command to view information about a configuration
set in your AWS End User Messaging SMS account.

###### To view information about specific configuration sets using the AWS CLI

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 describe-configuration-sets \
`>` --configuration-set-names `configurationSet`
```

In the preceding command, replace `configurationSet` with the
name of the configuration set that you want to find the details of. You can also specify
multiple configuration sets by separating the name of each configuration set with a
space.
