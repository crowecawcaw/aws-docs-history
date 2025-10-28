# Using service-linked roles for

re:Post Private

AWS re:Post Private uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that's
linked directly to re:Post Private. Service-linked roles are predefined by re:Post Private and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up re:Post Private easier because you don’t have to
manually add the necessary permissions. re:Post Private defines the permissions of its
service-linked roles, and unless defined otherwise, only re:Post Private can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy can't be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for re:Post Private

re:Post Private uses the service-linked role named **AWSServiceRoleForrePostPrivate**. re:Post Private uses this service-linked role to publish data to CloudWatch.

The AWSServiceRoleForrePostPrivate service-linked role trusts the following services to assume the
role:

- `repostspace.amazonaws.com`

The role permissions policy named `AWSrePostPrivateCloudWatchAccess` allows re:Post Private to complete the
following actions on the specified resources:

- Action on `cloudwatch`:

`PutMetricData`

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

For more information, see [AWSrePostPrivateCloudWatchAccess](security-with-iam-managed-policy.md#cloudwatch-metric-manpol "security-with-iam-managed-policy.md#cloudwatch-metric-manpol").

## Creating a service-linked role for re:Post Private

You don't need to manually create a service-linked role. When you
create your first private re:Post in the AWS Management Console, the AWS CLI, or the AWS API, re:Post Private creates
the service-linked role for you.

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role. Also, if you were using the
re:Post Private service before December 1, 2023, when it began supporting service-linked roles,
then re:Post Private created the `AWSServiceRoleForrePostPrivate` role in your account. To learn more, see [A
new role appeared in my AWS account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create your first private re:Post,
re:Post Private creates the service-linked role for you again.

In the AWS CLI or the AWS API, create a
service-linked role with the `repostspace.amazonaws.com` service name. For more
information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, you can use this same process to create the role
again.

## Editing a service-linked role for re:Post Private

re:Post Private doesn't allow you to edit the `AWSServiceRoleForrePostPrivate` service-linked role. After you
create a service-linked role, you can't change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for re:Post Private

You don't need to manually delete the `AWSServiceRoleForrePostPrivate` role. When you delete your private re:Post
in the AWS Management Console, the AWS CLI, or the AWS API, re:Post Private deletes the service-linked role for you.

You can also use the IAM console, the AWS CLI, or the AWS API to manually delete the
service-linked role.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForrePostPrivate service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for re:Post Private service-linked roles

re:Post Private supports using service-linked roles in the AWS Regions where the
service is available.

| Region name               | Region identity | Support in re:Post Private |
| ------------------------- | --------------- | -------------------------- |
| US East (N. Virginia)     | us-east-1       | Yes                        |
| US East (Ohio)            | us-east-2       | No                         |
| US West (N. California)   | us-west-1       | No                         |
| US West (Oregon)          | us-west-2       | Yes                        |
| Africa (Cape Town)        | af-south-1      | No                         |
| Asia Pacific (Hong Kong)  | ap-east-1       | No                         |
| Asia Pacific (Jakarta)    | ap-southeast-3  | No                         |
| Asia Pacific (Mumbai)     | ap-south-1      | No                         |
| Asia Pacific (Osaka)      | ap-northeast-3  | No                         |
| Asia Pacific (Seoul)      | ap-northeast-2  | No                         |
| Asia Pacific (Singapore)  | ap-southeast-1  | Yes                        |
| Asia Pacific (Sydney)     | ap-southeast-2  | Yes                        |
| Asia Pacific (Tokyo)      | ap-northeast-1  | No                         |
| Canada (Central)          | ca-central-1    | Yes                        |
| Europe (Frankfurt)        | eu-central-1    | Yes                        |
| Europe (Ireland)          | eu-west-1       | Yes                        |
| Europe (London)           | eu-west-2       | No                         |
| Europe (Milan)            | eu-south-1      | No                         |
| Europe (Paris)            | eu-west-3       | No                         |
| Europe (Stockholm)        | eu-north-1      | No                         |
| Middle East (Bahrain)     | me-south-1      | No                         |
| Middle East (UAE)         | me-central-1    | No                         |
| South America (São Paulo) | sa-east-1       | No                         |
