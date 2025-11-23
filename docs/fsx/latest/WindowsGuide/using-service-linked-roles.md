# Using service-linked roles for

FSx for Windows File Server

Amazon FSx for Windows File Server uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to FSx for Windows File Server. Service-linked roles are predefined by FSx for Windows File Server and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up FSx for Windows File Server easier because you don’t have to
manually add the necessary permissions. FSx for Windows File Server defines the permissions of its
service-linked roles, and unless defined otherwise, only FSx for Windows File Server can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your FSx for Windows File Server resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work
with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in
the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for
that service.

## Service-linked role permissions for FSx for Windows File Server

FSx for Windows File Server uses the service-linked role named `AWSServiceRoleForAmazonFSx`
– Which performs certain actions in your account, like creating Elastic Network
Interfaces for your file systems in your VPC.

The role permissions policy allows FSx for Windows File Server to complete the following actions on
the all applicable AWS resources:

You can't attach AmazonFSxServiceRolePolicy to your IAM entities. This policy is attached to a
service-linked role that allows FSx to manage AWS resources on your behalf. For more
information, see [Using service-linked roles for
FSx for Windows File Server](using-service-linked-roles.md "using-service-linked-roles.md").

For updates to this policy, see
[AmazonFSxServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonFSxServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonFSxServiceRolePolicy").

This policy grants administrative permissions that allows FSx to manage AWS resources on the user's behalf.

**Permissions details**

The AmazonFSxServiceRolePolicy role permissions are defined by the AmazonFSxServiceRolePolicy AWS managed policy. AmazonFSxServiceRolePolicy has
the following permissions:

###### Note

AmazonFSxServiceRolePolicy is used by all Amazon FSx file system types; some of the listed permissions may not applicable to FSx for Windows.

- `ds` – Allows FSx to view, authorize, and unauthorize applications in your Directory Service directory.
- `ec2` – Allows FSx to do the following:
  - View, create, and disassociate network interfaces associated with an Amazon FSx file system.
  - View one or more Elastic IP addresses associated with an Amazon FSx file system.
  - View Amazon VPCs, security groups, and subnets associated with an Amazon FSx file system.
  - Assign IPv6 addresses to customer network interfaces that have an `AmazonFSx.FileSystemId` tag.
  - Unassign IPv6 addresses from customer network interfaces that have an `AmazonFSx.FileSystemId` tag.
  - To provide enhanced security group validation of all security groups that can be used with a VPC.
  - Create a permission for an AWS-authorized user to perform certain operations on a network interface.

- `cloudwatch` – Allows FSx to publish metric data points to CloudWatch under the AWS/FSx namespace.
- `route53` – Allows FSx to associate an Amazon VPC with a private hosted zone.
- `logs` – Allows FSx to describe and write to CloudWatch Logs log streams. This is so that
  users can send file access audit logs for an FSx for Windows File Server file system to a CloudWatch Logs stream.
- `firehose` – Allows FSx to describe and write to Amazon Data Firehose delivery streams. This is so that
  users can publish the file access audit logs for an FSx for Windows File Server file system to an Amazon Data Firehose delivery stream.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateFileSystem",
 "Effect": "Allow",
 "Action": [
 "ds:AuthorizeApplication",
 "ds:GetAuthorizedApplicationDetails",
 "ds:UnauthorizeApplication",
 "ec2:CreateNetworkInterface",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:DeleteNetworkInterface",
 "ec2:DescribeAddresses",
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVPCs",
 "ec2:DisassociateAddress",
 "ec2:GetSecurityGroupsForVpc",
 "route53:AssociateVPCWithHostedZone"
 ],
 "Resource": "*"
 },
 {
 "Sid": "PutMetrics",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/FSx"
 }
 }
 },

 {
 "Sid": "TagResourceNetworkInterface",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*"
 ],
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": "CreateNetworkInterface"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "AmazonFSx.FileSystemId"
 }
 }
 },
 {
 "Sid": "ManageNetworkInterface",
 "Effect": "Allow",
 "Action": [
 "ec2:AssignPrivateIpAddresses",
 "ec2:ModifyNetworkInterfaceAttribute",
 "ec2:UnassignPrivateIpAddresses"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*"
 ],
 "Condition": {
 "Null": {
 "aws:ResourceTag/AmazonFSx.FileSystemId": "false"
 }
 }
 },
 {
 "Sid": "ManageRouteTable",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateRoute",
 "ec2:ReplaceRoute",
 "ec2:DeleteRoute"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:route-table/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/AmazonFSx": "ManagedByAmazonFSx"
 }
 }
 },
 {
 "Sid": "PutCloudWatchLogs",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/fsx/*"
 },
 {
 "Sid": "ManageAuditLogs",
 "Effect": "Allow",
 "Action": [
 "firehose:DescribeDeliveryStream",
 "firehose:PutRecord",
 "firehose:PutRecordBatch"
 ],
 "Resource": "arn:aws:firehose:*:*:deliverystream/aws-fsx-*"
 }
 ]
}`

```

Any updates to this policy are described in
[Amazon FSx updates to AWS managed
policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates").

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for FSx for Windows File Server

You don't need to manually create a service-linked role. When you create a file system
in the AWS Management Console, the IAM CLI, or the IAM API, FSx for Windows File Server creates the service-linked
role for you.

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role. To learn more, see [A New
Role Appeared in My IAM Account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you create a file system,
FSx for Windows File Server creates the service-linked role for you again.

## Editing a service-linked role for FSx for Windows File Server

FSx for Windows File Server does not allow you to edit the service-linked role. After you
create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using
IAM. For more information, see [Editing a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for FSx for Windows File Server

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must delete all of your file systems and
backups before you can manually delete the service-linked role.

###### Note

If the FSx for Windows File Server service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the IAM CLI, or the IAM API to delete the
service-linked role. For more information, see [Deleting a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported regions for FSx for Windows File Server service-linked

roles

FSx for Windows File Server supports using service-linked roles in all of the regions where the
service is available. For more information, see [AWS Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
