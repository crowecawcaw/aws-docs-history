# AWS Direct Connect in AWS GovCloud (US)

AWS Direct Connect links your internal network to an AWS Direct Connect location over a standard 1 gigabit, 10 gigabit, 100 gigabit, or 400 gigabit Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an AWS Direct Connect router. With this connection in place, you can create virtual interfaces directly to the AWS cloud and Amazon Virtual Private Cloud, bypassing Internet service providers in your network path.

## How AWS Direct Connect differs for AWS GovCloud (US)

- Using the AWS Direct Connect Gateway connectivity from any AWS Direct Connect location can be established into either or both AWS GovCloud (US) locations. For more information, see [https://aws.amazon.com/blogs/publicsector/aws-hybrid-connectivity-sharing-aws-direct-connect-aws-govcloud-us-commercial-regions/](https://aws.amazon.com/blogs/publicsector/aws-hybrid-connectivity-sharing-aws-direct-connect-aws-govcloud-us-commercial-regions/ "https://aws.amazon.com/blogs/publicsector/aws-hybrid-connectivity-sharing-aws-direct-connect-aws-govcloud-us-commercial-regions/")
- AWS Direct Connect Gateway is supported between an AWS GovCloud (US) account and a linked standard/commercial AWS account. From your AWS GovCloud (US) account, you can associate a virtual private gateway with an AWS Direct Connect gateway that exists in the linked commercial/standard AWS account.
- AWS Direct Connect Partners do not support Hosted connections to AWS GovCloud (US) Account IDs. When
  ordering connections through an AWS Direct Connect Partner for a hosted connection, use the
  commercial account ID.
- To set up an AWS Direct Connect connection to AWS GovCloud (US) Regions, you must use the [AWS GovCloud (US) console](https://console.amazonaws-us-gov.com/directconnect/ "https://console.amazonaws-us-gov.com/directconnect/") and
  the AWS GovCloud (US) credentials associated with your AWS GovCloud (US) account. For instructions about how to provision and configure AWS Direct Connect, see the [AWS Direct Connect User Guide](../../../directconnect/latest/UserGuide.md "../../../directconnect/latest/UserGuide.md").
- Alternatively, you can set up an AWS Direct Connect connection, in a different Region and connect to AWS GovCloud (US) Regions using a public virtual interface and a VPN connection. For more
  information, see [Setting up AWS Direct Connect with a VPN Connection](#setup_direct_connect "#setup_direct_connect").
- When you create a public virtual interface on your AWS Direct Connect connection [associated with any standard Region or
  AWS GovCloud (US) Region](https://aws.amazon.com/directconnect/locations/ "https://aws.amazon.com/directconnect/locations/"), a data path to AWS GovCloud (US) is made available. Public
  virtual interface on an AWS Direct Connect connections associated with an AWS China Region do not
  have a data path to AWS GovCloud (US).
- To access your VPC without using an Amazon VPC VPN (for non-export uses), create an AWS Direct Connect private
  virtual interface in AWS GovCloud (US) Regions (us-gov-west-1) only, or create an AWS Direct Connect
  gateway and use any AWS Direct Connect connection from any AWS Direct Connect location.
- An AWS Direct Connect gateway is supported between an AWS GovCloud (US) account and a linked public AWS
  account. From your AWS GovCloud (US) account, you can associate a virtual private gateway with
  an AWS Direct Connect gateway that's in the linked account.
- Use the Amazon VPC section of the AWS GovCloud (US) console to set up hardware VPN access to AWS GovCloud (US) Regions over a public virtual interface.
- If you are processing export-controlled workloads, you must configure your AWS Direct Connect connection with a VPN to encrypt data in transit. For detailed instructions about how to
  create your VPC and VPN, see [Adding a Hardware Virtual Private Gateway to Your VPC](../../../vpc/latest/userguide/VPC_VPN.md "../../../vpc/latest/userguide/VPC_VPN.md") in the Amazon VPC User Guide. For instructions
  about how to configure your on-premises VPN hardware, see the [AWS Site-to-Site VPN Network Administrator Guide](../../../vpn/latest/s2svpn/your-cgw.md "../../../vpn/latest/s2svpn/your-cgw.md").

## Documentation for AWS Direct Connect

[AWS Direct Connect documentation](../../../directconnect/index.md "../../../directconnect/index.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- AWS Direct Connect metadata is not permitted to contain export-controlled data. This
  metadata includes all of the configuration data that you enter when creating and
  maintaining AWS Direct Connect, such as connection names.
- Do not enter export-controlled data in the following console fields:
  - Connection Name
  - VIF Name

## Setting up AWS Direct Connect with a VPN Connection

You can create an AWS Direct Connect connection in a different Region and use a VPN on top of the
connection to encrypt all data in transit from your AWS GovCloud (US-West) virtual private cloud (VPC)
to your own network.

### Step 1: Create a AWS Direct Connect Connection and Virtual Interface

To provision a connection and public virtual interface, follow the steps in the [Getting Started with AWS Direct Connect](../../../directconnect/latest/UserGuide/getting_started.md "../../../directconnect/latest/UserGuide/getting_started.md") with AWS Direct Connect section of the AWS Direct Connect user guide and ensure that you do the
following:

- Submit a connection request at a location in any other supported Region.
- Create a public virtual interface (not a private virtual interface).

### Step 2: Verify Your Virtual Public Interface

After you have established virtual public interfaces to the AWS GovCloud (US-West) Region, verify
your virtual public interface connection to the AWS GovCloud (US-West) Region by running a traceroute
from your on-premises router and verifying that the AWS Direct Connect identifier is in the network
trace.

### Step 3: Set Up Your VPN Over Your Public Virtual Interface

Create your AWS GovCloud (US-West) VPC and VPN. For detailed instructions on how to create
your VPC and VPN, see [Adding a Hardware Virtual Private Gateway to Your VPC](../../../vpc/latest/userguide/VPC_VPN.md "../../../vpc/latest/userguide/VPC_VPN.md") in the Amazon
Virtual Private Cloud User Guide. For instructions on how to configure your on-premises VPN
hardware, see [Amazon Virtual Private Cloud Network Administrator Guide.](../../../vpc/latest/adminguide/Welcome.md "../../../vpc/latest/adminguide/Welcome.md")
