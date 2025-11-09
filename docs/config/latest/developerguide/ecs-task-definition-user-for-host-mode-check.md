# ecs-task-definition-user-for-host-mode-check

Checks if Amazon ECS task definitions with host network mode have privileged OR nonroot in the container definition. The rule is NON_COMPLIANT if the latest active revision of a task definition has privileged=false (or is null) AND user=root (or is null).

###### Important

**Only one condition needs to be met for the rule to return compliant**

The rule is COMPLIANT in any of following scenarios:

- If the network mode is not set to host,
- If the latest active revision of a task definition has privileged=true,
- If the latest active revision of a task definition has a user that is not the root.
  This means that only one of these conditions need to be met for the rule to return compliant.
  To check specifically if a task definition has privileged=true, see [ecs-containers-nonprivileged](ecs-containers-nonprivileged.md "ecs-containers-nonprivileged.md").
  To check specifically if a task definition has a user that is not the root, see [ecs-task-definition-nonroot-user](ecs-task-definition-nonroot-user.md "ecs-task-definition-nonroot-user.md").

**Identifier:** ECS_TASK_DEFINITION_USER_FOR_HOST_MODE_CHECK

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

SkipInactiveTaskDefinitions (Optional)
Type: boolean

Boolean flag to not check INACTIVE Amazon EC2 task definitions. If set to 'true', the rule won't evaluate INACTIVE Amazon EC2 task definitions. If set to 'false', the rule will evaluate the latest revision of INACTIVE Amazon EC2 task definitions.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
