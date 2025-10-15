# TaskSearchSummary

The details of a task search.


## Contents





**endedAt** 


The date and time the resource ended running.


Type: Timestamp


Required: No




**failureRetryCount** 


The number of times that the task failed and was retried.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.


Required: No




**jobId** 


The job ID.


Type: String


Pattern: `job-[0-9a-f]{32}`



Required: No




**parameters** 


The parameters to search for.


Type: String to [TaskParameterValue](API_TaskParameterValue.md "API_TaskParameterValue.md") object map


Required: No




**queueId** 


The queue ID.


Type: String


Pattern: `queue-[0-9a-f]{32}`



Required: No




**runStatus** 


The run status of the task.


Type: String


Valid Values: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`



Required: No




**startedAt** 


The date and time the resource started running.


Type: Timestamp


Required: No




**stepId** 


The step ID.


Type: String


Pattern: `step-[0-9a-f]{32}`



Required: No




**targetRunStatus** 


The run status that the task is being updated to.


Type: String


Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`



Required: No




**taskId** 


The task ID.


Type: String


Pattern: `task-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`



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



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/TaskSearchSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/TaskSearchSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/TaskSearchSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/TaskSearchSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/TaskSearchSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/TaskSearchSummary")
