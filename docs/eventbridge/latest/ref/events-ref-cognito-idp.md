

# Amazon Cognito user pools events
<a name="events-ref-cognito-idp"></a>

Amazon Cognito user pools sends service events to EventBridge via AWS CloudTrail.

## Amazon Cognito user pools events delivered via AWS CloudTrail
<a name="event-ref-cognito-idp-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Cognito user pools to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.cognito-idp
+ `eventSource`: cognito-idp.amazonaws.com

```
{
  "source": ["aws.cognito-idp"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["cognito-idp.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.cognito-idp"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["cognito-idp.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```