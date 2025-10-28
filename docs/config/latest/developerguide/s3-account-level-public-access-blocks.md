# s3-account-level-public-access-blocks

Checks if the required public access block settings are configured from account level. The rule is only NON_COMPLIANT when the fields set below do not match the corresponding fields in the configuration item.

###### Note

If you are using this rule, ensure that S3 Block Public Access is enabled. The rule is change-triggered, so it will not be invoked unless S3 Block Public Access is enabled. If S3 Block Public Access is not enabled the rule returns INSUFFICIENT_DATA. This means that you still might have some public buckets.
For more information about setting up S3 Block Public Access, see [Blocking public access to your Amazon S3 storage](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md").

**Identifier:** S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS

**Resource Types:** AWS::S3::AccountPublicAccessBlock

**Trigger type:** Configuration changes (current status not checked, only evaluated when changes generate new events)

###### Note

This rule is only triggered by configuration changes for the specific region where the S3 endpoint is located.
In all other regions, the rule is checked periodically.
If a change was made in another region,
there could be a delay before the rule returns NON_COMPLIANT.

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), AWS Secret - West, Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

IgnorePublicAcls (Optional)
Type: String
Default: True

IgnorePublicAcls is enforced or not, default True

BlockPublicPolicy (Optional)
Type: String
Default: True

BlockPublicPolicy is enforced or not, default True

BlockPublicAcls (Optional)
Type: String
Default: True

BlockPublicAcls is enforced or not, default True

RestrictPublicBuckets (Optional)
Type: String
Default: True

RestrictPublicBuckets is enforced or not, default True

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
