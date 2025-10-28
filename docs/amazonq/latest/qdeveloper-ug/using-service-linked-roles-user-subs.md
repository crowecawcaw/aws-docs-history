# Using service-linked-roles for User Subscriptions

User Subscriptions uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to User Subscriptions. Service-linked roles are predefined by
User Subscriptions and include all the permissions that the service requires to call other
AWS services on your behalf.

A service-linked role makes setting up User Subscriptions easier because you don’t have
to manually add the necessary permissions. User Subscriptions defines the permissions of
its service-linked roles, and unless defined otherwise, only User Subscriptions can assume
its roles. The defined permissions include the trust policy and the permissions policy, and
that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your User Subscriptions because you can't inadvertently remove permissions
required by the resources.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column. Choose
a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role

permissions for User Subscriptions

User Subscriptions uses the service-linked role named
**AWSServiceRoleForUserSubscriptions**. This role provides access for User Subscriptions to
your IAM Identity Center resources in order to automatically update your subscriptions.

The AWSServiceRoleForUserSubscriptions service-linked role trusts the following services to assume the
role:

- `user-subscriptions.amazonaws.com`

The role permissions policy named [AWSServiceRoleForUserSubscriptions](managed-policy.md#amazonq-policy-AWSServiceRoleForUserSubscriptions "managed-policy.md#amazonq-policy-AWSServiceRoleForUserSubscriptions")
allows User Subscriptions to complete the following actions on the specified
resources:

- Action: `identitystore:DescribeGroup` on `*`

Action: `identitystore:DescribeUser` on `*`

Action: `identitystore:IsMemberInGroups` on `*`

Action: `identitystore:ListGroupMemberships` on `*`

Action: `organizations:DescribeOrganization` on `*`

Action: `sso:DescribeApplication` on `*`

Action: `sso:DescribeInstance` on `*`

Action: `sso:ListInstances` on `*`

Action: `sso-directory:DescribeUser` on `*`

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for

User Subscriptions

You don't need to manually create a service-linked role. When you
create a User Subscription in the AWS Management Console, User Subscriptions creates the
service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you update the settings,
User Subscriptions creates the service-linked role for you again.

You can also use the IAM console or AWS CLI to create a service-linked role with the
`q.amazonaws.com` service name. For more information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If
you delete this service-linked role, you can use this same process to create the role
again.

## Editing a service-linked role for User Subscriptions

User Subscriptions does not allow you to edit the AWSServiceRoleForUserSubscriptions service-linked role.
After you create a service-linked role, you cannot change the name of the role because
various entities might reference the role. However, you can edit the description of the role
using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for

User Subscriptions

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the User Subscriptions service is using the role when you try to delete the
resources, then the deletion might fail. If that happens, wait for a few minutes and try
the operation again.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForUserSubscriptions
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for User Subscriptions

service-linked roles

Amazon Q Developer Subscriptions supports using service-linked roles in all of the Regions where
the service is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

Amazon Q Developer Subscriptions does not support using service-linked roles in every Region
where the service is available. You can use the AWSServiceRoleForUserSubscriptions role in the following
Regions.

| Region name               | Region identity | Support in User Subscriptions |
| ------------------------- | --------------- | ----------------------------- |
| US East (N. Virginia)     | us-east-1       | Yes                           |
| US West (Oregon)          | us-west-2       | Yes                           |
| US East (N. Virginia)     | us-east-1       | Yes                           |
| US East (Ohio)            | us-east-2       | Yes                           |
| US East (Ohio)            | us-east-2       | Yes                           |
| US West (N. California)   | us-west-1       | Yes                           |
| Asia Pacific (Mumbai)     | ap-south-1      | Yes                           |
| Asia Pacific (Osaka)      | ap-northeast-3  | Yes                           |
| Asia Pacific (Seoul)      | ap-northeast-2  | Yes                           |
| Asia Pacific (Singapore)  | ap-southeast-1  | Yes                           |
| Asia Pacific (Sydney)     | ap-southeast-2  | Yes                           |
| Asia Pacific (Tokyo)      | ap-northeast-1  | Yes                           |
| Canada (Central)          | ca-central-1    | Yes                           |
| Europe (Frankfurt)        | eu-central-1    | Yes                           |
| Europe (Ireland)          | eu-west-1       | Yes                           |
| Europe (London)           | eu-west-2       | Yes                           |
| Europe (Paris)            | eu-west-3       | Yes                           |
| Europe (Stockholm)        | eu-north-1      | Yes                           |
| South America (São Paulo) | sa-east-1       | Yes                           |
