

# ecs-service-propagate-tags-enabled
<a name="ecs-service-propagate-tags-enabled"></a>

Checks if AWS ECS Service has property PropagateTags with value of either SERVICE or TASK\_DEFINITION. The rule is NON\_COMPLIANT if the property does not exist or is NONE. 



**Identifier:** ECS\_SERVICE\_PROPAGATE\_TAGS\_ENABLED

**Resource Types:** AWS::ECS::Service

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d671c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).