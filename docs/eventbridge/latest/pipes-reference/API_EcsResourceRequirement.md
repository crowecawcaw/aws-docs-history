# EcsResourceRequirement

The type and amount of a resource to assign to a container. The supported resource types
are GPUs and Elastic Inference accelerators. For more information, see [Working with
GPUs on Amazon ECS](../../../AmazonECS/latest/developerguide/ecs-gpu.md "../../../AmazonECS/latest/developerguide/ecs-gpu.md") or [Working with Amazon Elastic
Inference on Amazon ECS](../../../AmazonECS/latest/developerguide/ecs-inference.md "../../../AmazonECS/latest/developerguide/ecs-inference.md") in the _Amazon Elastic Container Service
Developer Guide_

## Contents

**type**

The type of resource to assign to a container. The supported values are `GPU`
or `InferenceAccelerator`.

Type: String

Valid Values: `GPU | InferenceAccelerator`

Required: Yes

**value**

The value for the specified resource type.

If the `GPU` type is used, the value is the number of physical
`GPUs` the Amazon ECS container agent reserves for the container. The
number of GPUs that's reserved for all containers in a task can't exceed the number of
available GPUs on the container instance that the task is launched on.

If the `InferenceAccelerator` type is used, the `value` matches
the `deviceName` for an InferenceAccelerator specified in a task
definition.

Type: String

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/EcsResourceRequirement.md "../../../goto/SdkForCpp/pipes-2015-10-07/EcsResourceRequirement.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/EcsResourceRequirement.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/EcsResourceRequirement.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/EcsResourceRequirement.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/EcsResourceRequirement.md")
