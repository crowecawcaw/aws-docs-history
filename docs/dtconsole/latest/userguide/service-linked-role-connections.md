# Using service-linked roles for

AWS CodeConnections

AWS CodeConnections uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role
that is linked directly to AWS CodeConnections. Service-linked roles are predefined by AWS CodeConnections and
include all the permissions that the service requires to call other AWS services on your
behalf. This role is created for you the first time you create a connection. You don't have
to create the role.

A service-linked role makes setting up AWS CodeConnections easier because you don’t have to add
permissions manually. AWS CodeConnections defines the permissions of its service-linked roles, and
unless defined otherwise, only AWS CodeConnections can assume its roles. The defined permissions
include the trust policy and the permissions policy, and that permissions policy cannot be
attached to any other IAM entity.

To delete a service-linked role, you must first delete its related resources. This
protects your AWS CodeConnections resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS Services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md").

###### Note

Actions for resources that are created under the new service prefix
`codeconnections` are available. Creating a resource under the new
service prefix will use `codeconnections` in the resource ARN. Actions and
resources for the `codestar-connections` service prefix remain available.
When specifying a resource in the IAM policy, the service prefix needs to match that of
the resource.

## Service-linked role permissions for AWS CodeConnections

AWS CodeConnections uses the AWSServiceRoleForGitSync service-linked role to use Git sync with connected
Git-based repositories.

The AWSServiceRoleForGitSync service-linked role trusts the following services to assume the
role:

- `repository.sync.codeconnections.amazonaws.com`

The role permissions policy named AWSGitSyncServiceRolePolicy allows AWS CodeConnections to complete the
following actions on the specified resources:

- Action: Grants permissions to allow users to create connections to external
  Git-based repositories and use Git sync with those repositories.

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for

AWS CodeConnections

You don't need to manually create a service-linked role. You create the role when you
create a resource for your Git-synced project with the CreateRepositoryLink API.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account.

## Editing a service-linked role for

AWS CodeConnections

After you create a service-linked role, you cannot change its name because various
entities might reference the role. However, you can use IAM to edit the role
description. For more information, see [Editing a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for

AWS CodeConnections

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete the role. That way, you don’t have an unused entity that is
not actively monitored or maintained. You must clean up the resources for your
service-linked role before you can delete it. This means deleting all connections that
use the service role in your AWS account.

###### Note

If the AWS CodeConnections service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

###### To delete AWS CodeConnections resources used by AWSServiceRoleForGitSync

1. Open the Developer Tools console, and then choose **Settings**.
2. Choose all connections that appear in the list, and then choose
   **Delete**.
3. Repeat these steps in all AWS Regions where you created connections.

**To **use IAM** to delete the
service-linked role**

Use the IAM console, AWS CLI, or AWS Identity and Access Management API to delete the AWSServiceRoleForGitSync service-linked
role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported regions for AWS CodeConnections service-linked

roles

AWS CodeConnections supports using service-linked roles in all of the AWS Regions where the
service is available. For more information, see [AWS Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
