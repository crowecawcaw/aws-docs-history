# s3-bucket-acl-prohibited

Checks if Amazon Simple Storage Service (Amazon S3) Buckets allow user permissions through access control lists (ACLs). The rule is NON\_COMPLIANT if ACLs are configured for user access in Amazon S3 Buckets.

**Identifier:** S3\_BUCKET\_ACL\_PROHIBITED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
