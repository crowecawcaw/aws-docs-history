# WorkerSearchSummary

The details of a worker search.


## Contents





**createdAt** 


The date and time the resource was created.


Type: Timestamp


Required: No




**createdBy** 


The user or system that created this resource.


Type: String


Required: No




**fleetId** 


The fleet ID.


Type: String


Pattern: `fleet-[0-9a-f]{32}`



Required: No




**hostProperties** 


Provides the Amazon EC2 instance properties of the worker host.


Type: [HostPropertiesResponse](API_HostPropertiesResponse.md "API_HostPropertiesResponse.md") object


Required: No




**status** 


The status of the worker search.


Type: String


Valid Values: `CREATED | STARTED | STOPPING | STOPPED | NOT_RESPONDING | NOT_COMPATIBLE | RUNNING | IDLE`



Required: No




**updatedAt** 


The date and time the resource was updated.


Type: Timestamp


Required: No




**updatedBy** 


The user or system that updated this resource.


Type: String


Required: No




**workerId** 


The worker ID.


Type: String


Pattern: `worker-[0-9a-f]{32}`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/WorkerSearchSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/WorkerSearchSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/WorkerSearchSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/WorkerSearchSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/WorkerSearchSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/WorkerSearchSummary")
