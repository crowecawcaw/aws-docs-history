

# Infrastructure security for Amazon EVS

As a managed service, Amazon Elastic VMware Service (Amazon EVS) is protected by the AWS global network security procedures. These procedures are described in the [Amazon Web Services: Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf) whitepaper.

## Access to the Amazon EVS API
<a name="infrastructure-security-api-access"></a>

You use AWS published API calls to access Amazon EVS through the network. Clients must support Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3. Clients must also support cipher suites with perfect forward secrecy (PFS), such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems such as Java 7 and later support these modes.

Requests must be signed by using an access key ID and a secret access key that is associated with an IAM principal. You can also use the [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) (AWS STS) to generate temporary security credentials to sign requests. To control who can call Amazon EVS API operations, see [Identity and access management for Amazon Elastic VMware Service](security-iam.md).

## How Amazon EVS reaches your environment
<a name="infrastructure-security-service-access"></a>

Amazon EVS reaches the VMware Cloud Foundation (VCF) deployment in your account through the service access subnet. The service access subnet is a standard VPC subnet that you choose when you create the environment. Amazon EVS provisions elastic network interfaces into this subnet to provide management connectivity to VCF appliances and ESX hosts. Amazon EVS needs this connectivity to deploy, manage, and monitor the VCF deployment. For more information, see [Service access subnet](concepts.md#concepts-service-access-subnet).

The service-linked role `AWSServiceRoleForAmazonEVS` grants Amazon EVS the permissions to create and manage these network interfaces. For the actions that the role allows, see [AWS managed policies for Amazon EVS](security-iam-awsmanpol.md) and [Using service-linked roles for Amazon EVS](using-service-linked-roles.md).

## Network isolation in your VPC
<a name="infrastructure-security-network-isolation"></a>

Your Amazon EVS environment runs in an Amazon VPC that you own. The VPC creates boundaries between the resources in the environment and controls traffic between them, your on-premises network and the internet.

By default, Amazon EVS creates private VLAN subnets during environment creation that deny direct internet access. To add another layer of security, you can create a custom network access control list (network ACL) with rules that further restrict internet connectivity.

**Important**  
 Amazon EC2 security group rules are not enforced on Amazon EVS elastic network interfaces that are attached to VLAN subnets. To control traffic to and from VLAN subnets, you must use a network ACL. For the steps, see [Create a network ACL for VLAN subnet traffic](evs-env-nacl-cong.md).

Inside the VCF environment, you can segment and filter VM traffic with NSX features such as the VMware vDefend Gateway Firewall and Distributed Firewall. For details and links, see [Internetwork traffic privacy](data-protection.md#internetwork-traffic-privacy). For the network connections that Amazon EVS supports, see [Supported network configurations](plan-network-supported.md).