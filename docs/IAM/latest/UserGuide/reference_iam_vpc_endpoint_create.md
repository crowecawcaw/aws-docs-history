# Create a VPC endpoint for IAM

To start using IAM with your VPC, create an interface VPC endpoint for IAM. For more
information, see [Access an AWS service
using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _Amazon VPC User
Guide_.

Interface VPC endpoints for IAM can only be created in the Region where the [IAM control plane](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md") is located. In
commercial AWS Regions, the IAM control plane is located in the US East (N. Virginia) Region
(us-east-1). The AWS PrivateLink interface VPC endpoint service name for IAM
is `com.amazonaws.iam`. For a list of AWS Regions that support VPC endpoints
for IAM, see [VPC endpoint availability](reference_interface_vpc_endpoints.md#reference_vpc_endpoint_availability "reference_interface_vpc_endpoints.md#reference_vpc_endpoint_availability").

If your VPC is in a different Region from the IAM control plane Region, you must use
AWS Transit Gateway to allow access to the IAM interface VPC endpoint from another Region.

###### To access an IAM interface VPC endpoint from a VPC in a different Region using

AWS Transit Gateway

1. Create a transit gateway, or use an existing transit gateway to interconnect your
   virtual private clouds (VPCs). A transit gateway is required for each Region. For
   more information, see [Create a transit
   gateway](../../../vpc/latest/tgw/tgw-transit-gateways.md#create-tgw "../../../vpc/latest/tgw/tgw-transit-gateways.md#create-tgw") in the _AWS Transit Gateway Guide_.
2. Create transit gateway VPC attachments to connect each VPC to the transit gateway.
   For more information, see [Create a
   transit gateway attachment to a VPC](../../../vpc/latest/tgw/tgw-vpc-attachments.md#create-vpc-attachment "../../../vpc/latest/tgw/tgw-vpc-attachments.md#create-vpc-attachment") in the _AWS Transit Gateway
   Guide_.
3. Create a transit gateway VPC peering attachment to route traffic between peered
   VPCs. For more information, see [Create a peering
   attachment](../../../vpc/latest/tgw/tgw-peering.md#tgw-peering-create "../../../vpc/latest/tgw/tgw-peering.md#tgw-peering-create") in the _AWS Transit Gateway Guide_.

###### Note

VPC peering connections can also route traffic between peered VPCs, but this method
does not scale well with a large number of VPCs. Instead of VPC peering, we recommend
AWS Transit Gateway peering attachments which improve VPC and on-premises network management
through a scalable central hub. For more information about VPC peering connections, see
[Work with VPC peering connections](../../../vpc/latest/peering/working-with-vpc-peering.md "../../../vpc/latest/peering/working-with-vpc-peering.md") in the _Amazon VPC
Peering Guide_.
