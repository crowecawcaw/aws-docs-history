

# s3-directory-bucket-lifecycle-policy-rule-check
<a name="s3-directory-bucket-lifecycle-policy-rule-check"></a>

Checks if directory buckets for Amazon S3 have a lifecycle policy with at least one enabled rule. The rule is NON\_COMPLIANT if there are no lifecycle policy rules or if none of the lifecycle policy rules have status Enabled. 



**Identifier:** S3\_DIRECTORY\_BUCKET\_LIFECYCLE\_POLICY\_RULE\_CHECK

**Resource Types:** AWS::S3Express::DirectoryBucket

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Asia Pacific (Mumbai), US East (Ohio), Europe (Ireland), US East (N. Virginia), Asia Pacific (Tokyo), US West (Oregon) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1419c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).