# Using service-linked roles for Device Farm

AWS Device Farm uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Device Farm. Service-linked roles are predefined by Device Farm and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up Device Farm easier because you don’t have to
manually add the necessary permissions. Device Farm defines the permissions of its
service-linked roles, and unless defined otherwise, only Device Farm can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your Device Farm resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with
IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the
**Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

## Service-linked role permissions for Device Farm

Device Farm uses the service-linked role named **AWSServiceRoleForDeviceFarmTestGrid** –
Allows Device Farm to access AWS resources on your behalf.

The AWSServiceRoleForDeviceFarmTestGrid service-linked role trusts the following services to assume the
role:

- `testgrid.devicefarm.amazonaws.com`

The role permissions policy allows Device Farm to complete the following actions:

- For your account
  - Create network interfaces
  - Describe network interfaces
  - Describe VPCs
  - Describe subnets
  - Describe security groups
  - Delete interfaces
  - Modify network interfaces

- For network interfaces
  - Create tags

- For EC2 network interfaces managed by Device Farm
  - Create network interface permissions

The full IAM policy reads:

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
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:security-group/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/AWSDeviceFarmManaged": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:*:*:network-interface/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": "CreateNetworkInterface"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterfacePermission",
 "ec2:DeleteNetworkInterface"
 ],
 "Resource": "arn:aws:ec2:*:*:network-interface/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/AWSDeviceFarmManaged": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:ModifyNetworkInterfaceAttribute"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:security-group/*",
 "arn:aws:ec2:*:*:instance/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:ModifyNetworkInterfaceAttribute"
 ],
 "Resource": "arn:aws:ec2:*:*:network-interface/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/AWSDeviceFarmManaged": "true"
 }
 }
 }
 ]
}`

```

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for Device Farm

When you provide a VPC config for a TestGridProject, you don't need to manually create a service-linked role. When you
create your first Device Farm resource in the AWS Management Console, the AWS CLI, or the AWS API, Device Farm
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create your first Device Farm resource,
Device Farm creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**Device Farm** use case. In the AWS CLI or the AWS API, create
a service-linked role with the `testgrid.devicefarm.amazonaws.com` service name. For more
information, see [Creating a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you delete this
service-linked role, you can use this same process to create the role again.

## Editing a service-linked role for Device Farm

Device Farm does not allow you to edit the AWSServiceRoleForDeviceFarmTestGrid service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for Device Farm

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the Device Farm service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForDeviceFarmTestGrid
service-linked role. For more information, see [Deleting a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for Device Farm service-linked roles

Device Farm supports using service-linked roles in all of the regions where the service is available. For more information, see [AWS Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

Device Farm does not support using service-linked roles in every region where the service is available. You can use the AWSServiceRoleForDeviceFarmTestGrid role in the following regions.

| Region name               | Region identity | Support in Device Farm |
| ------------------------- | --------------- | ---------------------- |
| US East (N. Virginia)     | us-east-1       | No                     |
| US East (Ohio)            | us-east-2       | No                     |
| US West (N. California)   | us-west-1       | No                     |
| US West (Oregon)          | us-west-2       | Yes                    |
| Asia Pacific (Mumbai)     | ap-south-1      | No                     |
| Asia Pacific (Osaka)      | ap-northeast-3  | No                     |
| Asia Pacific (Seoul)      | ap-northeast-2  | No                     |
| Asia Pacific (Singapore)  | ap-southeast-1  | No                     |
| Asia Pacific (Sydney)     | ap-southeast-2  | No                     |
| Asia Pacific (Tokyo)      | ap-northeast-1  | No                     |
| Canada (Central)          | ca-central-1    | No                     |
| Europe (Frankfurt)        | eu-central-1    | No                     |
| Europe (Ireland)          | eu-west-1       | No                     |
| Europe (London)           | eu-west-2       | No                     |
| Europe (Paris)            | eu-west-3       | No                     |
| South America (São Paulo) | sa-east-1       | No                     |
| AWS GovCloud (US)         | us-gov-west-1   | No                     |
