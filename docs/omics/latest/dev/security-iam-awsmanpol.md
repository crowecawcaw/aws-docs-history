# AWS managed policies for AWS HealthOmics

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

## AWS managed policy:

AmazonOmicsFullAccess

You can attach the `AmazonOmicsFullAccess` policy to your IAM identities
to give them full access to HealthOmics.

This policy grants full access permissions to all HealthOmics actions. When you create an annotation or variant
store, Omics will also give you access tothat store through a Resource Share Invitation in the Resource Access
Manager (RAM) console. For more information on Resource Share invitations through Lake Formation, see the [Cross-account data sharing
in Lake Formation](../../../lake-formation/latest/dg/cross-account-permissions.md "../../../lake-formation/latest/dg/cross-account-permissions.md"). For an Omics admin policy, you also need the following permissions to access your
Amazon S3 bucket.

- PutObject
- GetObject
- ListBucket
- AbortMultipartUpload
- ListMultipartUploadParts

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "omics:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ram:AcceptResourceShareInvitation",
 "ram:GetResourceShareInvitations"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaLast": "omics.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "omics.amazonaws.com"
 }
 }
 }
 ]
}`

```

## AWS managed policy:

AmazonOmicsReadOnlyAccess

You can attach the `AWSOmicsReadOnlyAccess` policy to your IAM identities when you wish to limit the permissions for that identity to read-only access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "omics:Get*",
 "omics:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## HealthOmics updates to AWS managed

policies

View details about updates to AWS managed policies for HealthOmics since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the HealthOmics Document history page.

| Change                                          | Description                                                                                                                                                                                                                         | Date              |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| AmazonOmicsFullAccess<br>• New policy added     | HealthOmics added a new policy to grant a user full access to all actions and resources. To learn more, see [AmazonOmicsFullAccess](#security-iam-awsmanpol-AmazonOmicsFullAccess "#security-iam-awsmanpol-AmazonOmicsFullAccess"). | February 23, 2023 |
| HealthOmics started tracking<br>changes         | HealthOmics started tracking changes for its AWS managed<br>policies.                                                                                                                                                               | November 29, 2022 |
| AmazonOmicsReadOnlyAccess<br>• New policy added | HealthOmics added a new policy that limits access to read only. To learn more, [AmazonOmicsReadOnlyAccess](#security-iam-awsmanpol-AmazonOmicsReadOnlyAccess "#security-iam-awsmanpol-AmazonOmicsReadOnlyAccess").                  | November 29, 2022 |
