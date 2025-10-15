# WorkerSessionSummary

Summarizes the session for a particular worker.


## Contents





**jobId** 


The job ID for the job associated with the worker's session.


Type: String


Pattern: `job-[0-9a-f]{32}`



Required: Yes




**lifecycleStatus** 


The life cycle status for the worker's session.


Type: String


Valid Values: `STARTED | UPDATE_IN_PROGRESS | UPDATE_SUCCEEDED | UPDATE_FAILED | ENDED`



Required: Yes




**queueId** 


The queue ID for the queue associated to the worker.


Type: String


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




**sessionId** 


The session ID for the session action.


Type: String


Pattern: `session-[0-9a-f]{32}`



Required: Yes




**startedAt** 


The date and time the resource started running.


Type: Timestamp


Required: Yes




**endedAt** 


The date and time the resource ended running.


Type: Timestamp


Required: No




**targetLifecycleStatus** 


The life cycle status 


Type: String


Valid Values: `ENDED`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/WorkerSessionSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/WorkerSessionSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/WorkerSessionSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/WorkerSessionSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/WorkerSessionSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/WorkerSessionSummary")
