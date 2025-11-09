# AWS managed policies for Amazon Keyspaces

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

## AWS managed

policy: AmazonKeyspacesReadOnlyAccess_v2

You can attach the `AmazonKeyspacesReadOnlyAccess_v2` policy to your IAM identities.

This policy grants read-only access to Amazon Keyspaces and includes the required permissions
when connecting through private VPC endpoints.

**Permissions details**

This policy includes the following permissions.

- `Amazon Keyspaces` – Provides read-only access to Amazon Keyspaces.
- `Amazon Keyspaces CDC streams` – Allows principals to view Amazon Keyspaces CDC streams.
- `Application Auto Scaling` – Allows principals to view configurations from
  Application Auto Scaling. This is required so that users can view automatic scaling policies
  that are attached to a table.
- `CloudWatch` – Allows principals to view metric data and alarms
  configured in CloudWatch. This is required so users can view the billable table size
  and CloudWatch alarms that have been configured for a table.
- `AWS KMS` – Allows principals to view keys configured in AWS KMS.
  This is required so users can view AWS KMS keys that they create and manage in
  their account to confirm that the key assigned to
  Amazon Keyspaces is a symmetric encryption key that is enabled.
- `Amazon EC2` – Allows principals connecting to Amazon Keyspaces through VPC endpoints
  to query the VPC on your Amazon EC2 instance for endpoint and network interface information.
  This read-only access to the Amazon EC2 instance is required so Amazon Keyspaces can look up and
  store available interface VPC endpoints in the `system.peers` table used for connection
  load balancing.

To review the policy in `JSON` format, see
[AmazonKeyspacesReadOnlyAccess_v2](../../../aws-managed-policy/latest/reference/AmazonKeyspacesReadOnlyAccess_v2.md "../../../aws-managed-policy/latest/reference/AmazonKeyspacesReadOnlyAccess_v2.md").

## AWS managed

policy: AmazonKeyspacesReadOnlyAccess

You can attach the `AmazonKeyspacesReadOnlyAccess` policy to your IAM identities.

This policy grants read-only access to Amazon Keyspaces.

**Permissions details**

This policy includes the following permissions.

- `Amazon Keyspaces` – Provides read-only access to Amazon Keyspaces.
- `Amazon Keyspaces CDC streams` – Allows principals to view Amazon Keyspaces CDC streams.
- `Application Auto Scaling` – Allows principals to view configurations from
  Application Auto Scaling. This is required so that users can view automatic scaling policies
  that are attached to a table.
- `CloudWatch` – Allows principals to view metric data and alarms
  configured in CloudWatch. This is required so users can view the billable table size
  and CloudWatch alarms that have been configured for a table.
- `AWS KMS` – Allows principals to view keys configured in AWS KMS.
  This is required so users can view AWS KMS keys that they create and manage in
  their account to confirm that the key assigned to
  Amazon Keyspaces is a symmetric encryption key that is enabled.

