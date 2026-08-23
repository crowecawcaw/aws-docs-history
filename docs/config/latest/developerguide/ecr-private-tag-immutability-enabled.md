# ecr-private-tag-immutability-enabled

Checks if a private Amazon Elastic Container Registry (ECR) repository has tag immutability enabled. This rule is NON\_COMPLIANT if tag immutability is not enabled for the private ECR repository.

**Identifier:** ECR\_PRIVATE\_TAG\_IMMUTABILITY\_ENABLED

**Resource Types:** AWS::ECR::Repository

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Malaysia), Israel (Tel Aviv), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
