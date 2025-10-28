# List shared phone pools with the AWS CLI

You can use the [describe-pools](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-pools.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-pools.md") CLI or the [AWS RAM
console](https://console.aws.amazon.com/ram "https://console.aws.amazon.com/ram") to view information about pools shared with your
account. For more information about shared resources, see [Working with shared resources in AWS End User Messaging SMS](shared-resources.md "shared-resources.md").

###### To retrieve a list of pools shared with you using the AWS CLI

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 describe-pools --owner `SHARED`
```

In the preceding command, replace `SHARED` with
`SELF` to list the pools owned by your account.
