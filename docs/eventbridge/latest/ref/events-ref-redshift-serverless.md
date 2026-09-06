

# Amazon Redshift Serverless events
<a name="events-ref-redshift-serverless"></a>

Redshift Serverless sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Redshift Serverless service events
<a name="events-ref-redshift-serverless-events"></a>

Redshift Serverless sends the following events directly to EventBridge: 
+ Redshift Serverless Management
+ Redshift Serverless Data Sharing
+ Redshift Serverless Rate change
+ Redshift Serverless Base RPU Change
+ Redshift Serverless Configuration
+ Redshift Serverless Monitoring
+ Redshift Serverless Security
+ Redshift Serverless Pending

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.redshift-serverless

```
{
  "source": ["aws.redshift-serverless"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.redshift-serverless"],
  "detail-type": ["{{Redshift Serverless Management}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Redshift Serverless events delivered via AWS CloudTrail
<a name="event-ref-redshift-serverless-events-via-CT"></a>

AWS CloudTrail sends events originating from Redshift Serverless to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.redshift-serverless
+ `eventSource`: redshift-serverless.amazonaws.com

```
{
  "source": ["aws.redshift-serverless"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["redshift-serverless.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.redshift-serverless"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["redshift-serverless.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```