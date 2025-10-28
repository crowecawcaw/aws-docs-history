# Delete a phone pool in AWS End User Messaging SMS

Before you can delete a pool you need to turn off **Deletion protection**
and remove all but one of originators from the phone pool. For more information on how to disable
deletion protection, see [Using phone pool deletion protection in AWS End User Messaging SMS](phone-pool-deletion-protection.md "phone-pool-deletion-protection.md"). The phone numbers and sender IDs that were
associated with the pool remain in your AWS End User Messaging SMS account.

Delete a phone pool (Console)
Before you can delete a pool you need to turn off Deletion protection and remove all
originators from the phone pool. To delete a pool using the AWS End User Messaging SMS console, follow these
steps:

###### To delete a pool (Console)

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**, choose
   **Phone pool**.
3. On the **Phone Pools** page, choose the pool to delete.
4. Choose **Delete**.
5. Enter `release` and then **Confirm** to delete the
   pool.

Delete a phone pool (AWS CLI)
Before you can delete a pool you need to turn off Deletion protection and remove all
originators from the phone pool. You can use the [delete-pool](../../../cli/latest/reference/pinpoint-sms-voice-v2/delete-pool.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/delete-pool.md") API to
delete pools.

###### To delete a pool using the AWS CLI

- To delete a pool, enter the following command at the command line:

```
`$` aws pinpoint-sms-voice-v2 delete-pool \
`>` --pool-id `pool-78ec067f62f94d57bd3bab991example`
```

In the preceding command, replace
`pool-78ec067f62f94d57bd3bab991example` with the unique ID or the
Amazon Resource Name (ARN) of the pool. You can find both of these values by using the [describe-pools](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-pools.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-pools.md") operation.
