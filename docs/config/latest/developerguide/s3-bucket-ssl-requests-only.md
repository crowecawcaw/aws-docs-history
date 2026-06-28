# s3-bucket-ssl-requests-only

Checks if S3 buckets have policies that require requests to use SSL/TLS. The rule is NON\_COMPLIANT if any S3 bucket has policies allowing HTTP requests.

**Identifier:** S3\_BUCKET\_SSL\_REQUESTS\_ONLY

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
