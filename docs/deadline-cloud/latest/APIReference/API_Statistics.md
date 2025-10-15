# Statistics

A list of statistics for a session.


## Contents





**costInUsd** 


How the statistics should appear in USD. Options include: minimum, maximum, average or
 sum.


Type: [Stats](API_Stats.md "API_Stats.md") object


Required: Yes




**count** 


The number of instances in a list of statistics.


Type: Integer


Required: Yes




**runtimeInSeconds** 


The total aggregated runtime.


Type: [Stats](API_Stats.md "API_Stats.md") object


Required: Yes




**aggregationEndTime** 


The end time for the aggregation.


Type: Timestamp


Required: No




**aggregationStartTime** 


The start time for the aggregation.


Type: Timestamp


Required: No




**fleetId** 


The fleet ID.


Type: String


Pattern: `fleet-[0-9a-f]{32}`



Required: No




**instanceType** 


The type of instance.


Type: String


Pattern: `[a-zA-Z0-9]+\.[a-zA-Z0-9]+`



Required: No




**jobId** 


The job ID.


Type: String


Pattern: `job-[0-9a-f]{32}`



Required: No




**jobName** 


The job name.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Required: No




**licenseProduct** 


The licensed product.


Type: String


Required: No




**queueId** 


The queue ID.


Type: String


Pattern: `queue-[0-9a-f]{32}`



Required: No




**usageType** 


The type of usage for the statistics.


Type: String


Valid Values: `COMPUTE | LICENSE`



Required: No




**userId** 


The user ID.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/Statistics "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/Statistics")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/Statistics "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/Statistics")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/Statistics "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/Statistics")
