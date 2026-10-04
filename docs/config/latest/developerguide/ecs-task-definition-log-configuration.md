

# ecs-task-definition-log-configuration
<a name="ecs-task-definition-log-configuration"></a>

Checks if logConfiguration is set on active ECS Task Definitions. This rule is NON\_COMPLIANT if an active ECSTaskDefinition does not have the logConfiguration resource defined or the value for logConfiguration is null in at least one container definition. 

**Note**  
This rule only evaluates the latest active revision of an Amazon ECS task definition.

**Identifier:** ECS\_TASK\_DEFINITION\_LOG\_CONFIGURATION

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS GovCloud (US-East), AWS GovCloud (US-West) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d677c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).