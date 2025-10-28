# AWS managed policies for AWS Elemental MediaConnect

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

## AWS managed policy:

AWSElementalMediaConnectReadOnlyAccess

You can attach `AWSElementalMediaConnectReadOnlyAccess` to your users,
groups, and roles.

This policy grants read-only permissions that allow users to view all resources in
MediaConnect.

**Permissions details**

This policy includes the following permissions.

- `mediaconnect:ListBridges` – Allows principals to view a list of
  bridges in MediaConnect. This is required so that you can see all the available bridge
  resources in your account.
- `mediaconnect:ListEntitlements` – Allows principals to view a
  list of entitlements in MediaConnect. This is required so that you can see all
  permissions granted to other AWS accounts to access your transport stream
  flows.
- `mediaconnect:ListFlows` – Allows principals to view a list of
  flows in MediaConnect. This is required so that you can see all the available flow
  resources in your account.
- `mediaconnect:ListGatewayInstances` – Allows principals to view
  a list of gateway instances in MediaConnect. This is required so that you can see all
  the running gateway compute resources in your account.
- `mediaconnect:ListGateways` – Allows principals to view a list
  of gateways in MediaConnect. This is required so that you can see all the available
  gateway resources in your account.
- `mediaconnect:ListOfferings` – Allows principals to view a list
  of service offerings in MediaConnect. This is required so that you can see the available
  bandwidth discount options that require a commitment. The offerings that are
  displayed may vary based on your AWS Region.
- `mediaconnect:ListReservations` – Allows principals to view a
  list of reservations in MediaConnect. This is required so that you can see your active
  bandwidth commitments and their associated discounts.
- `mediaconnect:DescribeBridge` – Allows principals to view
  detailed information about a specific bridge in MediaConnect. This is required so that
  you can inspect the bridge configuration and status.
- `mediaconnect:DescribeFlow` – Allows principals to view detailed
  information about a specific flow in MediaConnect. This is required so that you can
  inspect the flow configuration and status.
- `mediaconnect:DescribeFlowSourceMetadata` – Allows principals to
  view metadata about a flow's source in MediaConnect. This is required so that you can
  see technical details about the input stream.
- `mediaconnect:DescribeFlowSourceThumbnail` – Allows principals
  to view the details of the thumbnail image for a flow's source in MediaConnect. This is
  required so that you can see visual previews of your video streams.
- `mediaconnect:DescribeGateway` – Allows principals to view
  detailed information about a specific gateway in MediaConnect. This is required so that
  you can inspect the gateway configuration and status.
- `mediaconnect:DescribeGatewayInstance` – Allows principals to
  view detailed information about a specific gateway instance in MediaConnect. This is
  required so that you can inspect the gateway instance configuration and
  status.
- `mediaconnect:DescribeOffering` – Allows principals to view
  detailed information about a specific service offering in MediaConnect. This is required
  so that you can see bandwidth commitment options and their associated discount
  rates.
- `mediaconnect:DescribeReservation` – Allows principals to view
  detailed information about a specific reservation in MediaConnect. This is required so
  that you can see the details of your bandwidth commitment and its associated
  discount.
- `mediaconnect:ListTagsForResource` – Allows principals to view
  tags associated with MediaConnect resources. This is required so that you can see
  resource organization and classification metadata.

