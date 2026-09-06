

# AWS IAM Identity Center directory events
<a name="events-ref-sso-directory"></a>

IAM Identity Center directory sends service events to EventBridge via AWS CloudTrail.

## IAM Identity Center directory events delivered via AWS CloudTrail
<a name="event-ref-sso-directory-events-via-CT"></a>

AWS CloudTrail sends events originating from IAM Identity Center directory to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.sso-directory
+ `eventSource`: sso-directory.amazonaws.com

```
{
  "source": ["aws.sso-directory"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["sso-directory.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.sso-directory"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["sso-directory.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```