

# AWS Systems Manager for SAP events
<a name="events-ref-ssm-sap"></a>

Systems Manager for SAP sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Systems Manager for SAP service events
<a name="events-ref-ssm-sap-events"></a>

Systems Manager for SAP sends the following events directly to EventBridge: 
+ SSM for SAP Operation State Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.ssm-sap

```
{
  "source": ["aws.ssm-sap"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.ssm-sap"],
  "detail-type": ["{{SSM for SAP Operation State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Systems Manager for SAP events delivered via AWS CloudTrail
<a name="event-ref-ssm-sap-events-via-CT"></a>

AWS CloudTrail sends events originating from Systems Manager for SAP to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.ssm-sap
+ `eventSource`: ssm-sap.amazonaws.com

```
{
  "source": ["aws.ssm-sap"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ssm-sap.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.ssm-sap"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ssm-sap.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```