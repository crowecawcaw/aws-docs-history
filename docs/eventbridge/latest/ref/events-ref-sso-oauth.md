

# AWS IAM Identity Center events
<a name="events-ref-sso-oauth"></a>

IAM Identity Center sends service events to EventBridge via AWS CloudTrail.

## IAM Identity Center events delivered via AWS CloudTrail
<a name="event-ref-sso-oauth-events-via-CT"></a>

AWS CloudTrail sends events originating from IAM Identity Center to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.sso-oauth
+ `eventSource`: sso-oauth.amazonaws.com

```
{
  "source": ["aws.sso-oauth"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["sso-oauth.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.sso-oauth"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["sso-oauth.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```