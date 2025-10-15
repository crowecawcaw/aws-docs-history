# JobDetailsEntity

The job details for a specific job.


## Contents





**jobId** 


The job ID.


Type: String


Pattern: `job-[0-9a-f]{32}`



Required: Yes




**logGroupName** 


The log group name.


Type: String


Required: Yes




**schemaVersion** 


The schema version.


Type: String


Required: Yes




**jobAttachmentSettings** 


The job attachment settings.


Type: [JobAttachmentSettings](API_JobAttachmentSettings.md "API_JobAttachmentSettings.md") object


Required: No




**jobRunAsUser** 


The user name and group that the job uses when run.


Type: [JobRunAsUser](API_JobRunAsUser.md "API_JobRunAsUser.md") object


Required: No




**parameters** 


The parameters.


Type: String to [JobParameter](API_JobParameter.md "API_JobParameter.md") object map


Key Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**pathMappingRules** 


The path mapping rules.


Type: Array of [PathMappingRule](API_PathMappingRule.md "API_PathMappingRule.md") objects


Required: No




**queueRoleArn** 


The queue role ARN.


Type: String


Pattern: `arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobDetailsEntity "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobDetailsEntity")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobDetailsEntity "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobDetailsEntity")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobDetailsEntity "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobDetailsEntity")
