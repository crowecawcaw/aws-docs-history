

# s3-account-level-public-access-blocks-periodic
<a name="s3-account-level-public-access-blocks-periodic"></a>

Checks if the required public access block settings are configured at the account level. The rule is NON\_COMPLIANT if the configuration item does not match one or more settings from parameters (or default). 



**Identifier:** S3\_ACCOUNT\_LEVEL\_PUBLIC\_ACCESS\_BLOCKS\_PERIODIC

**Resource Types:** AWS::::Account

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

IgnorePublicAcls (Optional)Type: String  
IgnorePublicAcls is enforced or not, default True

BlockPublicPolicy (Optional)Type: String  
BlockPublicPolicy is enforced or not, default True

BlockPublicAcls (Optional)Type: String  
BlockPublicAcls is enforced or not, default True

RestrictPublicBuckets (Optional)Type: String  
RestrictPublicBuckets is enforced or not, default True

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1383c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).