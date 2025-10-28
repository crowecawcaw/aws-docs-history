# AWS Application Cost Profiler events

Application Cost Profiler sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Application Cost Profiler service events

Application Cost Profiler sends the following events directly to EventBridge:

- Application Cost Profiler Report Generated
- Application Cost Profiler Report Generation Failure
- Application Cost Profiler Report Delivery Failure
- Application Cost Profiler Ingestion Data Access Failure
- Application Cost Profiler Ingestion Data Validation Failure

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.application-cost-profiler

```
{
  "source": ["aws.application-cost-profiler"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.application-cost-profiler"],
  "detail-type": ["`Application Cost Profiler Report Generated`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Application Cost Profiler events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Application Cost Profiler to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.application-cost-profiler
- `eventSource`: application-cost-profiler.amazonaws.com

```
{
  "source": ["aws.application-cost-profiler"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["application-cost-profiler.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.application-cost-profiler"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["application-cost-profiler.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
