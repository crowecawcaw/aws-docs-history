

# s3-bucket-server-side-encryption-enabled
<a name="s3-bucket-server-side-encryption-enabled"></a>

Checks if your Amazon S3 bucket either has the Amazon S3 default encryption enabled or that the Amazon S3 bucket policy explicitly denies `put-object` requests without server side encryption that uses AES-256 or AWS Key Management Service. The rule is NON\_COMPLIANT if your Amazon S3 bucket is not encrypted by default.

**Note**  
If a single value in an S3 bucket policy (for example, one Resource or Condition value) contains more than five IAM [policy variables](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html#policy-vars-using-variables), the rule can't evaluate that policy and returns NON\_COMPLIANT, even if the policy would otherwise be compliant. To get an accurate evaluation, split any value that contains more than five policy variables so that each value contains five or fewer.

**Identifier:** S3\_BUCKET\_SERVER\_SIDE\_ENCRYPTION\_ENABLED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1441c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).