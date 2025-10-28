# Adding a VPC interface to a MediaConnect flow

To avoid streaming your content over the public internet, you can add a VPC interface
to your AWS Elemental MediaConnect flow. You can add up to two VPC interfaces to each flow.

###### Important

When you add a VPC interface, MediaConnect creates a service-managed Elastic
Network Interface (ENI) in your AWS account. To ensure proper service operation,
be sure not to modify this resource in any manner.

## Prerequisites

Before you begin this procedure, make sure that you have completed the following
steps:

- In Amazon VPC, set up your VPC and associated security groups. For more
  information about VPCs, see the _[Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md")_. For information about
  configuring security groups to work with your VPC interface, see [Security group
  considerations](vpc-interface-security-groups.md "vpc-interface-security-groups.md").
- In IAM, [set up MediaConnect
  as a trusted service](security-iam-trusted-entity.md "security-iam-trusted-entity.md").

## Procedure

###### To add a VPC interface to a flow (console)

1. On the **Flows** page, choose the name of the flow that you
   want to update.
2. Choose the **VPC interfaces** tab.
3. Choose **Add VPC interface**.
4. For **Name**, specify a name for your VPC interface. The name
   of the VPC interface must be unique within the flow.
5. For **Network interface type**, specify the type of network
   adapter that you want MediaConnect to use on this interface. If you don't set
   this value, it defaults to **ENA**.

###### Note

    * You can add one EFA VPC interface per flow.
    * You can add up to two ENA VPC interfaces per flow.
    * You can only use an EFA VPC interface for sources that use the CDI
     protocol or the ST 2110 with JPEG XS protocol.

6. For **Role ARN**, specify the Amazon Resource Name (ARN) of
   the role that you created when you set up MediaConnect as a trusted
   service.
7. For **VPC**, choose the ID of the VPC that you want to
   use.
8. For **Subnet**, choose the VPC subnet that you want
   MediaConnect to use to set up your VPC configuration. The subnet must reside in
   the same Availability Zone as the flow.
9. For **Security groups**, specify the VPC security groups that
   you want MediaConnect to use to set up your VPC configuration. You must choose
   at least one security group.

## Additional resources

VPC Flow Logs can be used to capture information about the IP traffic going to and
from network interfaces in your VPC. Flow log data can be published to CloudWatch Logs,
Amazon S3, or Data Firehose. For more information about VPC Flow Logs, see [Logging IP
traffic using VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") in the
_Amazon VPC User Guide_.
