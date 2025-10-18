# RollbackTrigger

A rollback trigger CloudFormation monitors during creation and updating of stacks. If any of the
 alarms you specify goes to ALARM state during the stack operation or within the specified
 monitoring period afterwards, CloudFormation rolls back the entire stack operation.


## Contents





**Arn** 


The Amazon Resource Name (ARN) of the rollback trigger.


If a specified trigger is missing, the entire stack operation fails and is rolled
 back.


Type: String


Required: Yes




**Type** 


The resource type of the rollback trigger. Specify either [AWS::CloudWatch::Alarm](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-alarm.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-alarm.html") or [AWS::CloudWatch::CompositeAlarm](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-compositealarm.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-compositealarm.html") resource types.


Type: String


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RollbackTrigger "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RollbackTrigger")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RollbackTrigger "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RollbackTrigger")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RollbackTrigger "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RollbackTrigger")
