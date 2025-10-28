# Using service-linked roles for Network Firewall

AWS Network Firewall uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Network Firewall. Service-linked roles are predefined by Network Firewall and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up Network Firewall easier because you don’t have to
manually add the necessary permissions. Network Firewall defines the permissions of its
service-linked roles, and unless defined otherwise, only Network Firewall can assume its roles.
The defined permissions include the trust policy and the permissions policy. That
permissions policy can't be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources.
This protects your Network Firewall resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column. Choose a
**Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for

Network Firewall

Network Firewall uses the service-linked role named **`AWSServiceRoleForNetworkFirewall`** –
An access policy that allows AWS Network Firewall to manage Network Firewall related resources on behalf of your AWS account. Network Firewall uses its service-linked-role to create, describe, and delete VPC endpoints in support of your firewall management activities. Network Firewall is the only service that uses this service-linked role,
and Network Firewall doesn't use any other service's service-linked role. This
service-linked role is used in the Network Firewall managed policy
`AWSNetworkFirewallServiceRolePolicy`. For more information, see [AWS managed policies for AWS Network Firewall](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

The `AWSServiceRoleForNetworkFirewall` service-linked role trusts the `network-firewall.amazonaws.com` service
principal to assume the role. The following is the JSON trust policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "network-firewall.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

The role permissions policy allows Network Firewall to perform the following actions:

- Describe and create Amazon EC2 VPC resources for firewall management.
- Describe ACM certificates for use with TLS inspection configurations.
- Create and manage resource groups.
- Periodically check the VPC CIDR blocks and management of firewall endpoints in the VPC.
- Describe Amazon EC2 instances and Amazon EC2 network interfaces for use in resource groups.

The following is the JSON role permissions
policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:CreateVpcEndpoint",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeInstances",
 "ec2:DescribeNetworkInterfaces"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "acm:DescribeCertificate",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "resource-groups:ListGroupResources",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "tag:GetResources",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaLast": "resource-groups.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:*:*:vpc-endpoint/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": "CreateVpcEndpoint",
 "aws:RequestTag/AWSNetworkFirewallManaged": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteVpcEndpoints"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/AWSNetworkFirewallManaged": "true"
 }
 }
 }
 ]
}`

```

When you enable logging for a firewall, Network Firewall uses a log delivery service,
which might create a service-linked role in your account named
`AWSServiceRoleForLogDelivery` to deliver logs.

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for

Network Firewall

You don't need to manually create a service-linked role for AWS Network Firewall. When you
create a AWS Network Firewall firewall in the AWS Management Console, the AWS CLI, or the AWS API, if your account
doesn't have the Network Firewall service-linked role yet, Network Firewall creates the role
for you. If you manage your firewall resources through AWS Firewall Manager, Firewall Manager creates the
service-linked role for accounts that are within scope of the Firewall Manager policy. If you want
to, you can create the role through the IAM console. If you delete the service-linked
role, the next time you create an Network Firewall resource, Network Firewall creates one for
you again.

## Editing a service-linked role for

Network Firewall

Network Firewall doesn't allow you to edit the `AWSServiceRoleForNetworkFirewall` service-linked role. After you create
a service-linked role, you can't change the name of the role because various entities
might reference it. However, you can edit the description of the role using IAM. For
more information, see [Editing a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for

Network Firewall

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is
not actively monitored or maintained. You must clean up the resources that require your
service-linked role before you can manually delete it. You can delete the service-linked
role used by Network Firewall if you no longer want to use the service. To delete the role,
you must delete all firewalls, firewall policies, stateful rule groups, and stateless
rule groups, in all Regions where you have them defined.

###### Note

If the Network Firewall service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

###### To delete all Network Firewall resources

1. On the Amazon VPC console, update all route tables that send traffic through your firewall
   endpoints, to remove the endpoints from the traffic flow. For information about managing route tables for your VPC, see
   [Route
   tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") in the _Amazon Virtual Private Cloud User
   Guide_.
2. On the Network Firewall console, remove your firewalls, firewall policies,
   stateful rules groups, and stateless rule groups. For information, see [Deleting a firewall in AWS Network Firewall](deleting-firewall.md "deleting-firewall.md"), [Deleting a firewall policy in AWS Network Firewall](firewall-policy-deleting.md "firewall-policy-deleting.md"), and [Deleting a stateless rule group](rule-group-deleting.md "rule-group-deleting.md").

This removes all resources that Network Firewall used the service-linked role for.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the IAM CLI, or the IAM API to delete the `AWSServiceRoleForNetworkFirewall`
service-linked role. For more information, see [Deleting a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for

Network Firewall service-linked roles

Network Firewall supports using service-linked roles in all of the Regions where the service is
available. For a Region list, see [AWS Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
