

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# AWS PrivateLink for AWS Wickr
<a name="privatelink-overview"></a>

With AWS PrivateLink for AWS Wickr, you can establish a private connection between your Virtual Private Cloud (VPC) and a subset of endpoints in AWS Wickr by using interface VPC endpoints. Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that you can use to access services running on AWS by using private IP addresses.

For mobile clients or other on-prem devices, use a VPN to connect your device to the VPC for end to end private connectivity. For more information, see [AWS Virtual Private Network Documentation](https://docs.aws.amazon.com/vpn/).

For more information about AWS PrivateLink and AWS VPC, see [What is AWS PrivateLink?](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) in the *AWS PrivateLink Guide* and [What is AWS VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) in the *Amazon Virtual Private Cloud User Guide.* 

**Supported AWS Wickr Services**

The following AWS Wickr services support AWS PrivateLink:


| Service | Endpoint Format | 
| --- | --- | 
| AWS Wickr Admin | `com.amazonaws.{{your-region}}.wickr-admin`  | 
| AWS Wickr Messaging | `com.amazonaws.{{your-region}}.wickr-messaging`  | 
| AWS Wickr Calling | `com.amazonaws.{{your-region}}.wickr-calling`  | 

All Wickr VPC endpoints currently require Private DNS Names to be enabled. For more information, see [Enable private DNS names](https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html#enable-private-dns-names).

Wickr VPC Endpoints supports FIPS in regions where the public Wickr endpoints support FIPS. For more information, see [Federal Information Processing Standard ](https://aws.amazon.com/compliance/fips/).

**Not Currently Supported**
+ VPC endpoint policies for Messaging and Calling endpoints
+ Messaging and Calling endpoints are not available in `us-east-1`.

**Topics**
+ [Prerequisites](#privatelink-prerequisites)
+ [Create VPC endpoints](vpc-endpoints.md)
+ [Limitations](privatelink-limitations.md)

## Prerequisites
<a name="privatelink-prerequisites"></a>

Before creating VPC endpoints, be sure you have the following prerequisites:

1. **VPC Configuration**: A properly configured VPC with subnets in multiple Availability Zones

1. **Security Groups**: Appropriate security groups allowing HTTPS traffic (port 443)

1. **DNS Resolution**: DNS hostnames and DNS resolutions enabled in the VPC 

1. **IAM Permissions**: Necessary permissions to create and manage VPC endpoints