On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# AWS managed policies for Amazon Lookout for Equipment

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed

policy: AmazonLookoutEquipmentReadOnlyAccess

You can attach AmazonLookoutEquipmentReadOnlyAccess to your IAM entities. Lookout for Equipment also
attaches this policy to a service role that allows Lookout for Equipment to perform actions on your behalf.

This policy grants `read-only` permissions that allow read-only
access to all Lookout for Equipment resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lookoutequipment:DescribeDataset",
 "lookoutequipment:DescribeDataIngestionJob",
 "lookoutequipment:DescribeModel",
 "lookoutequipment:DescribeInferenceScheduler",
 "lookoutequipment:ListDatasets",
 "lookoutequipment:ListDataIngestionJobs",
 "lookoutequipment:ListModels",
 "lookoutequipment:ListInferenceSchedulers",
 "lookoutequipment:ListInferenceExecutions",
 "lookoutequipment:ListSensorStatistics",
 "lookoutequipment:ListTagsForResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed

policy: AmazonLookoutEquipmentFullAccess

You can attach AmazonLookoutEquipmentFullAccess to your IAM entities. Lookout for Equipment also
attaches this policy to a service role that allows Lookout for Equipment to perform actions on your behalf.

This policy grants `administrative` permissions that allow
access to all Lookout for Equipment resources and operations. This policy enables you to use any IAM role
or AWS KMS key with Lookout for Equipment.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lookoutequipment:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "lookoutequipment.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "kms:ViaService": "lookoutequipment.*.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:ListAliases"
 ],
 "Resource": "*"
 }
 ]
 }`

```

## Lookout for Equipment updates to AWS managed

policies

View details about updates to AWS managed policies for Lookout for Equipment since this service began
tracking these changes. For automatic alerts about changes to this page, subscribe to the
RSS feed on the Lookout for Equipment Document history page.

| Change                                                                                                                                                                                             | Description                                                                                                                                                                                                                 | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AmazonLookoutEquipmentReadOnlyAccess](#security-iam-awsmanpol-AmazonLookoutEquipmentReadOnlyAccess "#security-iam-awsmanpol-AmazonLookoutEquipmentReadOnlyAccess") – Update to an existing policy | Lookout for Equipment modified the policy so as to enable you to list sensor statistics.                                                                                                                                    | June 22, 2022     |
| [AmazonLookoutEquipmentFullAccess](#security-iam-awsmanpol-AmazonLookoutEquipmentFullAccess "#security-iam-awsmanpol-AmazonLookoutEquipmentFullAccess") – Update to grant retirement policy        | Lookout for Equipment removed RetireGrant from the managed policy as the service will be using retiring grant principal to retire the grants. You dont need to provide the retire grant permissions in the managed policy.  | November 22, 2021 |
| [AmazonLookoutEquipmentFullAccess](#security-iam-awsmanpol-AmazonLookoutEquipmentFullAccess "#security-iam-awsmanpol-AmazonLookoutEquipmentFullAccess") – Update to an existing policy             | Lookout for Equipment modified the policy so as to only apply the kms:ViaService condition to DescribeKey and CreateGrant.                                                                                                  | Oct 29, 2021      |
| [AmazonLookoutEquipmentReadOnlyAccess](#security-iam-awsmanpol-AmazonLookoutEquipmentReadOnlyAccess "#security-iam-awsmanpol-AmazonLookoutEquipmentReadOnlyAccess") – New policy                   | Lookout for Equipment added a new policy to allow read only access for all Lookout for Equipment resources.                                                                                                                 | May 05, 2021      |
| [AmazonLookoutEquipmentFullAccess](#security-iam-awsmanpol-AmazonLookoutEquipmentFullAccess "#security-iam-awsmanpol-AmazonLookoutEquipmentFullAccess") – Update to an existing policy             | Lookout for Equipment added permissions to describe AWS KMS managed encryption keys. You must use these permissions to use the Lookout for Equipment console to display information about AWS KMS keys across AWS accounts. | May 05, 2021      |
| Lookout for Equipment started tracking changes                                                                                                                                                     | Lookout for Equipment started tracking changes for its AWS managed policies.                                                                                                                                                | April 08, 2021    |
