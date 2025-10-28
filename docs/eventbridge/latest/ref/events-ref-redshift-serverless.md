# Amazon Redshift Serverless events

Redshift Serverless sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Redshift Serverless service events

Redshift Serverless sends the following events directly to EventBridge:

- Redshift Serverless Management
- Redshift Serverless Data Sharing
- Redshift Serverless Rate change
- Redshift Serverless Base RPU Change
- Redshift Serverless Configuration
- Redshift Serverless Monitoring
- Redshift Serverless Security
- Redshift Serverless Pending

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.redshift-serverless

```
{
  "source": ["aws.redshift-serverless"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.redshift-serverless"],
  "detail-type": ["`Redshift Serverless Management`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Redshift Serverless events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Redshift Serverless to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.redshift-serverless
- `eventSource`: redshift-serverless.amazonaws.com

```
{
  "source": ["aws.redshift-serverless"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["redshift-serverless.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.redshift-serverless"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["redshift-serverless.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
