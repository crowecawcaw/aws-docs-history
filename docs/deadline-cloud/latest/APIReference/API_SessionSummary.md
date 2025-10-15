# SessionSummary

The summary of a session.


## Contents





**fleetId** 


The fleet ID.


Type: String


Pattern: `fleet-[0-9a-f]{32}`



Required: Yes




**lifecycleStatus** 


The life cycle status for the session.


Type: String


Valid Values: `STARTED | UPDATE_IN_PROGRESS | UPDATE_SUCCEEDED | UPDATE_FAILED | ENDED`



Required: Yes




**sessionId** 


The session ID.


Type: String


Pattern: `session-[0-9a-f]{32}`



Required: Yes




**startedAt** 


The date and time the resource started running.


Type: Timestamp


Required: Yes




**workerId** 


The worker ID.


Type: String


Pattern: `worker-[0-9a-f]{32}`



Required: Yes




**endedAt** 


The date and time the resource ended running.


Type: Timestamp


Required: No




**targetLifecycleStatus** 


The target life cycle status for the session.


Type: String


Valid Values: `ENDED`



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



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SessionSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SessionSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SessionSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SessionSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SessionSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SessionSummary")
