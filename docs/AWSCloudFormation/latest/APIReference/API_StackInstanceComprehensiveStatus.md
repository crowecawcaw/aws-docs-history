# StackInstanceComprehensiveStatus

The detailed status of the stack instance.


## Contents





**DetailedStatus** 



* `CANCELLED`: The operation in the specified account and Region has been
 canceled. This is either because a user has stopped the StackSet operation, or because the
 failure tolerance of the StackSet operation has been exceeded.
* `FAILED`: The operation in the specified account and Region failed. If the
 StackSet operation fails in enough accounts within a Region, the failure tolerance for the
 StackSet operation as a whole might be exceeded.
* `FAILED_IMPORT`: The import of the stack instance in the specified account and
 Region failed and left the stack in an unstable state. Once the issues causing the failure are
 fixed, the import operation can be retried. If enough StackSet operations fail in enough
 accounts within a Region, the failure tolerance for the StackSet operation as a whole might be
 exceeded.
* `INOPERABLE`: A `DeleteStackInstances` operation has failed and left
 the stack in an unstable state. Stacks in this state are excluded from further
 `UpdateStackSet` operations. You might need to perform a
 `DeleteStackInstances` operation, with `RetainStacks` set to
 `true`, to delete the stack instance, and then delete the stack manually.
* `PENDING`: The operation in the specified account and Region has yet to
 start.
* `RUNNING`: The operation in the specified account and Region is currently in
 progress.
* `SKIPPED_SUSPENDED_ACCOUNT`: The operation in the specified account and Region
 has been skipped because the account was suspended at the time of the operation.
* `SUCCEEDED`: The operation in the specified account and Region completed
 successfully.

Type: String


Valid Values: `PENDING | RUNNING | SUCCEEDED | FAILED | CANCELLED | INOPERABLE | SKIPPED_SUSPENDED_ACCOUNT | FAILED_IMPORT`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackInstanceComprehensiveStatus "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackInstanceComprehensiveStatus")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackInstanceComprehensiveStatus "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackInstanceComprehensiveStatus")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackInstanceComprehensiveStatus "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackInstanceComprehensiveStatus")
