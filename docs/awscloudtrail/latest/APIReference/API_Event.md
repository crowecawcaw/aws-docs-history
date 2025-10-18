# Event

Contains information about an event that was returned by a lookup request. The result
 includes a representation of a CloudTrail event.


## Contents





**AccessKeyId** 


The AWS access key ID that was used to sign the request. If the request
 was made with temporary security credentials, this is the access key ID of the temporary
 credentials.


Type: String


Required: No




**CloudTrailEvent** 


A JSON string that contains a representation of the event returned.


Type: String


Required: No




**EventId** 


The CloudTrail ID of the event returned.


Type: String


Required: No




**EventName** 


The name of the event returned.


Type: String


Required: No




**EventSource** 


The AWS service to which the request was made.


Type: String


Required: No




**EventTime** 


The date and time of the event returned.


Type: Timestamp


Required: No




**ReadOnly** 


Information about whether the event is a write event or a read event. 


Type: String


Required: No




**Resources** 


A list of resources referenced by the event returned.


Type: Array of [Resource](API_Resource.md "API_Resource.md") objects


Required: No




**Username** 


A user name or role name of the requester that called the API in the event
 returned.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Event "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Event")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Event "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Event")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Event "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Event")
