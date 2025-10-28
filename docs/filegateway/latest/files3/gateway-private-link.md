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

To activate your gateway in a VPC, use the Amazon VPC Console to [create a VPC
endpoint for Storage Gateway](create-vpc-endpoint.md "create-vpc-endpoint.md") and get the VPC endpoint ID, then specify this VPC endpoint ID when
you create and activate the gateway. For more information, see [Connect your Amazon S3 File Gateway to AWS](create-gateway-file.md#connect-to-amazon-s3-file "create-gateway-file.md#connect-to-amazon-s3-file").

To configure your S3 File Gateway to transfer data through the VPC, you must
create a separate VPC endpoint for Amazon S3, then specify this VPC endpoint when you create file
shares for the gateway.

###### Note

You must activate your gateway in the same region where you create
the VPC endpoint for Storage Gateway, and the Amazon S3 storage that you configure for the file share
must be in the same region where you create the VPC endpoint for Amazon S3.
