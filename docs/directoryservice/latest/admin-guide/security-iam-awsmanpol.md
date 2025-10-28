# AWS managed policies for AWS Directory Service

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

The following sections describe the AWS managed policies that are specific to AWS Directory Service.
You can attach these policies to users in your account.

For more information, see [AWS
managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

## AWS managed

policy: AWSDirectoryServiceFullAccess

You can attach the `AWSDirectoryServiceFullAccess` policy to your IAM
identities. To view the full permissions for this policy, see [AWSDirectoryServiceFullAccess](../../../aws-managed-policy/latest/reference/AWSDirectoryServiceFullAccess.md "../../../aws-managed-policy/latest/reference/AWSDirectoryServiceFullAccess.md") in the _AWS Managed Policy
Reference_.

This policy grants administrative permissions that allow a principal full access to
all AWS Directory Service actions. Principals with these permissions can create, configure, and manage
directories, including Simple AD, AD Connector, and Managed Microsoft AD. They can also
manage directory sharing, trust relationships, and monitoring configurations. This
policy includes permissions to manage the underlying network infrastructure required for
directory services.

**Permissions details**

This policy includes the following permissions:

- `ds` – Allows principals full access to all AWS Directory Service
  actions.
- `ec2` – Allows principals to manage network interfaces,
  security groups, and describe VPC resources required for directory
  operations.
- `sns` – Allows principals to create and manage SNS topics
  for directory monitoring, specifically topics with names beginning with
  "DirectoryMonitoring".
- `iam` – Allows principals to list IAM roles for directory
  service operations.
- `organizations` – Allows principals to manage AWS
  Organizations integration and enable/disable service access for directory
  services.

## AWS managed

policy: AWSDirectoryServiceReadOnlyAccess

You can attach the `AWSDirectoryServiceReadOnlyAccess` policy to your IAM
identities. To view the full permissions for this policy, see [AWSDirectoryServiceReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSDirectoryServiceReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSDirectoryServiceReadOnlyAccess.md") in the _AWS Managed Policy
Reference_.

This policy grants read-only permissions that allow users to view information in
AWS Directory Service. Principals with this policy attached cannot make any updates to directories or
their configurations. For example, principals with these permissions can view directory
details, trust relationships, and monitoring configurations, but cannot create new
directories or modify existing ones. They can also view related EC2 network resources
and SNS topics associated with directories.

**Permissions details**

This policy includes the following permissions:

- `ds` – Allows users to perform read-only actions that return
  directory information. This includes API operations that start with
  `Check`, `Describe`, `Get`,
  `List`, or `Verify`.
- `ec2` – Allows users to describe network interfaces,
  subnets, and VPCs associated with directory services.
- `sns` – Allows users to list and get information about SNS
  topics and subscriptions used for directory monitoring.
- `organizations` – Allows users to describe AWS Organizations
  accounts and service access configurations related to directory services.

## AWS managed

policy: AWSDirectoryServiceDataFullAccess

You can attach the `AWSDirectoryServiceDataFullAccess` policy to your IAM
identities. To view the full permissions for this policy, see [AWSDirectoryServiceDataFullAccess](../../../aws-managed-policy/latest/reference/AWSDirectoryServiceDataFullAccess.md "../../../aws-managed-policy/latest/reference/AWSDirectoryServiceDataFullAccess.md") in the _AWS Managed Policy
Reference_.

This policy grants administrative permissions that allow a principal full access to
Directory Service Data operations. Principals with these permissions can create, update, and delete
Active Directory users and groups within managed directories. They can manage group
memberships, enable or disable users, and perform comprehensive user and group
management operations. This policy is designed for administrators who need to manage
Active Directory objects programmatically.

**Permissions details**

This policy includes the following permissions:

- `ds` – Allows principals to access directory data through
  the Directory Service Data API.
- `ds-data` – Allows principals full access to all Directory
  Service Data operations, including creating, updating, and deleting users and
  groups, managing group memberships, and searching directory objects.

## AWS

managed policy: AWSDirectoryServiceDataReadOnlyAccess

You can attach the `AWSDirectoryServiceDataReadOnlyAccess` policy to your
IAM identities. To view the full permissions for this policy, see [AWSDirectoryServiceDataReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSDirectoryServiceDataReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSDirectoryServiceDataReadOnlyAccess.md") in the _AWS Managed Policy
Reference_.

This policy grants read-only permissions that allow users to view and search Active
Directory objects within managed directories. Principals with this policy attached
cannot make any updates to users, groups, or group memberships. For example, principals
with these permissions can search for users and groups, view user and group details, and
list group memberships, but cannot create, modify, or delete any directory
objects.

**Permissions details**

This policy includes the following permissions:

- `ds` – Allows principals to access directory data through
  the Directory Service Data API.
- `ds-data` – Allows users to perform read-only actions that
  return directory object information. This includes API operations that start
  with `Describe`, `List`, or `Search`.

## AWSDirectoryServiceServiceRolePolicy

You cannot attach the `AWSDirectoryServiceServiceRolePolicy` policy to your
IAM identities. This policy is attached to a service-linked role that allows AWS
Directory Service to perform actions on your behalf. To view the permissions for this
policy, see [AWSDirectoryServiceServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSDirectoryServiceServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSDirectoryServiceServiceRolePolicy.md") in the _AWS Managed Policy
Reference_.

This policy grants permissions that allow AWS Directory Service to monitor and
assess self-managed domain controllers in hybrid Active Directory environments. The
service uses these permissions to run automated health assessments, execute PowerShell
scripts for compatibility testing, and gather network configuration information to
ensure proper hybrid connectivity and automated recovery capabilities.

**Permissions details**

This policy includes the following permissions:

- `ssm` – Allows the service to send PowerShell commands to
  on-premises domain controllers and retrieve command execution results for
  monitoring and assessment purposes.
- `ec2` – Allows the service to describe network resources
  such as VPCs, subnets, security groups, and network interfaces to validate
  hybrid connectivity configurations.

## IAM and AWS Directory Service updates to AWS

managed policies

View details about updates to IAM and AWS managed policies since the service began
tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the IAM and AWS Directory Service Document history pages.

| Change                                                                                                                                                                                                  | Description                                                                                                                                                                                   | Date               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSDirectoryServiceServiceRolePolicy](#security-iam-awsmanpol-AWSDirectoryServiceServiceRolePolicy "#security-iam-awsmanpol-AWSDirectoryServiceServiceRolePolicy") – New policy                        | AWS Directory Service added a new policy to allow AWS to monitor a customer's self-managed domain controllers.                                                                                | July 30, 2025      |
| [AWS managed policy: AWSDirectoryServiceDataReadOnlyAccess](#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess "#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess") – New policy | AWS Directory Service added a new policy to allow a user or group access to view and search AD users, members, and groups.                                                                    | September 17, 2024 |
| [AWS managed policy: AWSDirectoryServiceDataFullAccess](#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess "#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess") – New policy             | AWS Directory Service added a new policy to allow a user or group access to built-in object management with Directory Service Data to create, manage, and view AD users, members, and groups. | September 17, 2024 |
| AWS Directory Service started tracking changes                                                                                                                                                          | AWS Directory Service started tracking changes for its AWS managed policies.                                                                                                                  | September 17, 2024 |
