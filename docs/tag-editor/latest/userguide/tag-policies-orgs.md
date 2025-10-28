# AWS Organizations tag policies

A [_tag policy_](../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md "../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md") is a type of policy that you create in
AWS Organizations. You can use tag policies to help standardize tags across the resources in your
organization's accounts. To use tag policies, we recommend that you follow the workflows
described in [Getting
started with tag policies](../../../organizations/latest/userguide/orgs_manage_policies_tag-policies-getting-started.md "../../../organizations/latest/userguide/orgs_manage_policies_tag-policies-getting-started.md") in the _AWS Organizations User Guide_. As
mentioned on that page, the recommended workflows include finding and correcting
noncompliant tags. To accomplish these tasks, you use the Tag Editor console.

## Prerequisites and permissions

Before you can evaluate compliance with tag policies in Tag Editor, you must meet the
requirements and set the necessary permissions.

###### Topics

- [Prerequisites for evaluating compliance
  with tag policies](#tag-policies-prereqs-overview "#tag-policies-prereqs-overview")
- [Permissions for evaluating compliance
  for an account](#tag-policies-permissions-account "#tag-policies-permissions-account")
- [Permissions for evaluating
  organization-wide compliance](#tag-policies-permissions-org "#tag-policies-permissions-org")
- [Amazon S3 bucket policy for report storage](#bucket-policy "#bucket-policy")

### Prerequisites for evaluating compliance

with tag policies

Evaluating compliance with tag policies requires the following:

- You must first enable the feature in AWS Organizations, and create and attach tag
  policies. For more information, see the following pages in the
  _AWS Organizations User Guide_:
  - [Prerequisites and permissions for managing tag
    policies](../../../organizations/latest/userguide/orgs_manage_policies_tag-policies-prereqs.md "../../../organizations/latest/userguide/orgs_manage_policies_tag-policies-prereqs.md")
  - [Enabling tag policies](../../../organizations/latest/userguide/orgs_manage_policies_enable-disable.md "../../../organizations/latest/userguide/orgs_manage_policies_enable-disable.md")
  - [Getting started with tag policies](../../../organizations/latest/userguide/orgs_manage_policies_tag-policies-getting-started.md "../../../organizations/latest/userguide/orgs_manage_policies_tag-policies-getting-started.md")

- To [find noncompliant tags on an account's
  resources](tag-policies-orgs-finding-noncompliant-tags.md "tag-policies-orgs-finding-noncompliant-tags.md"), you need sign-in credentials for that account
  and the permissions listed in [Permissions for evaluating compliance
  for an account](#tag-policies-permissions-account "#tag-policies-permissions-account").
- To [evaluate organization-wide compliance](tag-policies-orgs-evaluating-org-wide-compliance.md "tag-policies-orgs-evaluating-org-wide-compliance.md"), you
  need sign-in credentials for the organization's management account and the
  permissions listed in [Permissions for evaluating
  organization-wide compliance](#tag-policies-permissions-org "#tag-policies-permissions-org") . You can request the
  compliance report from only the AWS Region US East (N. Virginia) .

### Permissions for evaluating compliance

for an account

Finding noncompliant tags on an account's resources requires the following
permissions:

- `organizations:DescribeEffectivePolicy` – To get the
  contents of the effective tag policy for the account.
- `tag:GetResources` – To get a list of resources that don't
  comply with the attached tag policy.
- `tag:TagResources` – To add or update tags. You also need
  service-specific permissions to create tags. For example, to tag resources in
  Amazon Elastic Compute Cloud (Amazon EC2), you need permissions for `ec2:CreateTags`.
- `tag:UnTagResources` – To remove a tag. You also need
  service-specific permissions to remove tags. For example, to untag resources in
  Amazon EC2, you need permissions for `ec2:DeleteTags`.

The following example AWS Identity and Access Management (IAM) policy provides permissions for evaluating tag
compliance for an account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EvaluateAccountCompliance",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeEffectivePolicy",
 "tag:GetResources",
 "tag:TagResources",
 "tag:UnTagResources"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information about IAM policies and permissions, see the
[IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

### Permissions for evaluating

organization-wide compliance

Evaluating organization-wide compliance with tag policies requires the following
permissions:

- `organizations:DescribeEffectivePolicy` – To get the
  contents of the tag policy that's attached to the organization, organizational
  unit (OU), or account.
- `tag:GetComplianceSummary` – To get a summary of
  noncompliant resources in all accounts in the organization.
- `tag:StartReportCreation` – To export the results of the
  most recent compliance evaluation to a file. Organization-wide compliance is
  evaluated every 48 hours.
- `tag:DescribeReportCreation` – To check the status of report
  creation.
- `s3:ListAllMyBuckets` — To assist with accessing the organization-wide
  compliance report.
- `s3:GetBucketAcl` – To inspect the Access Control List (ACL) of the
  Amazon S3 bucket receiving the compliance report.
- `s3:GetObject` – To retrieve the compliance report from the
  service-owned Amazon S3 bucket.
- `s3:PutObject` – To place the compliance report in the specified
  Amazon S3 bucket.

If the Amazon S3 bucket where the report is being delivered is encrypted via SSE-KMS, you must also
have the `kms:GenerateDataKey` permission for that bucket.

The following example IAM policy provides permissions for evaluating
organization-wide compliance. Replace each `placeholder` with your
own information:

- `bucket_name` – Your Amazon S3 bucket name
- `organization_id` – Your organization's ID

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EvaluateAccountCompliance",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeEffectivePolicy",
 "tag:StartReportCreation",
 "tag:DescribeReportCreation",
 "tag:GetComplianceSummary",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "GetBucketAclForReportDelivery",
 "Effect": "Allow",
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::`bucket_name`",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaLast": "tagpolicies.tag.amazonaws.com"
 }
 }
 },
 {
 "Sid": "GetObjectForReportDelivery",
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::*/tag-policy-compliance-reports/*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaLast": "tagpolicies.tag.amazonaws.com"
 }
 }
 },
 {
 "Sid": "PutObjectForReportDelivery",
 "Effect": "Allow",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`bucket_name`/AwsTagPolicies/`organization_id`/*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaLast": "tagpolicies.tag.amazonaws.com"
 },
 "StringLike": {
 "s3:x-amz-copy-source": "*/tag-policy-compliance-reports/*"
 }
 }
 }
 ]
}`

```

For more information about IAM policies and permissions, see the
[IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

### Amazon S3 bucket policy for report storage

To create an organization-wide compliance report, the identity that you use to call
the `StartReportCreation` API must have access to an
Amazon Simple Storage Service (Amazon S3) bucket in the US East (N. Virginia) Region to store the report.
Tag Policies uses the credentials of the calling identity to deliver the compliance
report to the specified bucket.

If the bucket and the identity being used to call the `StartReportCreation` API
_belong to the same account_, additional Amazon S3 bucket policies are not needed for this use case.

If the account associated with the identity used to call the `StartReportCreation` API
is _different_ from the account that owns the Amazon S3 bucket,
the following bucket policy must be attached to the bucket. Replace each
`placeholder` with your own information:

- `bucket_name` – Your Amazon S3 bucket name
- `organization_id` – Your organization's ID
- `identity_ARN` – The ARN of the IAM identity used to call the
  `StartReportCreation` API

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CrossAccountTagPolicyACL",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`identity_ARN`"
 },
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::`bucket_name`"
 },
 {
 "Sid": "CrossAccountTagPolicyBucketDelivery",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`identity_ARN`"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`bucket_name`/AwsTagPolicies/`organization_id`/*"
 }
 ]
}`

```
