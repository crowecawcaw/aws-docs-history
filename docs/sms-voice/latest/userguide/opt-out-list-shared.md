# List shared opt-out lists with the AWS CLI

You can use the [describe-opt-out-lists](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-opt-out-lists.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-opt-out-lists.md") to view opt-out lists shared with your
account. For more information about shared resources, see [Working with shared resources in AWS End User Messaging SMS](shared-resources.md "shared-resources.md").

###### To list all opt-out lists shared with your account using the

AWS CLI

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 describe-opt-out-lists --owner `SHARED`
```

In the preceding command, replace `SHARED` with
`SELF` to list the opt-out lists owned by your
account.
