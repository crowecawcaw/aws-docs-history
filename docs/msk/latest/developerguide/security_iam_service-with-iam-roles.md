# Amazon MSK IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your Amazon Web Services account that has specific permissions.

## Using temporary

credentials with Amazon MSK

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security
credentials by calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Amazon MSK supports using temporary credentials.

## Service-linked roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow Amazon Web Services to access resources in
other services to complete an action on your behalf. Service-linked roles appear
in your IAM account and are owned by the service. An administrator can
view but not edit the permissions for service-linked roles.

Amazon MSK supports service-linked roles. For details about creating or
managing Amazon MSK service-linked roles, [Service-linked roles for
Amazon MSK](using-service-linked-roles.md "using-service-linked-roles.md").
