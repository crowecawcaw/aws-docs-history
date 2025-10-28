# Prerequisites

The following list describes some requirements and suggestions to review when creating VPC-ENI
configurations:

- Private devices must be assigned to your AWS Account.
- You must have an AWS account user or role with permissions to create a Service-linked role. When
  using Amazon VPC endpoints with Device Farm mobile testing features, Device Farm creates an AWS Identity and Access Management (IAM)
  service-linked role.
- Device Farm can connect to VPCs only in the `us-west-2` Region. If you don't have a VPC in
  the `us-west-2` Region, you need to create one. Then, to access resources in a VPC in
  another Region, you must establish a peering connection between the VPC in the
  `us-west-2` Region and the VPC in the other Region. For information on peering VPCs,
  see the [Amazon VPC Peering
  Guide](../../../vpc/latest/peering.md "../../../vpc/latest/peering.md").

You should verify that you have access to your specified VPC when you configure the connection.
You must configure certain Amazon Elastic Compute Cloud (Amazon EC2) permissions for Device Farm.

- DNS resolution is required in the VPC that you use.
- Once your VPC has been created, you will need the following information about the VPC in the
  `us-west-2` Region:
  - VPC ID
  - Subnet IDs (private subnets only)
  - Security group IDs

- You must configure Amazon VPC connections on a per-project basis. At this time, you can configure only
  one VPC configuration per project. When you configure a VPC, Amazon VPC creates an interface within your
  VPC and assigns it to the specified subnets and security groups. All future sessions associated with
  the project will use the configured VPC connection.
- You cannot use VPC-ENI configurations along with the legacy VPCE feature.
- We strongly recommend **not updating an existing project** with a
  VPC-ENI configuration as existing projects may have VPCE settings that persist on the run level.
  Instead, if you already use the existing VPCE features, use VPC-ENI for all new projects.
