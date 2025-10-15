# QueueLimitAssociationSummary

Provides information about the association between a queue and a limit.


## Contents





**createdAt** 


The Unix timestamp of the date and time that the association was created.


Type: Timestamp


Required: Yes




**createdBy** 


The user identifier of the person that created the association.


Type: String


Required: Yes




**limitId** 


The unique identifier of the limit in the association.


Type: String


Pattern: `limit-[0-9a-f]{32}`



Required: Yes




**queueId** 


The unique identifier of the queue in the association.


Type: String


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




**status** 


The status of task scheduling in the queue-limit association.



* `ACTIVE` - Association is active.
* `STOP_LIMIT_USAGE_AND_COMPLETE_TASKS` - Association has stopped
 scheduling new tasks and is completing current tasks.
* `STOP_LIMIT_USAGE_AND_CANCEL_TASKS` - Association has stopped
 scheduling new tasks and is canceling current tasks.
* `STOPPED` - Association has been stopped.

Type: String


Valid Values: `ACTIVE | STOP_LIMIT_USAGE_AND_COMPLETE_TASKS | STOP_LIMIT_USAGE_AND_CANCEL_TASKS | STOPPED`



Required: Yes




**updatedAt** 


The Unix timestamp of the date and time that the association was last updated.


Type: Timestamp


Required: No




**updatedBy** 


The user identifier of the person that updated the association.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/QueueLimitAssociationSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/QueueLimitAssociationSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/QueueLimitAssociationSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/QueueLimitAssociationSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/QueueLimitAssociationSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/QueueLimitAssociationSummary")
