# StackSetOperationPreferences

The user-specified preferences for how CloudFormation performs a StackSet operation.

For more information about maximum concurrent accounts and failure tolerance, see [StackSet
 operation options](../UserGuide/stacksets-concepts.md#stackset-ops-options "../UserGuide/stacksets-concepts.md#stackset-ops-options").

###### Note


`StackSetOperationPreferences` don't apply to `AutoDeployment`, even
 if it's enabled.


## Contents





**ConcurrencyMode** 


Specifies how the concurrency level behaves during the operation execution.



* `STRICT_FAILURE_TOLERANCE`: This option dynamically lowers the concurrency
 level to ensure the number of failed accounts never exceeds the value of
 `FailureToleranceCount` +1. The initial actual concurrency is set to the lower of
 either the value of the `MaxConcurrentCount`, or the value of
 `FailureToleranceCount` +1. The actual concurrency is then reduced proportionally
 by the number of failures. This is the default behavior.


If failure tolerance or Maximum concurrent accounts are set to percentages, the behavior
 is similar.
* `SOFT_FAILURE_TOLERANCE`: This option decouples
 `FailureToleranceCount` from the actual concurrency. This allows StackSet
 operations to run at the concurrency level set by the `MaxConcurrentCount` value, or
 `MaxConcurrentPercentage`, regardless of the number of failures.

Type: String


Valid Values: `STRICT_FAILURE_TOLERANCE | SOFT_FAILURE_TOLERANCE`



Required: No




**FailureToleranceCount** 


The number of accounts per Region this operation can fail in before CloudFormation stops the
 operation in that Region. If the operation is stopped in a Region, CloudFormation doesn't attempt the
 operation in any subsequent Regions.


You can specify either `FailureToleranceCount` or
 `FailureTolerancePercentage`, but not both.


By default, `0` is specified.


Type: Integer


Valid Range: Minimum value of 0.


Required: No




**FailureTolerancePercentage** 


The percentage of accounts per Region this stack operation can fail in before CloudFormation
 stops the operation in that Region. If the operation is stopped in a Region, CloudFormation doesn't
 attempt the operation in any subsequent Regions.


When calculating the number of accounts based on the specified percentage, CloudFormation rounds
 *down* to the next whole number.


You can specify either `FailureToleranceCount` or
 `FailureTolerancePercentage`, but not both.


By default, `0` is specified.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 100.


Required: No




**MaxConcurrentCount** 


The maximum number of accounts in which to perform this operation at one time. This can
 depend on the value of `FailureToleranceCount` depending on your
 `ConcurrencyMode`. `MaxConcurrentCount` is at most one more than the
 `FailureToleranceCount` if you're using `STRICT_FAILURE_TOLERANCE`.


Note that this setting lets you specify the *maximum* for operations. For
 large deployments, under certain circumstances the actual number of accounts acted upon
 concurrently may be lower due to service throttling.


You can specify either `MaxConcurrentCount` or
 `MaxConcurrentPercentage`, but not both.


By default, `1` is specified.


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**MaxConcurrentPercentage** 


The maximum percentage of accounts in which to perform this operation at one time.


When calculating the number of accounts based on the specified percentage, CloudFormation rounds
 down to the next whole number. This is true except in cases where rounding down would result is
 zero. In this case, CloudFormation sets the number as one instead.


Note that this setting lets you specify the *maximum* for operations. For
 large deployments, under certain circumstances the actual number of accounts acted upon
 concurrently may be lower due to service throttling.


You can specify either `MaxConcurrentCount` or
 `MaxConcurrentPercentage`, but not both.


By default, `1` is specified.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 100.


Required: No




**RegionConcurrencyType** 


The concurrency type of deploying StackSets operations in Regions, could be in parallel or
 one Region at a time.


Type: String


Valid Values: `SEQUENTIAL | PARALLEL`



Required: No




**RegionOrder.member.N** 


The order of the Regions where you want to perform the stack operation.


Type: Array of strings


Pattern: `^[a-zA-Z0-9-]{1,128}$`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetOperationPreferences "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackSetOperationPreferences")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetOperationPreferences "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackSetOperationPreferences")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetOperationPreferences "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackSetOperationPreferences")
