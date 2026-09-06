

# Enable cross-network access for Amazon SageMaker Unified Studio using VPC peering connections
<a name="enable-cross-network-access-using-vpc-peering"></a>

**Note**  
 If your Amazon SageMaker Unified Studio domain and your Amazon EKS cluster are configured with the same Amazon VPC, you can skip the steps in this section. 

 Amazon SageMaker Unified Studio requires network connectivity between your Amazon SageMaker Unified Studio domain and your Amazon EKS cluster in order to maintain interactive sessions. See [What is VPC peering?](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) and [Update your route tables for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html) for more information regarding cross-network connectivity with Amazon VPC. 