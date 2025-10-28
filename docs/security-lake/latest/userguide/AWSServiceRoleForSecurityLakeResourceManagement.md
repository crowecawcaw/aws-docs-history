# Service-linked role (SLR) permissions for resource management

Security Lake uses the service-linked role named
`AWSServiceRoleForSecurityLakeResourceManagement` to perform ongoing
monitoring and performance improvements, which can reduce latency and costs. This
service-linked role trusts the
`resource-management.securitylake.amazonaws.com` service to assume the
role. Enabling `AWSServiceRoleForSecurityLakeResourceManagement` will also
grant it access to Lake Formation and automatically register your Security Lake managed S3 buckets with
Lake Formation across all Regions for improved security.

The permissions policy for the role, which is an AWS managed policy named
`SecurityLakeResourceManagementServiceRolePolicy`, allows access to
manage resources created by Security Lake; including managing the metadata in your data
lake. For more information about, AWS managed policies for Amazon Security Lake, see [AWS managed policies for Amazon Security Lake](security-iam-awsmanpol.md#security-iam-awsmanpol-SecurityLakeServiceLinkedRole-ResourceManagement.html "security-iam-awsmanpol.md#security-iam-awsmanpol-SecurityLakeServiceLinkedRole-ResourceManagement.html").

This service-linked role allows Security Lake to monitor the health of the resources
deployed by Security Lake (S3 Bucket, AWS Glue tables, Amazon SQS Queue, Metastore Manager (MSM)
Lambda Function, and EventBridge rules) to your account. Some examples of operations
that Security Lake can perform with this service-linked role are:

- Apache Iceberg manifest file compaction, which improves query performance and lowers Lambda MSM processing times and costs.
- Monitor the state of Amazon SQS to detect ingestion issues.
- Optimize cross region data replication to exclude metadata files.

###### Note

If you do not install the `AWSServiceRoleForSecurityLakeResourceManagement`
service-linked role, Security Lake will continue to function but it's highly recommended
to accept this service-linked role so Security Lake can monitor and optimize the resources
in your account.

**Permissions details**

The role is configured with the following permissions policy:

- `events` – Allows principals to manage EventBridge rules required for log sources and log subscribers.
- `lambda` – Allows principals to manage the lambda used to update AWS Glue table partitions following AWS source delivery and cross-region replication.
- `glue` – Allows principals to perform specific write actions for AWS Glue Data Catalog tables. This also allows AWS Glue crawlers to identify partitions in your data, and allows
  Security Lake to manage Apache Iceberg metadata for your Apache Iceberg tables.
- `s3` – Allows principals to perform specific read and write actions on the Security Lake buckets containing log data and Glue table metadata.
- `logs` – Allows principals read access to log the output
  of the Lambda function to CloudWatch Logs.
- `sqs` – Allows principals to perform specific read and
  write actions for Amazon SQS queues that receive event notifications when objects are
  added to or updated in your data lake.
- `lakeformation` – Allows principals to read Lake Formation settings to monitor for misconfigurations.
  To review the permissions for this policy, see [SecurityLakeResourceManagementServiceRolePolicy](../../../aws-managed-policy/latest/reference/SecurityLakeResourceManagementServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/SecurityLakeResourceManagementServiceRolePolicy.md") in the _AWS Managed Policy Reference Guide_.

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating the Security Lake service-linked role

You can create the
`AWSServiceRoleForSecurityLakeResourceManagement` service-linked role
for Security Lake using the Security Lake console or the AWS CLI.

To create the service-linked role you must grant the following permissions to your IAM user or IAM role. The IAM role must be a Lake Formation administrator in all Security Lake enabled Regions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowLakeFormationActionsViaSecurityLakeConsole",
 "Effect": "Allow",
 "Action": [
 "lakeformation:GrantPermissions",
 "lakeformation:ListPermissions",
 "lakeformation:ListResources",
 "lakeformation:RegisterResource",
 "lakeformation:RevokePermissions"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowIamActionsViaSecurityLakeConsole",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole",
 "iam:GetPolicyVersion",
 "iam:GetRole",
 "iam:PutRolePolicy"
 ],
 "Resource": [
 "arn:*:iam::*:role/aws-service-role/resource-management.securitylake.amazonaws.com/AWSServiceRoleForSecurityLakeResourceManagement",
 "arn:*:iam::*:role/*AWSServiceRoleForLakeFormationDataAccess",
 "arn:*:iam::aws:policy/service-role/AWSGlueServiceRole",
 "arn:*:iam::aws:policy/service-role/AmazonSecurityLakeMetastoreManager",
 "arn:*:iam::aws:policy/aws-service-role/SecurityLakeResourceManagementServiceRolePolicy"
 ],
 "Condition": {
 "StringLikeIfExists": {
 "iam:AWSServiceName": [
 "securitylake.amazonaws.com",
 "resource-management.securitylake.amazonaws.com",
 "lakeformation.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "AllowGlueActionsViaConsole",
 "Effect": "Allow",
 "Action": [
 "glue:GetDatabase",
 "glue:GetTables"
 ],
 "Resource": [
 "arn:*:glue:*:*:catalog",
 "arn:*:glue:*:*:database/amazon_security_lake_glue_db*",
 "arn:*:glue:*:*:table/amazon_security_lake_glue_db*/*"
 ]
 }
 ]
}`

```

Console1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/"). 2. Accept the new service-linked role by clicking **Enable service-linked role**
in the information bar on the Summary page.

Once you’ve enabled the service-linked role, you won’t
need to repeat this process for future use of Security Lake.

CLI
To create the
`AWSServiceRoleForSecurityLakeResourceManagement`
service-linked role programatically, use the following CLI command.

```
`$` `aws iam create-service-linked-role
--aws-service-name resource-management.securitylake.amazonaws.com`
```

When creating the
`AWSServiceRoleForSecurityLakeResourceManagement`
service-linked role using AWS CLI, you must also grant it Lake Formation table-level
permissions (ALTER, DESCRIBE) to all tables on the Security Lake Glue
database to manage table metadata and access data. If Glue tables in any
region reference S3 buckets from previous Security Lake enablement, you must
temporarily allow DATA_LOCATION_ACCESS permissions to the service-linked
role to allow Security Lake to remediate this situation.

You also have to grant Lake Formation permissions to the `AWSServiceRoleForSecurityLakeResourceManagement` service-linked role for your account.

The following example shows how to grant the Lake Formation permissions to the service-linked role in the designated Region. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws lakeformation grant-permissions --region `{region}` --principal DataLakePrincipalIdentifier=`{AWSServiceRoleForSecurityLakeResourceManagement ARN}` \
--permissions ALTER DESCRIBE --resource '{ "Table": { "DatabaseName": "amazon_security_lake_glue_db_`{region}`", "TableWildcard": {} } }'`
```

The following example shows how the Role ARN will look like. You must edit the Role ARN to match your Region.

`"AWS": "arn:[partition]:iam::[accountid]:role/aws-service-role/resource-management.securitylake.amazonaws.com/AWSServiceRoleForSecurityLakeResourceManagement"`

You can also use the [CreateServiceLinkedRole](../../../IAM/latest/APIReference/API_CreateServiceLinkedRole.md "../../../IAM/latest/APIReference/API_CreateServiceLinkedRole.md") API call. In the request, specify
the `AWSServiceName` as
`resource-management.securitylake.amazonaws.com`.

After enabling the `AWSServiceRoleForSecurityLakeResourceManagement` role, if you are using AWS KMS Customer Managed Key (CMK) for encryption, you must allow the service-linked role
to write encrypted objects to S3 buckets in the AWS
Regions where CMK exists. In the AWS KMS console, add the
following policy to the KMS key in the AWS Regions where CMK exists.
For the details on how to change the KMS key policy, see [Key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the AWS Key Management Service Developer Guide.

```
{
    "Sid": "Allow SLR",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:[partition]:iam::[accountid]:role/aws-service-role/resource-management.securitylake.amazonaws.com/AWSServiceRoleForSecurityLakeResourceManagement"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey*"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::[regional-datalake-s3-bucket-name]"
        },
        "StringLike": {
            "kms:ViaService": "s3.[region].amazonaws.com"
        }
    }
},
```

## Editing the Security Lake service-linked role

Security Lake doesn't allow you to edit the
`AWSServiceRoleForSecurityLakeResourceManagement` service-linked
role. After a service-linked role is created, you can't change the name of the role
because various entities might reference the role. However, you can edit the
description of the role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting the Security Lake service-linked role

You cannot delete the service-linked role from Security Lake. Instead, you may delete the service-linked role from the IAM
console, API, or AWS CLI. For more information, see
[Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

Before you can delete the service-linked role, you must first confirm that the
role has no active sessions and remove any resources that
`AWSServiceRoleForSecurityLakeResourceManagement` is using.

###### Note

If Security Lake is using the
`AWSServiceRoleForSecurityLakeResourceManagement` role when you
try to delete the resources, the deletion might fail. If that happens, wait a
few minutes and then try the operation again.

If you delete the `AWSServiceRoleForSecurityLakeResourceManagement`
service-linked role and need to create it again, you can create it again by enabling
Security Lake for your account. When you enable Security Lake again, Security Lake automatically
creates the service-linked role again for you.

## Supported AWS Regions for the Security Lake service-linked role

Security Lake supports using the
`AWSServiceRoleForSecurityLakeResourceManagement` service-linked role
in all the AWS Regions where Security Lake is available. For a list of Regions where
Security Lake is currently available, see [Security Lake Regions and endpoints](supported-regions.md "supported-regions.md").
