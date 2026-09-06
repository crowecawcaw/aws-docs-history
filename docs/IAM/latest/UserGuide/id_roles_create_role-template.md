# Overview of role templates

A role template is a role blueprint used to create new roles. The template sets the role's
trust policy and permissions so you get a ready-to-use role for a service without writing the
policies yourself.

Role manager uses AWS-managed role templates, but you can also use role templates without
role manager. This page explains how role templates work and lists the template for each
service.

## How role templates work

A role template contains a trust policy and permissions, and has an Amazon Resource Name
(ARN). The trust policy defines which principals can assume the role. The permissions define
what the role can do. Template versions are immutable. When AWS updates a template, it
publishes a new version rather than changing an existing one.

Role templates may accept additional parameters to customize and scope the role's
properties and permissions. For example, a template might take a `RoleName` for the
role it creates, or a resource identifier such as a `bucketName`. When role manager
creates a role in the console, it applies the parameters to the permissions and trust policy
for the role. When you create a role from a template directly with the IAM API, you supply
these parameters.

To create a role from a template, use the `iam:AcquireRole` API with the
template's ARN and pass the parameters that the template requires.

A role template's definitions can change between versions. To see the current trust policy
and permissions for a template, retrieve it with `iam:GetRoleTemplateVersion` using
the template ARN. AWS recommends inspecting the template before relying on it, especially
for a template that grants broad access.

## How role manager uses templates

When creating a resource in a supported service console, role manager provides a role from
the template that matches the service and use case. Role manager chooses the template and
supplies the parameters for you. The result is the same role that you would get calling
`iam:AcquireRole`. To enable role manager, see [Manage access to role manager](id_roles_create_role-manager_enable-use.md "id_roles_create_role-manager_enable-use.md").

## Role template directory

The following table lists the role template for each service that role manager supports,
with the template ARN and the parameters it takes. Use the ARN to create a role from the
template, or to review what role manager grants for that service. Services are listed
alphabetically.

| Service                         | Role template                                               | Template ARN                                                                                                                            | Parameters                                                                                                 |
| ------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| AWS Backup                      | AWSBackupDefaultServiceRoleTemplate                         | `arn:aws:iam::aws:role-template/backup.amazonaws.com/AWSBackupDefaultServiceRoleTemplate:1`                                             | accountId, RoleName                                                                                        |
| AWS CloudFormation              | PowerUserRoleTemplate                                       | `arn:aws:iam::aws:role-template/iam.amazonaws.com/PowerUserRoleTemplate:1`                                                              | AWSServiceName, RoleName                                                                                   |
| AWS Elastic Beanstalk           | PowerUserRoleTemplate                                       | `arn:aws:iam::aws:role-template/iam.amazonaws.com/PowerUserRoleTemplate:1`                                                              | AWSServiceName, RoleName                                                                                   |
| Amazon EventBridge              | PowerUserRoleTemplate                                       | `arn:aws:iam::aws:role-template/iam.amazonaws.com/PowerUserRoleTemplate:1`                                                              | AWSServiceName, RoleName                                                                                   |
| AWS Lambda                      | PowerUserRoleTemplate                                       | `arn:aws:iam::aws:role-template/iam.amazonaws.com/PowerUserRoleTemplate:1`                                                              | AWSServiceName, RoleName                                                                                   |
| Amazon SageMaker Unified Studio | AmazonSageMakerAdminIAMPermissiveExecutionRoleTemplate      | `arn:aws:iam::aws:role-template/datazone.amazonaws.com/AmazonSageMakerAdminIAMPermissiveExecutionRoleTemplate:1`                        | CMK\_ENABLED, RoleName, accountId, keyAccountId, keyRegion, kmsKeyId                                       |
| Amazon SageMaker Unified Studio | AmazonSageMakerUserIAMPermissiveExecutionRoleTemplate       | `arn:aws:iam::aws:role-template/datazone.amazonaws.com/AmazonSageMakerUserIAMPermissiveExecutionRoleTemplate:1`                         | RoleName, accountId                                                                                        |
| AWS Secrets Manager             | AWSSecretsManagerRotationRoleTemplate                       | `arn:aws:iam::aws:role-template/secretsmanager.amazonaws.com/AWSSecretsManagerRotationRoleTemplate:1`                                   | ADMIN\_RESOURCE\_ENABLED, CMK\_ENABLED, RoleName, accountId, adminType,<br>kmsKeyArn, region, resourceType |
| Amazon CloudWatch               | PowerUserRoleTemplate                                       | `arn:aws:iam::aws:role-template/iam.amazonaws.com/PowerUserRoleTemplate:1`                                                              | AWSServiceName, RoleName                                                                                   |
| Amazon CloudWatch               | AmazonCloudWatchLogsScheduledQueryExecutionRoleTemplate     | `arn:aws:iam::aws:role-template/logs.amazonaws.com/AmazonCloudWatchLogsScheduledQueryExecutionRoleTemplate:1`                           | RoleName, account, region                                                                                  |
| Amazon CloudWatch               | AmazonCloudWatchMetricStreamsFirehosePutRecordsRoleTemplate | `arn:aws:iam::aws:role-template/streams.metrics.cloudwatch.amazonaws.com/AmazonCloudWatchMetricStreamsFirehosePutRecordsRoleTemplate:1` | RoleName, accountId, deliveryStreamName, region                                                            |
| Amazon CloudWatch               | AmazonCloudWatchMetricStreamsFirehoseToS3RoleTemplate       | `arn:aws:iam::aws:role-template/firehose.amazonaws.com/AmazonCloudWatchMetricStreamsFirehoseToS3RoleTemplate:1`                         | RoleName, accountId, bucketName, logGroupName, logStreamName, region                                       |
| Amazon CloudWatch               | AmazonCloudWatchRUMPutEventsRoleTemplate                    | `arn:aws:iam::aws:role-template/rum.amazonaws.com/AmazonCloudWatchRUMPutEventsRoleTemplate:1`                                           | RoleName, accountId, appMonitor, identityPool, region                                                      |
| Amazon CloudWatch               | AmazonCloudWatchSyntheticsExecutionRoleTemplate             | `arn:aws:iam::aws:role-template/synthetics.amazonaws.com/AmazonCloudWatchSyntheticsExecutionRoleTemplate:1`                             | RoleName, account\_id, canary\_name, region\_name, role\_uuid                                              |
| Amazon CloudWatch               | AmazonCloudWatchSyntheticsKmsExecutionRoleTemplate          | `arn:aws:iam::aws:role-template/synthetics.amazonaws.com/AmazonCloudWatchSyntheticsKmsExecutionRoleTemplate:1`                          | RoleName, account\_id, canary\_name, region\_name, role\_uuid                                              |
| Amazon CloudWatch               | AmazonCloudWatchSyntheticsVpcExecutionRoleTemplate          | `arn:aws:iam::aws:role-template/synthetics.amazonaws.com/AmazonCloudWatchSyntheticsVpcExecutionRoleTemplate:1`                          | RoleName, account\_id, canary\_name, region\_name, role\_uuid                                              |

## Related information

- [Create roles automatically with role manager](id_roles_create_role-manager.md "id_roles_create_role-manager.md")
- [Manage access to role manager](id_roles_create_role-manager_enable-use.md "id_roles_create_role-manager_enable-use.md")
- [IAM API Reference](../APIReference/welcome.md "../APIReference/welcome.md")
