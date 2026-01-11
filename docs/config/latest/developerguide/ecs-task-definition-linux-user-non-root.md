# ecs-task-definition-linux-user-non-root

Checks if the latest active revision of an Amazon ECS task definition configures Linux containers to run as non-root users.The rule is NON_COMPLIANT if root user is specified or user configuration is absent for any container.

**Identifier:** ECS_TASK_DEFINITION_LINUX_USER_NON_ROOT

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
