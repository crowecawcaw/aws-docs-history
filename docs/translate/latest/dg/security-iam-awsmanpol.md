# AWS managed policies for Amazon Translate

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

###### Topics

- [AWS managed policy:
  TranslateFullAccess](#security-iam-awsmanpol-TranslateFullAccess "#security-iam-awsmanpol-TranslateFullAccess")
- [AWS managed policy:
  TranslateReadOnly](#security-iam-awsmanpol-TranslateReadOnly "#security-iam-awsmanpol-TranslateReadOnly")
- [Amazon Translate updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed policy:

TranslateFullAccess

This policy grants full access to Amazon Translate resources, the Amazon Comprehend DetectDominantLanguage
API operation, and required CloudWatch API operations. The policy also grants list and get
permissions for Amazon S3 buckets and IAM roles.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "translate:*",
 "comprehend:DetectDominantLanguage",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics",
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:GetBucketLocation",
 "iam:ListRoles",
 "iam:GetRole"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy:

TranslateReadOnly

This policy grants permission to access the Amazon Translate API operations that do not modify
resources associated with your account. The policy also grants permission to access the
Amazon Comprehend DetectDominantLanguage API operation and required CloudWatch API operations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "translate:TranslateText",
 "translate:TranslateDocument",
 "translate:GetTerminology",
 "translate:ListTerminologies",
 "translate:ListTextTranslationJobs",
 "translate:DescribeTextTranslationJob",
 "translate:GetParallelData",
 "translate:ListParallelData",
 "comprehend:DetectDominantLanguage",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## Amazon Translate updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon Translate since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the Amazon Translate [Document history](doc-history.md "doc-history.md")
page.

| Change                                                                                                                                    | Description                                                                                | Date         |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------ |
| [TranslateReadOnly](#security-iam-awsmanpol-TranslateReadOnly "#security-iam-awsmanpol-TranslateReadOnly") – Update to an existing policy | Amazon Translate now allows the `TranslateDocument` action in the TranslateReadOnly policy | May 23, 2023 |
| Amazon Translate started tracking changes                                                                                                 | Amazon Translate started tracking changes for its AWS managed policies.                    | May 23, 2023 |
