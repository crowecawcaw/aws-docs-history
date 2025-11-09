# Access WorkSpaces Applications API Operations and CLI Commands Through an Interface VPC Endpoint

If you use Amazon Virtual Private Cloud to host your AWS resources, you can connect directly to WorkSpaces Applications API operations or command line interface (CLI) commands through an [interface VPC
endpoint](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") (interface endpoint) in your virtual private cloud (VPC) instead of connecting over the internet. Interface endpoints are powered by AWS PrivateLink, a technology that lets you keep streaming traffic within a VPC that you
specify by using private IP addresses. When you use an interface endpoint, communication between your VPC and WorkSpaces Applications is conducted entirely and securely within the AWS network.

###### Note

This topic describes how to access the WorkSpaces Applications API operations and CLI commands through an interface endpoint. For information about how to create and stream from WorkSpaces Applications interface endpoints, see [Tutorial: Creating and Streaming from Interface VPC Endpoints](creating-streaming-from-interface-vpc-endpoints.md "creating-streaming-from-interface-vpc-endpoints.md").

**Prerequisites**

To use interface endpoints, you must meet the following prerequisites:

- The security groups that are associated with the interface endpoint must allow inbound access to port 443 (TCP) from the IP address range from which your users connect.
- The network access control list for the subnets must allow outbound traffic from ephemeral network ports 1024-65535 (TCP) to the IP address range from which your users connect.

###### Topics

- [Create an Interface Endpoint to Access WorkSpaces Applications API Operations and CLI Commands](access-api-cli-through-interface-vpc-endpoint-create-interface-endpoint.md "access-api-cli-through-interface-vpc-endpoint-create-interface-endpoint.md")
- [Use an Interface Endpoint to Access WorkSpaces Applications API Operations and CLI Commands](how-to-access-api-cli-through-interface-vpc-endpoint.md "how-to-access-api-cli-through-interface-vpc-endpoint.md")
