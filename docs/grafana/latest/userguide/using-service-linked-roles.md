# Using service-linked roles for

Amazon Managed Grafana

Amazon Managed Grafana uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that
is linked directly to Amazon Managed Grafana. Service-linked roles are predefined by Amazon Managed Grafana
and include all the permissions that the service requires to call other AWS services on
your behalf.

A service-linked role makes setting up Amazon Managed Grafana easier because you don’t have to
manually add the necessary permissions. Amazon Managed Grafana defines the permissions of its
service-linked roles, and unless defined otherwise, only Amazon Managed Grafana can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your Amazon Managed Grafana resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS Services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column. Choose a
**Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for

Amazon Managed Grafana

Amazon Managed Grafana uses the service-linked role named **AmazonManagedGrafana**
– Amazon Managed Grafana uses this role to create and configure resources, such as ENIs or Secrets Manager secrets, within customer accounts. The AmazonManagedGrafana service-linked role trusts the following
services to assume the role:

- `grafana.amazonaws.com`

The AmazonManagedGrafana service-linked role is attached to the `AmazonGrafanaServiceLinkedRolePolicy`
policy. For updates to this policy, see [Amazon Managed Grafana updates to AWS managed
policies](security-iam-awsmanpol.md#iam-awsmanpol-updates "security-iam-awsmanpol.md#iam-awsmanpol-updates").

The role permissions policy allows Amazon Managed Grafana to complete the following actions
on the specified resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeVpcs",
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateNetworkInterface",
 "Resource": "*",
 "Condition": {
 "ForAllValues:StringEquals": {
 "aws:TagKeys": [
 "AmazonGrafanaManaged"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": "arn:aws:ec2:*:*:network-interface/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": "CreateNetworkInterface"
 },
 "Null": {
 "aws:RequestTag/AmazonGrafanaManaged": "false"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:DeleteNetworkInterface",
 "Resource": "*",
 "Condition": {
 "Null": {
 "ec2:ResourceTag/AmazonGrafanaManaged": "false"
 }
 }
 }
 ]
}`

```

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for Amazon Managed Grafana

You don't need to manually create a service-linked role. When you
call CreateWorkspace with a VpcConfiguration in the AWS Management Console, the AWS CLI, or the AWS API, Amazon Managed Grafana
creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role. Also, if you were
using the Amazon Managed Grafana service before November 30, 2022, when it began supporting
service-linked roles, then Amazon Managed Grafana created the AmazonManagedGrafana role in your
account. To learn more, see [A new role appeared in my IAM account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you
call CreateWorkspace with a VpcConfiguration, Amazon Managed Grafana creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**Grafana** use case. In the AWS CLI or the AWS API,
create a service-linked role with the `grafana.amazonaws.com` service name.
For more information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the
_IAM User Guide_. If you delete this service-linked role, you can
use this same process to create the role again.

## Editing a service-linked role for Amazon Managed Grafana

Amazon Managed Grafana does not allow you to edit the AmazonManagedGrafana service-linked role. After you
create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role
using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for Amazon Managed Grafana

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don’t have an unused entity that is
not actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the Amazon Managed Grafana service is using the role when you try to delete the
resources, then the deletion might fail. If that happens, wait for a few minutes and
try the operation again.

###### To delete Amazon Managed Grafana resources used by the AmazonManagedGrafana

1. Navigate to the **All workspaces** view in your
   `Region` in the AWS console.
2. Delete all the workspaces in the `Region`. You have to check the
   radio button for each workspace and choose the **delete**
   button in the upper right side of the **All workspaces** view.
   Repeat deleting each workspace until all the workspaces are deleted from the
   `Region`. For more information about deleting a workspace in
   Amazon Managed Grafana, see [Deleting a workspace](AMG-edit-delete-workspace.md "AMG-edit-delete-workspace.md") topic in this user guide.

###### Note

Repeat the procedure for each AWS Region where you have workspaces. You must
delete all workspaces _in all Regions_ before you can delete the
service-linked role.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AmazonManagedGrafana
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported regions for Amazon Managed Grafana service-linked

roles

Amazon Managed Grafana supports using service-linked roles in all of the regions where the
service is available. For more information, see [AWS regions and endpoints](../../../general/latest/gr/grafana-service.md "../../../general/latest/gr/grafana-service.md").
