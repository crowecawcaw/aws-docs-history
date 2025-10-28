Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Customer Managed Policy

Examples

In this section, you can find example user policies that grant permissions for
various AWS Snowball Edge job management actions. These policies work when you are using
AWS SDKs or the AWS CLI. When you are using the console, you need to grant
additional permissions specific to the console, which is discussed in [Permissions Required to
Use the AWS Snowball Edge Console](access-control-managing-permissions.md#additional-console-required-permissions "access-control-managing-permissions.md#additional-console-required-permissions").

###### Note

All examples use the us-west-2 region and contain fictitious account
IDs.

###### Examples

- [Example 1: Role Policy That
  Allows a User to Create a Job to order a Snowball Edge device with the API](#access-policy-example-create-api "#access-policy-example-create-api")
- [Example 2: Role Policy for Creating
  Import Jobs](#role-policy-example-import "#role-policy-example-import")
- [Example 3: Role Policy for Creating
  Export Jobs](#role-policy-example-export "#role-policy-example-export")
- [Example 4: Expected
  Role Permissions and Trust Policy](#expected-role-permissions-and-trust-policy "#expected-role-permissions-and-trust-policy")
- [AWS Snowball Edge API Permissions: Actions,
  Resources, and Conditions Reference](#snowball-api-permissions-ref "#snowball-api-permissions-ref")

## Example 1: Role Policy That

Allows a User to Create a Job to order a Snowball Edge device with the API

The following permissions policy is a necessary component of any policy that
is used to grant job or cluster creation permission using the job management
API. The statement is needed as a Trust Relationship policy statement for the
Snowball IAM role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "importexport.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Example 2: Role Policy for Creating

Import Jobs

You use the following role trust policy for creating import jobs for
Snowball Edge that use AWS Lambda powered by AWS IoT Greengrass functions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:ListBucketMultipartUploads"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketPolicy",
 "s3:GetBucketLocation",
 "s3:ListBucketMultipartUploads",
 "s3:ListBucket",
 "s3:PutObject",
 "s3:AbortMultipartUpload",
 "s3:ListMultipartUploadParts",
 "s3:PutObjectAcl",
 "s3:GetObject"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "snowball:*"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:AttachPrincipalPolicy",
 "iot:AttachThingPrincipal",
 "iot:CreateKeysAndCertificate",
 "iot:CreatePolicy",
 "iot:CreateThing",
 "iot:DescribeEndpoint",
 "iot:GetPolicy"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:GetFunction"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "greengrass:CreateCoreDefinition",
 "greengrass:CreateDeployment",
 "greengrass:CreateDeviceDefinition",
 "greengrass:CreateFunctionDefinition",
 "greengrass:CreateGroup",
 "greengrass:CreateGroupVersion",
 "greengrass:CreateLoggerDefinition",
 "greengrass:CreateSubscriptionDefinition",
 "greengrass:GetDeploymentStatus",
 "greengrass:UpdateGroupCertificateConfiguration",
 "greengrass:CreateGroupCertificateAuthority",
 "greengrass:GetGroupCertificateAuthority",
 "greengrass:ListGroupCertificateAuthorities",
 "greengrass:ListDeployments",
 "greengrass:GetGroup",
 "greengrass:GetGroupVersion",
 "greengrass:GetCoreDefinitionVersion"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Example 3: Role Policy for Creating

Export Jobs

You use the following role trust policy for creating export jobs for
Snowball Edge that use AWS Lambda powered by AWS IoT Greengrass functions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "snowball:*"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:AttachPrincipalPolicy",
 "iot:AttachThingPrincipal",
 "iot:CreateKeysAndCertificate",
 "iot:CreatePolicy",
 "iot:CreateThing",
 "iot:DescribeEndpoint",
 "iot:GetPolicy"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:GetFunction"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "greengrass:CreateCoreDefinition",
 "greengrass:CreateDeployment",
 "greengrass:CreateDeviceDefinition",
 "greengrass:CreateFunctionDefinition",
 "greengrass:CreateGroup",
 "greengrass:CreateGroupVersion",
 "greengrass:CreateLoggerDefinition",
 "greengrass:CreateSubscriptionDefinition",
 "greengrass:GetDeploymentStatus",
 "greengrass:UpdateGroupCertificateConfiguration",
 "greengrass:CreateGroupCertificateAuthority",
 "greengrass:GetGroupCertificateAuthority",
 "greengrass:ListGroupCertificateAuthorities",
 "greengrass:ListDeployments",
 "greengrass:GetGroup",
 "greengrass:GetGroupVersion",
 "greengrass:GetCoreDefinitionVersion"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Example 4: Expected

Role Permissions and Trust Policy

The following expected role permissions policy is a necessary for an existing
service role to use. It is a one time set up.

The following expected role trust policy is a necessary for an existing
service role to use. It is a one time set up.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "importexport.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## AWS Snowball Edge API Permissions: Actions,

Resources, and Conditions Reference

When you are setting up [Access Control in the AWS Cloud](access-control.md "access-control.md") and writing a permissions policy that you can attach to an IAM identity
(identity-based policies), you can use the following table
as a reference. The table following
each AWS Snowball Edge job management API
operation and the corresponding actions for which you can grant permissions to perform
the action. It also includes for each API operation the AWS resource for which you can
grant the permissions. You specify the actions in the policy's `Action`
field, and you specify the resource value in the policy's `Resource` field.

You can use AWS-wide condition keys in your AWS Snowball Edge policies to express
conditions. For a complete list of AWS-wide keys, see [Available
Keys](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.

###### Note

To specify an action, use the `snowball:` prefix followed by the API
operation name (for example, `snowball:CreateJob`).

Use the scroll bars to see the rest of the table.

| AWS Snowball Edge Job Management API and Required Permissions for Actions                                  | Job Management API Actions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Required Permissions |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| [CancelCluster](../api-reference/API_CancelCluster.md "../api-reference/API_CancelCluster.md")             | `snowball:CancelCluster`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [CancelJob](../api-reference/API_CancelJob.md "../api-reference/API_CancelJob.md")                         | `snowball:CancelJob`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [CreateAddress](../api-reference/API_CreateAddress.md "../api-reference/API_CreateAddress.md")             | `snowball:CreateAddress`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [CreateCluster](../api-reference/API_CreateCluster.md "../api-reference/API_CreateCluster.md")             | This action requires the following permissions: <br>• The complete console permissions in [Permissions Required to Use the AWS Snowball Edge Console](access-control-managing-permissions.md#additional-console-required-permissions "access-control-managing-permissions.md#additional-console-required-permissions") <br>• The additional API-only permissions in [Example 1: Role Policy That Allows a User to Create a Job to order a Snowball Edge device with the API](#access-policy-example-create-api "#access-policy-example-create-api") <br>• `snowball:CreateCluster` |
| [CreateJob](../api-reference/API_CreateJob.md "../api-reference/API_CreateJob.md")                         | <br>• The complete console permissions in [Permissions Required to Use the AWS Snowball Edge Console](access-control-managing-permissions.md#additional-console-required-permissions "access-control-managing-permissions.md#additional-console-required-permissions") <br>• The additional API-only permissions in [Example 1: Role Policy That Allows a User to Create a Job to order a Snowball Edge device with the API](#access-policy-example-create-api "#access-policy-example-create-api") <br>• `snowball:CreateJob`                                                     |
| [DescribeAddress](../api-reference/API_DescribeAddress.md "../api-reference/API_DescribeAddress.md")       | `snowball:DescribeAddress`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [DescribeAddresses](../api-reference/API_DescribeAddresses.md "../api-reference/API_DescribeAddresses.md") | `snowball:DescribeAddresses`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [DescribeCluster](../api-reference/API_DescribeCluster.md "../api-reference/API_DescribeCluster.md")       | `snowball:DescribeCluster`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [DescribeJob](../api-reference/API_DescribeJob.md "../api-reference/API_DescribeJob.md")                   | `snowball:DescribeJob`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [GetJobManifest](../api-reference/API_GetJobManifest.md "../api-reference/API_GetJobManifest.md")          | `snowball:GetJobManifest`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [GetJobUnlockCode](../api-reference/API_GetJobUnlockCode.md "../api-reference/API_GetJobUnlockCode.md")    | `snowball:GetJobUnlockCode`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [GetSnowballUsage](../api-reference/API_GetSnowballUsage.md "../api-reference/API_GetSnowballUsage.md")    | `snowball:GetSnowballUsage`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [ListClusterJobs](../api-reference/API_ListClusterJobs.md "../api-reference/API_ListClusterJobs.md")       | `snowball:ListClusterJobs`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [ListClusters](../api-reference/API_ListClusters.md "../api-reference/API_ListClusters.md")                | `snowball:ListClusters`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [ListJobs](../api-reference/API_ListJobs.md "../api-reference/API_ListJobs.md")                            | `snowball:ListJobs`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [UpdateCluster](../api-reference/API_UpdateCluster.md "../api-reference/API_UpdateCluster.md")             | `snowball:UpdateCluster`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [UpdateJob](../api-reference/API_UpdateJob.md "../api-reference/API_UpdateJob.md")                         | `snowball:UpdateJob`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
