# AWS managed policies for AWS Global Accelerator

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy: AWSServiceRoleForGlobalAccelerator

You can't attach `AWSServiceRoleForGlobalAccelerator` to your IAM entities.
This policy is attached to a service-linked role that allows AWS Global Accelerator to access AWS
services and resources that are used or managed by Global Accelerator. For more information, see
[Service-linked role for AWS Global Accelerator](using-service-linked-roles.md "using-service-linked-roles.md").

## AWS managed policy: GlobalAcceleratorReadOnlyAccess

You can attach `GlobalAcceleratorReadOnlyAccess` to your IAM entities.
This policy grants read-only access to actions for working with accelerators in Global Accelerator. It's
useful for users who only need to view information in the console or
make calls to the AWS Command Line Interface or the API that use `List*` or `Describe*` operations.

To view the permissions for this policy, see [GlobalAcceleratorReadOnlyAccess](../../../aws-managed-policy/latest/reference/GlobalAcceleratorReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/GlobalAcceleratorReadOnlyAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: GlobalAcceleratorFullAccess

You can attach `GlobalAcceleratorFullAccess` to your IAM entities.
This policy grants full access to actions for working with accelerators in Global Accelerator. Attach
it to IAM users and other principals who need full access to Global Accelerator actions.

###### Note

If you create an identity-based permissions policy that does not include
the required permissions for Amazon EC2 and Elastic Load Balancing, users with that policy will not be able to
add Amazon EC2 and Elastic Load Balancing resources to accelerators.

To view the permissions for this policy, see [GlobalAcceleratorFullAccess](../../../aws-managed-policy/latest/reference/GlobalAcceleratorFullAccess.md "../../../aws-managed-policy/latest/reference/GlobalAcceleratorFullAccess.md") in the _AWS Managed Policy Reference_.

## Global Accelerator updates to AWS managed

policies

View details about updates to AWS managed policies for Global Accelerator since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the Global Accelerator [Document history page](WhatsNew.md "WhatsNew.md").

| Change                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                           | Date              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSGlobalAcceleratorSLRPolicy](using-service-linked-roles.md#GAXSLRRole "using-service-linked-roles.md#GAXSLRRole") – Updated policy                                                                                                                                                               | Global Accelerator added a new permission to describe target groups on load balancers. Global Accelerator uses `elasticloadbalancing:DescribeTargetGroups` to identify load balancers with target type `ip`, which is not a supported target type for dual-stack load balancer endpoints in Global Accelerator.                                                                                       | October 20, 2023  |
| [AWSGlobalAcceleratorSLRPolicy](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/aws-service-role/AWSGlobalAcceleratorSLRPolicy "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/aws-service-role/AWSGlobalAcceleratorSLRPolicy") – Updated policy | Global Accelerator added new permissions to describe listeners on load balancers and describe addresses on EC2 instances. Global Accelerator uses `elasticloadbalancing:DescribeListeners` to support making listener management decisions for load balancers, based on listener configurations. Global Accelerator uses `ec2:DescribeAddresses` to add Elastic IP address endpoints to accelerators. | May 23, 2023      |
| [AWSGlobalAcceleratorSLRPolicy](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/aws-service-role/AWSGlobalAcceleratorSLRPolicy "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/aws-service-role/AWSGlobalAcceleratorSLRPolicy") – Updated policy | Global Accelerator added new permissions to support IPv6 addresses. Global Accelerator uses `ec2:AssignIpv6Addresses` to update the Global Accelerator ENI on a customer subnet with an IPv6 address for sending and receiving IPv6 traffic, and uses `UnassignIpv6Addresses` to remove the IPv6 address when it's no longer needed.                                                                  | November 15, 2021 |
| [AWSGlobalAcceleratorSLRPolicy](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/aws-service-role/AWSGlobalAcceleratorSLRPolicy "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/aws-service-role/AWSGlobalAcceleratorSLRPolicy") – Updated policy | Global Accelerator added a new permission to help Global Accelerator to diagnose errors. Global Accelerator uses `ec2:DescribeRegions` to determine the AWS Region that a customer is in, which can help Global Accelerator to troubleshoot errors.                                                                                                                                                   | May 18, 2021      |
| Global Accelerator started tracking changes                                                                                                                                                                                                                                                         | Global Accelerator started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                             | May 18, 2021      |
