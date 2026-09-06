

# Amazon Bedrock events
<a name="events-ref-bedrock"></a>

Amazon Bedrock sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon Bedrock service events
<a name="events-ref-bedrock-events"></a>

Amazon Bedrock sends the following events directly to EventBridge: 
+ Model Customization Job State Change
+ Batch Inference Job State Change
+ Bedrock Data Automation Job Created
+ Bedrock Data Automation Job Succeeded
+ Bedrock Data Automation Job Failed With Client Error
+ Bedrock Data Automation Job Failed With Service Error

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.bedrock

```
{
  "source": ["aws.bedrock"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.bedrock"],
  "detail-type": ["{{Model Customization Job State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon Bedrock events delivered via AWS CloudTrail
<a name="event-ref-bedrock-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Bedrock to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.bedrock
+ `eventSource`: bedrock.amazonaws.com

```
{
  "source": ["aws.bedrock"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["bedrock.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.bedrock"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["bedrock.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```