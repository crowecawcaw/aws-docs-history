# PipeTargetEcsTaskParameters

The parameters for using an Amazon ECS task as a target.

## Contents

**TaskDefinitionArn**

The ARN of the task definition to use if the event target is an Amazon ECS task.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`

Required: Yes

**CapacityProviderStrategy**

The capacity provider strategy to use for the task.

If a `capacityProviderStrategy` is specified, the `launchType`
parameter must be omitted. If no `capacityProviderStrategy` or launchType is
specified, the `defaultCapacityProviderStrategy` for the cluster is used.

Type: Array of [CapacityProviderStrategyItem](API_CapacityProviderStrategyItem.md "API_CapacityProviderStrategyItem.md") objects

Array Members: Minimum number of 0 items. Maximum number of 6 items.

Required: No

**EnableECSManagedTags**

Specifies whether to enable Amazon ECS managed tags for the task. For more
information, see [Tagging Your Amazon ECS Resources](../../../AmazonECS/latest/developerguide/ecs-using-tags.md "../../../AmazonECS/latest/developerguide/ecs-using-tags.md") in the Amazon Elastic Container Service Developer Guide.

Type: Boolean

Required: No

**EnableExecuteCommand**

Whether or not to enable the execute command functionality for the containers in this
task. If true, this enables execute command functionality on all containers in the
task.

Type: Boolean

Required: No

**Group**

Specifies an Amazon ECS task group for the task. The maximum length is 255
characters.

Type: String

Required: No

**LaunchType**

Specifies the launch type on which your task is running. The launch type that you
specify here must match one of the launch type (compatibilities) of the target task. The
`FARGATE` value is supported only in the Regions where AWS Fargate with Amazon ECS is supported. For more information, see
[AWS Fargate on Amazon ECS](../../../AmazonECS/latest/developerguide/AWS-Fargate.md "../../../AmazonECS/latest/developerguide/AWS-Fargate.md") in the _Amazon Elastic Container Service Developer Guide_.

Type: String

Valid Values: `EC2 | FARGATE | EXTERNAL`

Required: No

**NetworkConfiguration**

Use this structure if the Amazon ECS task uses the `awsvpc` network
mode. This structure specifies the VPC subnets and security groups associated with the
task, and whether a public IP address is to be used. This structure is required if
`LaunchType` is `FARGATE` because the `awsvpc` mode is
required for Fargate tasks.

If you specify `NetworkConfiguration` when the target ECS task does not use
the `awsvpc` network mode, the task fails.

Type: [NetworkConfiguration](API_NetworkConfiguration.md "API_NetworkConfiguration.md") object

Required: No

**Overrides**

The overrides that are associated with a task.

Type: [EcsTaskOverride](API_EcsTaskOverride.md "API_EcsTaskOverride.md") object

Required: No

**PlacementConstraints**

An array of placement constraint objects to use for the task. You can specify up to 10
constraints per task (including constraints in the task definition and those specified at
runtime).

Type: Array of [PlacementConstraint](API_PlacementConstraint.md "API_PlacementConstraint.md") objects

Array Members: Minimum number of 0 items. Maximum number of 10 items.

Required: No

**PlacementStrategy**

The placement strategy objects to use for the task. You can specify a maximum of five
strategy rules per task.

Type: Array of [PlacementStrategy](API_PlacementStrategy.md "API_PlacementStrategy.md") objects

Array Members: Minimum number of 0 items. Maximum number of 5 items.

Required: No

**PlatformVersion**

Specifies the platform version for the task. Specify only the numeric portion of the
platform version, such as `1.1.0`.

This structure is used only if `LaunchType` is `FARGATE`. For more
information about valid platform versions, see [AWS Fargate
Platform Versions](../../../AmazonECS/latest/developerguide/platform_versions.md "../../../AmazonECS/latest/developerguide/platform_versions.md") in the _Amazon Elastic Container Service Developer
Guide_.

Type: String

Required: No

**PropagateTags**

Specifies whether to propagate the tags from the task definition to the task. If no
value is specified, the tags are not propagated. Tags can only be propagated to the task
during task creation. To add tags to a task after task creation, use the
`TagResource` API action.

Type: String

Valid Values: `TASK_DEFINITION`

Required: No

**ReferenceId**

The reference ID to use for the task.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Required: No

**Tags**

The metadata that you apply to the task to help you categorize and organize them. Each
tag consists of a key and an optional value, both of which you define. To learn more, see
[RunTask](../../../AmazonECS/latest/APIReference/API_RunTask.md#ECS-RunTask-request-tags "../../../AmazonECS/latest/APIReference/API_RunTask.md#ECS-RunTask-request-tags") in the Amazon ECS API Reference.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Required: No

**TaskCount**

The number of tasks to create based on `TaskDefinition`. The default is

1.

Type: Integer

Valid Range: Minimum value of 1.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetEcsTaskParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetEcsTaskParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetEcsTaskParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetEcsTaskParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetEcsTaskParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetEcsTaskParameters.md")
