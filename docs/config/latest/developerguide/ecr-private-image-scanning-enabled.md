# ecr-private-image-scanning-enabled

Checks if a private Amazon Elastic Container Registry (Amazon ECR) repository has image scanning enabled.
The rule is NON_COMPLIANT if the private Amazon ECR repository's scan frequency is not on scan on push or continuous scan.
For more information on enabling image scanning, see [Image scanning](../../../AmazonECR/latest/userguide/image-scanning.md "../../../AmazonECR/latest/userguide/image-scanning.md") in the _Amazon ECR User Guide_.

**Identifier:** ECR_PRIVATE_IMAGE_SCANNING_ENABLED

**Resource Types:** AWS::ECR::Repository

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
