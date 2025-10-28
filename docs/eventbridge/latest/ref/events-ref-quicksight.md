# Amazon Quick Suite events

Quick Suite sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Quick Suite service events

Quick Suite sends the following events directly to EventBridge:

- QuickSight Theme Creation Successful
- QuickSight Theme Creation Failed
- QuickSight Theme Permissions Updated
- QuickSight Theme Update Successful
- QuickSight Theme Update Failed
- QuickSight Theme Deleted
- QuickSight Theme Alias Created
- QuickSight Theme Alias Updated
- QuickSight Theme Alias Deleted
- QuickSight DataSet Created
- QuickSight DataSet Updated
- QuickSight DataSet Deleted
- QuickSight DataSet Permissions Updated
- QuickSight DataSource Creation Successful
- QuickSight DataSource Creation Failed
- QuickSight DataSource Update Successful
- QuickSight DataSource Update Failed
- QuickSight DataSource Permissions Updated
- QuickSight DataSource Deleted
- QuickSight Folder Created
- QuickSight Folder Updated
- QuickSight Folder Membership Updated
- QuickSight Folder Permissions Updated
- QuickSight Folder Deleted
- QuickSight Analysis Creation Successful
- QuickSight Analysis Creation Failed
- QuickSight Analysis Update Successful
- QuickSight Analysis Permissions Updated
- QuickSight Analysis Update Failed
- QuickSight Analysis Deleted
- QuickSight VPC Connection Creation Successful
- QuickSight VPC Connection Creation Failed
- QuickSight VPC Connection Update Successful
- QuickSight VPC Connection Update Failed
- QuickSight VPC Connection Deletion Successful
- QuickSight VPC Connection Deletion Failed
- QuickSight Dashboard Creation Successful
- QuickSight Dashboard Creation Failed
- QuickSight Dashboard Update Successful
- QuickSight Dashboard Update Failed
- QuickSight Dashboard Permissions Updated
- QuickSight Dashboard Published Version Updated
- QuickSight Dashboard Deleted

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.quicksight

```
{
  "source": ["aws.quicksight"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.quicksight"],
  "detail-type": ["`QuickSight Theme Creation Successful`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Quick Suite events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Quick Suite to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.quicksight
- `eventSource`: quicksight.amazonaws.com

```
{
  "source": ["aws.quicksight"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["quicksight.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.quicksight"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["quicksight.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
