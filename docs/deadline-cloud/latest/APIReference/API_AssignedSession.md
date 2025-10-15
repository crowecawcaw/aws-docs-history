# AssignedSession

The assigned session for the worker.


## Contents





**jobId** 


The job ID for the assigned session.


Type: String


Pattern: `job-[0-9a-f]{32}`



Required: Yes




**logConfiguration** 


The log configuration for the worker's assigned session.


Type: [LogConfiguration](API_LogConfiguration.md "API_LogConfiguration.md") object


Required: Yes




**queueId** 


The queue ID of the assigned session.


Type: String


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




**sessionActions** 


The session actions to apply to the assigned session.


Type: Array of [AssignedSessionAction](API_AssignedSessionAction.md "API_AssignedSessionAction.md") objects


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssignedSession "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssignedSession")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssignedSession "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssignedSession")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssignedSession "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssignedSession")