To review the policy in `JSON` format, see
[AmazonKeyspacesReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonKeyspacesReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonKeyspacesReadOnlyAccess.md").

## AWS managed policy:

AmazonKeyspacesFullAccess

You can attach the `AmazonKeyspacesFullAccess` policy to your IAM identities.

This policy grants administrative permissions that allow
your administrators unrestricted access to Amazon Keyspaces.

**Permissions details**

This policy includes the following permissions.

- `Amazon Keyspaces` – Allows principals to access any Amazon Keyspaces resource and perform all actions.
- `Application Auto Scaling` – Allows principals to create, view, and delete automatic scaling policies
  for Amazon Keyspaces tables. This is
  required so that administrators can manage automatic scaling policies for Amazon Keyspaces tables.
- `CloudWatch` – Allows principals to see the billable table size as
  well as create, view, and delete CloudWatch alarms for Amazon Keyspaces automatic scaling
  policies. This is required so that administrators can view the billable table
  size and create a CloudWatch dashboard.
- `IAM` – Allows Amazon Keyspaces to create service-linked roles with
  IAM automatically when the following features are turned on:
  - `Amazon Keyspaces CDC streams` – When an administrator enables a stream for a table,
    Amazon Keyspaces creates the service-linked role [AWSServiceRoleForAmazonKeyspacesCDC](using-service-linked-roles-CDC-streams.md#service-linked-role-permissions-CDC-streams "using-service-linked-roles-CDC-streams.md#service-linked-role-permissions-CDC-streams") to publish CloudWatch metrics into your account on your behalf.
  - `Application Auto Scaling` – When an administrator enables Application Auto Scaling for a table, Amazon Keyspaces
    creates the service-linked role [AWSServiceRoleForApplicationAutoScaling_CassandraTable](using-service-linked-roles-app-auto-scaling.md#service-linked-role-permissions-app-auto-scaling "using-service-linked-roles-app-auto-scaling.md#service-linked-role-permissions-app-auto-scaling") to perform
    automatic scaling actions on your behalf.
  - `Amazon Keyspaces multi-Region replication` – When an administrator creates a new multi-Region keyspace,
    or adds a new AWS Region to an existing single-Region keyspace, Amazon Keyspaces creates the
    service-linked role [AWSServiceRoleForAmazonKeyspacesReplication](using-service-linked-roles-multi-region-replication.md#service-linked-role-permissions-multi-region-replication "using-service-linked-roles-multi-region-replication.md#service-linked-role-permissions-multi-region-replication") to perform replication of tables, data, and metadata to the selected
    Regions on your behalf.

- `AWS KMS` – Allows principals to view keys configured in
  AWS KMS. This is required so that users can view AWS KMS keys that they create and
  manage in their account to confirm that the key assigned to Amazon Keyspaces is a symmetric
  encryption key that is enabled.
- `Amazon EC2` – Allows principals connecting to Amazon Keyspaces through VPC endpoints
  to query the VPC on your Amazon EC2 instance for endpoint and network interface information.
  This read-only access to the Amazon EC2 instance is required so Amazon Keyspaces can look up and
  store available interface VPC endpoints in the `system.peers` table used for connection
  load balancing.

To review the policy in `JSON` format, see
[AmazonKeyspacesFullAccess](../../../aws-managed-policy/latest/reference/AmazonKeyspacesFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonKeyspacesFullAccess.md").

## AWS managed

policy: KeyspacesCDCServiceRolePolicy

You can't attach `KeyspacesCDCServiceRolePolicy` to your IAM entities.
This policy is attached to a service-linked role that allows Amazon Keyspaces to perform actions on
your behalf. For more information, see [Using roles for Amazon Keyspaces CDC streams](using-service-linked-roles-CDC-streams.md "using-service-linked-roles-CDC-streams.md").

This policy grants the required permissions to the service-linked role `AWSServiceRoleForAmazonKeyspacesCDC`
to publish Amazon Keyspaces CDC stream metrics data to CloudWatch on your behalf.

**Permissions details**

This policy includes the following permissions.

- `CloudWatch` – Allows the service-linked-role [AWSServiceRoleForAmazonKeyspacesCDC](using-service-linked-roles-CDC-streams.md#service-linked-role-permissions-CDC-streams "using-service-linked-roles-CDC-streams.md#service-linked-role-permissions-CDC-streams") to publish
  metric data from Amazon Keyspaces CDC streams into the
  `"cloudwatch:namespace": "AWS/Cassandra"` in your CloudWatch account on your behalf.

To review the policy in `JSON` format, see
[KeyspacesCDCServiceRolePolicy](../../../aws-managed-policy/latest/reference/KeyspacesCDCServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/KeyspacesCDCServiceRolePolicy.md").

## Amazon Keyspaces updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon Keyspaces since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the [Document history for Amazon Keyspaces (for Apache Cassandra)](doc-history.md "doc-history.md") page.

| Change                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Date               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [KeyspacesCDCServiceRolePolicy](#security-iam-awsmanpol-KeyspacesCDCServiceRolePolicy "#security-iam-awsmanpol-KeyspacesCDCServiceRolePolicy") –<br>New policy                            | Amazon Keyspaces added a new managed policy `KeyspacesCDCServiceRolePolicy` which grants the required permissions to the<br>service-linked role `AWSServiceRoleForAmazonKeyspacesCDC`<br>to publish Amazon Keyspaces CDC stream metrics data to CloudWatch on your behalf. For more information, see [Using roles for Amazon Keyspaces CDC streams](using-service-linked-roles-CDC-streams.md "using-service-linked-roles-CDC-streams.md").                                                                                                                                                                                                                                                                                                                                                                                                                                               | July 02, 2025      |
| [AmazonKeyspacesReadOnlyAccess_v2](#security-iam-awsmanpol-AmazonKeyspacesReadOnlyAccess_v2 "#security-iam-awsmanpol-AmazonKeyspacesReadOnlyAccess_v2") –<br>Update to an existing policy | Amazon Keyspaces added new permissions to allow IAM principals to view Amazon Keyspaces CDC<br>streams. For more information, see [View CDC streams in Amazon Keyspaces](keyspaces-view-cdc.md "keyspaces-view-cdc.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | July 02, 2025      |
| [AmazonKeyspacesReadOnlyAccess](#security-iam-awsmanpol-AmazonKeyspacesReadOnlyAccess "#security-iam-awsmanpol-AmazonKeyspacesReadOnlyAccess") –<br>Update to an existing policy          | Amazon Keyspaces added new permissions to allow IAM principals to view Amazon Keyspaces CDC<br>streams. For more information, see [View CDC streams in Amazon Keyspaces](keyspaces-view-cdc.md "keyspaces-view-cdc.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | July 02, 2025      |
| [AmazonKeyspacesFullAccess](#security-iam-awsmanpol-AmazonKeyspacesFullAccess "#security-iam-awsmanpol-AmazonKeyspacesFullAccess") –<br>Update to an existing policy                      | Amazon Keyspaces created the `KeyspacesCDCServiceRolePolicy` managed policy for the service<br>linked role [AWSServiceRoleForAmazonKeyspacesCDC](using-service-linked-roles-CDC-streams.md#service-linked-role-permissions-CDC-streams "using-service-linked-roles-CDC-streams.md#service-linked-role-permissions-CDC-streams") to add the<br>permissions that are required when an administrator enables a stream<br>for a table.<br>Amazon Keyspaces uses the service-linked role `AWSServiceRoleForAmazonKeyspacesCDC`<br>to publish CloudWatch metrics into your account on your behalf. For more information, see [Using roles for Amazon Keyspaces CDC streams](using-service-linked-roles-CDC-streams.md "using-service-linked-roles-CDC-streams.md").                                                                                                                             | July 02, 2025      |
| [AmazonKeyspacesFullAccess](#security-iam-awsmanpol-AmazonKeyspacesFullAccess "#security-iam-awsmanpol-AmazonKeyspacesFullAccess") –<br>Update to an existing policy                      | Amazon Keyspaces updated the `KeyspacesReplicationServiceRolePolicy` of the<br>service linked role [AWSServiceRoleForAmazonKeyspacesReplication](using-service-linked-roles-multi-region-replication.md#service-linked-role-permissions-multi-region-replication "using-service-linked-roles-multi-region-replication.md#service-linked-role-permissions-multi-region-replication") to add the permissions<br>that are required when an administrator adds a new AWS Region to a single or multi-Region keyspace.<br>Amazon Keyspaces uses the service-linked role `AWSServiceRoleForAmazonKeyspacesReplication`<br>to replicate tables, their settings, and data on your behalf. For more information, see [Using roles for Amazon Keyspaces Multi-Region Replication](using-service-linked-roles-multi-region-replication.md "using-service-linked-roles-multi-region-replication.md"). | November 19, 2024  |
| [AmazonKeyspacesFullAccess](#security-iam-awsmanpol-AmazonKeyspacesFullAccess "#security-iam-awsmanpol-AmazonKeyspacesFullAccess") –<br>Update to an existing policy                      | Amazon Keyspaces added new permissions to allow Amazon Keyspaces to create a service-linked role when an<br>administrator adds a new Region to a single or multi-Region keyspace.<br>Amazon Keyspaces uses the service-linked role to perform data replication<br>tasks on your behalf. For more information, see [Using roles for Amazon Keyspaces Multi-Region Replication](using-service-linked-roles-multi-region-replication.md "using-service-linked-roles-multi-region-replication.md").                                                                                                                                                                                                                                                                                                                                                                                           | October 3, 2023    |
| [AmazonKeyspacesReadOnlyAccess_v2](#security-iam-awsmanpol-AmazonKeyspacesReadOnlyAccess "#security-iam-awsmanpol-AmazonKeyspacesReadOnlyAccess") –<br>New policy                         | Amazon Keyspaces created a new policy to add read-only permissions for clients connecting<br>to Amazon Keyspaces through interface VPC endpoints to access the Amazon EC2 instance to look up network information.<br>Amazon Keyspaces stores available interface VPC endpoints in the `system.peers` table for connection<br>load balancing. For more information, see [Using Amazon Keyspaces with interface VPC endpoints](vpc-endpoints.md "vpc-endpoints.md").                                                                                                                                                                                                                                                                                                                                                                                                                       | September 12, 2023 |
| [AmazonKeyspacesFullAccess](#security-iam-awsmanpol-AmazonKeyspacesFullAccess "#security-iam-awsmanpol-AmazonKeyspacesFullAccess") –<br>Update to an existing policy                      | Amazon Keyspaces added new permissions to allow Amazon Keyspaces to create a service-linked role when an<br>administrator creates a multi-Region keyspace.<br>Amazon Keyspaces uses the service-linked role `AWSServiceRoleForAmazonKeyspacesReplication`<br>to perform data replication<br>tasks on your behalf. For more information, see [Using roles for Amazon Keyspaces Multi-Region Replication](using-service-linked-roles-multi-region-replication.md "using-service-linked-roles-multi-region-replication.md").                                                                                                                                                                                                                                                                                                                                                                 | June 5, 2023       |
| [AmazonKeyspacesReadOnlyAccess](#security-iam-awsmanpol-AmazonKeyspacesReadOnlyAccess "#security-iam-awsmanpol-AmazonKeyspacesReadOnlyAccess") –<br>Update to an existing policy          | Amazon Keyspaces added new permissions to allow users to view the billable size of a table using CloudWatch.<br>Amazon Keyspaces integrates with Amazon CloudWatch to allow you to monitor the<br>billable table size. For more information, see [Amazon Keyspaces metrics](metrics-dimensions.md#keyspaces-metrics-dimensions "metrics-dimensions.md#keyspaces-metrics-dimensions").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | July 7, 2022       |
| [AmazonKeyspacesFullAccess](#security-iam-awsmanpol-AmazonKeyspacesFullAccess "#security-iam-awsmanpol-AmazonKeyspacesFullAccess") –<br>Update to an existing policy                      | Amazon Keyspaces added new permissions to allow users to view the billable size of a table using CloudWatch.<br>Amazon Keyspaces integrates with Amazon CloudWatch to allow you to monitor the<br>billable table size. For more information, see [Amazon Keyspaces metrics](metrics-dimensions.md#keyspaces-metrics-dimensions "metrics-dimensions.md#keyspaces-metrics-dimensions").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | July 7, 2022       |
| [AmazonKeyspacesReadOnlyAccess](#security-iam-awsmanpol-AmazonKeyspacesReadOnlyAccess "#security-iam-awsmanpol-AmazonKeyspacesReadOnlyAccess") –<br>Update to an existing policy          | Amazon Keyspaces added new permissions to allow users to view AWS KMS keys that<br>have been configured for Amazon Keyspaces encryption at rest.<br>Amazon Keyspaces encryption at rest integrates with AWS KMS for protecting and<br>managing the encryption keys used to encrypt data at rest. To view<br>the AWS KMS key configured for Amazon Keyspaces, read-only permissions have been<br>added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | June 1, 2021       |
| [AmazonKeyspacesFullAccess](#security-iam-awsmanpol-AmazonKeyspacesFullAccess "#security-iam-awsmanpol-AmazonKeyspacesFullAccess") –<br>Update to an existing policy                      | Amazon Keyspaces added new permissions to allow users to view AWS KMS keys that<br>have been configured for Amazon Keyspaces encryption at rest.<br>Amazon Keyspaces encryption at rest integrates with AWS KMS for protecting and<br>managing the encryption keys used to encrypt data at rest. To view<br>the AWS KMS key configured for Amazon Keyspaces, read-only permissions have been<br>added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | June 1, 2021       |
| Amazon Keyspaces started tracking changes                                                                                                                                                 | Amazon Keyspaces started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | June 1, 2021       |
