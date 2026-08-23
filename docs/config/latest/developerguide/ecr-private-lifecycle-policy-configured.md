# ecr-private-lifecycle-policy-configured

Checks if a private Amazon Elastic Container Registry (ECR) repository has at least one lifecycle policy configured. The rule is NON\_COMPLIANT if no lifecycle policy is configured for the ECR private repository.

**Identifier:** ECR\_PRIVATE\_LIFECYCLE\_POLICY\_CONFIGURED

**Resource Types:** AWS::ECR::Repository

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Israel (Tel Aviv) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
