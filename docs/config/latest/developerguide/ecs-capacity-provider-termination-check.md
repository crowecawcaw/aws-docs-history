# ecs-capacity-provider-termination-check

Checks if an Amazon ECS Capacity provider containing Auto Scaling groups has managed termination protection enabled. This rule is NON\_COMPLIANT if managed termination protection is disabled on the ECS Capacity Provider.

**Identifier:** ECS\_CAPACITY\_PROVIDER\_TERMINATION\_CHECK

**Resource Types:** AWS::ECS::CapacityProvider

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Malaysia), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
