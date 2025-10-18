# IngestionStatus

A table showing information about the most recent successful and failed attempts 
 to ingest events.


## Contents





**LatestIngestionAttemptEventID** 


The event ID of the most recent attempt to ingest events.


Type: String


Length Constraints: Fixed length of 36.


Pattern: `^[a-f0-9\-]+$`



Required: No




**LatestIngestionAttemptTime** 


The time stamp of the most recent attempt to ingest events on the channel.


Type: Timestamp


Required: No




**LatestIngestionErrorCode** 


The error code for the most recent failure to ingest events.


Type: String


Length Constraints: Minimum length of 4. Maximum length of 1000.


Pattern: `.*`



Required: No




**LatestIngestionSuccessEventID** 


The event ID of the most recent successful ingestion of events.


Type: String


Length Constraints: Fixed length of 36.


Pattern: `^[a-f0-9\-]+$`



Required: No




**LatestIngestionSuccessTime** 


The time stamp of the most recent successful ingestion of events for the channel.


Type: Timestamp


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/IngestionStatus "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/IngestionStatus")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/IngestionStatus "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/IngestionStatus")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/IngestionStatus "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/IngestionStatus")
