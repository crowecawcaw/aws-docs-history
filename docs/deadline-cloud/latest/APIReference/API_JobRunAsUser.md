# JobRunAsUser

Identifies the user for a job.


## Contents





**runAs** 


Specifies whether the job should run using the queue's system user or if the job should
 run using the worker agent system user.


Type: String


Valid Values: `QUEUE_CONFIGURED_USER | WORKER_AGENT_USER`



Required: Yes




**posix** 


The user and group that the jobs in the queue run as.


Type: [PosixUser](API_PosixUser.md "API_PosixUser.md") object


Required: No




**windows** 


Identifies a Microsoft Windows user.


Type: [WindowsUser](API_WindowsUser.md "API_WindowsUser.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobRunAsUser "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobRunAsUser")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobRunAsUser "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobRunAsUser")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobRunAsUser "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobRunAsUser")
