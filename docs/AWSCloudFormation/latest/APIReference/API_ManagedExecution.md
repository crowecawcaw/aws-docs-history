# ManagedExecution

Describes whether StackSets performs non-conflicting operations concurrently and queues
 conflicting operations.


## Contents





**Active** 


When `true`, CloudFormation performs non-conflicting operations concurrently and
 queues conflicting operations. After conflicting operations finish, CloudFormation starts queued
 operations in request order.


###### Note

If there are already running or queued operations, CloudFormation queues all incoming
 operations even if they are non-conflicting.

You can't modify your StackSet's execution configuration while there are running or queued
 operations for that StackSet.


When `false` (default), StackSets performs one operation at a time in request
 order.


Type: Boolean


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ManagedExecution "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ManagedExecution")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ManagedExecution "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ManagedExecution")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ManagedExecution "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ManagedExecution")
