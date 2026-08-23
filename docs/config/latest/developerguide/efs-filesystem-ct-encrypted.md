# efs-filesystem-ct-encrypted

Checks if Amazon Elastic File System (Amazon EFS) encrypts data with AWS Key Management Service (AWS KMS). The rule is NON\_COMPLIANT if a file system is not encrypted. Optionally, you can check if a file system is not encrypted with specified KMS keys.

**Identifier:** EFS\_FILESYSTEM\_CT\_ENCRYPTED

**Resource Types:** AWS::EFS::FileSystem

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Israel (Tel Aviv), Canada West (Calgary) Region

**Parameters:**

kmsKeyArns (Optional)
Type: String

(Optional) Comma-separated list of Amazon Resource Names (ARNs) for AWS KMS keys. If provided, the rule checks if the specified KMS keys do not encrypt an Amazon EFS file system.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
