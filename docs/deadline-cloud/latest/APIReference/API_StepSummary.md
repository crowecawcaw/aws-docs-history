# StepSummary

The details for a step.


## Contents





**createdAt** 


The date and time the resource was created.


Type: Timestamp


Required: Yes




**createdBy** 


The user or system that created this resource.


Type: String


Required: Yes




**lifecycleStatus** 


The life cycle status.


Type: String


Valid Values: `CREATE_COMPLETE | UPDATE_IN_PROGRESS | UPDATE_FAILED | UPDATE_SUCCEEDED`



Required: Yes




**name** 


The name of the step.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Required: Yes




**stepId** 


The step ID.


Type: String


Pattern: `step-[0-9a-f]{32}`



Required: Yes




**taskRunStatus** 


The task run status for the job.



* `PENDING`–pending and waiting for resources.
* `READY`–ready to process.
* `ASSIGNED`–assigned and will run next on a worker.
* `SCHEDULED`–scheduled to run on a worker.
* `INTERRUPTING`–being interrupted.
* `RUNNING`–running on a worker.
* `SUSPENDED`–the task is suspended.
* `CANCELED`–the task has been canceled.
* `FAILED`–the task has failed.
* `SUCCEEDED`–the task has succeeded.

Type: String


Valid Values: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`



Required: Yes




**taskRunStatusCounts** 


The number of tasks running on the job.


Type: String to integer map


Valid Keys: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`



Required: Yes




**dependencyCounts** 


The number of dependencies for the step.


Type: [DependencyCounts](API_DependencyCounts.md "API_DependencyCounts.md") object


Required: No




**endedAt** 


The date and time the resource ended running.


Type: Timestamp


Required: No




**lifecycleStatusMessage** 


A message that describes the lifecycle of the step.


Type: String


Required: No




**startedAt** 


The date and time the resource started running.


Type: Timestamp


Required: No




**targetTaskRunStatus** 


The task status to start with on the job.


Type: String


Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`



Required: No




**taskFailureRetryCount** 


The total number of times tasks from the step failed and were retried.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.


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



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StepSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StepSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StepSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StepSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StepSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StepSummary")
