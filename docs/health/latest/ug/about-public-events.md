# Monitoring account-specific and public events for

AWS Health

When you create an EventBridge rule to monitor events from AWS Health, the rule delivers both
account-specific events and public events:

- _Account-specific_ events affect your account and resources, such
  as an event that tells you about a required update to an Amazon EC2 instance or other scheduled
  change events.
- _Public_ events appear on the [AWS Health Dashboard – Service health](https://status.aws.amazon.com "https://status.aws.amazon.com"). Public events aren't specific to
  AWS accounts and provide public information about the Regional availability of a
  service.

###### Important

To receive both event types, your rule must use the `"source": [
 "aws.health"]` value. Wildcards, such as `"source": [ "aws.health*"]`
won't match the pattern to monitor for any events.

You can identify if an event is public or account-specific in EventBridge, by using the
eventScopeCode parameter. Events can have the `PUBLIC` or
`ACCOUNT_SPECIFIC`. You can also filter your rule on this parameter.

**Example: Public events for Amazon Elastic Compute Cloud**

The following event shows an operational issue for Amazon EC2 in the US East (N. Virginia) Region.

```

{
    "version": "0",
    "id": "fd9d4512-1eb0-50f6-0491-d016ae56aef0",
    "detail-type": "AWS Health Event",
    "source": "aws.health",
    "account": "123456789012",
    "time": "2023-02-15T10:07:10Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "eventArn": "arn:aws:health:us-east-1::event/EC2/AWS_EC2_OPERATIONAL_ISSUE",
        "service": "EC2",
        "eventTypeCode": "AWS_EC2_OPERATIONAL_ISSUE",
        "eventTypeCategory": "issue",
        "eventScopeCode": "PUBLIC",
        "communicationId": "01b0993207d81a09dcd552ebd1e633e36cf1f09a-1",
        "startTime": "Wed, 15 Feb 2023 22:07:07 GMT",
        "lastUpdatedTime": "Wed, 15 Feb 2023 22:07:07 GMT",
        "statusCode": "open",
        "eventRegion": "us-east-1",
        "eventDescription": [{
            "latestDescription": "We are investigating increased API Error rates and Latencies for Amazon Elastic Compute Cloud in the US-EAST-1 Region.",
            "language": "en_US"
        }],
        "page": "1",
        "totalPages": "1",
        "affectedAccount": "123456789012"

    }
}
```

## Backup rules for AWS Health events

If you're monitoring public events from an AWS Region, we recommend that you create a
back up rule. Public events for AWS Health are sent simultaneously to both the impacted
Region and to the backup Region when a valid rule is set in the impacted Region.

AWS Health sends account-specific events to both the impacted Region and to the backup Region, regardless of any rules configured in the impacted Region.

We recommend that you deduplicate AWS Health events using `eventARN` and `communicationId` because these values remain consistent for AWS Health messages that are sent to the backup Region.
