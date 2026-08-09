# AWS managed policies for AWS HealthLake

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

## AWS managed policy: AmazonHealthLakeFullAccess

The `AmazonHealthLakeFullAccess` policy provides full access to HealthLake.
With this policy attached to their user or role, users can use HealthLake to access, query,
import, and export data in HealthLake. To perform many common actions in HealthLake, you must add
additional policies to the user or role. For more information, see [Setting up AWS HealthLake](getting-started-setting-up.md "getting-started-setting-up.md") and
[HealthLake operations and
permissions](#security-iam-awsmanpol-operations-and-permissions "#security-iam-awsmanpol-operations-and-permissions").

You can attach the `AmazonHealthLakeFullAccess` policy to your IAM
identities.

This policy grants administrative and contributor permissions
that allow users and roles to query, search, import, and export with HealthLake, and it also
makes it possible for HealthLake to perform actions on behalf of the users and roles that have
these permissions.

**Permissions details**

This policy includes the following statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "healthlake:*",
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:GetBucketLocation",
 "iam:ListRoles"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "healthlake.amazonaws.com"
 }
 }
 }
 ]
}`

```

## AWS managed policy: AmazonHealthLakeReadOnlyAccess

With the `AmazonHealthLakeReadOnlyAccess` policy, you have read-only access
to HealthLake. You can view and query HealthLake data stores. You can also view HealthLake Data Transformation Agent
profiles and transformation jobs. You can't create, modify, or delete these
resources.

You can attach the `AmazonHealthLakeReadOnlyAccess` policy to your IAM
identities.

This policy grants `read-only` permissions that allow users and
roles to query HealthLake.

**Permissions details**

For more information about the permissions for this policy, see [AmazonHealthLakeReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonHealthLakeReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonHealthLakeReadOnlyAccess.md") in the _AWS Managed Policy
Reference_.

## HealthLake operations and permissions

The following table lists typical operations in HealthLake and the permissions needed to
perform them.

| HealthLake operations                                                 | Required permissions                                                                                                                                                                                                                  |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create a data store in HealthLake                                     | `AmazonHealthLakeFullAccess`,`AmazonLakeFormationDataAdmin`,<br>[inline policy](getting-started-setting-up.md "getting-started-setting-up.md"), and<br>AWS Lake Formation Administrator permissions managed by<br>AWS Lake Formation  |
| Delete a data store in HealthLake                                     | `AmazonHealthLakeFullAccess`,<br>`AmazonLakeFormationDataAdmin`, [inline policy](getting-started-setting-up.md "getting-started-setting-up.md"), and<br>AWS Lake Formation Administrator permissions managed by<br>AWS Lake Formation |
| List, search, or query a data store in HealthLake                     | `AmazonHealthLakeReadOnlyAccess`                                                                                                                                                                                                      |
| Query a data store using Amazon Athena                                | `AmazonAthenaFullAccess`, `AmazonS3FullAccess`,<br>AWS Lake Formation `Select` and `Describe`<br>permissions on tables managed by AWS Lake Formation                                                                                  |
| Import data from HealthLake                                           | See [Setting up permissions for import jobs](getting-started-setting-up.md#setting-up-import-permissions "getting-started-setting-up.md#setting-up-import-permissions").                                                              |
| Export data from HealthLake                                           | See [Setting up permissions for export jobs](getting-started-setting-up.md#setting-up-export-permissions "getting-started-setting-up.md#setting-up-export-permissions").                                                              |
| View or list HealthLake Data Transformation Agent profiles            | `AmazonHealthLakeReadOnlyAccess`                                                                                                                                                                                                      |
| View or list HealthLake Data Transformation Agent jobs                | `AmazonHealthLakeReadOnlyAccess`                                                                                                                                                                                                      |
| Validate a source C-CDA file for HealthLake Data Transformation Agent | `AmazonHealthLakeReadOnlyAccess`                                                                                                                                                                                                      |

## HealthLake updates to AWS managed policies

View details about updates to AWS managed policies for HealthLake from the time that
this service began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the HealthLake Document history page.

| Change                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Date               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| [AmazonHealthLakeReadOnlyAccess](#security-iam-awsmanpol-AmazonHealthLakeReadOnlyAccess "#security-iam-awsmanpol-AmazonHealthLakeReadOnlyAccess") – Update to an existing<br>policy | We added permissions to allow read-only access to HealthLake Data Transformation Agent profiles and<br>jobs.<br>Added the `healthlake:GetDataTransformationProfile`,<br>`healthlake:ListDataTransformationProfiles`,<br>`healthlake:ListDataTransformationProfileVersions`,<br>`healthlake:DescribeDataTransformationJob`,<br>`healthlake:ListDataTransformationJobs`, and<br>`healthlake:ValidateSource` permissions.<br>You can now view transformation profiles and profile versions, view<br>transformation job status, and validate source C-CDA files. | August 4, 2026     |
| [AmazonHealthLakeFullAccess](#security-iam-awsmanpol-AmazonHealthLakeFullAccess "#security-iam-awsmanpol-AmazonHealthLakeFullAccess")                                               | `AmazonHealthLakeFullAccess` policy required to allow full<br>access to HealthLake.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | November, 14, 2022 |
| [AmazonHealthLakeReadOnlyAccess](#security-iam-awsmanpol-AmazonHealthLakeReadOnlyAccess "#security-iam-awsmanpol-AmazonHealthLakeReadOnlyAccess")                                   | `AmazonHealthLakeReadOnlyAccess` policy required for read-only<br>access to HealthLake.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | November, 14, 2022 |
| HealthLake started tracking changes                                                                                                                                                 | HealthLake started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | November, 14, 2022 |
