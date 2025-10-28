# EcsTaskOverride

The overrides that are associated with a task.

## Contents

**ContainerOverrides**

One or more container overrides that are sent to a task.

Type: Array of [EcsContainerOverride](API_EcsContainerOverride.md "API_EcsContainerOverride.md") objects

Required: No

**Cpu**

The cpu override for the task.

Type: String

Required: No

**EphemeralStorage**

The ephemeral storage setting override for the task.

###### Note

This parameter is only supported for tasks hosted on Fargate that use
the following platform versions:

- Linux platform version `1.4.0` or later.
- Windows platform version `1.0.0` or later.

Type: [EcsEphemeralStorage](API_EcsEphemeralStorage.md "API_EcsEphemeralStorage.md") object

Required: No

**ExecutionRoleArn**

The Amazon Resource Name (ARN) of the task execution IAM role override for the task. For
more information, see [Amazon ECS
task execution IAM role](../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md "../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md") in the _Amazon Elastic Container Service Developer
Guide_.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`

Required: No

**InferenceAcceleratorOverrides**

The Elastic Inference accelerator override for the task.

Type: Array of [EcsInferenceAcceleratorOverride](API_EcsInferenceAcceleratorOverride.md "API_EcsInferenceAcceleratorOverride.md") objects

Required: No

**Memory**

The memory override for the task.

Type: String

Required: No

**TaskRoleArn**

The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume.
All containers in this task are granted the permissions that are specified in this role.
For more information, see [IAM Role for Tasks](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md") in
the _Amazon Elastic Container Service Developer Guide_.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/EcsTaskOverride.md "../../../goto/SdkForCpp/pipes-2015-10-07/EcsTaskOverride.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/EcsTaskOverride.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/EcsTaskOverride.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/EcsTaskOverride.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/EcsTaskOverride.md")
