# RollbackConfiguration

Structure that contains the rollback triggers for CloudFormation to monitor during stack
 creation and updating operations, and for the specified monitoring period afterwards.

Rollback triggers enable you to have CloudFormation monitor the state of your application during
 stack creation and updating, and to roll back that operation if the application breaches the
 threshold of any of the alarms you've specified. For more information, see [Roll back your CloudFormation stack on alarm breach with rollback triggers](../UserGuide/using-cfn-rollback-triggers.md "../UserGuide/using-cfn-rollback-triggers.md").


## Contents





**MonitoringTimeInMinutes** 


The amount of time, in minutes, during which CloudFormation should monitor all the rollback
 triggers after the stack creation or update operation deploys all necessary resources.


The default is 0 minutes.


If you specify a monitoring period but don't specify any rollback triggers, CloudFormation still
 waits the specified period of time before cleaning up old resources after update operations. You
 can use this monitoring period to perform any manual stack validation desired, and manually
 cancel the stack creation or update (using [CancelUpdateStack](API_CancelUpdateStack.md "API_CancelUpdateStack.md"), for example) as necessary.


If you specify 0 for this parameter, CloudFormation still monitors the specified rollback
 triggers during stack creation and update operations. Then, for update operations, it begins
 disposing of old resources immediately once the operation completes.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 180.


Required: No




**RollbackTriggers.member.N** 


The triggers to monitor during stack creation or update actions.


By default, CloudFormation saves the rollback triggers specified for a stack and applies them to
 any subsequent update operations for the stack, unless you specify otherwise. If you do specify
 rollback triggers for this parameter, those triggers replace any list of triggers previously
 specified for the stack. This means:



* To use the rollback triggers previously specified for this stack, if any, don't specify
 this parameter.
* To specify new or updated rollback triggers, you must specify *all* the
 triggers that you want used for this stack, even triggers you've specified before (for example,
 when creating the stack or during a previous stack update). Any triggers that you don't include
 in the updated list of triggers are no longer applied to the stack.
* To remove all currently specified triggers, specify an empty list for this
 parameter.

If a specified trigger is missing, the entire stack operation fails and is rolled
 back.


Type: Array of [RollbackTrigger](API_RollbackTrigger.md "API_RollbackTrigger.md") objects


Array Members: Maximum number of 5 items.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RollbackConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RollbackConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RollbackConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RollbackConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RollbackConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RollbackConfiguration")
