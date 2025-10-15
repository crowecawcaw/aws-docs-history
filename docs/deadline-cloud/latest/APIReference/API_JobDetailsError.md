# JobDetailsError

The details of a job error.


## Contents





**code** 


The error code.


Type: String


Valid Values: `AccessDeniedException | InternalServerException | ValidationException | ResourceNotFoundException | MaxPayloadSizeExceeded | ConflictException`



Required: Yes




**jobId** 


The job ID.


Type: String


Pattern: `job-[0-9a-f]{32}`



Required: Yes




**message** 


The error message detailing the error's cause.


Type: String


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobDetailsError "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobDetailsError")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobDetailsError "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobDetailsError")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobDetailsError "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobDetailsError")
