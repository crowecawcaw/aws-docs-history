# Determine whether Amazon EC2 terminated a Spot Instance

A Spot Instance runs until Amazon EC2 terminates it in response to a Spot Instance interruption, or until
you terminate it yourself. For more information, see [Behavior of Spot Instance interruptions](interruption-behavior.md "interruption-behavior.md").

After a Spot Instance is terminated, you can use AWS CloudTrail to see whether Amazon EC2 terminated it.
If the CloudTrail log includes a `BidEvictedEvent`, this indicates that Amazon EC2
terminated the Spot Instance. If instead you see a `TerminateInstances` event,
this indicates that a user terminated the Spot Instance.

Alternatively, if you want to receive notification that Amazon EC2 is going to interrupt
your Spot Instance, use Amazon EventBridge to respond to the [EC2 Spot Instance Interruption Warning event](spot-instance-termination-notices.md#ec2-spot-instance-interruption-warning-event "spot-instance-termination-notices.md#ec2-spot-instance-interruption-warning-event").

###### To view BidEvictedEvent events in CloudTrail

1. Open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, choose **Event history**.
3. From the list of filters, choose **Event name**, and
   then in the filter field to the right, enter `BidEvictedEvent`.
4. (Optional) Select a time range.
5. If the list is not empty, choose **BidEvictedEvent** from
   the resulting entry to open its details page. You can find information about
   the Spot Instance in the **Event record** pane, including the ID of
   the Spot Instance. The following is an example of the event record.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "accountId": "123456789012",
        "invokedBy": "ec2.amazonaws.com"
    },
    "eventTime": "2016-08-16T22:30:00Z",
    "eventSource": "ec2.amazonaws.com",
    "userAgent": "ec2.amazonaws.com",
    "sourceIPAddress": "ec2.amazonaws.com",
    "eventName": "BidEvictedEvent",
    "awsRegion": "us-east-2",
    "eventID": "d27a6096-807b-4bd0-8c20-a33a83375054",
    "eventType": "AwsServiceEvent",
    "recipientAccountId": "123456789012",
    "RequestParameters": null,
    "ResponseElements": null,
    "serviceEventDetails": {
        "instanceIdSet": [
          "i-1eb2ac8eEXAMPLE"
        ]
    }
}
```

6. If you did not find an entry for the `BidEvictedEvent` event,
   enter `TerminateInstances` as the event name. For more
   information about the event record for `TerminateInstances`, see
   [Amazon EC2 API event examples](monitor-with-cloudtrail.md#cloudtrail-event-examples "monitor-with-cloudtrail.md#cloudtrail-event-examples").
