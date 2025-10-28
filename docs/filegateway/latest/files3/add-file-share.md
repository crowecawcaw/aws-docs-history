# Granting access and permissions for file shares and

buckets

After your S3 File Gateway is activated and running, you can add additional file shares and
grant access to Amazon S3 buckets, including buckets in different AWS accounts than your
gateways and file shares. The following sections describe how to use IAM roles to
provide your gateway with access permissions for Amazon S3 buckets and VPC endpoints, prevent
certain security issues, and connect file shares to buckets across
AWS accounts.

For information about how to create a new file share, see [Creating a file share](GettingStartedCreateFileShare.md "GettingStartedCreateFileShare.md").

This section contains the following topics, which provide additional information about
how to grant access and permissions for file shares and Amazon S3 buckets:

**Topics**

- [Granting access to an Amazon S3 bucket](grant-access-s3.md "grant-access-s3.md") - Learn how
  to grant access for your File Gateway to upload files into your Amazon S3 bucket,
  and to perform actions on any access points or Amazon Virtual Private Cloud (Amazon VPC) endpoints that
  it uses to connect to the bucket.
- [Cross-service confused deputy
  prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md") - Learn how to
  prevent a common security issue where an entity that doesn't have permission to
  perform an action can coerce a more-privileged entity to perform the
  action.
- [Using a file share for cross-account access](cross-account-access.md "cross-account-access.md") -
  Learn how to grant access for an Amazon Web Services account and users of that account to
  access resources that belong to another Amazon Web Services account.

###### Note

If your File Gateway uses SSE-KMS or DSSE-KMS for encryption, make sure the IAM
role associated with the file share includes _kms:Encrypt_,
_kms:Decrypt_, \*kms:ReEncrypt\**,
*kms:GenerateDataKey*, and
*kms:DescribeKey\* permissions. For more information, see
[Using
Identity-Based Policies (IAM Policies) for Storage Gateway](using-identity-based-policies.md "using-identity-based-policies.md").
