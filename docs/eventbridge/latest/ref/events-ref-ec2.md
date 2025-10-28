# Amazon Elastic Compute Cloud events

Amazon EC2 sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon EC2 service events

Amazon EC2 sends the following events directly to EventBridge:

- EC2 Instance State-change Notification
- On-Demand Capacity Reservation Billing Ownership Request Pending
- On-Demand Capacity Reservation Billing Ownership Request Expired
- On-Demand Capacity Reservation Billing Ownership Request Cancelled
- On-Demand Capacity Reservation Billing Ownership Revoked
- On-Demand Capacity Reservation Billing Ownership Request Accepted
- On-Demand Capacity Reservation Billing Ownership Request Rejected
- EC2 On-Demand Capacity Reservation Suspended
- EC2 On-Demand Capacity Reservation Suspension Failed
- EC2 On-Demand Capacity Reservation Unsuspended
- EC2 On-Demand Capacity Reservation Unsuspension Failed
- Capacity Block Delivered
- Capacity Block Expiration Warning
- EC2 Capacity Reservation Scheduled
- EC2 Capacity Reservation Active
- EC2 Capacity Reservation Failed
- EC2 Capacity Reservation Delayed
- EC2 Capacity Reservation Expired
- EC2 Capacity Reservation Unsupported
- EC2 Capacity Reservation Cancelled
- Future Capacity Request in Assessing
- Future Capacity Request Scheduled
- Future Capacity Request Unsupported
- Future Capacity Request Delayed
- Future Capacity Request Completed
- Future Capacity Request Canceled
- Future Capacity Request Failed
- EC2 Capacity Loan Request Pending Acceptance
- EC2 Capacity Loan Request Automatically Accepted
- EC2 Capacity Loan Request Accepted
- EC2 Capacity Loan Request Rejected
- EC2 Capacity Loan Request Expired
- EC2 Capacity Loan Request Canceled
- EC2 Capacity Loan Active
- EC2 Capacity Loan Release Request Pending Acceptance
- EC2 Capacity Loan Release Request Automatically Accepted
- EC2 Capacity Loan Release Request Accepted
- EC2 Capacity Loan Release Request Rejected
- EC2 Capacity Loan Release Request Expired
- EC2 Capacity Loan Release Completed
- EBS Volume Notification
- EBS Snapshot Notification
- EBS Multi-Volume Snapshots Completion Status
- EBS Snapshot Block Public Access Enabled
- EBS Snapshot Block Public Access Disabled
- EBS Copy Snapshot Missed Completion Duration
- EC2 Spot Instance Interruption Warning
- EC2 Spot Instance Request Fulfillment
- EC2 Spot Instance Rebalance Recommended
- EC2 Instance Rebalance Recommendation
- EBS Snapshot Acceleration State-change Notification
- EBS Fast Snapshot Restore State-change Notification
- Launch Template Alias Change
- EC2 AMI Available
- EC2 AMI Failed
- EC2 AMI State Change
- EC2 Fast Launch State-change Notification

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.ec2

```
{
  "source": ["aws.ec2"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.ec2"],
  "detail-type": ["`EC2 Instance State-change Notification`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Amazon EC2 events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon EC2 to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.ec2
- `eventSource`: ec2.amazonaws.com

```
{
  "source": ["aws.ec2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ec2.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.ec2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ec2.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
