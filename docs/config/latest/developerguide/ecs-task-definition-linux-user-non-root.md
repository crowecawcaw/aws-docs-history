

# ecs-task-definition-linux-user-non-root
<a name="ecs-task-definition-linux-user-non-root"></a>

Checks if the latest active revision of an Amazon ECS task definition configures Linux containers to run as non-root users.The rule is NON\_COMPLIANT if root user is specified or user configuration is absent for any container. 



**Identifier:** ECS\_TASK\_DEFINITION\_LINUX\_USER\_NON\_ROOT

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Taipei) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d675c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).