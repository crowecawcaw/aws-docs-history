# `AWS-ECSRunTask`

**Description**

The `AWS-ECSRunTask` runbook runs the Amazon Elastic Container Service (Amazon ECS) task that you
specify.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ECSRunTask "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ECSRunTask")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- capacityProviderStrategy

Type: String

Description: (Optional) The capacity provider strategy to use for the
task.

- cluster

Type: String

Description: (Optional) The short name or ARN of the cluster to run your
task on. If you do not specify a cluster, the default cluster is
used.

- count

Type: String

Description: (Optional) The number of instantiations of the specified task
to place on your cluster. You can specify up to 10 tasks for each
request.

- enableECSManagedTags

Type: Boolean

Description: (Optional) Specifies whether to use Amazon ECS managed tags for
the task. For more information, see [Tagging your
Amazon ECS resources](../../../AmazonECS/latest/developerguide/ecs-using-tags.md "../../../AmazonECS/latest/developerguide/ecs-using-tags.md") in the
_Amazon Elastic Container Service Developer Guide_.

- enableExecuteCommand

Type: Boolean

Description: (Optional) Determines whether to activate the execute command
functionality for the containers in this task. If true, this activates
execute command functionality on all containers in the task.

- group

Type: String

Description: (Optional) The name of the task group to associate with the
task. The default value is the family name of the task definition. For
example, `family:my-family-name`.

- launchType

Type: String

Valid values: EC2 | FARGATE | EXTERNAL

Description: (Optional) The infrastructure to run your standalone task
on.

- networkConfiguration

Type: String

Description: (Optional) The network configuration for the task. This
parameter is required for task definitions that use the `awsvpc`
network mode to receive their own elastic network interface, and it isn't
supported for other network modes.

- overrides

Type: String

Description: (Optional) A list of container overrides in JSON format that
specify the name of a container in the specified task definition and the
overrides it should receive. You can override the default command for a
container that's specified in the task definition or Docker image with a
command override. You can also override existing environment variables that
are specified in the task definition or Docker image on a container.
Additionally, you can add new environment variables with an environment
override.

- placementConstraints

Type: String

Description: (Optional) An array of placement constraint objects to use
for the task. You can specify up to 10 constraints for each task including
constraints in the task definition and those specified at runtime.

- placementStrategy

Type: String

Description: (Optional) The placement strategy objects to use for the
task. You can specify a maximum of 5 strategy rules for each task.

- platformVersion

Type: String

Description: (Optional) The platform version that the task uses. A
platform version is only specified for tasks hosted on Fargate. If a
platform version isn't specified, the `LATEST` platform version
is used.

- propagateTags

Type: String

Description: (Optional) Determines whether tags propagate from the task
definition to the task. If no value is specified, the tags aren't
propagated. Tags can only be propagated to the task during task
creation.

- referenceId

Type: String

Description: (Optional) The reference ID to use for the task. The
reference ID can have a maximum length of 1024 characters.

- startedBy

Type: String

Description: (Optional) An optional tag specified when a task is started.
This helps you identify which tasks belong to a specific job by filtering
the results of a `ListTasks` API operation. Up to 36 letters
(uppercase and lowercase), numbers, hyphens (-), and underscores (\_) are
allowed.

- tags

Type: String

Description: (Optional) Metadata that you want to apply to the task to
help you categorize and organize tasks. Each tag consists of a user-defined
key and value.

- taskDefinition

Type: String

Description: (Optional) The `family` and `revision`
(`family`:`revision`) or full ARN of the task
definition to run. If a revision isn't specified, the latest
`ACTIVE` revision is used.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ecs:RunTask`

**Document Steps**

`aws:executeScript` - Runs the Amazon ECS task based on the values that you
specify for the runbook input parameters.
