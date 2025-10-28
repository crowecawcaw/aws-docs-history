# AWS IoT SiteWise IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within your
AWS account that has specific permissions.

## Use temporary credentials

with AWS IoT SiteWise

You can use temporary credentials to sign in with federation, assume an IAM role, or
to assume a cross-account role. You obtain temporary security credentials by calling
AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

AWS IoT SiteWise supports using temporary credentials.

SiteWise Monitor supports federated users to access portals. Portal users authenticate with
their IAM Identity Center or IAM credentials.

###### Important

Users or roles must have the `iotsitewise:DescribePortal`
permission to sign in to the portal.

When a user signs in to a portal, SiteWise Monitor generates a session policy that provides the
following permissions:

- Read-only access to the assets and asset data in AWS IoT SiteWise in your account to which
  that portal's role provides access.
- Access to projects in that portal to which the user has administrator (project
  owner) or read-only (project viewer) access.

For more information about federated portal user permissions, see [Use service roles for AWS IoT SiteWise Monitor](monitor-service-role.md "monitor-service-role.md").

## Forward access

sessions (FAS) for AWS IoT SiteWise

**Supports forward access sessions (FAS):**

Yes

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

## Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts") allow AWS services to access resources in other services
to complete an action on your behalf. service-linked roles appear in your AWS account
and are owned by the service. An IAM administrator can view but not edit the permissions
for service-linked roles.

AWS IoT SiteWise supports service-linked roles. For details about creating or managing AWS IoT SiteWise
service-linked roles, see [Use service-linked roles for AWS IoT SiteWise](using-service-linked-roles.md "using-service-linked-roles.md").

## Service roles

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts") on your behalf. This role allows the service to access resources in other
services to complete an action on your behalf. Service roles appear in your AWS account
and are owned by the account. This means that an IAM administrator can change the
permissions for this role. However, doing so might break the functionality of the
service.

AWS IoT SiteWise uses a service role to allow SiteWise Monitor portal users to access some of your AWS IoT SiteWise
resources on your behalf. For more information, see [Use service roles for AWS IoT SiteWise Monitor](monitor-service-role.md "monitor-service-role.md").

You must have required permissions before you can create AWS IoT Events alarm models in AWS IoT SiteWise.
For more information, see [Set up permissions for event alarms in AWS IoT SiteWise](alarms-iam-permissions.md "alarms-iam-permissions.md").

## Choose an IAM role in

AWS IoT SiteWise

When you create a `portal` resource in AWS IoT SiteWise, you must choose a role to
allow the federated users of your SiteWise Monitor portal to access AWS IoT SiteWise on your behalf. If you
have previously created a service role, then AWS IoT SiteWise provides you with a list of roles to
choose from. Otherwise, you can create a role with the required permissions when you
create a portal. It's important to choose a role that allows access to your assets and
asset data. For more information, see [Use service roles for AWS IoT SiteWise Monitor](monitor-service-role.md "monitor-service-role.md").
