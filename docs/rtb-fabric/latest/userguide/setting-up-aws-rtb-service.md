# Setting up AWS RTB Fabric

Before you can use RTB Fabric, you must complete several setup tasks including account configuration, IAM permissions, and VPC networking. This chapter walks you through the prerequisites and configuration steps needed to get started with RTB Fabric.

## Prerequisites

Before you begin using RTB Fabric, ensure you have completed the following prerequisites:

- **AWS account** – You need an AWS account with appropriate permissions to create and manage RTB Fabric resources. If you don't have an AWS account, you can sign up at [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
- **IAM permissions** – You must configure appropriate AWS Identity and Access Management (IAM) permissions to create and manage RTB Fabric resources. RTB Fabric requires permissions for core operations such as creating gateways and links, as well as optional permissions for features like log delivery.

For details about required permissions and example policies, see [Identity and access management for AWS RTB Fabric](security-iam.md "security-iam.md"). RTB Fabric also uses service-linked roles that are automatically created when you first use the service.

## VPC requirements

RTB Fabric gateways connect to your existing virtual private clouds (VPCs). Most customers already have an existing VPC where their RTB application (SSP or DSP) is running. RTB Fabric gateways connect to this existing VPC to facilitate real-time bidding traffic. If you don't have an existing VPC, see [What is Amazon VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the _Amazon VPC User Guide_ to create one.

Your VPC must meet the following requirements for RTB Fabric:

- **IP address availability** – RTB Fabric supports IPv4 only. Ensure you have sufficient free IPv4 addresses in each VPC subnet where you plan to connect your gateway. The number of required addresses depends on your expected traffic scale.
- **Security group configuration** – Configure security groups with appropriate inbound rules based on your role:
  - **For requesters**: HTTPS (TCP port 443) inbound from your VPC Classless Inter-Domain Routing (CIDR) range or compute instance IP.
  - **For responders**: HTTPS (TCP port 443) inbound to your VPC CIDR range or fleet endpoint IP.

- **Network access controls** – Configure network ACLs, security groups, and routes to prevent unauthorized access within your AWS account.
- **DNS configuration** – For requesters, set your DNS TTL (time to live) value to 30 seconds for clients sending requests to the service.

When selecting or configuring your VPC for RTB Fabric, ensure you have the following information ready:

- **VPC ID** – The VPC where your RTB application runs.
- **Subnet IDs** – Subnets with sufficient IPv4 addresses for gateway connections.
- **Availability Zone configuration** – RTB Fabric supports single Availability Zone deployment by default. Multi-AZ deployment is optional and may require a service quota increase.
- **Security group ID** – Configured with the appropriate inbound rules for your role (requester or responder).

You will provide this VPC information when creating RTB Fabric gateways to connect your RTB applications.
