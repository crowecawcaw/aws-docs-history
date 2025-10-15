# GetJobEntityError

The error for the job entity.


## Contents


###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.





**environmentDetails** 


The environment details for the failed job entity.


Type: [EnvironmentDetailsError](API_EnvironmentDetailsError.md "API_EnvironmentDetailsError.md") object


Required: No




**jobAttachmentDetails** 


The job attachment details for the failed job entity.


Type: [JobAttachmentDetailsError](API_JobAttachmentDetailsError.md "API_JobAttachmentDetailsError.md") object


Required: No




**jobDetails** 


The job details for the failed job entity.


Type: [JobDetailsError](API_JobDetailsError.md "API_JobDetailsError.md") object


Required: No




**stepDetails** 


The step details for the failed job entity.


Type: [StepDetailsError](API_StepDetailsError.md "API_StepDetailsError.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetJobEntityError "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetJobEntityError")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetJobEntityError "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetJobEntityError")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetJobEntityError "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetJobEntityError")
