# High availability disaster recovery deployment

Create an additional Amazon EC2 instance and perform the installation in a secondary Availability Zone. The steps for creating a high availability or disaster recovery instance in a secondary Availability Zone are the same as described in Standalone deployment. You can simplify this step by using the following methods.

- If you have built any automation using AWS CloudFormation or other tools to create the primary Amazon EC2 instance and install database software, you can use the same automation to build the HA instance.
- You can create an [Amazon Machine Image](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md") of the primary Amazon EC2 instance and launch another instance in the secondary Availability Zone.
  The configuration of high availability or disaster recovery depends on the tools you use. See the next sections for more details.

###### Note

You must configure cross-regional [Amazon VPC peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") or [Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/") to enable SAP ASE asynchronous replication between two Regions.
