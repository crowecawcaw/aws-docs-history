# ecs-task-definition-efs-encryption-enabled

Checks if Amazon ECS Task Definitions with EFS volumes have in-transit encryption enabled. The rule is NON_COMPLIANT if an ECS Task Definition contains an EFS volume without transit encryption enabled.

**Identifier:** ECS_TASK_DEFINITION_EFS_ENCRYPTION_ENABLED

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
