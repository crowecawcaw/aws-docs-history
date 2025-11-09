# s3-bucket-policy-not-more-permissive

Checks if your Amazon Simple Storage Service bucket policies do not allow other inter-account permissions than the control Amazon S3 bucket policy that you provide.

###### Note

If you provide an invalid parameter value, you will see the following error: Value for controlPolicy parameter must be an Amazon S3 bucket policy.

**Identifier:** S3_BUCKET_POLICY_NOT_MORE_PERMISSIVE

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West Region

**Parameters:**

controlPolicy
Type: String

Amazon S3 bucket policy that defines an upper bound on the permissions of your S3 buckets. The policy can be a maximum of 1024 characters long.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
