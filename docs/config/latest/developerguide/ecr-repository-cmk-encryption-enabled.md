

# ecr-repository-cmk-encryption-enabled
<a name="ecr-repository-cmk-encryption-enabled"></a>

Checks if ECR repository is encrypted at rest using customer-managed KMS key. This rule is NON\_COMPLIANT if the repository is encrypted using AES256 or the default KMS key ('aws/ecr'). 



**Identifier:** ECR\_REPOSITORY\_CMK\_ENCRYPTION\_ENABLED

**Resource Types:** AWS::ECR::Repository

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Malaysia), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

kmsKeyArns (Optional)Type: CSV  
Comma-separated list of KMS key Amazon Resource Names (ARNs) intended to encrypt the ECR repository.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d651c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).