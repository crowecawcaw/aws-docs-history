# Amazon Forecast events

Forecast sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Forecast service events

Forecast sends the following events directly to EventBridge:

- Forecast Dataset Import Job State Change
- Forecast Predictor Creation State Change
- Forecast Predictor Deployment State Change
- Forecast Export Job State Change
- Forecast Forecast Creation State Change
- Forecast Forecast Deletion State Change
- Forecast Forecast Export Job State Change
- Forecast Predictor Backtest Export Job State Change
- Forecast Predictor Deletion State Change
- Forecast Dataset Deletion State Change
- Forecast Dataset Import Job Deletion State Change
- Forecast Explainability Creation State Change
- Forecast Explainability Export Job State Change
- Forecast Explainability Deletion State Change
- Forecast What-If Analysis Creation State Change
- Forecast What-If Forecast Creation State Change
- Forecast What-If Forecast Export Creation State Change
- Forecast What-If Analysis Deletion State Change
- Forecast What-If Forecast Deletion State Change
- Forecast What-If Forecast Export Deletion State Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.forecast

```
{
  "source": ["aws.forecast"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.forecast"],
  "detail-type": ["`Forecast Dataset Import Job State Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Forecast events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Forecast to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.forecast
- `eventSource`: forecast.amazonaws.com

```
{
  "source": ["aws.forecast"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["forecast.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.forecast"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["forecast.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
