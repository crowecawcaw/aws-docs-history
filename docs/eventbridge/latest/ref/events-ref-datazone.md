# Amazon DataZone events

Amazon DataZone sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon DataZone service events

Amazon DataZone sends the following events directly to EventBridge:

- Asset Publication Approval Update
- New Asset Version Available
- Asset Publication Expiration Warning
- Account Association State Change
- Account Association Repair Notification
- Domain Creation Succeeded
- Domain Creation Failed
- Domain Deletion Succeeded
- Domain Deletion Failed
- Domain Unit Created
- Domain Unit Updated
- Domain Unit Deleted
- Domain Unit Owner Added
- Domain Unit Owner Removed
- Policy Grant Added
- Policy Grant Removed
- Project Owner Added With Override
- Project Moved Between Domain Unit
- Environment Deployment Started
- Environment Deployment Completed
- Environment Deployment Failed
- Environment Deletion Started
- Environment Deletion Completed
- Environment Deletion Failed
- Project Creation Succeeded
- Project Member Addition Succeeded
- Project Member Removal Succeeded
- Project Member Role Change Succeeded
- Environment Deployment Customer Workflow Initiated
- Subscription Request Created
- Subscription Request Accepted
- Subscription Request Rejected
- Subscription Request Deleted
- Subscription Created
- Subscription Revoked
- Subscription Cancelled
- Subscription Grant Requested
- Subscription Grant Completed
- Subscription Grant Failed
- Subscription Grant Revoke Requested
- Subscription Grant Revoke Completed
- Subscription Grant Revoke Failed
- Asset Added To Inventory
- Asset Added To Catalog
- Asset Schema Changed
- Asset Unpublished
- Asset Listing Deleted
- Business Name Generation Succeeded
- Business Name Generation Failed
- Metadata Generation Succeeded
- Metadata Generation Failed
- Metadata Generation Canceled
- Metadata Generation Accepted
- Metadata Generation Rejected
- Data Source Created
- Data Source Updated
- Data Source Run Triggered
- Data Source Run Succeeded
- Data Source Run Failed
- Data Product Added To Catalog
- Data Product Publishing Failed
- Data Product Revised
- Subscribed Data Product Updated
- Project Membership Sync Failed
- Project Quick Sight Custom Connection Sync Failed

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.datazone

```
{
  "source": ["aws.datazone"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.datazone"],
  "detail-type": ["`Asset Publication Approval Update`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Amazon DataZone events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon DataZone to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.datazone
- `eventSource`: datazone.amazonaws.com

```
{
  "source": ["aws.datazone"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["datazone.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.datazone"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["datazone.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
