# Enable cross-network access for Amazon SageMaker Unified Studio using VPC peering connections

###### Note

If your Amazon SageMaker Unified Studio domain and your Amazon EKS cluster are configured with the same Amazon VPC,
you can skip the steps in this section.

Amazon SageMaker Unified Studio requires network connectivity between your Amazon SageMaker Unified Studio domain and your Amazon EKS cluster in order to maintain interactive sessions.
See [What is VPC peering?](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md")
and [Update your route tables for a VPC peering connection](../../../vpc/latest/peering/vpc-peering-routing.md "../../../vpc/latest/peering/vpc-peering-routing.md")
for more information regarding cross-network connectivity with Amazon VPC.
