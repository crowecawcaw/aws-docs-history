# Use service-linked roles for

CloudFront

Amazon CloudFront uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to CloudFront. Service-linked roles are predefined by CloudFront and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up CloudFront easier because you don’t have to
manually add the necessary permissions. CloudFront defines the permissions of its
service-linked roles, and unless defined otherwise, only CloudFront can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your CloudFront resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for CloudFront VPC Origins

CloudFront VPC Origins uses the service-linked role named **AWSServiceRoleForCloudFrontVPCOrigin** –
Allows CloudFront to manage EC2 elastic network interfaces and security groups on your behalf.

The AWSServiceRoleForCloudFrontVPCOrigin service-linked role trusts the following services to assume the
role:

- `vpcorigin.cloudfront.amazonaws.com`

The role permissions policy named AWSCloudFrontVPCOriginServiceRolePolicy allows CloudFront VPC Origins to complete the
following actions on the specified resources:

- Action: `ec2:CreateNetworkInterface` on
  `arn:aws:ec2:*:*:network-interface/*`
- Action: `ec2:CreateNetworkInterface` on
  `arn:aws:ec2:*:*:subnet/*` and `arn:aws:ec2:*:*:security-group/*`
- Action: `ec2:CreateSecurityGroup` on
  `arn:aws:ec2:*:*:security-group/*`
- Action: `ec2:CreateSecurityGroup` on
  `arn:aws:ec2:*:*:vpc/*`
- Action: `ec2:ModifyNetworkInterfaceAttribute`, `ec2:DeleteNetworkInterface`, `ec2:DeleteSecurityGroup`, `ec2:AssignIpv6Addresses`, and `ec2:UnassignIpv6Addresses` on
  `supported AWS resources that have the `aws:ResourceTag/aws.cloudfront.vpcorigin` tag enabled`
- Action: `ec2:DescribeNetworkInterfaces`, `ec2:DescribeSecurityGroups`, `ec2:DescribeInstances`, `ec2:DescribeInternetGateways`, `ec2:DescribeSubnets`, `ec2:DescribeRegions`, and `ec2:DescribeAddresses` on
  `all AWS resources that the actions support`
- Action: `ec2:CreateTags` on
  `arn:aws:ec2:*:*:security-group/*` and `arn:aws:ec2:*:*:network-interface/*`
- Action: `elasticloadbalancing:DescribeLoadBalancers`, `elasticloadbalancing:DescribeListeners`, and `elasticloadbalancing:DescribeTargetGroups` on
  `all AWS resources that the actions support`

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Create a service-linked role for CloudFront VPC Origins

You don't need to manually create a service-linked role. When you
create a VPC origin in the AWS Management Console, the AWS CLI, or the AWS API, CloudFront VPC Origins creates
the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create a VPC origin,
CloudFront VPC Origins creates the service-linked role for you again.

## Edit a service-linked role for CloudFront VPC Origins

CloudFront VPC Origins does not allow you to edit the AWSServiceRoleForCloudFrontVPCOrigin service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Delete a service-linked role for CloudFront VPC Origins

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the CloudFront service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### To delete CloudFront VPC Origins resources used by the AWSServiceRoleForCloudFrontVPCOrigin

- Delete the VPC origin resources in your account.
  - It might take some time for CloudFront to finish deleting the resources from your account. If you can't delete the service-linked role right away, wait and try again.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForCloudFrontVPCOrigin service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for CloudFront VPC Origins service-linked roles

CloudFront VPC Origins does not support using service-linked roles in every Region where the
service is available. You can use the AWSServiceRoleForCloudFrontVPCOrigin role in the following Regions.

| Region name               | Region identity                      | Support in CloudFront |
| ------------------------- | ------------------------------------ | --------------------- |
| US East (N. Virginia)     | us-east-1                            | Yes                   |
| US East (Ohio)            | us-east-2                            | Yes                   |
| US West (N. California)   | us-west-1 (except AZ usw1-az2)       | Yes                   |
| US West (Oregon)          | us-west-2                            | Yes                   |
| Africa (Cape Town)        | af-south-1                           | Yes                   |
| Asia Pacific (Hong Kong)  | ap-east-1                            | Yes                   |
| Asia Pacific (Jakarta)    | ap-southeast-3                       | Yes                   |
| Asia Pacific (Melbourne)  | ap-southeast-4                       | Yes                   |
| Asia Pacific (Mumbai)     | ap-south-1                           | Yes                   |
| Asia Pacific (Hyderabad)  | ap-south-2                           | Yes                   |
| Asia Pacific (Osaka)      | ap-northeast-3                       | Yes                   |
| Asia Pacific (Seoul)      | ap-northeast-2                       | Yes                   |
| Asia Pacific (Singapore)  | ap-southeast-1                       | Yes                   |
| Asia Pacific (Sydney)     | ap-southeast-2                       | Yes                   |
| Asia Pacific (Tokyo)      | ap-northeast-1 (except AZ apne1-az3) | Yes                   |
| Canada (Central)          | ca-central-1 (except AZ cac1-az3)    | Yes                   |
| Canada West (Calgary)     | ca-west-1                            | Yes                   |
| Europe (Frankfurt)        | eu-central-1                         | Yes                   |
| Europe (Ireland)          | eu-west-1                            | Yes                   |
| Europe (London)           | eu-west-2                            | Yes                   |
| Europe (Milan)            | eu-south-1                           | Yes                   |
| Europe (Paris)            | eu-west-3                            | Yes                   |
| Europe (Spain)            | eu-south-2                           | Yes                   |
| Europe (Stockholm)        | eu-north-1                           | Yes                   |
| Europe (Zurich)           | eu-central-2                         | Yes                   |
| Israel (Tel Aviv)         | il-central-1                         | Yes                   |
| Middle East (Bahrain)     | me-south-1                           | Yes                   |
| Middle East (UAE)         | me-central-1                         | Yes                   |
| South America (São Paulo) | sa-east-1                            | Yes                   |
