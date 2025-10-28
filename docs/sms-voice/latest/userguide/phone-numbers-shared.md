# List shared phone numbers with the AWS CLI

You can use the [describe-phone-numbers](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-phone-numbers.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-phone-numbers.md") or the [AWS RAM
console](https://console.aws.amazon.com/ram "https://console.aws.amazon.com/ram") to view origination phone numbers shared with your
account. For more information about shared resources, see [Working with shared resources in AWS End User Messaging SMS](shared-resources.md "shared-resources.md").

###### To list all of the phone numbers shared with your account using the AWS CLI

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 describe-phone-numbers --owner `SHARED`
```

In the preceding command, replace `SHARED` with
`SELF` to list the phone numbers owned by your account.
