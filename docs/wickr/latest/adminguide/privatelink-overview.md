This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# AWS PrivateLink for AWS Wickr

With AWS PrivateLink for AWS Wickr, you can establish a private connection between your
Virtual Private Cloud (VPC) and a subset of endpoints in AWS Wickr by using interface VPC
endpoints. Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that
you can use to access services running on AWS by using private IP addresses.

For mobile clients or other on-prem devices, use a VPN to connect your device to the VPC
for end to end private connectivity. For more information, see [AWS Virtual Private Network Documentation](../../../vpn.md "../../../vpn.md").

For more information about AWS PrivateLink and AWS VPC, see [What is AWS PrivateLink?](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") in
the _AWS PrivateLink Guide_ and [What is AWS VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the
_Amazon Virtual Private Cloud User Guide._

**Supported AWS Wickr Services**

The following AWS Wickr services support AWS PrivateLink:

| Service             | Endpoint Format                               |
| ------------------- | --------------------------------------------- |
| AWS Wickr Admin     | `com.amazonaws.`your-region`.wickr-admin`     |
| AWS Wickr Messaging | `com.amazonaws.`your-region`.wickr-messaging` |
| AWS Wickr Calling   | `com.amazonaws.`your-region`.wickr-calling`   |

All Wickr VPC endpoints currently require Private DNS Names to be enabled. For more
information, see [Enable private DNS names](../../../vpc/latest/privatelink/interface-endpoints.md#enable-private-dns-names "../../../vpc/latest/privatelink/interface-endpoints.md#enable-private-dns-names").

Wickr VPC Endpoints supports FIPS in regions where the public Wickr endpoints support
FIPS. For more information, see [Federal
Information Processing Standard](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/") .

**Not Currently Supported**

- VPC endpoint policies for Messaging and Calling endpoints
- Messaging and Calling endpoints are not available in
  `us-east-1`.

###### Topics

- [Prerequisites](#privatelink-prerequisites "#privatelink-prerequisites")
- [Create VPC endpoints](vpc-endpoints.md "vpc-endpoints.md")
- [Limitations](privatelink-limitations.md "privatelink-limitations.md")

## Prerequisites

Before creating VPC endpoints, be sure you have the following prerequisites:

1. **VPC Configuration**: A properly configured VPC with subnets
   in multiple Availability Zones
2. **Security Groups**: Appropriate security groups allowing
   HTTPS traffic (port 443)
3. **DNS Resolution**: DNS hostnames and DNS resolutions enabled
   in the VPC
4. **IAM Permissions**: Necessary permissions to create and
   manage VPC endpoints
