# AWS managed policies for Amazon EC2

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy: AmazonEC2FullAccess

You can attach the `AmazonEC2FullAccess` policy to your IAM identities.
This policy grants permissions that allow full access to Amazon EC2.

To view the permissions for this policy, see [AmazonEC2FullAccess](../../../aws-managed-policy/latest/reference/AmazonEC2FullAccess.md "../../../aws-managed-policy/latest/reference/AmazonEC2FullAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AmazonEC2ReadOnlyAccess

You can attach the `AmazonEC2ReadOnlyAccess` policy to your IAM identities.
This policy grants permissions that allow read-only access to Amazon EC2.

To view the permissions for this policy, see [AmazonEC2ReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonEC2ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonEC2ReadOnlyAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AmazonEC2ImageReferencesAccessPolicy

You can attach the `AmazonEC2ImageReferencesAccessPolicy` policy
to your IAM identities. This policy grants the permissions needed to use the EC2
DescribeImageReferences API, including permission to view EC2 instances, launch
templates, Systems Manager parameters, and Image Builder recipes. The policy supports
the `IncludeAllResourceTypes` flag and will continue to work when AWS adds
support for new resource types, removing the need for future policy updates.

To view the permissions for this policy, see [AmazonEC2ImageReferencesAccessPolicy](../../../aws-managed-policy/latest/reference/AmazonEC2ImageReferencesAccessPolicy.md "../../../aws-managed-policy/latest/reference/AmazonEC2ImageReferencesAccessPolicy.md") in
the _AWS Managed Policy Reference_.

## AWS managed policy: AWSEC2CapacityReservationFleetRolePolicy

This policy is attached to the service-linked role named **AWSServiceRoleForEC2CapacityReservationFleet**
to allow the service to create, modify, and cancel Capacity Reservations in a Capacity Reservation Fleet on your behalf. For more information, see [Using service-linked roles for
Capacity Reservation Fleet](using-service-linked-roles.md "using-service-linked-roles.md").

To view the permissions for this policy, see [AWSEC2CapacityReservationFleetRolePolicy](../../../aws-managed-policy/latest/reference/AWSEC2CapacityReservationFleetRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSEC2CapacityReservationFleetRolePolicy.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSEC2FleetServiceRolePolicy

This policy is attached to the service-linked role named **AWSServiceRoleForEC2Fleet**
to allow EC2 Fleet to request, launch, terminate, and tag instances on your behalf. For more information, see [Service-linked role for
EC2 Fleet](ec2-fleet-prerequisites.md#ec2-fleet-service-linked-role "ec2-fleet-prerequisites.md#ec2-fleet-service-linked-role").

To view the permissions for this policy, see [AWSEC2FleetServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSEC2FleetServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSEC2FleetServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSEC2SpotFleetServiceRolePolicy

This policy is attached to the service-linked role named **AWSServiceRoleForEC2SpotFleet**
to allow Spot Fleet to launch and manage instances on your behalf. For more information, see [Service-linked role for
Spot Fleet](spot-fleet-prerequisites.md#service-linked-roles-spot-fleet-requests "spot-fleet-prerequisites.md#service-linked-roles-spot-fleet-requests").

To view the permissions for this policy, see [AWSEC2SpotFleetServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSEC2SpotFleetServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSEC2SpotFleetServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSEC2SpotServiceRolePolicy

This policy is attached to the service-linked role named **AWSServiceRoleForEC2Spot**
to allow Amazon EC2 to launch and manage Spot Instances on your behalf. For more information, see [Service-linked role for Spot Instance requests](service-linked-roles-spot-instance-requests.md "service-linked-roles-spot-instance-requests.md").

To view the permissions for this policy, see [AWSEC2SpotServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSEC2SpotServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSEC2SpotServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSEC2VssSnapshotPolicy

You can attach this managed policy to the IAM instance profile role that you use for your
Amazon EC2 Windows instances. The policy grants permissions to allow Amazon EC2 to create and
manage VSS snapshots on your behalf.

To view the permissions for this policy, see [AWSEC2VssSnapshotPolicy](../../../aws-managed-policy/latest/reference/AWSEC2VssSnapshotPolicy.md "../../../aws-managed-policy/latest/reference/AWSEC2VssSnapshotPolicy.md") in the _AWS Managed Policy Reference_.

## AWS managed policy:

DeclarativePoliciesEC2Report

This policy is attached to the service-linked role named
`AWSServiceRoleForDeclarativePoliciesEC2Report` to provide access to
read-only APIs needed to generate the account status report for declarative
policies.

To view the permissions for this policy, see [DeclarativePoliciesEC2Report](../../../aws-managed-policy/latest/reference/DeclarativePoliciesEC2Report.md "../../../aws-managed-policy/latest/reference/DeclarativePoliciesEC2Report.md") in the _AWS
Managed Policy Reference_.

## AWS managed policy: EC2FastLaunchFullAccess

You can attach the `EC2FastLaunchFullAccess` policy to your
instance profile or other IAM role. This policy grants full access to EC2 Fast Launch actions,
and targeted permissions as follows.

###### Permissions details

- **EC2 Fast Launch** – Administrative access
  is granted, so that the role can enable or disable EC2 Fast Launch, and describe EC2 Fast Launch
  images.
- **Amazon EC2** – Access is granted for Amazon EC2 RunInstances,
  CreateTags, Describe, and Create and Modify Launch Template operations. Access is also
  granted to create network and security group resources, authorize ingress rules, and delete
  resources that EC2 Fast Launch created.
- **IAM** – Access is granted to get and use
  instance profiles whose name contains `ec2fastlaunch` to create the
  EC2FastLaunchServiceRolePolicy service-linked role.
- **AWS CloudFormation** – Access is granted for EC2 Fast Launch to describe and
  create CloudFormation stacks, and to delete stacks that it created.

To view the permissions for this policy, see [EC2FastLaunchFullAccess](../../../aws-managed-policy/latest/reference/EC2FastLaunchFullAccess.md "../../../aws-managed-policy/latest/reference/EC2FastLaunchFullAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSEC2CapacityManagerServiceRolePolicy

This policy is attached to the service-linked role named **AWSServiceRoleForEC2CapacityManager**
to allow EC2 Capacity Manager to manage capacity resources and integrate with AWS Organizations on your behalf. For more information, see [Service-linked roles for EC2 Capacity Manager](using-service-linked-roles-cm.md "using-service-linked-roles-cm.md").

To view the permissions for this policy, see [AWSEC2CapacityManagerServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSEC2CapacityManagerServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSEC2CapacityManagerServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: EC2FastLaunchServiceRolePolicy

This policy is attached to the service-linked role named **AWSServiceRoleForEC2FastLaunch**
to allow Amazon EC2 to create and manage a set of pre-provisioned snapshots that reduce the time it takes
to launch instances from your EC2 Fast Launch-enabled AMI. For more information, see [Service-linked role for
EC2 Fast Launch](slr-windows-fast-launch.md "slr-windows-fast-launch.md").

To view the permissions for this policy, see [EC2FastLaunchServiceRolePolicy](../../../aws-managed-policy/latest/reference/EC2FastLaunchServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/EC2FastLaunchServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: Ec2InstanceConnect

You can attach the `Ec2InstanceConnect` policy to your IAM
identities. This policy grants permissions that allows customers to call EC2 Instance
Connect to publish ephemeral keys to their EC2 instances and connect via ssh or the EC2
Instance Connect CLI.

To view the permissions for this policy, see [Ec2InstanceConnect](../../../aws-managed-policy/latest/reference/EC2InstanceConnect.md "../../../aws-managed-policy/latest/reference/EC2InstanceConnect.md") in the _AWS Managed Policy
Reference_.

## AWS managed policy: Ec2InstanceConnectEndpoint

This policy is attached to a service-linked role named **AWSServiceRoleForEC2InstanceConnect**
to allow EC2 Instance Connect Endpoint to perform actions on your behalf. For more information, see [Service-linked role for EC2 Instance Connect Endpoint](eice-slr.md "eice-slr.md").

To view the permissions for this policy, see [Ec2InstanceConnectEndpoint](../../../aws-managed-policy/latest/reference/Ec2InstanceConnectEndpoint.md "../../../aws-managed-policy/latest/reference/Ec2InstanceConnectEndpoint.md") in the _AWS
Managed Policy Reference_. For a description of the updates to this
policy, see [Amazon EC2 updates to AWS managed policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates").

## Amazon EC2 updates to AWS managed policies

View details about updates to AWS managed policies for Amazon EC2 since this service
began tracking these changes.

| Change                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                          | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| [AWSEC2CapacityManagerServiceRolePolicy](#security-iam-awsmanpol-AWSEC2CapacityManagerServiceRolePolicy "#security-iam-awsmanpol-AWSEC2CapacityManagerServiceRolePolicy") – New policy                | Amazon EC2 added this policy to allow you to manage capacity resources and integrate with AWS Organizations on your behalf.                                                                                                                                                                                                                                                          | October 15, 2025  |
| [AmazonEC2ImageReferencesAccessPolicy](#security-iam-awsmanpol-AmazonEC2ImageReferencesAccessPolicy "#security-iam-awsmanpol-AmazonEC2ImageReferencesAccessPolicy") – New policy                      | Amazon EC2 added this policy to provide permission to scan all resources types supported by the EC2 DescribeImageReferences API.                                                                                                                                                                                                                                                     | August 26, 2025   |
| [Ec2InstanceConnectEndpoint](#Ec2InstanceConnectEndpoint "#Ec2InstanceConnectEndpoint") – Updated policy                                                                                              | To support the modification of existing Instance Connect Endpoints, Amazon EC2 updated this policy to add permissions to assign and unassign IPv6 addresses and modify security groups on network interfaces created by EC2 Instance Connect Endpoint. Amazon EC2 also updated this policy to replace the `Null` condition operator with the `StringLike` condition operator.        | July 31, 2025     |
| [EC2FastLaunchServiceRolePolicy](#security-iam-awsmanpol-EC2FastLaunchServiceRolePolicy "#security-iam-awsmanpol-EC2FastLaunchServiceRolePolicy") – Updated policy                                    | To help prevent orphaned resources, Amazon EC2 updated this policy to add permission to describe volumes, volume attributes and network interfaces, and to delete volumes and network interfaces that EC2 Fast Launch created.                                                                                                                                                       | July 17, 2025     |
| [EC2FastLaunchFullAccess](#security-iam-awsmanpol-EC2FastLaunchFullAccess "#security-iam-awsmanpol-EC2FastLaunchFullAccess") – Updated policy                                                         | Amazon EC2 updated this policy to include Create and Modify Launch Template operations, to create network and security group resources, authorize ingress rules, and delete resources that EC2 Fast Launch created. It can additionally describe and create CloudFormation stacks, and delete stacks that EC2 Fast Launch created.                                                   | May 14, 2025      |
| [EC2FastLaunchServiceRolePolicy](#security-iam-awsmanpol-EC2FastLaunchServiceRolePolicy "#security-iam-awsmanpol-EC2FastLaunchServiceRolePolicy") – Updated policy                                    | Amazon EC2 updated this policy to add Amazon EventBridge access to create and manage event rules for EC2 Fast Launch. Additionally, EC2 Fast Launch can now describe AWS CloudFormation stacks, launch an instance from an AMI that's associated with AWS License Manager, get a list of AWS KMS grants it created that can be retired, and delete launch templates that it created. | May 14, 2025      |
| [AWSEC2CapacityReservationFleetRolePolicy](#security-iam-awsmanpol-AWSEC2CapacityReservationFleetRolePolicy "#security-iam-awsmanpol-AWSEC2CapacityReservationFleetRolePolicy") – Updated permissions | Amazon EC2 updated the `AWSEC2CapacityReservationFleetRolePolicy` managed policy to use the `ArnLike` condition operator instead of the `StringLike` condition operator.                                                                                                                                                                                                             | March 03, 2025    |
| [AmazonEC2ReadOnlyAccess](#security-iam-awsmanpol-AmazonEC2ReadOnlyAccess "#security-iam-awsmanpol-AmazonEC2ReadOnlyAccess") – Added permissions                                                      | Amazon EC2 added a permission that allows you to retrieve security groups using the `GetSecurityGroupsForVpc` operation.                                                                                                                                                                                                                                                             | December 27, 2024 |
| [EC2FastLaunchFullAccess](#security-iam-awsmanpol-EC2FastLaunchFullAccess "#security-iam-awsmanpol-EC2FastLaunchFullAccess") – New policy                                                             | Amazon EC2 added this policy to perform API actions related to the EC2 Fast Launch feature from an instance. The policy can be attached to the instance profile for an instance that's launched from a EC2 Fast Launch enabled AMI.                                                                                                                                                  | May 14, 2024      |
| [AWSEC2VssSnapshotPolicy](#security-iam-awsmanpol-AWSEC2VssSnapshotPolicy "#security-iam-awsmanpol-AWSEC2VssSnapshotPolicy") – New policy                                                             | Amazon EC2 added the `AWSEC2VssSnapshotPolicy` policy that contains permissions to create and add tags to Amazon Machine Images (AMIs) and EBS snapshots.                                                                                                                                                                                                                            | March 28, 2024    |
| [Ec2InstanceConnectEndpoint](#Ec2InstanceConnectEndpoint "#Ec2InstanceConnectEndpoint") – New policy                                                                                                  | Amazon EC2 added the `Ec2InstanceConnectEndpoint` policy. This policy is attached to the **AWSServiceRoleForEC2InstanceConnect** service-linked role, to allow Amazon EC2 to perform actions on your behalf when you create an EC2 Instance Connect Endpoint.                                                                                                                        | January 24, 2023  |
| [EC2FastLaunchServiceRolePolicy](#security-iam-awsmanpol-EC2FastLaunchServiceRolePolicy "#security-iam-awsmanpol-EC2FastLaunchServiceRolePolicy") – New policy                                        | Amazon EC2 added the EC2 Fast Launch feature to enable Windows AMIs to launch instances faster by creating a set of pre-provisioned snapshots.                                                                                                                                                                                                                                       | November 26, 2021 |
| Amazon EC2 started tracking changes                                                                                                                                                                   | Amazon EC2 started tracking changes to its AWS managed policies                                                                                                                                                                                                                                                                                                                      | March 1, 2021     |
