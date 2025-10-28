# EcsInferenceAcceleratorOverride

Details on an Elastic Inference accelerator task override. This parameter is used to
override the Elastic Inference accelerator specified in the task definition. For more
information, see [Working with Amazon Elastic
Inference on Amazon ECS](../../../AmazonECS/latest/userguide/ecs-inference.md "../../../AmazonECS/latest/userguide/ecs-inference.md") in the _Amazon Elastic Container Service
Developer Guide_.

## Contents

**deviceName**

The Elastic Inference accelerator device name to override for the task. This parameter
must match a `deviceName` specified in the task definition.

Type: String

Required: No

**deviceType**

The Elastic Inference accelerator type to use.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/EcsInferenceAcceleratorOverride.md "../../../goto/SdkForCpp/pipes-2015-10-07/EcsInferenceAcceleratorOverride.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/EcsInferenceAcceleratorOverride.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/EcsInferenceAcceleratorOverride.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/EcsInferenceAcceleratorOverride.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/EcsInferenceAcceleratorOverride.md")
