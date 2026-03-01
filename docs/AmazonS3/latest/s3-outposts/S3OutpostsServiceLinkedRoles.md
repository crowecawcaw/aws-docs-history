# Using service-linked roles for Amazon S3 on Outposts

Amazon S3 on Outposts uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to S3 on Outposts. Service-linked roles are predefined by S3 on Outposts and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up S3 on Outposts easier because you don’t have to
manually add the necessary permissions. S3 on Outposts defines the permissions of its
service-linked roles, and unless defined otherwise, only S3 on Outposts can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your S3 on Outposts resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with
IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the
**Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

## Service-linked role permissions for S3 on Outposts

S3 on Outposts uses the service-linked role named **AWSServiceRoleForS3OnOutposts** to
help manage network resources for you.

The `AWSServiceRoleForS3OnOutposts` service-linked role trusts the following services to assume
the role:

- `s3-outposts.amazonaws.com`

The role permissions policy named `AWSS3OnOutpostsServiceRolePolicy` allows S3 on Outposts to
complete the following actions on the specified resources:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeVpcs",
 "ec2:DescribeCoipPools",
 "ec2:GetCoipPoolUsage",
 "ec2:DescribeAddresses",
 "ec2:DescribeLocalGatewayRouteTableVpcAssociations"
 ],
 "Resource": "*",
 "Sid": "DescribeVpcResources"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:security-group/*"
 ],
 "Sid": "CreateNetworkInterface"
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
 "aws:RequestTag/CreatedBy": "S3 On Outposts"
 }
 },
 "Sid": "CreateTagsForCreateNetworkInterface"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AllocateAddress"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:ipv4pool-ec2/*"
 ],
 "Sid": "AllocateIpAddress"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AllocateAddress"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:elastic-ip/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/CreatedBy": "S3 On Outposts"
 }
 },
 "Sid": "CreateTagsForAllocateIpAddress"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:ModifyNetworkInterfaceAttribute",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:DeleteNetworkInterface",
 "ec2:DeleteNetworkInterfacePermission",
 "ec2:DisassociateAddress",
 "ec2:ReleaseAddress",
 "ec2:AssociateAddress"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/CreatedBy": "S3 On Outposts"
 }
 },
 "Sid": "ReleaseVpcResources"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": [
 "CreateNetworkInterface",
 "AllocateAddress"
 ],
 "aws:RequestTag/CreatedBy": [
 "S3 On Outposts"
 ]
 }
 },
 "Sid": "CreateTags"
 }
 ]
}`

```

You must configure permissions to allow an IAM entity (such as a role) to create, edit,
or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for S3 on Outposts

You don't need to manually create a service-linked role. When you create an S3 on Outposts endpoint in the
AWS Management Console, the AWS CLI, or the AWS API, S3 on Outposts creates the service-linked role
for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create an S3 on Outposts endpoint,
S3 on Outposts creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**S3 on Outposts** use case. In the AWS CLI or the AWS API, create
a service-linked role with the `s3-outposts.amazonaws.com` service name. For more
information, see [Creating a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you delete this
service-linked role, you can use this same process to create the role again.

## Editing a service-linked role for S3 on Outposts

S3 on Outposts does not allow you to edit the `AWSServiceRoleForS3OnOutposts` service-linked role.
This includes the name of the role because various entities might reference it. However, you
can edit the description of the role using IAM. For more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for S3 on Outposts

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the S3 on Outposts service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

###### To delete S3 on Outposts resources used by the AWSServiceRoleForS3OnOutposts role

1. [Delete the S3 on Outposts
   endpoints](S3OutpostsDeleteEndpoints.md "S3OutpostsDeleteEndpoints.md") in your AWS account across all AWS Regions.
2. Delete the service-linked role using IAM.

Use the IAM console, the AWS CLI, or the AWS API to delete the
`AWSServiceRoleForS3OnOutposts` service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for S3 on Outposts service-linked roles

S3 on Outposts supports using service-linked roles in all of the AWS Regions where
the service is available. For more information, see [S3 on Outposts Regions and endpoints](../../../general/latest/gr/outposts_region.md#outposts_region_s3 "../../../general/latest/gr/outposts_region.md#outposts_region_s3").
