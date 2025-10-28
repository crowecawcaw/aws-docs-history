# s3-bucket-public-write-prohibited

Checks if your Amazon S3 buckets do not allow public write access. The rule checks the Block Public Access settings, the bucket policy, and the bucket access control list (ACL).

The rule is compliant when both of the following are true:

- The Block Public Access setting restricts public policies or the bucket policy does not allow public write access.
- The Block Public Access setting restricts public ACLs or the bucket ACL does not allow public write access.
  The rule is noncompliant when:

- If the Block Public Access setting does not restrict public policies, AWS Config evaluates whether the policy allows public write access. If the policy allows public write access, the rule is noncompliant.
- If the Block Public Access setting does not restrict public bucket ACLs, AWS Config evaluates whether the bucket ACL allows public write access. If the bucket ACL allows public write access, the rule is noncompliant.

###### Note

This rule does not evaluate changes to account level public block access. To check if the required public access block settings are configured from the account level,
see [s3-account-level-public-access-blocks](s3-account-level-public-access-blocks.md "s3-account-level-public-access-blocks.md") and [s3-account-level-public-access-blocks-periodic](s3-account-level-public-access-blocks-periodic.md "s3-account-level-public-access-blocks-periodic.md").

###### Note

To be considered non-public, an S3 bucket policy must grant access only to fixed values. This means values that don't contain a wildcard or the following IAM policy element: [Variables](../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-using-variables "../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-using-variables").

**Identifier:** S3_BUCKET_PUBLIC_WRITE_PROHIBITED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes and Periodic

**AWS Region:** All supported AWS regions except AWS Secret - West Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
