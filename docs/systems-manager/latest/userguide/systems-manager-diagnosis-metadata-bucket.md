# Working with Amazon S3 buckets and

bucket policies for Systems Manager

During the [onboarding process](systems-manager-setting-up-console.md "systems-manager-setting-up-console.md")
for AWS Systems Manager, Quick Setup creates an Amazon Simple Storage Service (Amazon S3) bucket in the delegated
administrator account for organization setups. For single-account setups, the bucket is
stored in the account being set up.

You can use Systems Manager to run diagnostic operations on your fleet to identify cases of failed
deployments and drifted configurations. Systems Manager can also detect cases where configuration
issues are preventing Systems Manager from managing EC2 instances in your account or organization. The
results of these diagnostic operations are stored in this Amazon S3 bucket, which is protected by
both an encryption method and an S3 bucket policy. For information about the diagnostic
operations that output data to this bucket, see [Diagnosing and remediating](diagnose-and-remediate.md "diagnose-and-remediate.md").

###### Changing the bucket encryption method

By default, the S3 bucket uses server-side encryption with Amazon S3 managed keys
(SSE-S3).

You can instead use server-side encryption with AWS KMS keys (SSE-KMS) using a
customer managed key (CMK) as an alternative to Amazon S3 managed keys, as explained in [Changing to an AWS KMS customer managed key to
encrypt S3 resources](remediate-s3-bucket-encryption.md "remediate-s3-bucket-encryption.md").

###### Contents of the bucket policy

The bucket policy prevents member accounts in an organization from discovering one
another. Read and write permissions to the bucket are allowed only for the diagnosis and
remediation roles created for Systems Manager. The contents of these system-generated policies are
presented in [S3 bucket policies for the unified Systems Manager
console](remediate-s3-bucket-policies.md "remediate-s3-bucket-policies.md").

###### Warning

Modifying the default bucket policy might allow member accounts in an organization to
discover one another, or read diagnosis outputs for instances in another account. We
recommend using extreme caution if you choose to modify this policy.

###### Topics

- [Changing to an AWS KMS customer managed key to
  encrypt S3 resources](remediate-s3-bucket-encryption.md "remediate-s3-bucket-encryption.md")
- [S3 bucket policies for the unified Systems Manager
  console](remediate-s3-bucket-policies.md "remediate-s3-bucket-policies.md")
