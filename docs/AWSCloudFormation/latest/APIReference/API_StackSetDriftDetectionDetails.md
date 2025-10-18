# StackSetDriftDetectionDetails

Detailed information about the drift status of the StackSet.

For StackSets, contains information about the last *completed* drift
 operation performed on the StackSet. Information about drift operations in-progress isn't
 included.

For StackSet operations, includes information about drift operations currently being
 performed on the StackSet.

For more information, see [Performing drift detection on
 CloudFormation StackSets](../UserGuide/stacksets-drift.md "../UserGuide/stacksets-drift.md") in the *AWS CloudFormation User Guide*.


## Contents





**DriftDetectionStatus** 


The status of the StackSet drift detection operation.



* `COMPLETED`: The drift detection operation completed without failing on any
 stack instances.
* `FAILED`: The drift detection operation exceeded the specified failure
 tolerance.
* `PARTIAL_SUCCESS`: The drift detection operation completed without exceeding
 the failure tolerance for the operation.
* `IN_PROGRESS`: The drift detection operation is currently being
 performed.
* `STOPPED`: The user has canceled the drift detection operation.

Type: String


Valid Values: `COMPLETED | FAILED | PARTIAL_SUCCESS | IN_PROGRESS | STOPPED`



Required: No




**DriftedStackInstancesCount** 


The number of stack instances that have drifted from the expected template and parameter
 configuration of the StackSet. A stack instance is considered to have drifted if one or more of
 the resources in the associated stack don't match their expected configuration.


Type: Integer


Valid Range: Minimum value of 0.


Required: No




**DriftStatus** 


Status of the StackSet's actual configuration compared to its expected template and
 parameter configuration.



* `DRIFTED`: One or more of the stack instances belonging to the StackSet differs
 from the expected template and parameter configuration. A stack instance is considered to have
 drifted if one or more of the resources in the associated stack have drifted.
* `NOT_CHECKED`: CloudFormation hasn't checked the StackSet for drift.
* `IN_SYNC`: All of the stack instances belonging to the StackSet stack match the
 expected template and parameter configuration.

Type: String


Valid Values: `DRIFTED | IN_SYNC | NOT_CHECKED`



Required: No




**FailedStackInstancesCount** 


The number of stack instances for which the drift detection operation failed.


Type: Integer


Valid Range: Minimum value of 0.


Required: No




**InProgressStackInstancesCount** 


The number of stack instances that are currently being checked for drift.


Type: Integer


Valid Range: Minimum value of 0.


Required: No




**InSyncStackInstancesCount** 


The number of stack instances which match the expected template and parameter configuration
 of the StackSet.


Type: Integer


Valid Range: Minimum value of 0.


Required: No




**LastDriftCheckTimestamp** 


Most recent time when CloudFormation performed a drift detection operation on the StackSet. This
 value will be `NULL` for any StackSet that drift detection hasn't yet been performed
 on.


Type: Timestamp


Required: No




**TotalStackInstancesCount** 


The total number of stack instances belonging to this StackSet.


The total number of stack instances is equal to the total of:



* Stack instances that match the StackSet configuration.
* Stack instances that have drifted from the StackSet configuration.
* Stack instances where the drift detection operation has failed.
* Stack instances currently being checked for drift.

Type: Integer


Valid Range: Minimum value of 0.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetDriftDetectionDetails "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetDriftDetectionDetails")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetDriftDetectionDetails "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetDriftDetectionDetails")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetDriftDetectionDetails "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetDriftDetectionDetails")
