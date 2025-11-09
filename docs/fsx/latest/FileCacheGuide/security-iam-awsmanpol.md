# AWS managed policies for Amazon File Cache

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

## AmazonFSxServiceRolePolicy

Allows Amazon FSx to manage AWS resources on your behalf. See
[Using service-linked roles for
Amazon FSx](using-service-linked-roles.md "using-service-linked-roles.md") to learn more.

## AWS managed policy: AmazonFSxDeleteServiceLinkedRoleAccess

You can't attach `AmazonFSxDeleteServiceLinkedRoleAccess` to your IAM entities. This policy is linked to a service and used
only with the service-linked role for that service. You cannot attach, detach, modify, or delete this policy. For more
information, see [Using service-linked roles for
Amazon FSx](using-service-linked-roles.md "using-service-linked-roles.md").

This policy grants administrative permissions that allow Amazon FSx to delete its Service Linked Role for Amazon S3 access, used only by Amazon FSx for Lustre.

**Permissions details**

This policy includes permissions in `iam` to allow Amazon FSx to view, delete, and view the deletion status for the FSx Service Linked Roles for Amazon S3 access.

To view the permissions for this policy, see
[AmazonFSxDeleteServiceLinkedRoleAccess](../../../aws-managed-policy/latest/reference/FSxDeleteServiceLinkedRoleAccess.md "../../../aws-managed-policy/latest/reference/FSxDeleteServiceLinkedRoleAccess.md")
in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonFSxFullAccess

You can attach AmazonFSxFullAccess to your IAM entities. Amazon FSx also attaches this policy to
a service role that allows Amazon FSx to perform actions on your behalf.

Provides full access to Amazon FSx and access to related AWS services.

**Permissions details**

This policy includes the following permissions.

- `fsx` – Allows principals full access to perform all Amazon FSx actions,
  except for `BypassSnaplockEnterpriseRetention`.
- `ds` – Allows principals to view information about the AWS Directory Service directories.
- `ec2`
  - Allows principals to create tags under the specified conditions.
  - To provide enhanced security group validation of all security groups that can be used with a VPC.

- `iam` – Allows principles to create an Amazon FSx service linked role on the user's behalf.
  This is required so that Amazon FSx can manage AWS resources on the user's behalf.
- `firehose` – Allows principals to write records to a Amazon Data Firehose. This is required so that users can
  monitor FSx for Windows File Server file system access by sending audit access logs to Firehose.
- `logs` – Allows principals to create log groups, log streams, and write events to log streams. This is
  required so that users can monitor FSx for Windows File Server file system access by sending audit access logs to CloudWatch Logs.

