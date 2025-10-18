# EventSelector

Use event selectors to further specify the management and data event settings for your
 trail. By default, trails created without specific event selectors will be configured to
 log all read and write management events, and no data events. When an event occurs in your
 account, CloudTrail evaluates the event selector for all trails. For each trail, if
 the event matches any event selector, the trail processes and logs the event. If the event
 doesn't match any event selector, the trail doesn't log the event.

You can configure up to five event selectors for a trail.

You cannot apply both event selectors and advanced event selectors to a trail.


## Contents





**DataResources** 


CloudTrail supports data event logging for Amazon S3 objects in standard S3 buckets, AWS Lambda functions, and Amazon DynamoDB tables with basic event selectors.
 You can specify up to 250 resources for an individual event selector, but the total number
 of data resources cannot exceed 250 across all event selectors in a trail. This limit does
 not apply if you configure resource logging for all data events.


For more information, see [Data
 Events](../userguide/logging-data-events-with-cloudtrail.md "../userguide/logging-data-events-with-cloudtrail.md") and [Limits in AWS CloudTrail](../userguide/WhatIsCloudTrail-Limits.md "../userguide/WhatIsCloudTrail-Limits.md") in the *AWS CloudTrail User
 Guide*.


###### Note

To log data events for all other resource types including objects stored in 
 [directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html"), you must use [AdvancedEventSelectors](API_AdvancedEventSelector.md "API_AdvancedEventSelector.md"). You must also 
 use `AdvancedEventSelectors` if you want to filter on the `eventName` field.


Type: Array of [DataResource](API_DataResource.md "API_DataResource.md") objects


Required: No




**ExcludeManagementEventSources** 


An optional list of service event sources from which you do not want management events
 to be logged on your trail. In this release, the list can be empty (disables the filter),
 or it can filter out AWS Key Management Service or Amazon RDS Data API events by
 containing `kms.amazonaws.com` or `rdsdata.amazonaws.com`. By
 default, `ExcludeManagementEventSources` is empty, and AWS KMS and
 Amazon RDS Data API events are logged to your trail. You can exclude management
 event sources only in Regions that support the event source.


Type: Array of strings


Required: No




**IncludeManagementEvents** 


Specify if you want your event selector to include management events for your
 trail.


 For more information, see [Management Events](../userguide/logging-management-events-with-cloudtrail.md "../userguide/logging-management-events-with-cloudtrail.md") in the *AWS CloudTrail User
 Guide*.


By default, the value is `true`.


The first copy of management events is free. You are charged for additional copies of
 management events that you are logging on any subsequent trail in the same Region. For more
 information about CloudTrail pricing, see [AWS CloudTrail Pricing](http://aws.amazon.com/cloudtrail/pricing/ "http://aws.amazon.com/cloudtrail/pricing/").


Type: Boolean


Required: No




**ReadWriteType** 


Specify if you want your trail to log read-only events, write-only events, or all. For
 example, the EC2 `GetConsoleOutput` is a read-only API operation and
 `RunInstances` is a write-only API operation.


 By default, the value is `All`.


Type: String


Valid Values: `ReadOnly | WriteOnly | All`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/EventSelector "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/EventSelector")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/EventSelector "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/EventSelector")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/EventSelector "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/EventSelector")
