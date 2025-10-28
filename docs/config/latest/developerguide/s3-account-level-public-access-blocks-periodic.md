# s3-account-level-public-access-blocks-periodic

Checks if the required public access block settings are configured at the account level. The rule is NON_COMPLIANT if the configuration item does not match one or more settings from parameters (or default).

**Identifier:** S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS_PERIODIC

**Resource Types:** AWS::::Account

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

IgnorePublicAcls (Optional)
Type: String

IgnorePublicAcls is enforced or not, default True

BlockPublicPolicy (Optional)
Type: String

BlockPublicPolicy is enforced or not, default True

BlockPublicAcls (Optional)
Type: String

BlockPublicAcls is enforced or not, default True

RestrictPublicBuckets (Optional)
Type: String

RestrictPublicBuckets is enforced or not, default True

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
