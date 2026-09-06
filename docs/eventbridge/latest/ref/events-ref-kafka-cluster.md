

# Amazon Managed Streaming for Apache Kafka events
<a name="events-ref-kafka-cluster"></a>

Amazon MSK sends service events to EventBridge via AWS CloudTrail.

## Amazon MSK events delivered via AWS CloudTrail
<a name="event-ref-kafka-cluster-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon MSK to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.kafka-cluster
+ `eventSource`: kafka-cluster.amazonaws.com

```
{
  "source": ["aws.kafka-cluster"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["kafka-cluster.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.kafka-cluster"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["kafka-cluster.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```