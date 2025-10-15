# WorkerSummary

The summary of details for a worker.


## Contents





**createdAt** 


The date and time the resource was created.


Type: Timestamp


Required: Yes




**createdBy** 


The user or system that created this resource.


Type: String


Required: Yes




**farmId** 


The farm ID.


Type: String


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**fleetId** 


The fleet ID.


Type: String


Pattern: `fleet-[0-9a-f]{32}`



Required: Yes




**status** 


The status of the worker.


Type: String


Valid Values: `CREATED | STARTED | STOPPING | STOPPED | NOT_RESPONDING | NOT_COMPATIBLE | RUNNING | IDLE`



Required: Yes




**workerId** 


The worker ID.


Type: String


Pattern: `worker-[0-9a-f]{32}`



Required: Yes




**hostProperties** 


The host properties of the worker.


Type: [HostPropertiesResponse](API_HostPropertiesResponse.md "API_HostPropertiesResponse.md") object


Required: No




**log** 


The log configuration for the worker.


Type: [LogConfiguration](API_LogConfiguration.md "API_LogConfiguration.md") object


Required: No




**updatedAt** 


The date and time the resource was updated.


Type: Timestamp


Required: No




**updatedBy** 


The user or system that updated this resource.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/WorkerSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/WorkerSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/WorkerSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/WorkerSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/WorkerSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/WorkerSummary")
