

# AWS Data Exchange events
<a name="events-ref-dataexchange"></a>

AWS Data Exchange sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Data Exchange service events
<a name="events-ref-dataexchange-events"></a>

AWS Data Exchange sends the following events directly to EventBridge: 
+ Revision Published To Data Set
+ Data Sets Published To Product
+ Revision Revoked
+ API Gateway API Data Sets Published To Product
+ API Gateway API Data Set Removed From Product
+ Data Set Removed From Product
+ Revision Published To Redshift Data Shares Data Set
+ Redshift Data Shares Data Sets Published To Product
+ Action Performed On Redshift Data Share By Provider
+ Redshift Data Share Access Lost
+ Revision Published To API Gateway API Data Set
+ Revision Published To Lake Formation Data Permission Data Set
+ Lake Formation Data Permission Data Sets Published To Product
+ S3 Data Access Data Set(s) Published to Product(s)
+ Revision Published to S3 Data Access Data Set(s)
+ Revision Revoked from S3 Data Access Data Set(s)
+ Data Set Update Delayed
+ Data Updated in Data Set
+ Deprecation Planned for Data Set
+ Schema Change Planned for Data Set
+ Auto-export Job Completed
+ Auto-export Job Failed
+ Data Grant Extended
+ Data Grant Accepted
+ Data Grant Revoked

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.dataexchange

```
{
  "source": ["aws.dataexchange"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.dataexchange"],
  "detail-type": ["{{Revision Published To Data Set}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## AWS Data Exchange events delivered via AWS CloudTrail
<a name="event-ref-dataexchange-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Data Exchange to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.dataexchange
+ `eventSource`: dataexchange.amazonaws.com

```
{
  "source": ["aws.dataexchange"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["dataexchange.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.dataexchange"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["dataexchange.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```