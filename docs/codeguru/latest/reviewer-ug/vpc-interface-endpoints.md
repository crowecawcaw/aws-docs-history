As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# CodeGuru Reviewer and interface VPC endpoints

(AWS PrivateLink)

You can use VPC endpoints when you call Amazon CodeGuru Reviewer APIs. When you use VPC endpoints, your
API calls are more secure because they are contained within your VPC and don't access the
internet. For more information, see [Actions](../reviewer-api/API_Operations.md "../reviewer-api/API_Operations.md") in the
_Amazon CodeGuru Reviewer API Reference_.

You establish a private connection between your VPC and CodeGuru Reviewer by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md"), a technology that enables you to privately access CodeGuru Reviewer APIs without
an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances
in your VPC don't need public IP addresses to communicate with CodeGuru Reviewer APIs. Traffic between your
VPC and CodeGuru Reviewer does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic network interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Access an AWS service using an
interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _AWS PrivateLink Guide_.

###### Note

CodeGuru Reviewer does not support Amazon VPC endpoint policies.

## Considerations for CodeGuru Reviewer VPC endpoints

Before you set up an interface VPC endpoint for CodeGuru Reviewer, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") and [Prerequisites](../../../vpc/latest/privatelink/create-interface-endpoint.md#prerequisites-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#prerequisites-interface-endpoints") in the _AWS PrivateLink Guide_.

CodeGuru Reviewer supports making calls to all of its API actions from your VPC.

VPC endpoint policies are not supported for CodeGuru Reviewer. By default, full access to CodeGuru Reviewer is
allowed through the endpoint.

## Creating an interface VPC endpoint for CodeGuru Reviewer

You can create a VPC endpoint for the CodeGuru Reviewer service using either the Amazon VPC console or the
AWS Command Line Interface (AWS CLI).

Create a VPC endpoint for CodeGuru Reviewer using the following service name:

- com.amazonaws.`region`.codeguru-reviewer

If you enable private DNS for the endpoint, you can make API requests to CodeGuru Reviewer using its
default DNS name for the Region, for example,
`codeguru-reviewer.us-east-1.amazonaws.com`.

For more information, see [Access an AWS service
using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#access-service-though-endpoint "../../../vpc/latest/privatelink/create-interface-endpoint.md#access-service-though-endpoint") in the _AWS PrivateLink Guide_.
