

# Registering an endpoint in MediaConnect
<a name="registering-endpoint"></a>

You can register endpoints to represent the senders and receivers in your media workflows.

## Prerequisites
<a name="registering-endpoint-prerequisites"></a>
+ You have an AWS account.
+ You know the AWS Region where you want to register the endpoint.
+ For a standard endpoint:
  + You have the connection details of the sender or receiver that the endpoint represents, such as its protocol, address, and port.
  + To encrypt content, you have a secret in AWS Secrets Manager.
+ For a router endpoint:
  + You have a router output (for a source endpoint) or a router input (for a destination endpoint) that uses **MediaConnect endpoints** connection management. For more information about creating router I/Os, see [Creating a router I/O in MediaConnect](creating-router-io.md).

## Procedure
<a name="registering-endpoint-procedure"></a>

### To register a source endpoint
<a name="register-source-endpoint-section"></a><a name="register-source-endpoint-procedure"></a>

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, under **Endpoints**, choose **Source endpoints**.

1. Choose **Register source endpoint**.

1. Under **Source endpoint details**, provide the following information:

   1. **Description** - (Optional) Enter a description for the source endpoint.

   1. **AWS Region** - Choose the AWS Region where you want to register the source endpoint.

   1. **Configuration type** - Choose **Standard** or **Router output**.

1. Complete the configuration for the configuration type that you chose:

   1. **Standard** - To represent a sender outside MediaConnect, follow these steps:

      1. Under **Source endpoint details**, for **Name**, enter a descriptive name to help you identify the source endpoint.

      1. Under **Protocol configuration**, choose a **Protocol** (**SRT Caller**, **SRT Listener**, **RTP**, or **RIST**), and then complete the protocol settings.

      1. (Optional) To encrypt content, complete the encryption configuration and provide a secret. For more information about encrypting endpoints, see [Encrypting endpoints in MediaConnect](encrypting-endpoints.md).

      1. Under **Source network configuration**, choose a **Network type**:

         1. For the **Public** network type, specify the allowed Classless Inter-Domain Routing (CIDR) ranges.

         1. For **VPC**, choose a **Subnet ID** and up to five entries for **Security group IDs**.

   1. **Router output** - To represent a router output, under **Router output configuration**, choose the **Router output ARN**. You can choose only router outputs that use **MediaConnect endpoints** connection management.

1. (Optional) Under **Tags**, add tags to help you identify and organize the source endpoint.

1. Choose **Register**.

### To register a destination endpoint
<a name="register-destination-endpoint-section"></a><a name="register-destination-endpoint-procedure"></a>

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, under **Endpoints**, choose **Destination endpoints**.

1. Choose **Register destination endpoint**.

1. Under **Destination endpoint details**, provide the following information:

   1. **Description** - (Optional) Enter a description for the destination endpoint.

   1. **AWS Region** - Choose the AWS Region where you want to register the destination endpoint.

   1. **Configuration type** - Choose **Standard** or **Router input**.

1. Complete the configuration for the configuration type that you chose:

   1. **Standard** - To represent a receiver outside MediaConnect, follow these steps:

      1. Under **Destination endpoint details**, for **Name**, enter a descriptive name to help you identify the destination endpoint.

      1. Under **Protocol configuration**, choose a **Protocol** (**SRT Caller**, **SRT Listener**, **RTP**, or **RIST**), and then complete the protocol settings.

      1. (Optional) To decrypt content, complete the decryption configuration and provide a secret. For more information about encrypting endpoints, see [Encrypting endpoints in MediaConnect](encrypting-endpoints.md).

      1. Under **Destination network configuration**, choose a **Network type**:

         1. For the **Public** network type, specify the allowed CIDR ranges.

         1. For **VPC**, choose a **Subnet ID** and up to five entries for **Security group IDs**.

   1. **Router input** - To represent a router input, under **Router input configuration**, choose the **Router input ARN**. You can choose only router inputs that use **MediaConnect endpoints** connection management.

1. (Optional) Under **Tags**, add tags to help you identify and organize the destination endpoint.

1. Choose **Register**.

## Next steps
<a name="registering-endpoint-next-steps"></a>

After you register an endpoint, you can perform the following action:
+ [Connecting and disconnecting endpoints in MediaConnect](connecting-endpoints.md)

## Additional resources
<a name="registering-endpoint-additional-resources"></a>

For more information about encrypting endpoints, see [Encrypting endpoints in MediaConnect](encrypting-endpoints.md).

For more information about registering endpoints programmatically, see the following pages in the *MediaConnect API Reference*:
+ [RegisterSourceEndpoint](https://docs.aws.amazon.com/mediaconnect/latest/api/API_RegisterSourceEndpoint.html)
+ [RegisterDestinationEndpoint](https://docs.aws.amazon.com/mediaconnect/latest/api/API_RegisterDestinationEndpoint.html)