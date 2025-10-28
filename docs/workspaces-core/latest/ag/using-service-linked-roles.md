# Using service-linked roles for

Amazon WorkSpaces Instances

Amazon WorkSpaces Instances uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to WorkSpaces Instances. Service-linked roles are predefined by WorkSpaces Instances and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up WorkSpaces Instances easier because you don’t have to
manually add the necessary permissions. WorkSpaces Instances defines the permissions of its
service-linked roles, and unless defined otherwise, only WorkSpaces Instances can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your WorkSpaces Instances resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for WorkSpaces Instances

WorkSpaces Instances uses the service-linked role named **AWSServiceRoleForWorkSpacesInstances** –
This service linked role provides administrative access to Amazon WorkSpaces to manage EC2 instances in your AWS account.

The AWSServiceRoleForWorkSpacesInstances service-linked role trusts the following services to assume the
role:

- `workspaces-instances.amazonaws.com`

It uses the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeInstanceStatus",
 "ec2:DescribeVolumes"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:TerminateInstances",
 "ec2:DeleteVolume",
 "ec2:StopInstances",
 "ec2:StartInstances"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "ec2:ManagedResourceOperator": "workspaces-instances.amazonaws.com"
 }
 }
 }
 ]
}`

```

The role permissions policy named AWSServiceRolePolicyForWorkspacesInstances allows WorkSpaces Instances to complete the
following actions on the specified resources:

- For monitoring your resources: `ec2:DescribeInstances`, `ec2:DescribeInstanceStatus`,
  and `ec2:DescribeVolumes`.
- For managing the ec2 instances which workspaces-instances.amazonaws.com operate:
  `ec2:TerminateInstances`, `ec2:DeleteVolume`, `ec2:StopInstances`,
  and `ec2:StartInstances`.

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for WorkSpaces Instances

You can use either the IAM or WorkSpaces console to create a service-linked role with the
**Workspaces instances** use case.

If you are using either the AWS CLI or the AWS API, create a
service-linked role with the `workspaces-instances.amazonaws.com` service name.

For more information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, you can use this same process to create the role
again.

## Editing a service-linked role for WorkSpaces Instances

WorkSpaces Instances does not allow you to edit the AWSServiceRoleForWorkSpacesInstances service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for WorkSpaces Instances

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the WorkSpaces Instances service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### To remove WorkSpaces Instances resources used by the AWSServiceRoleForWorkSpacesInstances

1. Use the ec2 console or api to list all the volumes with the operator.principal being workspaces-instances.amazonaws.com.
2. Delete all those volumes using the console or api of workspaces-instances service.
3. Delete all WorkSpaces instances in your account.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForWorkSpacesInstances service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for WorkSpaces Instances service-linked roles

WorkSpaces Instances supports using service-linked roles in all of the Regions where the service
is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
