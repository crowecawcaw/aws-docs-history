# EnvironmentDetailsEntity

The details of a specified environment.


## Contents





**environmentId** 


The environment ID.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `(STEP:step-[0-9a-f]{32}:.*)|(JOB:job-[0-9a-f]{32}:.*)`



Required: Yes




**jobId** 


The job ID.


Type: String


Pattern: `job-[0-9a-f]{32}`



Required: Yes




**schemaVersion** 


The schema version in the environment.


Type: String


Required: Yes




**template** 


The template used for the environment.


Type: JSON value


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/EnvironmentDetailsEntity "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/EnvironmentDetailsEntity")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/EnvironmentDetailsEntity "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/EnvironmentDetailsEntity")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/EnvironmentDetailsEntity "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/EnvironmentDetailsEntity")
