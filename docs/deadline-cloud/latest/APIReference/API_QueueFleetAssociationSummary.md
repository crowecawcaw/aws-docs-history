# QueueFleetAssociationSummary

The details of a queue-fleet association.


## Contents





**createdAt** 


The date and time the resource was created.


Type: Timestamp


Required: Yes




**createdBy** 


The user or system that created this resource.


Type: String


Required: Yes




**fleetId** 


The fleet ID.


Type: String


Pattern: `fleet-[0-9a-f]{32}`



Required: Yes




**queueId** 


The queue ID.


Type: String


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




**status** 


The status of task scheduling in the queue-fleet association.



* `ACTIVE`–Association is active.
* `STOP_SCHEDULING_AND_COMPLETE_TASKS`–Association has stopped
 scheduling new tasks and is completing current tasks.
* `STOP_SCHEDULING_AND_CANCEL_TASKS`–Association has stopped
 scheduling new tasks and is canceling current tasks.
* `STOPPED`–Association has been stopped.

Type: String


Valid Values: `ACTIVE | STOP_SCHEDULING_AND_COMPLETE_TASKS | STOP_SCHEDULING_AND_CANCEL_TASKS | STOPPED`



Required: Yes




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



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/QueueFleetAssociationSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/QueueFleetAssociationSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/QueueFleetAssociationSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/QueueFleetAssociationSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/QueueFleetAssociationSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/QueueFleetAssociationSummary")
