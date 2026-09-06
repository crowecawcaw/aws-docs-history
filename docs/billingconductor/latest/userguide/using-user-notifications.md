

# Using AWS User Notifications with AWS Billing Conductor
<a name="using-user-notifications"></a>

You can use [AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html) to set up delivery channels that notify you about AWS Billing Conductor events. You will receive a notification when an event matches a specified rule. You can receive notifications for events through multiple channels, including email, [Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) such as Amazon Chime, Microsoft Teams, and Slack, or [AWS Console Mobile Application](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/what-is-consolemobileapp.html) push notifications. You can also see notifications using the [Console Notifications Center](https://console.aws.amazon.com/notifications/) in the AWS User Notifications console.

AWS User Notifications also supports aggregation, which can reduce the number of notifications you receive during specific events. For more information, see the [AWS User Notifications User Guide](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html).

To use AWS User Notifications, you must have the correct AWS Identity and Access Management (IAM) permissions. For more information about configuring your IAM permissions, see [Creating a notification configuration](https://docs.aws.amazon.com/notifications/latest/userguide/getting-started.html#getting-started-step1) in the *AWS User Notifications User Guide*.

The following table lists the AWS Billing Conductor event types supported by AWS User Notifications.


**AWS Billing Conductor event types**  

| Event type | Description | 
| --- | --- | 
| Billing Group Configuration Recommended for Billing Transfer | A daily summary of billing transfer events where accepted transfers don't have a corresponding billing group configured, or where billing groups associated with active billing transfers were deleted. When a billing transfer is accepted, we recommend configuring a billing group for the bill source account's organization, which enables accounts in that organization to access pro forma cost data in Billing and Cost Management tools. Without a billing group, usage data remains available through CloudWatch, but configuring a billing group makes it easier for bill source account administrators to monitor costs, such as through budgets configuration. This event type is currently only supported in the US East (N. Virginia) Region (us-east-1). | 

## Example event
<a name="using-user-notifications-example-event"></a>

The following is an example of a `Billing Group Configuration Recommended for Billing Transfer` event from AWS Billing Conductor. This event is emitted to Amazon EventBridge with the source `aws.billingconductor`.

```
{
  "account": "<account ID>", // 12-digit account ID
  "region": "us-east-1", // Currently only us-east-1 is supported
  "detail-type": "Billing Group Configuration Recommended for Billing Transfer",
  "source": "aws.billingconductor",
  "version": "0",
  "time": "<date>", // Format: yyyy-MM-dd'T'HH:mm:ssZ
  "id": "<id>", // alphanumeric string
  "resources": [],
  "detail": {
    "targetDate": "<date>", // Format: yyyy-MM-dd
    "recipientId": "<account ID>", // 12-digit recipient account ID
    "eventBridgeEventId": "<event ID>", // unique event identifier
    "directTransfersAccepted": [
      {
        "transferArn": "<transfer ARN>", // ARN of the one-level billing transfer
        "billSourceAccountId": "<account ID>", // 12-digit bill source account ID
        "effectiveTimestamp": "<timestamp>", // Format: yyyy-MM-dd'T'HH:mm:ssZ
        "acceptedTimestamp": "<timestamp>" // Format: yyyy-MM-dd'T'HH:mm:ssZ
      }
    ],
    "indirectTransfersAccepted": [
      {
        "receiverTransferTransferArn": "<transfer ARN>", // ARN of the receiver's transfer
        "transferBillSourceTransferArn": "<transfer ARN>", // ARN of the bill source's transfer
        "billTransferAccountId": "<account ID>", // 12-digit bill transfer account ID
        "billSourceAccountId": "<account ID>", // 12-digit bill source account ID
        "effectiveTimestamp": "<timestamp>", // Format: yyyy-MM-dd'T'HH:mm:ssZ
        "acceptedTimestamp": "<timestamp>" // Format: yyyy-MM-dd'T'HH:mm:ssZ
      }
    ],
    "directBillingGroupsDeleted": [
      {
        "billingGroupArn": "<billing group ARN>", // ARN of the deleted billing group
        "billSourceAccountId": "<account ID>", // 12-digit bill source account ID
        "transferId": "<transfer ID>", // associated transfer ID
        "deletedTimestamp": "<timestamp>" // Format: yyyy-MM-dd'T'HH:mm:ssZ
      }
    ],
    "indirectBillingGroupsDeleted": [
      {
        "billingGroupArn": "<billing group ARN>", // ARN of the deleted billing group
        "billTransferAccountId": "<account ID>", // 12-digit bill transfer account ID
        "billSourceAccountId": "<account ID>", // 12-digit bill source account ID
        "receiverTransferTransferId": "<transfer ID>", // receiver's transfer ID
        "transferBillSourceTransferId": "<transfer ID>", // bill source's transfer ID
        "deletedTimestamp": "<timestamp>" // Format: yyyy-MM-dd'T'HH:mm:ssZ
      }
    ]
  }
}
```