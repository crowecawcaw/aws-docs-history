# HA/DR deployment

## Installing SAP Oracle on Amazon EC2 instances and configuring HA/DR

Create an additional Amazon EC2 instance and perform the installation in a secondary Availability Zone. The steps for creating a HA or DR instance in a secondary Availability Zone are the same as described in Standalone deployment. You can simplify this step by using the following methods.

- If you have built any automation using AWS CloudFormation or other tools to create the primary Amazon EC2 instance and install database software, you can use the same automation to build the HA instance.
- You can create an [Amazon Machine Image](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md") of the primary Amazon EC2 instance and launch another instance in the secondary Availability Zone.
- For cross-regional deployments, configure [Amazon VPC peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") or [Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/") to enable SAP Oracle asynchronous replication between the two Regions.

## SAP documentation

For information about supported Oracle functions and Data Guard configuration options in the SAP environment, refer to the following SAP documentation.

- [SAP Note: 105047 - Support for Oracle functions in the SAP environment](https://me.sap.com/notes/105047 "https://me.sap.com/notes/105047")
- [SAP Note: 1552925 - Linux: High Availability Cluster Solutions](https://me.sap.com/notes/1552925 "https://me.sap.com/notes/1552925")

You must have SAP portal access for reading all SAP Notes.

To perform a manual failover or switchover, see [HA/DR operations](hadrops-orc-sap-nw-lx.md "hadrops-orc-sap-nw-lx.md").
