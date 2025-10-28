Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Activating a gateway in a virtual private

cloud

You can create a private connection between your on-premises gateway appliance and
cloud-based storage infrastructure. You can use this connection to activate your gateway and
configure it to transfer data to AWS storage services without communicating over the
public internet. Using the Amazon VPC service, you can launch AWS resources, including private
network interface endpoints, in a custom virtual private cloud (VPC). A VPC gives you
control over network settings such as IP address range, subnets, route tables, and network
gateways. For more information about VPCs, see [What is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the
_Amazon VPC User Guide_.

To activate your gateway in a VPC, use the Amazon VPC Console to [create a VPC endpoint for
Storage Gateway](create-vpc-endpoint.md "create-vpc-endpoint.md") and get the VPC endpoint ID, then specify this VPC endpoint ID when
you create and activate the gateway. For more information, see [Connect your Amazon FSx File Gateway to AWS](create-gateway-file.md#connect-to-amazon-fsx-file "create-gateway-file.md#connect-to-amazon-fsx-file").

To configure your FSx File Gateway to transfer data through the VPC, you
must establish a VPN or AWS DirectConnect link between the Amazon FSx for Windows File Server VPC and the
network where your gateway is deployed.

###### Note

You must activate your gateway in the same region where you
create the VPC endpoint for Storage Gateway.
