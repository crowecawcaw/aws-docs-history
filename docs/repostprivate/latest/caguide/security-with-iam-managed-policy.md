# AWS managed policies for AWS re:Post Private

Using AWS managed policies makes adding permissions to users, groups, and roles easier than writing policies yourself.
It takes time and expertise to create [IAM customer managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. Use AWS managed policies to get started quickly.
These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see
[AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies")
in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies.
Services might occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when
new operations become available. Services don't remove permissions from an AWS managed policy, so policy updates don't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the `ReadOnlyAccess`
AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions
for new operations and resources. For more information, see
[AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

###### Topics

- [AWS managed policy: AWSRepostSpaceSupportOperationsPolicy](#support-case-manpol "#support-case-manpol")
- [AWS managed policy: AWSrePostPrivateCloudWatchAccess](#cloudwatch-metric-manpol "#cloudwatch-metric-manpol")
- [AWS re:Post Private updates to
  AWS managed policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed policy: AWSRepostSpaceSupportOperationsPolicy

This policy allows the AWS re:Post Private service to create, manage, and resolve Support cases that are created through the re:Post Private web application.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RepostSpaceSupportOperations",
 "Effect": "Allow",
 "Action": [
 "support:AddAttachmentsToSet",
 "support:AddCommunicationToCase",
 "support:CreateCase",
 "support:DescribeCases",
 "support:DescribeCommunications",
 "support:ResolveCase"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AWSrePostPrivateCloudWatchAccess

This policy allows the re:Post Private service to publish data to CloudWatch.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CloudWatchPublishMetrics",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": [
 "AWS/rePostPrivate",
 "AWS/Usage"
 ]
 }
 }
 }
 ]
}`

```

## AWS re:Post Private updates to

AWS managed policies

View details about updates to AWS managed policies for re:Post Private since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the [Document history](doc-history.md "doc-history.md") page.

The following table describes important updates to the re:Post Private managed policies
since November 26, 2023.

| Change                                                                                                                                                                       | Description                                                           | Date              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ----------------- |
| New policy - [AWSrePostPrivateCloudWatchAccess](security-with-iam-managed-policy.md#cloudwatch-metric-manpol "security-with-iam-managed-policy.md#cloudwatch-metric-manpol") | New managed policy for publishing data to CloudWatch                  | November 26, 2023 |
| New policy - [AWSRepostSpaceSupportOperationsPolicy](security-with-iam-managed-policy.md#support-case-manpol "security-with-iam-managed-policy.md#support-case-manpol")      | New managed policy for the AWS Support feature in AWS re:Post Private | November 26, 2023 |
| re:Post Private started tracking changes                                                                                                                                     | re:Post Private started tracking changes for its AWS managed policies | November 26, 2023 |
