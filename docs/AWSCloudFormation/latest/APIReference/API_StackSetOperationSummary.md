# StackSetOperationSummary

The structures that contain summary information about the specified operation.


## Contents





**Action** 


The type of operation: `CREATE`, `UPDATE`, or `DELETE`.
 Create and delete operations affect only the specified stack instances that are associated with
 the specified StackSet. Update operations affect both the StackSet itself and
 *all* associated StackSet instances.


Type: String


Valid Values: `CREATE | UPDATE | DELETE | DETECT_DRIFT`



Required: No




**CreationTimestamp** 


The time at which the operation was initiated. Note that the creation times for the StackSet
 operation might differ from the creation time of the individual stacks themselves. This is
 because CloudFormation needs to perform preparatory work for the operation, such as dispatching the
 work to the requested Regions, before actually creating the first stacks.


Type: Timestamp


Required: No




**EndTimestamp** 


The time at which the StackSet operation ended, across all accounts and Regions specified.
 Note that this doesn't necessarily mean that the StackSet operation was successful, or even
 attempted, in each account or Region.


Type: Timestamp


Required: No




**OperationId** 


The unique ID of the StackSet operation.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`



Required: No




**OperationPreferences** 


The user-specified preferences for how CloudFormation performs a StackSet operation.


For more information about maximum concurrent accounts and failure tolerance, see [StackSet
 operation options](../UserGuide/stacksets-concepts.md#stackset-ops-options "../UserGuide/stacksets-concepts.md#stackset-ops-options").


Type: [StackSetOperationPreferences](API_StackSetOperationPreferences.md "API_StackSetOperationPreferences.md") object


Required: No




**Status** 


The overall status of the operation.



* `FAILED`: The operation exceeded the specified failure tolerance. The failure
 tolerance value that you've set for an operation is applied for each Region during stack create
 and update operations. If the number of failed stacks within a Region exceeds the failure
 tolerance, the status of the operation in the Region is set to `FAILED`. This in
 turn sets the status of the operation as a whole to `FAILED`, and CloudFormation cancels
 the operation in any remaining Regions.
* `QUEUED`: [Service-managed permissions] For automatic deployments that require
 a sequence of operations, the operation is queued to be performed. For more information, see
 the [StackSet status codes](../UserGuide/stacksets-concepts.md#stackset-status-codes "../UserGuide/stacksets-concepts.md#stackset-status-codes") in the *AWS CloudFormation User Guide*.
* `RUNNING`: The operation is currently being performed.
* `STOPPED`: The user has canceled the operation.
* `STOPPING`: The operation is in the process of stopping, at user
 request.
* `SUCCEEDED`: The operation completed creating or updating all the specified
 stacks without exceeding the failure tolerance for the operation.

Type: String


Valid Values: `RUNNING | SUCCEEDED | FAILED | STOPPING | STOPPED | QUEUED`



Required: No




**StatusDetails** 


Detailed information about the StackSet operation.


Type: [StackSetOperationStatusDetails](API_StackSetOperationStatusDetails.md "API_StackSetOperationStatusDetails.md") object


Required: No




**StatusReason** 


The status of the operation in details.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetOperationSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetOperationSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetOperationSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetOperationSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetOperationSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetOperationSummary")