To view the permissions for this policy, see
[AmazonFSxFullAccess](../../../aws-managed-policy/latest/reference/AmazonFSxFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonFSxFullAccess.md")
in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonFSxConsoleFullAccess

You can attach the `AmazonFSxConsoleFullAccess` policy to your IAM identities.

This policy grants administrative permissions that allow full access to Amazon FSx and
access to related AWS services via the AWS Management Console.

**Permissions details**

This policy includes the following permissions.

- `fsx` – Allows principals to perform all actions in the Amazon FSx management console,
  except for `BypassSnaplockEnterpriseRetention`.
- `cloudwatch` – Allows principals to view CloudWatch Alarms and metrics in the Amazon FSx management console.
- `ds` – Allows principals to list information about an AWS Directory Service directory.
- `ec2`
  - Allows principals to create tags on route tables, list network interfaces, route tables,
    security groups, subnets and the VPC associated with an Amazon FSx file system.
  - Allows principals to provide enhanced security group validation of all security groups
    that can be used with a VPC.
  - Allows principals to view the elastic network interfaces associated with an Amazon FSx file system.

- `kms` – Allows principals to list aliases for AWS Key Management Service keys.
- `s3` – Allows principals to list some or all of the objects in an Amazon S3 bucket (up to 1000).
- `iam` – Grants permission to create a service linked role that allows Amazon FSx to perform actions on the user's behalf.

To view the permissions for this policy, see
[AmazonFSxConsoleFullAccess](../../../aws-managed-policy/latest/reference/AmazonFSxConsoleFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonFSxConsoleFullAccess.md")
in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonFSxConsoleReadOnlyAccess

You can attach the `AmazonFSxConsoleReadOnlyAccess` policy to your IAM identities.

This policy grants read-only permissions to Amazon FSx and related AWS services so
that users can view information about these services in the AWS Management Console.

**Permissions details**

This policy includes the following permissions.

- `fsx` – Allows principals to view information about Amazon FSx file systems, including all tags, in the Amazon FSx Management Console.
- `cloudwatch` – Allows principals to view CloudWatch Alarms and metrics in the Amazon FSx Management Console.
- `ds` – Allows principals to view information about an AWS Directory Service directory in the Amazon FSx Management Console.
- `ec2`
  - Allows principals to view network interfaces, security groups, subnets and the VPC associated with an Amazon FSx
    file system in the Amazon FSx Management Console.
  - Allows principals to provide enhanced security group validation of all security groups that can be used with a VPC.
  - Allows principals to view the elastic network interfaces associated with an Amazon FSx file system.

- `kms` – Allows principals to view aliases for AWS Key Management Service keys in the Amazon FSx Management Console.
- `log` – Allows principals to describe the Amazon CloudWatch Logs log groups associated with the account making the request.
  This is required so that principals can view the existing file access auditing configuration for an FSx for Windows File Server file system.
- `firehose` – Allows principals to describe the Amazon Data Firehose delivery streams associated with the account making the request.
  This is required so that principals can view the existing file access auditing configuration for an FSx for Windows File Server file system.

To view the permissions for this policy, see
[AmazonFSxConsoleReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonFSxConsoleReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonFSxConsoleReadOnlyAccess.md")
in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonFSxReadOnlyAccess

You can attach the `AmazonFSxReadOnlyAccess` policy to your IAM identities.

- `fsx` – Allows principals to view information about Amazon FSx file systems, including all tags, in the Amazon FSx Management Console.
- `ec2` – To provide enhanced security group validation of all security groups that can be used with a VPC.

To view the permissions for this policy, see
[AmazonFSxReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonFSxReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonFSxReadOnlyAccess.md")
in the AWS Managed Policy Reference Guide.

## Amazon FSx updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon FSx since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the Amazon FSx [Document history](doc-history.md "doc-history.md") page.

| Change                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                             | Date               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AmazonFSxServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Update to an existing policy                                          | Amazon FSx added a new permission, `ec2:AssignIpv6Addresses` that allows principals to assign IPv6 addresses<br>to customer network interfaces that have an `AmazonFSx.FileSystemId` tag.                                                                                                                                               | July 22, 2025      |
| [AmazonFSxServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Update to an existing policy                                          | Amazon FSx added a new permission, `ec2:UnassignIpv6Addresses` that allows principals to unassign IPv6 addresses<br>from customer network interfaces that have an `AmazonFSx.FileSystemId` tag.                                                                                                                                         | July 22, 2025      |
| [AmazonFSxConsoleFullAccess](#security-iam-awsmanpol-AmazonFSxConsoleFullAccess "#security-iam-awsmanpol-AmazonFSxConsoleFullAccess") – Update to an existing policy                                | Amazon FSx added a new permission, `fsx:CreateAndAttachS3AccessPoint` that allows principals to create an S3 access point and attach it to an FSx volume.                                                                                                                                                                               | June 25, 2025      |
| [AmazonFSxConsoleFullAccess](#security-iam-awsmanpol-AmazonFSxConsoleFullAccess "#security-iam-awsmanpol-AmazonFSxConsoleFullAccess") – Update to an existing policy                                | Amazon FSx added a new permission, `fsx:DescribeS3AccessPointAttachments` that allows principals to list all S3 access points in an AWS account in an AWS Region.                                                                                                                                                                       | June 25, 2025      |
| [AmazonFSxConsoleFullAccess](#security-iam-awsmanpol-AmazonFSxConsoleFullAccess "#security-iam-awsmanpol-AmazonFSxConsoleFullAccess") – Update to an existing policy                                | Amazon FSx added a new permission, `fsx:DetachAndDeleteS3AccessPoint` that allows principals to delete an S3 access point.                                                                                                                                                                                                              | June 25, 2025      |
| [AmazonFSxFullAccess](#security-iam-awsmanpol-AmazonFSxFullAccess "#security-iam-awsmanpol-AmazonFSxFullAccess") – Update to an existing policy                                                     | Amazon FSx added a new permission, `fsx:CreateAndAttachS3AccessPoint` that allows principals to create an S3 access point and attach it to an FSx volume.                                                                                                                                                                               | June 25, 2025      |
| [AmazonFSxFullAccess](#security-iam-awsmanpol-AmazonFSxFullAccess "#security-iam-awsmanpol-AmazonFSxFullAccess") – Update to an existing policy                                                     | Amazon FSx added a new permission, `fsx:DescribeS3AccessPointAttachments` that allows principals to list all S3 access points in an AWS account in an AWS Region.                                                                                                                                                                       | June 25, 2025      |
| [AmazonFSxFullAccess](#security-iam-awsmanpol-AmazonFSxFullAccess "#security-iam-awsmanpol-AmazonFSxFullAccess") – Update to an existing policy                                                     | Amazon FSx added a new permission, `fsx:DetachAndDeleteS3AccessPoint` that allows principals to delete an S3 access point.                                                                                                                                                                                                              | June 25, 2025      |
| [AmazonFSxConsoleReadOnlyAccess](#security-iam-awsmanpol-AmazonFSxConsoleReadOnlyAccess "#security-iam-awsmanpol-AmazonFSxConsoleReadOnlyAccess") – Update to an existing policy                    | Amazon FSx added new permission, `ec2:DescribeNetworkInterfaces` that allows principals to view the elastic network interfaces associated with their file system.                                                                                                                                                                       | February 25, 2025  |
| [AmazonFSxConsoleFullAccess](#security-iam-awsmanpol-AmazonFSxConsoleFullAccess "#security-iam-awsmanpol-AmazonFSxConsoleFullAccess") – Update to an existing policy                                | Amazon FSx added new permission, `ec2:DescribeNetworkInterfaces` that allows principals to view the elastic network interfaces associated with their file system.                                                                                                                                                                       | February 07, 2025  |
| [AmazonFSxServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Update to an existing policy                                          | Amazon FSx added new permission, `ec2:GetSecurityGroupsForVpc` that allows principals to provide enhanced security group validation of all security groups that can be used with a VPC.                                                                                                                                                 | January 9, 2024    |
| [AmazonFSxReadOnlyAccess](#security-iam-awsmanpol-AmazonFSxReadOnlyAccess "#security-iam-awsmanpol-AmazonFSxReadOnlyAccess") – Update to an existing policy                                         | Amazon FSx added new permission, `ec2:GetSecurityGroupsForVpc` that allows principals to provide enhanced security group validation of all security groups that can be used with a VPC.                                                                                                                                                 | January 9, 2024    |
| [AmazonFSxConsoleReadOnlyAccess](#security-iam-awsmanpol-AmazonFSxConsoleReadOnlyAccess "#security-iam-awsmanpol-AmazonFSxConsoleReadOnlyAccess") – Update to an existing policy                    | Amazon FSx added new permission, `ec2:GetSecurityGroupsForVpc` that allows principals to provide enhanced security group validation of all security groups that can be used with a VPC.                                                                                                                                                 | January 9, 2024    |
| [AmazonFSxFullAccess](#security-iam-awsmanpol-AmazonFSxFullAccess "#security-iam-awsmanpol-AmazonFSxFullAccess") – Update to an existing policy                                                     | Amazon FSx added new permission, `ec2:GetSecurityGroupsForVpc` that allows principals to provide enhanced security group validation of all security groups that can be used with a VPC.                                                                                                                                                 | January 9, 2024    |
| [AmazonFSxConsoleFullAccess](#security-iam-awsmanpol-AmazonFSxConsoleFullAccess "#security-iam-awsmanpol-AmazonFSxConsoleFullAccess") – Update to an existing policy                                | Amazon FSx added new permission, `ec2:GetSecurityGroupsForVpc` that allows principals to provide enhanced security group validation of all security groups that can be used with a VPC.                                                                                                                                                 | January 9, 2024    |
| [AmazonFSxFullAccess](#security-iam-awsmanpol-AmazonFSxFullAccess "#security-iam-awsmanpol-AmazonFSxFullAccess") – Update to an existing policy                                                     | Amazon FSx added new permission to enable users to perform cross-region and cross-account data replication for FSx for OpenZFS file systems.                                                                                                                                                                                            | December 20, 2023  |
| [AmazonFSxConsoleFullAccess](#security-iam-awsmanpol-AmazonFSxConsoleFullAccess "#security-iam-awsmanpol-AmazonFSxConsoleFullAccess") – Update to an existing policy                                | Amazon FSx added new permission to enable users to perform cross-region and cross-account data replication for FSx for OpenZFS file systems.                                                                                                                                                                                            | December 20, 2023  |
| [AmazonFSxFullAccess](#security-iam-awsmanpol-AmazonFSxFullAccess "#security-iam-awsmanpol-AmazonFSxFullAccess") – Update to an existing policy                                                     | Amazon FSx added new permission to enable users to perform on-demand replication of volumes for FSx for OpenZFS file systems.                                                                                                                                                                                                           | November 26, 2023  |
| [AmazonFSxConsoleFullAccess](#security-iam-awsmanpol-AmazonFSxConsoleFullAccess "#security-iam-awsmanpol-AmazonFSxConsoleFullAccess") – Update to an existing policy                                | Amazon FSx added new permission to enable users to perform on-demand replication of volumes for FSx for OpenZFS file systems.                                                                                                                                                                                                           | November 26, 2023  |
| [AmazonFSxFullAccess](#security-iam-awsmanpol-AmazonFSxFullAccess "#security-iam-awsmanpol-AmazonFSxFullAccess") – Update to an existing policy                                                     | Amazon FSx added new permissions to enable users to view, enable, and disable shared VPC support for FSx for ONTAP Multi-AZ file systems.                                                                                                                                                                                               | November 14, 2023  |
| [AmazonFSxConsoleFullAccess](#security-iam-awsmanpol-AmazonFSxConsoleFullAccess "#security-iam-awsmanpol-AmazonFSxConsoleFullAccess") – Update to an existing policy                                | Amazon FSx added new permissions to enable users to view, enable, and disable shared VPC support for FSx for ONTAP Multi-AZ file systems.                                                                                                                                                                                               | November 14, 2023  |
| [AmazonFSxFullAccess](#security-iam-awsmanpol-AmazonFSxFullAccess "#security-iam-awsmanpol-AmazonFSxFullAccess") – Update to an existing policy                                                     | Amazon FSx added new permissions to allow Amazon FSx to manage network configurations for FSx for OpenZFS Multi-AZ file systems.                                                                                                                                                                                                        | August 9, 2023     |
| [AWS managed policy: AmazonFSxServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Update to an existing policy                      | Amazon FSx modified the existing `cloudwatch:PutMetricData` permission so that Amazon FSx publishes CloudWatch metrics to the `AWS/FSx` namespace.                                                                                                                                                                                      | July 24, 2023      |
| [AmazonFSxFullAccess](#security-iam-awsmanpol-AmazonFSxFullAccess "#security-iam-awsmanpol-AmazonFSxFullAccess") – Update to an existing policy                                                     | Amazon FSx updated the policy to remove the `fsx:*` permission and add specific `fsx` actions.                                                                                                                                                                                                                                          | July 13, 2023      |
| [AmazonFSxConsoleFullAccess](#security-iam-awsmanpol-AmazonFSxConsoleFullAccess "#security-iam-awsmanpol-AmazonFSxConsoleFullAccess") – Update to an existing policy                                | Amazon FSx updated the policy to remove the `fsx:*` permission and add specific `fsx` actions.                                                                                                                                                                                                                                          | July 13, 2023      |
| [AmazonFSxConsoleReadOnlyAccess](#security-iam-awsmanpol-AmazonFSxConsoleReadOnlyAccess "#security-iam-awsmanpol-AmazonFSxConsoleReadOnlyAccess") – Update to an existing policy                    | Amazon FSx added new permissions to enable users to view enhanced performance metrics and recommended actions for FSx for Windows File Server<br>file systems in the Amazon FSx console.                                                                                                                                                | September 21, 2022 |
| [AmazonFSxConsoleFullAccess](#security-iam-awsmanpol-AmazonFSxConsoleFullAccess "#security-iam-awsmanpol-AmazonFSxConsoleFullAccess") – Update to an existing policy                                | Amazon FSx added new permissions to enable users to view enhanced performance metrics and recommended actions for FSx for Windows File Server<br>file systems in the Amazon FSx console.                                                                                                                                                | September 21, 2022 |
| [AmazonFSxReadOnlyAccess](#security-iam-awsmanpol-AmazonFSxReadOnlyAccess "#security-iam-awsmanpol-AmazonFSxReadOnlyAccess") – Started tracking policy                                              | This policy grants read-only access to all Amazon FSx resources and any tags associated with them.                                                                                                                                                                                                                                      | February 4, 2022   |
| [AmazonFSxDeleteServiceLinkedRoleAccess](#security-iam-awsmanpol-AmazonFSxDeleteServiceLinkedRoleAccess "#security-iam-awsmanpol-AmazonFSxDeleteServiceLinkedRoleAccess") – Started tracking policy | This policy grants administrative permissions that allow Amazon FSx to delete its Service Linked Role for Amazon S3 access.                                                                                                                                                                                                             | January 7, 2022    |
| [AmazonFSxServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Update to an existing policy                                          | Amazon FSx added new permissions to allow Amazon FSx to manage network configurations for Amazon FSx for NetApp ONTAP file systems.                                                                                                                                                                                                     | September 2, 2021  |
| [AmazonFSxFullAccess](#security-iam-awsmanpol-AmazonFSxFullAccess "#security-iam-awsmanpol-AmazonFSxFullAccess") – Update to an existing policy                                                     | Amazon FSx added new permissions to allow Amazon FSx to create tags on EC2 route tables for scoped down calls.                                                                                                                                                                                                                          | September 2, 2021  |
| [AmazonFSxConsoleFullAccess](#security-iam-awsmanpol-AmazonFSxConsoleFullAccess "#security-iam-awsmanpol-AmazonFSxConsoleFullAccess") – Update to an existing policy                                | Amazon FSx added new permissions to allow Amazon FSx to create Amazon FSx for NetApp ONTAP Multi-AZ file systems.                                                                                                                                                                                                                       | September 2, 2021  |
| [AmazonFSxConsoleFullAccess](#security-iam-awsmanpol-AmazonFSxConsoleFullAccess "#security-iam-awsmanpol-AmazonFSxConsoleFullAccess") – Update to an existing policy                                | Amazon FSx added new permissions to allow Amazon FSx to create tags on EC2 route tables for scoped down calls.                                                                                                                                                                                                                          | September 2, 2021  |
| [AmazonFSxServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Update to an existing policy                                          | Amazon FSx added new permissions to allow Amazon FSx to describe and write to CloudWatch Logs log streams.<br>This is required so that users can view file access audit logs for FSx for Windows File Server file systems using CloudWatch Logs.                                                                                        | June 8, 2021       |
| [AmazonFSxServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") –<br>Update to an existing policy                                       | Amazon FSx added new permissions to allow Amazon FSx to describe and write to Amazon Data Firehose delivery streams.<br>This is required so that users can view file access audit logs for an FSx for Windows File Server file system using Amazon Data Firehose.                                                                       | June 8, 2021       |
| [AmazonFSxFullAccess](#security-iam-awsmanpol-AmazonFSxFullAccess "#security-iam-awsmanpol-AmazonFSxFullAccess") –<br>Update to an existing policy                                                  | Amazon FSx added new permissions to allow principals to describe and create CloudWatch Logs log groups, log streams, and write events to log streams.<br>This is required so that principals can view file access audit logs for FSx for Windows File Server file systems using CloudWatch Logs.                                        | June 8, 2021       |
| [AmazonFSxFullAccess](#security-iam-awsmanpol-AmazonFSxFullAccess "#security-iam-awsmanpol-AmazonFSxFullAccess") –<br>Update to an existing policy                                                  | Amazon FSx added new permissions to allow principals to describe and write records to a Amazon Data Firehose.<br>This is required so that users can view file access audit logs for an FSx for Windows File Server file system using Amazon Data Firehose.                                                                              | June 8, 2021       |
| [AmazonFSxConsoleFullAccess](#security-iam-awsmanpol-AmazonFSxConsoleFullAccess "#security-iam-awsmanpol-AmazonFSxConsoleFullAccess") –<br>Update to an existing policy                             | Amazon FSx added new permissions to allow principals to describe the Amazon CloudWatch Logs log groups associated with the account making the request.<br>This is required so that principals can choose an existing CloudWatch Logs log group when configuring file access auditing for an FSx for Windows File Server file system.    | June 8, 2021       |
| [AmazonFSxConsoleFullAccess](#security-iam-awsmanpol-AmazonFSxConsoleFullAccess "#security-iam-awsmanpol-AmazonFSxConsoleFullAccess") –<br>Update to an existing policy                             | Amazon FSx added new permissions to allow principals to describe the Amazon Data Firehose delivery streams associated with the account making the request.<br>This is required so that principals can choose an existing Firehose delivery stream when configuring file access auditing for an FSx for Windows File Server file system. | June 8, 2021       |
| [AmazonFSxConsoleReadOnlyAccess](#security-iam-awsmanpol-AmazonFSxConsoleReadOnlyAccess "#security-iam-awsmanpol-AmazonFSxConsoleReadOnlyAccess") –<br>Update to an existing policy                 | Amazon FSx added new permissions to allow principals to describe the Amazon CloudWatch Logs log groups associated with the account making the request.<br>This is required so that principals can view the existing file access auditing configuration for an FSx for Windows File Server file system.                                  | June 8, 2021       |
| [AmazonFSxConsoleReadOnlyAccess](#security-iam-awsmanpol-AmazonFSxConsoleReadOnlyAccess "#security-iam-awsmanpol-AmazonFSxConsoleReadOnlyAccess") –<br>Update to an existing policy                 | Amazon FSx added new permissions to allow principals to describe the Amazon Data Firehose delivery streams associated with the account making the request.<br>This is required so that principals can view the existing file access auditing configuration for an FSx for Windows File Server file system.                              | June 8, 2021       |
| Amazon FSx started tracking changes                                                                                                                                                                 | Amazon FSx started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                       | June 8, 2021       |
