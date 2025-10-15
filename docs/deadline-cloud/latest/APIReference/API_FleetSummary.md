# FleetSummary

The details of a fleet.


## Contents





**configuration** 


The configuration details for the fleet.


Type: [FleetConfiguration](API_FleetConfiguration.md "API_FleetConfiguration.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.


Required: Yes




**createdAt** 


The date and time the resource was created.


Type: Timestamp


Required: Yes




**createdBy** 


The user or system that created this resource.


Type: String


Required: Yes




**displayName** 


The display name of the fleet summary to update.


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




**fleetId** 


The fleet ID.


Type: String


Pattern: `fleet-[0-9a-f]{32}`



Required: Yes




**maxWorkerCount** 


The maximum number of workers specified in the fleet.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.


Required: Yes




**minWorkerCount** 


The minimum number of workers in the fleet.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.


Required: Yes




**status** 


The status of the fleet.


Type: String


Valid Values: `ACTIVE | CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | CREATE_FAILED | UPDATE_FAILED | SUSPENDED`



Required: Yes




**workerCount** 


The number of workers in the fleet summary.


Type: Integer


Required: Yes




**autoScalingStatus** 


The AWS Auto Scaling status of a fleet.


Type: String


Valid Values: `GROWING | STEADY | SHRINKING`



Required: No




**statusMessage** 


A message that communicates a suspended status of the fleet.


Type: String


Required: No




**targetWorkerCount** 


The target number of workers in a fleet.


Type: Integer


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



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/FleetSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/FleetSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/FleetSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/FleetSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/FleetSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/FleetSummary")
