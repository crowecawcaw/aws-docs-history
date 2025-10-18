# ImportStatistics

 Provides statistics for the specified `ImportID`. CloudTrail does not
 update import statistics in real-time. Returned values for parameters such as
 `EventsCompleted` may be lower than the actual value, because CloudTrail updates statistics incrementally over the course of the import. 


## Contents





**EventsCompleted** 


 The number of trail events imported into the event data store. 


Type: Long


Required: No




**FailedEntries** 


 The number of failed entries. 


Type: Long


Required: No




**FilesCompleted** 


The number of log files that completed import.


Type: Long


Required: No




**PrefixesCompleted** 


 The number of S3 prefixes that completed import. 


Type: Long


Required: No




**PrefixesFound** 


 The number of S3 prefixes found for the import. 


Type: Long


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ImportStatistics "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ImportStatistics")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ImportStatistics "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ImportStatistics")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ImportStatistics "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ImportStatistics")
