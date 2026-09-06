

# EcsResourceRequirement
<a name="API_EcsResourceRequirement"></a>

The type and amount of a resource to assign to a container. The supported resource types are GPUs and Elastic Inference accelerators. For more information, see [Working with GPUs on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html) or [Working with Amazon Elastic Inference on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-inference.html) in the *Amazon Elastic Container Service Developer Guide* 

## Contents
<a name="API_EcsResourceRequirement_Contents"></a>

 ** type **   <a name="eventbridge-Type-EcsResourceRequirement-type"></a>
The type of resource to assign to a container. The supported values are `GPU` or `InferenceAccelerator`.  
Type: String  
Valid Values: `GPU | InferenceAccelerator`   
Required: Yes

 ** value **   <a name="eventbridge-Type-EcsResourceRequirement-value"></a>
The value for the specified resource type.  
If the `GPU` type is used, the value is the number of physical `GPUs` the Amazon ECS container agent reserves for the container. The number of GPUs that's reserved for all containers in a task can't exceed the number of available GPUs on the container instance that the task is launched on.  
If the `InferenceAccelerator` type is used, the `value` matches the `deviceName` for an InferenceAccelerator specified in a task definition.  
Type: String  
Required: Yes

## See Also
<a name="API_EcsResourceRequirement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/EcsResourceRequirement) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/EcsResourceRequirement) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/EcsResourceRequirement) 