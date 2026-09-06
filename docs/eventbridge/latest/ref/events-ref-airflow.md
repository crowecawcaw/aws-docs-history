

# Amazon Managed Workflows for Apache Airflow events
<a name="events-ref-airflow"></a>

Amazon MWAA sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon MWAA service events
<a name="events-ref-airflow-events"></a>

Amazon MWAA sends the following events directly to EventBridge: 
+ MWAA Environment Status Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.airflow

```
{
  "source": ["aws.airflow"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.airflow"],
  "detail-type": ["{{MWAA Environment Status Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon MWAA events delivered via AWS CloudTrail
<a name="event-ref-airflow-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon MWAA to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.airflow
+ `eventSource`: airflow.amazonaws.com

```
{
  "source": ["aws.airflow"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["airflow.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.airflow"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["airflow.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```