

# ecs-task-definition-efs-encryption-enabled
<a name="ecs-task-definition-efs-encryption-enabled"></a>

Checks if Amazon ECS Task Definitions with EFS volumes have in-transit encryption enabled. The rule is NON\_COMPLIANT if an ECS Task Definition contains an EFS volume without transit encryption enabled. 



**Identifier:** ECS\_TASK\_DEFINITION\_EFS\_ENCRYPTION\_ENABLED

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d673c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).