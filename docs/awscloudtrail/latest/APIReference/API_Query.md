# Query

A SQL string of criteria about events that you want to collect in an event data
 store.


## Contents





**CreationTime** 


The creation time of a query.


Type: Timestamp


Required: No




**QueryId** 


The ID of a query.


Type: String


Length Constraints: Fixed length of 36.


Pattern: `^[a-f0-9\-]+$`



Required: No




**QueryStatus** 


The status of the query. This can be `QUEUED`, `RUNNING`,
 `FINISHED`, `FAILED`, `TIMED_OUT`, or
 `CANCELLED`.


Type: String


Valid Values: `QUEUED | RUNNING | FINISHED | FAILED | CANCELLED | TIMED_OUT`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Query "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Query")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Query "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Query")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Query "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Query")
