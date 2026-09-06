

# Internetwork privacy
<a name="internetwork-privacy"></a>

This topic describes how Amazon EFS secures connections from the service to other locations. 

## Traffic between service and on-premises clients and applications
<a name="on-prem-traffic-apps"></a>

You have two connectivity options between your private network and AWS:
+  An AWS Site-to-Site VPN connection. For more information, see [What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) 
+  An Direct Connect connection. For more information, see [What is Direct Connect?](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) 

 Access to Amazon EFS via the network is through AWS published APIs. Clients must support Transport Layer 1.2 or above. We recommend TLS 1.3 or above. Clients must also support cipher suites with Perfect Forward Secrecy (PFS), such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Diffie-Hellman Ephemeral (ECDHE). Most modern systems such as Java 7 and later support these modes. Additionally, you must sign requests using an access key ID and a secret access key that are associated with an IAM principal, or you can use the [AWS Security Token Service (AWS STS)](https://docs.aws.amazon.com/STS/latest/APIReference/) to generate temporary security credentials to sign requests. 

## Traffic between VPC and Amazon EFS API
<a name="vpc-endpoints"></a>

To establish a private connection between your virtual private cloud (VPC) and the Amazon EFS API, you can create an interface VPC endpoint. You can use this connection to call the Amazon EFS API from your VPC without sending traffic over the internet. The endpoint provides secure connectivity to the Amazon EFS API without requiring an internet gateway, NAT instance, or virtual private network (VPN) connection. For more information, see [Working with interface VPC endpoints in Amazon EFS](efs-vpc-endpoints.md).

## Traffic between AWS resources in the same Region
<a name="intra-aws-resource-traffic"></a>

 An Amazon Virtual Private Cloud (Amazon VPC) endpoint for Amazon EFS is a logical entity within a VPC that allows connectivity only to Amazon EFS. The Amazon VPC routes requests to Amazon EFS and routes responses back to the VPC. For more information, see [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html) in the *Amazon VPC User Guide*. 