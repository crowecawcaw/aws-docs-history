

# Using Amazon EventBridge with AWS Billing Conductor
<a name="using-eventbridge"></a>

AWS Billing Conductor is integrated with Amazon EventBridge, an event bus service that you can use to connect your applications with data from a variety of sources. For more information, see the [*Amazon EventBridge User Guide*](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

You can use Amazon EventBridge to receive AWS Billing Conductor events. Then, based on rules that you create, Amazon EventBridge invokes one or more target actions when an event matches the values that you specify in a rule. Depending on the type of event, you can capture event information, send notifications, or perform other actions. To set up an Amazon EventBridge rule for AWS Billing Conductor events, see [Create a rule in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html#eb-gs-create-rule) in the *Amazon EventBridge User Guide*.

## Example: Amazon EventBridge event for AWS Billing Conductor
<a name="using-eventbridge-example-event"></a>

AWS Billing Conductor emits a daily summary event with the `Billing Group Configuration Recommended for Billing Transfer` detail type when a billing transfer is accepted but no corresponding billing group is configured, or when a billing group associated with an active billing transfer is deleted. When a billing transfer is accepted, we recommend configuring a billing group for the bill source account's organization, which enables accounts in that organization to access pro forma cost data in Billing and Cost Management tools. Without a billing group, usage data remains available through CloudWatch, but configuring a billing group makes it easier for bill source account administrators to monitor costs, such as through budgets configuration.

**Note**  
This event type is currently only supported in the US East (N. Virginia) Region (`us-east-1`).

The following is a generalized example of this event. You can subscribe to Amazon EventBridge events (such as this one) using AWS User Notifications.

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