To view the permissions for this policy, see [AWSElementalMediaConnectReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSElementalMediaConnectReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSElementalMediaConnectReadOnlyAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy:

AWSElementalMediaConnectFullAccess

You can attach `AWSElementalMediaConnectFullAccess` to your users, groups,
and roles.

This policy grants administrative permissions that allow the user permission to create,
read, update, and delete MediaConnect resources.

**Permissions details**

This policy includes the following permissions.

- `mediaconnect:*` – Allows principals to perform all actions in
  MediaConnect. This is required so that administrators and other users can create, read,
  update, and delete MediaConnect resources and manage all aspects of video transport
  workflows. The wildcard (\*) permission includes all possible MediaConnect actions, such
  as creating and deleting flows, managing entitlements and outputs, and configuring
  video transport workflows.

To view the permissions for this policy, see [AWSElementalMediaConnectFullAccess](../../../aws-managed-policy/latest/reference/AWSElementalMediaConnectFullAccess.md "../../../aws-managed-policy/latest/reference/AWSElementalMediaConnectFullAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy:

MediaConnectGatewayInstanceRolePolicy

You can attach the `MediaConnectGatewayInstanceRolePolicy` policy to your
IAM identities.

This policy grants permission to register MediaConnect Gateway Instances to a
MediaConnect Gateway. This policy will be attached to a role. The entity assuming the role
will have the ability to register instances to the gateway.

**Permissions details**

This policy includes the following permissions.

- `mediaconnect:DiscoverGatewayPollEndpoint` – Allows principals
  to locate the gateway poll endpoints for the specified gateway.
- `mediaconnect:PollGateway` – Allows principals to regularly
  query the gateway in MediaConnect. This is required so that MediaConnect Gateway
  Instances can check for and receive updates, configurations, and instructions from
  the gateway service.
- `mediaconnect:SubmitGatewayStateChange` – Allows principals to
  report status updates in MediaConnect. This is required so that MediaConnect Gateway
  Instances can notify the gateway service about changes in their operational state,
  health, and configuration status.

To view the permissions for this policy, see [MediaConnectGatewayInstanceRolePolicy](../../../aws-managed-policy/latest/reference/MediaConnectGatewayInstanceRolePolicy.md "../../../aws-managed-policy/latest/reference/MediaConnectGatewayInstanceRolePolicy.md") in the _AWS
Managed Policy Reference_.

## AWS managed policy:

AWSMediaConnectServicePolicy

You can’t attach AWSMediaConnectServicePolicy to your IAM entities. This policy is
attached to a service-linked role that allows MediaConnect to perform actions on your
behalf. For more information, visit [Using service-linked roles](using-service-linked-roles.md "using-service-linked-roles.md").

This policy is attached to the **AWSServiceRoleForMediaConnect** service-linked role. This policy allows the
service-linked role to manage Amazon ECS resources on your behalf. AWS Elemental MediaConnect Gateway uses Amazon ECS as the
foundation for the on-premises implementation of AWS Elemental MediaConnect Gateway and MediaConnect must have the ability
to create, update, and delete Amazon ECS resources as needed.

**Permissions details**

This policy includes the following permissions.

###### Note

All these permissions are restricted to ECS clusters with names starting with
`MediaConnectGateway` through the condition block.

- `ecs:UpdateService` – Allows principals to modify existing ECS
  services. This is required so that MediaConnect can update service configurations for
  MediaConnect Gateway components running on ECS.
- `ecs:DeleteService` – Allows principals to remove ECS services. This is
  required so that MediaConnect can clean up services when they're no longer
  needed.
- `ecs:CreateService` – Allows principals to establish new ECS services.
  This is required so that MediaConnect can set up new service components for the Gateway
  implementation.
- `ecs:DescribeServices` – Allows principals to view details about ECS
  services. This is required so that MediaConnect can monitor and manage the state of its
  services.
- `ecs:PutAttributes` – Allows principals to add attributes to ECS
  resources. This is required so that MediaConnect can configure resources by applying the
  necessary metadata.
- `ecs:DeleteAttributes` – Allows principals to remove attributes from
  ECS resources. This is required so that MediaConnect can clean up metadata when no
  longer needed.
- `ecs:RunTask` – Allows principals to start new tasks in ECS. This is
  required so that MediaConnect can launch new Gateway components as needed.
- `ecs:ListTasks` – Allows principals to view all tasks in ECS. This is
  required so that MediaConnect can monitor and manage running tasks.
- `ecs:StartTask` – Allows principals to initiate specific tasks in ECS.
  This is required so that MediaConnect can launch specific Gateway components.
- `ecs:StopTask` – Allows principals to terminate running tasks in ECS.
  This is required so that MediaConnect can stop Gateway components when needed.
- `ecs:DescribeTasks` – Allows principals to view details about ECS
  tasks. This is required so that MediaConnect can monitor the status of running
  tasks.
- `ecs:DescribeContainerInstances` – Allows principals to view details
  about ECS container instances. This is required so that MediaConnect can monitor the
  health and status of Gateway components.
- `ecs:UpdateContainerInstancesState` – Allows principals to modify the
  state of container instances. This is required so that MediaConnect can manage the
  lifecycle of container instances.

To view the permissions for this policy, see [AWSMediaConnectServicePolicy](../../../aws-managed-policy/latest/reference/AWSMediaConnectServicePolicy.md "../../../aws-managed-policy/latest/reference/AWSMediaConnectServicePolicy.md") in the _AWS
Managed Policy Reference_.

## MediaConnect updates to AWS managed

policies

View details about updates to AWS managed policies for MediaConnect since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the MediaConnect [document history](doc-history.md "doc-history.md") page.

| Change                                                                                     | Description                                                                                                                  | Date              |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| The MediaConnect managed policy **AWSElementalMediaConnectReadOnlyAccess** has been added. | This policy provides read-only access to MediaConnect resources.                                                             | February 12, 2025 |
| The MediaConnect managed policy **AWSElementalMediaConnectFullAccess** has been added.     | This policy provides full access to MediaConnect resources.                                                                  | February 12, 2025 |
| The MediaConnect managed policy **MediaConnectGatewayInstanceRolePolicy** has been added.  | This policy grants permission to register MediaConnect Gateway Instances to a MediaConnect Gateway.                          | April 12, 2023    |
| The MediaConnect managed policy **AWSMediaConnectServicePolicy** has been added.           | This policy is used by a service-link role and grants permissions to access AWS services and resources used by MediaConnect. | April 12, 2023    |
| MediaConnect started tracking changes                                                      | MediaConnect started tracking changes for its AWS managed policies.                                                          | April 12, 2023    |
