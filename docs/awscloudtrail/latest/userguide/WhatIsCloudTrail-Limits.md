# Quotas in AWS CloudTrail

This section describes the resource quotas (formerly referred to as limits) in CloudTrail. 
 For information about all quotas in CloudTrail, see [Service quotas](https://docs.aws.amazon.com/general/latest/gr/ct.html#limits_cloudtrail "https://docs.aws.amazon.com/general/latest/gr/ct.html#limits_cloudtrail") 
 in the *AWS General Reference*.

###### Note

CloudTrail has no adjustable quotas.


## CloudTrail resource quotas


The following table describes the resource quotas within CloudTrail.




| Resource | Default quota | Comments |
| --- | --- | --- |
| Trails per Region | 5 | The maximum number of trails per AWS Region. In shadow Regions, to get latest resource count metric, call the `ListTrails` API. This quota cannot be increased. |
| Event data stores | 10 | The maximum number of event data stores per AWS Region. This includes single-Region event data stores for the Region, multi-Region event data stores across all AWS Regions, and organization event data stores. This includes event data stores in any [lifecycle stage](query-eds-disable-termination.md "query-eds-disable-termination.md"). In shadow Regions, to get latest resource count metric, call the `ListEventDataStores` API. This quota cannot be increased. |
| Channels | 25 | This quota applies to channels used for CloudTrail Lake integrations with event sources outside of AWS, and does not apply to service-linked channels. This quota cannot be increased.  |
| Dashboards per Region | 100 | The maximum number of CloudTrail Lake custom dashboards per AWS Region. In shadow Regions, to get the latest resource count metric, call the `ListDashboards` API. This quota cannot be increased.  |
| Widgets per dashboard | 10 | This maximum number of widgets per CloudTrail Lake dashboard. This quota cannot be increased.  |
| Concurrent dashboard refreshes | 1 | The maximum number of ongoing refreshes per dashboard. This quota cannot be increased.  |
| Concurrent queries | 10 | The maximum number of queued or running queries that you can run simultaneously in CloudTrail Lake. This quota cannot be increased. |
| Events per PutAuditEvents request | 100 | You can add up to 100 activity events (or up to 1 MB) per `PutAuditEvents` request. This quota cannot be increased. |
| Event selectors | 5 per trail | This quota cannot be increased. |
| Advanced event selectors | 500 conditions across all advanced event selectors | If a trail or event data store uses advanced event selectors, a maximum of 500 total values for all conditions in all advanced event selectors is allowed. This quota cannot be increased. |
| Data resources in event selectors | 250 across all event selectors in a trail | If you choose to limit data events by using event selectors, the total number of data resources cannot exceed 250 across all event selectors in a trail. The limit of number of resources on an individual event selector is configurable up to 250. This upper limit is allowed only if the total number of data resources does not exceed 250 across all event selectors. Examples: <br>• A trail with 5 event selectors, each configured with 50 data resources, is allowed. (5\*50=250) <br>• A trail with 5 event selectors, 3 of which are configured with 50 data resources, 1 of which is configured with 99 data resources, and 1 of which is configured with 1 data resource, is also allowed. ((3\*50)+1+99=250) <br>• A trail configured with 5 event selectors, all of which are configured with 100 data resources, is not allowed. (5\*100=500) Event selectors apply only to trails. For event data stores, you must use advanced event selectors.This quota cannot be increased.The quota does not apply if you choose to log data events on all resources, such as all S3 buckets or all Lambda functions. |
| Event size | All event versions: events over 256 KB cannot be sent to CloudWatch Logs Event version 1.05 and newer: total event size limit of 256 KB | Amazon CloudWatch Logs and Amazon EventBridge each allow a maximum event size of 256 KB. CloudTrail does not send events over 256 KB to CloudWatch Logs or EventBridge. Starting with event version 1.05, events have a maximum size of 256 KB. This is to help prevent exploitation by malicious actors, and allow events to be consumed by other AWS services, such as CloudWatch Logs and EventBridge. |
| CloudTrail file size sent to Amazon S3 | 50 MB before compression | For management, data, and network activity events, CloudTrail sends events to S3 in compressed gzip files. The maximum file size before compression is 50 MB. If enabled on the trail, log delivery notifications are sent by Amazon SNS after CloudTrail sends gzip files to S3. | ## Transactions per second (TPS) quotas in CloudTrail The [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html "https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html") lists the transactions per second (TPS) quota for AWS APIs. The transactions per second (TPS) quota for an API represents how many requests you can make per second for a given API without being throttled. For example, the TPS quota for the CloudTrail `LookupEvents` API is 2. For information about the TPS quota for each CloudTrail API, see [Service quotas](https://docs.aws.amazon.com/general/latest/gr/ct.html#limits_cloudtrail "https://docs.aws.amazon.com/general/latest/gr/ct.html#limits_cloudtrail") in the *AWS General Reference*.
