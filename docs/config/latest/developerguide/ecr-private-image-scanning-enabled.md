

# ecr-private-image-scanning-enabled
<a name="ecr-private-image-scanning-enabled"></a>

Checks if a private Amazon Elastic Container Registry (Amazon ECR) repository has image scanning enabled. The rule is NON\_COMPLIANT if the private Amazon ECR repository's scan frequency is not on scan on push or continuous scan. For more information on enabling image scanning, see [Image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) in the *Amazon ECR User Guide*.



**Identifier:** ECR\_PRIVATE\_IMAGE\_SCANNING\_ENABLED

**Resource Types:** AWS::ECR::Repository

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d645c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).