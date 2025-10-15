# QueueSummary

The details of a queue summary.


## Contents





**createdAt** 


The date and time the resource was created.


Type: Timestamp


Required: Yes




**createdBy** 


The user or system that created this resource.


Type: String


Required: Yes




**defaultBudgetAction** 


The default action taken on a queue summary if a budget wasn't configured.


Type: String


Valid Values: `NONE | STOP_SCHEDULING_AND_COMPLETE_TASKS | STOP_SCHEDULING_AND_CANCEL_TASKS`



Required: Yes




**displayName** 


The display name of the queue summary to update.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.


Required: Yes




**farmId** 


The farm ID.


Type: String


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**queueId** 


The queue ID.


Type: String


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




**status** 


That status of the queue.


Type: String


Valid Values: `IDLE | SCHEDULING | SCHEDULING_BLOCKED`



Required: Yes




**blockedReason** 


The reason the queue is blocked, if applicable.


Type: String


Valid Values: `NO_BUDGET_CONFIGURED | BUDGET_THRESHOLD_REACHED`



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



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/QueueSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/QueueSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/QueueSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/QueueSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/QueueSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/QueueSummary")
