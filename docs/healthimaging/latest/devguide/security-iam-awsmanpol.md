# AWS managed policies for AWS HealthImaging

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
  AWSHealthImagingServiceRolePolicy](#security-iam-awsmanpol-AWSHealthImagingServiceRolePolicy "#security-iam-awsmanpol-AWSHealthImagingServiceRolePolicy")
- [AWS managed policy:
  AWSHealthImagingFullAccess](#security-iam-awsmanpol-AWSHealthImagingFullAccess "#security-iam-awsmanpol-AWSHealthImagingFullAccess")
- [AWS managed
  policy: AWSHealthImagingReadOnlyAccess](#security-iam-awsmanpol-AWSHealthImagingReadOnlyAccess "#security-iam-awsmanpol-AWSHealthImagingReadOnlyAccess")
- [HealthImaging updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed policy:

AWSHealthImagingServiceRolePolicy

This policy is attached to service-linked role `AWSServiceRoleForHealthImaging`.
It grants permissions for HealthImaging to manage service operations and publish service metrics.

For more information about this policy, including the JSON policy document,
see [AWSHealthImagingServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSHealthImagingServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSHealthImagingServiceRolePolicy.md")
in the _AWS Managed Policy Reference Guide_.

## AWS managed policy:

AWSHealthImagingFullAccess

You can attach the `AWSHealthImagingFullAccess` policy to your IAM
identities.

This policy grants administrative permission to all HealthImaging actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "medical-imaging:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "medical-imaging.amazonaws.com"
 }
 }
 }
 ]
}`

```

## AWS managed

policy: AWSHealthImagingReadOnlyAccess

You can attach the `AWSHealthImagingReadOnlyAccess` policy to your IAM
identities.

This policy grants read-only permission to specific AWS HealthImaging actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "medical-imaging:GetDICOMImportJob",
 "medical-imaging:GetDatastore",
 "medical-imaging:GetImageFrame",
 "medical-imaging:GetImageSet",
 "medical-imaging:GetImageSetMetadata",
 "medical-imaging:ListDICOMImportJobs",
 "medical-imaging:ListDatastores",
 "medical-imaging:ListImageSetVersions",
 "medical-imaging:ListTagsForResource",
 "medical-imaging:SearchImageSets"
 ],
 "Resource": "*"
 }]
}`

```

## HealthImaging updates to AWS managed

policies

View details about updates to AWS managed policies for HealthImaging since this service began
tracking these changes. For automatic alerts about changes to this page, subscribe to the
RSS feed on the [Releases](releases.md "releases.md") page.

| Change                                 | Description                                                                                                                                                                          | Date             |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| AWSHealthImagingServiceRolePolicy      | AWS HealthImaging added a new managed policy for the service-linked role<br>that provides permissions for HealthImaging to manage service operations and<br>publish service metrics. | February 9, 2026 |
| HealthImaging started tracking changes | HealthImaging started tracking changes for its AWS managed policies.                                                                                                                 | July 19, 2023    |
