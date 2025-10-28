# Using a service-linked role for

Network Synthetic Monitor

Network Synthetic Monitor uses the following service-linked role for the permissions that it requires to
call other AWS services on your behalf:

- [AWSServiceRoleForNetworkMonitor](#security-iam-awsmanpol-AWSServiceRoleForNetworkMonitor "#security-iam-awsmanpol-AWSServiceRoleForNetworkMonitor")

## `AWSServiceRoleForNetworkMonitor`

Network Synthetic Monitor uses the service-linked role named
`AWSServiceRoleForNetworkMonitor` to update and manage monitors.

The `AWSServiceRoleForNetworkMonitor` service-linked role trusts the
following service to assume the role:

- `networkmonitor.amazonaws.com`

The `CloudWatchNetworkMonitorServiceRolePolicy` is attached to the service
linked role and grants access for the service to access VPC and EC2 resources in your account,
as well as manage the monitors that you create.

### Permissions groupings

The policy is grouped into the following sets of permissions:

- `**cloudwatch**` - This allows the service principal to publish network
  monitoring metrics to CloudWatch resources.
- `**ec2**` - This allows the service principal to describe VPCs and subnets in
  your account to create or update monitors and probes. This also allows the service principal
  to create, modify, and delete security groups, network interfaces, and their associated
  permissions to configure the monitor or probe to send monitoring traffic to your
  endpoints.

To view the permissions for this policy, see [CloudWatchNetworkMonitorServiceRolePolicy](../../../aws-managed-policy/latest/reference/CloudWatchNetworkMonitorServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/CloudWatchNetworkMonitorServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

## Create the service-linked role

`AWSServiceRoleForNetworkMonitor`

You don't need to manually create the `AWSServiceRoleForNetworkMonitor`
role.

- Network Synthetic Monitor creates the `AWSServiceRoleForNetworkMonitor` role when you create
  your first monitor with the feature. This role then applies to all additional monitors that you create.

To create a service-linked role on your behalf, you must have the required permissions. For
more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Edit the service-linked role

You can edit the `AWSServiceRoleForNetworkMonitor` descriptions using IAM. For more
information, see [Editing
a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Delete the service-linked role

If you no longer need to use Network Synthetic Monitor, we recommend that you delete the
`AWSServiceRoleForNetworkMonitor` role.

You can delete these service-linked roles only after you delete your monitors.
For more information, see [Delete a monitor](../../../index.md "../../../index.md").

You can use the IAM console, the IAM CLI, or the IAM API to delete
service-linked roles. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

After you delete `AWSServiceRoleForNetworkMonitor` Network Synthetic Monitor will create the role again when you
create a new monitor.

## Supported Regions for the Network Synthetic Monitor service-linked role

Network Synthetic Monitor supports the service-linked role in all of AWS Regions where the service
is available. For more information, see [AWS endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the
_AWS General Reference_.
