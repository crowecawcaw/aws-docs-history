

# EcsInferenceAcceleratorOverride
<a name="API_EcsInferenceAcceleratorOverride"></a>

Details on an Elastic Inference accelerator task override. This parameter is used to override the Elastic Inference accelerator specified in the task definition. For more information, see [Working with Amazon Elastic Inference on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/userguide/ecs-inference.html) in the *Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_EcsInferenceAcceleratorOverride_Contents"></a>

 ** deviceName **   <a name="eventbridge-Type-EcsInferenceAcceleratorOverride-deviceName"></a>
The Elastic Inference accelerator device name to override for the task. This parameter must match a `deviceName` specified in the task definition.  
Type: String  
Required: No

 ** deviceType **   <a name="eventbridge-Type-EcsInferenceAcceleratorOverride-deviceType"></a>
The Elastic Inference accelerator type to use.  
Type: String  
Required: No

## See Also
<a name="API_EcsInferenceAcceleratorOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/EcsInferenceAcceleratorOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/EcsInferenceAcceleratorOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/EcsInferenceAcceleratorOverride) 