

# AWS managed policies for Amazon S3 Express One Zone
<a name="s3-express-one-zone-security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: AmazonS3ExpressFullAccess
<a name="s3-express-one-zone-security-iam-awsmanpol-amazons3expressfullaccess"></a>

You can attach the `AmazonS3ExpressFullAccess` policy to your IAM identities. This policy grants full access to Amazon S3 Express One Zone directory buckets and operations. It allows all actions under the `s3express` service prefix on all resources.

This policy is intended for users or roles that need unrestricted access to directory buckets. This policy covers only Amazon S3 Express One Zone operations. For standard Amazon S3 operations, you need additional policies.

To view the permissions for this policy, see [AmazonS3ExpressFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonS3ExpressFullAccess.html) in the AWS Managed Policy Reference.

## AWS managed policy: AmazonS3ExpressReadOnlyAccess
<a name="s3-express-one-zone-security-iam-awsmanpol-amazons3expressreadonlyaccess"></a>

You can attach the `AmazonS3ExpressReadOnlyAccess` policy to your IAM identities. This policy grants permissions that allow `ReadOnly` access to Amazon S3 Express One Zone directory buckets.

**Note**  
The `CreateSession` action supports the `SessionMode` condition key which can be set to `ReadOnly` or `ReadWrite`. This policy uses `SessionMode` for a `ReadOnly` session.

To view the permissions for this policy, see [AmazonS3ExpressReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonS3ExpressReadOnlyAccess.html) in the AWS Managed Policy Reference.

## Amazon S3 Express One Zone updates to AWS managed policies
<a name="s3-express-one-zone-security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Amazon S3 Express One Zone since this service began tracking these changes.


| Change | Description | Date | 
| --- | --- | --- | 
| Amazon S3 Express One Zone added `AmazonS3ExpressFullAccess`. | Amazon S3 Express One Zone added a new AWS managed policy called `AmazonS3ExpressFullAccess`. This policy grants permissions that allow full access to Amazon S3 Express One Zone directory buckets and operations. | April 03, 2026 | 
| Amazon S3 Express One Zone added `AmazonS3ExpressReadOnlyAccess`. | Amazon S3 Express One Zone added a new AWS managed policy called `AmazonS3ExpressReadOnlyAccess`. This policy grants permissions that allow read-only access to Amazon S3 Express One Zone directory buckets. | April 03, 2026 | 
| Amazon S3 Express One Zone started tracking changes. | Amazon S3 Express One Zone started tracking changes for its AWS managed policies. | April 03, 2026 | 