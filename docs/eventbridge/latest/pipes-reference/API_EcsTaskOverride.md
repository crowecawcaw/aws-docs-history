

# EcsTaskOverride
<a name="API_EcsTaskOverride"></a>

The overrides that are associated with a task.

## Contents
<a name="API_EcsTaskOverride_Contents"></a>

 ** ContainerOverrides **   <a name="eventbridge-Type-EcsTaskOverride-ContainerOverrides"></a>
One or more container overrides that are sent to a task.  
Type: Array of [EcsContainerOverride](API_EcsContainerOverride.md) objects  
Required: No

 ** Cpu **   <a name="eventbridge-Type-EcsTaskOverride-Cpu"></a>
The cpu override for the task.  
Type: String  
Required: No

 ** EphemeralStorage **   <a name="eventbridge-Type-EcsTaskOverride-EphemeralStorage"></a>
The ephemeral storage setting override for the task.  
This parameter is only supported for tasks hosted on Fargate that use the following platform versions:  
+ Linux platform version `1.4.0` or later.
+ Windows platform version `1.0.0` or later.
Type: [EcsEphemeralStorage](API_EcsEphemeralStorage.md) object  
Required: No

 ** ExecutionRoleArn **   <a name="eventbridge-Type-EcsTaskOverride-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the task execution IAM role override for the task. For more information, see [Amazon ECS task execution IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html) in the *Amazon Elastic Container Service Developer Guide*.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`   
Required: No

 ** InferenceAcceleratorOverrides **   <a name="eventbridge-Type-EcsTaskOverride-InferenceAcceleratorOverrides"></a>
The Elastic Inference accelerator override for the task.  
Type: Array of [EcsInferenceAcceleratorOverride](API_EcsInferenceAcceleratorOverride.md) objects  
Required: No

 ** Memory **   <a name="eventbridge-Type-EcsTaskOverride-Memory"></a>
The memory override for the task.  
Type: String  
Required: No

 ** TaskRoleArn **   <a name="eventbridge-Type-EcsTaskOverride-TaskRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see [IAM Role for Tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`   
Required: No

## See Also
<a name="API_EcsTaskOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/EcsTaskOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/EcsTaskOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/EcsTaskOverride) 