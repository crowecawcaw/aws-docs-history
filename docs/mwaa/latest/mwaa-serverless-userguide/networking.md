# Networking

###### Note

Creating a VPC network is **optional** with Amazon MWAA Serverless.

An Amazon VPC is a virtual network that is linked to your AWS account. It gives you cloud security and the ability to scale dynamically by providing fine-grained control over your virtual infrastructure and network traffic segmentation. This page describes the Amazon VPC infrastructure with _public routing_ (Amazon VPC network has access to the internet) or _private routing_ (Amazon VPC network doees not have access to the internet).

To learn more about VPCs in AWS, refer to [AWS PrivateLink concepts](../../../vpc/latest/privatelink/concepts.md "../../../vpc/latest/privatelink/concepts.md").

## VPC support

The following table describes the types of Amazon VPCs Amazon MWAA Serverless supports.

| Amazon VPC types                                                               | Supported |
| ------------------------------------------------------------------------------ | --------- |
| An Amazon VPC owned by the customer that is attempting to create the workflow. | Yes       |
| A shared Amazon VPC owned by service to host customer tasks.                   | Yes       |

## VPC infrastructure overview

VPC endpoints appear as Elastic Network Interfaces (ENIs) with private IPs in your Amazon VPC. After these endpoints are created, any traffic destined to these IPs is privately or publicly routed to the corresponding AWS services that are used by your workflow.

The following section describes the Amazon VPC infrastructure required to route traffic publicly _over the internet_, or privately _within your Amazon VPC_.

### Public routing over the internet

This section describes the Amazon VPC infrastructure of a workflow with public routing. You'll need the following VPC infrastructure:

- **One VPC security group**. A VPC security group acts as a virtual firewall to control ingress (inbound) and egress (outbound) network traffic on an instance.
  - Up to 5 security groups can be specified.
  - The security groups **must** be part of the same VPC.
  - The security group **must** specify a self-referencing inbound rule to itself.
  - The security group **must** specify an outbound rule for all traffic (`0.0.0.0/0`; for IPv6, use `::/0`).
  - The security group **must** allow all traffic in the self-referencing rule. For example, [(Recommended) Example all access self-referencing security group](networking-security.md#networking-security-sg-example "networking-security.md#networking-security-sg-example") .

- **Two private subnets**. A private subnet is a subnet that's **not** associated with a route table that has a route to an internet gateway.
  - **Minimum 2** and **Minimum 16** subnets are supported in Amazon MWAA Serverless.
  - These subnets **must** be private.
  - At least two subnets **must** be in different Availability Zones. For example, `us-east-1a`, `us-east-1b`.
    This allows Amazon MWAA Serverless to run your workflow tasks in your other availability zone, if one container fails.
  - The subnets **must** have a route table to a NAT device (gateway or instance).
  - The subnets **must not** route to an internet gateway.
  - Set `assignIpV6AddressOnCreation` to `true` for IPv6 subnets.
  - For IPv6 private subnets, you **must** have a connection to an egress-only internet gateway (EIGW).

- **A network access control list (ACL)**. An NACL manages (by allow or deny rules) inbound and outbound traffic at the subnet level.
  - The NACL **must** have an inbound rule that allows all traffic (`0.0.0.0/0`; for IPv6, use `::/0`).
  - The NACL **must** have an outbound rule that allows all traffic (`0.0.0.0/0`; for IPv6, use `::/0`).

- **Two NAT gateways (or NAT instances)**. A NAT device forwards traffic from the instances in the private subnet to the internet or other AWS services, and then routes the response back to the instances.
  - The NAT device **must** be attached to a public subnet. (One NAT device per public subnet.)
  - The NAT device **must** have an Elastic IPv4 Address (EIP) attached to each public subnet.

- **An internet gateway**. An internet gateway connects an Amazon VPC to the internet and other AWS services.
  - An internet gateway **must** be attached to the Amazon VPC.

### Private routing without internet access

This section describes the Amazon VPC infrastructure of a workflow with _private routing_. You'll need the following VPC infrastructure:

- **One VPC security group**. A VPC security group acts as a virtual firewall to control ingress (inbound) and egress (outbound) network traffic on an instance.
  - Up to 5 security groups can be specified.
  - The security groups **must** be part of the same VPC.
  - The security group must specify a self-referencing inbound rule to itself.
  - The security group must specify an outbound rule for all traffic (`0.0.0.0/0`; for IPv6, use `::/0`).

- **Two private subnets**. A private subnet is a subnet that's **not** associated with a route table that has a route to an internet gateway.
  - **Minimum 2** and **Minimum 16** subnets are supported in Amazon MWAA Serverless.
  - These subnets **must** be private.
  - At least two subnets **must** be in different Availability Zones. For example, `us-east-1a`, `us-east-1b`.
    This allows Amazon MWAA Serverless to run your workflow tasks in your other availability zone, if one container fails.
  - The subnets **must** have a route table to your VPC endpoints.
  - The subnets **must** have a route table to an EIGW in order to download from the internet as part of a DAG.
  - The subnets **must not** have a route table to a NAT device (gateway or instance), **nor** an internet gateway.

- **A network access control list (ACL)**. An NACL manages (by allow or deny rules) inbound and outbound traffic at the subnet level.
  - The NACL **must** have an inbound rule that allows all traffic (`0.0.0.0/0`; for IPv6, use `::/0`).
  - The NACL **must** have an outbound rule that denies all traffic (`0.0.0.0/0`; for IPv6, use `::/0`).
  - For example, [(Recommended) Example ACLs](networking-security.md#networking-security-acl-example "networking-security.md#networking-security-acl-example").

- **A local route table**. A local route table is a default route for communication within the VPC.
  - The local route table **must** be associated to your private subnets.
  - The local route table **must** enable instances in your VPC to communicate with your own network. For example, if you're using an AWS Client VPN to access the VPC interface endpoint for your Apache Airflow _Web server_, the route table must route to the VPC endpoint.

- **VPC endpoints** for each AWS service that your workflow uses, and Apache Airflow VPC endpoints in the same AWS Region and Amazon VPC as your Amazon MWAA Serverless workflow.
  - A VPC endpoint for each AWS service that your workflow uses and VPC endpoints for Apache Airflow.
  - The VPC endpoints **must** have private DNS enabled.
  - The VPC endpoints **must** be associated to your workflow's two private subnets.
  - The VPC endpoints **must** be associated to your workflow's security group.
  - The VPC endpoint policy for each endpoint should be configured to allow access to AWS services used by the workflow. For example, [(Recommended) Example VPC endpoint policy to allow all access](networking-security.md#networking-security-policies-all "networking-security.md#networking-security-policies-all").
  - A VPC endpoint policy for Amazon S3 should be configured to allow bucket access. For example, [(Recommended) Example Amazon S3 gateway endpoint policy to allow bucket access](networking-security.md#networking-security-external-policies-s3 "networking-security.md#networking-security-external-policies-s3").
