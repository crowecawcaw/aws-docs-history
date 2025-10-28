# Connect to AWS KMS through a VPC endpoint

You can connect directly to AWS KMS through a private interface endpoint in your virtual
private cloud (VPC). When you use an interface VPC endpoint, communication between your VPC and
AWS KMS is conducted entirely within the AWS network.

AWS KMS supports Amazon Virtual Private Cloud (Amazon VPC) endpoints powered by [AWS PrivateLink](../../../vpc/latest/privatelink.md "../../../vpc/latest/privatelink.md"). Each VPC endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") (ENIs) with private IP
addresses in your VPC subnets.

The interface VPC endpoint connects your VPC directly to AWS KMS without an internet gateway,
NAT device, VPN connection, or AWS Direct Connect connection. The instances in your VPC do not need
public IP addresses to communicate with AWS KMS.

**Regions**

AWS KMS supports VPC endpoints and VPC endpoint policies in all AWS Regions in which
[AWS KMS](../../../general/latest/gr/kms.md "../../../general/latest/gr/kms.md") is supported.

**Considerations for AWS KMS VPC endpoints**

Before you set up an interface VPC endpoint for AWS KMS, review the [Interface endpoint
properties and limitations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") topic in the _AWS PrivateLink Guide_.

AWS KMS support for a VPC endpoint includes the following.

- You can use your VPC endpoint to call all [AWS KMS API operations](../APIReference/API_Operations.md "../APIReference/API_Operations.md") from your
  VPC.
- You can create an interface VPC endpoint that connects to an AWS KMS region endpoint or an [AWS KMS FIPS
  endpoint](../../../general/latest/gr/kms.md "../../../general/latest/gr/kms.md").
- You can use AWS CloudTrail logs to audit your use of KMS keys through the VPC endpoint.
  For details, see [Logging AWS KMS requests that use a VPC endpoint](vpce-logging.md "vpce-logging.md").

###### Topics

- [Create a VPC endpoint for AWS KMS](vpce-create-endpoint.md "vpce-create-endpoint.md")
- [Connect to an AWS KMS VPC endpoint](vpce-connect.md "vpce-connect.md")
- [Use VPC endpoints to control access to AWS KMS resources](vpce-policy-condition.md "vpce-policy-condition.md")
- [Logging AWS KMS requests that use a VPC endpoint](vpce-logging.md "vpce-logging.md")
