# s3-resources-in-logically-air-gapped-vault

Checks if Amazon Simple Storage Service (Amazon S3) buckets are in a logically air-gapped vault. The rule is NON_COMPLIANT if an Amazon S3 bucket is not in a logically air-gapped vault within the specified time period.

**Identifier:** S3_RESOURCES_IN_LOGICALLY_AIR_GAPPED_VAULT

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Periodic

**AWS Region:** Only available in Europe (Stockholm), Middle East (Bahrain), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

resourceTags (Optional)
Type: String

Tags of Amazon S3 bucket for the rule to check, in JSON format.

resourceId (Optional)
Type: String

Name of Amazon S3 bucket for the rule to check.

recoveryPointAgeValue (Optional)
Type: int
Default: 1

Numerical value for maximum allowed age. No more than 2184 for hours, 91 for days.

recoveryPointAgeUnit (Optional)
Type: String
Default: days

Unit of time for maximum allowed age. Accepted values: 'hours', 'days'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
