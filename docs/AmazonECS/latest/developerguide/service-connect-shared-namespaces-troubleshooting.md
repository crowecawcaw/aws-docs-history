# Troubleshooting

Amazon ECS Service Connect with shared AWS Cloud Map namespaces

Use the following information to troubleshoot issues with shared AWS Cloud Map namespaces and
Service Connect. For more information on locating error messages, see [Amazon ECS troubleshooting](troubleshooting.md "troubleshooting.md").

Error messages related to permissions issues appear due to
missing permissions, or if access to the namespace is revoked.

###### Important

You must use the
`AWSRAMPermissionCloudMapECSFullPermission` managed
permission to share the namespace for Service Connect to work properly with the
namespace.

Error message appears in
one of the following formats:

**`An error occurred (ClientException) when calling the <OperationName>
 operation: User: arn:aws:iam::<account-id>:user/<user-name> is not
 authorized to perform: <ActionName> on resource: <ResourceArn> because
 no resource-based policy allows the <ActionName> action`**

The following scenarios can result in an error message in this format:

**Cluster creation or update failure**

These issues occur when Amazon ECS operations such as
`CreateCluster` or `UpdateCluster` fail due to
missing AWS Cloud Map permissions. The operations require permissions for the
following AWS Cloud Map actions:

- `servicediscovery:GetNamespace`

Ensure that the resource share invitation has been accepted in the
consumer account and that the correct namespace ARN is being used in the
Service Connect configuration.

**Service creation or update failure**

These issues occur when Amazon ECS operations such as
`CreateService` or `UpdateService` fail due to
missing AWS Cloud Map permissions. The operations require permissions for the
following AWS Cloud Map actions:

- `servicediscovery:CreateService`
- `servicediscovery:GetNamespace`
- `servicediscovery:GetOperation` (for creating a new
  AWS Cloud Map service)
- `servicediscovery:GetService` (for when a AWS Cloud Map
  service already exists)

Ensure that the resource share invitation has been accepted in the
consumer account and that the correct namespace ARN is being used in the
Service Connect configuration.

**`ListServicesByNamespace` operation
fails**

This issue occurs when the Amazon ECS `ListServicesByNamespace`
operation fails. The operation requires permissions for the following AWS Cloud Map
actions:

- `servicediscovery:GetNamespace`

To resolve this issue:

- Verify that the consumer account has the
  `servicediscovery:GetNamespace` permission.
- Use the namespace ARN when calling the API, not the name.
- Ensure the resource share is active and the invitation has been
  accepted.

**`User: <iam-user> is not authorized to perform: <ActionName> on
 resource: <ResourceArn> with an explicit deny in an identity-based
 policy.`**

The following scenarios can result in an error message in this format:

**Service deletion fails and gets stuck in
`DRAINING`
state**

This issue occurs when Amazon ECS `DeleteService` operations fail
due to the missing `servicediscovery:DeleteService` permission
when access to the namespace is revoked. The service may appear to delete
successfully initially but will get stuck in the `DRAINING` state. The error message appears as an Amazon ECS
service event.

To resolve this issue, the namespace owner must share the namespace with
the consumer account to allow service deletion to complete.

**Tasks in service fail to run**

This issue occurs when tasks fail to start due to missing permissions. The
error message is surfaced as a stopped task error. For more information, see
[Resolve Amazon ECS stopped task errors](resolve-stopped-errors.md "resolve-stopped-errors.md").

The following AWS Cloud Map actions are required for running a task:

- `servicediscovery:GetOperation`
- `servicediscovery:RegisterInstance`

Ensure that the consumer account has the required permissions and that the
shared namespace is accessible.

**Tasks fail to stop cleanly or get stuck in
`DEACTIVATING` or `DEPROVISIONING` state**

This issue occurs when tasks fail to deregister from the AWS Cloud Map service
during shutdown due to missing permissions. The error is surfaced as a
`statusReason` in the task attachment that can be retreived
using the `DescribeTasks` API. For more information, see [DescribeTasks](../APIReference/API_DescribeTasks.md "../APIReference/API_DescribeTasks.md") in the
_Amazon Elastic Container Service API Reference_.

The following AWS Cloud Map actions are required to stop a task:

- `servicediscovery:DeregisterInstance`
- `servicediscovery:GetOperation`

If access to the shared namespace is revoked, tasks may remain in a
`DEACTIVATING` or `DEPROVISIONING` state until namespace access is restored. Request
the namespace owner to restore access to the namespace.
