# AWS Lambda VPC configuration in AWS ParallelCluster

AWS ParallelCluster uses AWS Lambda to perform operations during the lifecycle of the cluster.
An [AWS Lambda function always runs in a VPC](../../../lambda/latest/dg/foundation-networking.md "../../../lambda/latest/dg/foundation-networking.md") owned by the Lambda service.
This Lambda function can also be connected to private subnets in a virtual private cloud (VPC) to access private resources.

###### Note

Lambda functions can't connect directly to a VPC with dedicated instance tenancy. To connect to resources in a dedicated VPC, peer the dedicated VPC to a second VPC with a default tenancy that can
connect to a dedicated VPC.

For more information, see [Dedicated Instances](../../../AWSEC2/latest/UserGuide/dedicated-instance.md "../../../AWSEC2/latest/UserGuide/dedicated-instance.md") in the _Amazon EC2 User Guide for Linux Instances_ and [How do I connect a Lambda function to a dedicated VPC?](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-dedicated-vpc/ "https://aws.amazon.com/premiumsupport/knowledge-center/lambda-dedicated-vpc/")
from the _AWS Knowledge Center_.

Lambda functions that are created by AWS ParallelCluster can be connected to a private VPC. These Lambda functions need to access AWS services.
You can provide access through the internet or VPC endpoints by using the following methods.

- **Internet access**

To access the internet and AWS services, a Lambda function requires network address translation (NAT). Route outbound traffic from your
private subnet to a [NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in a public subnet.

- **VPC endpoints**

Several AWS services offer [VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md"). You can use VPC
endpoints to connect to AWS services from a VPC that doesn't have internet access. To view the list of AWS ParallelCluster VPC endpoints, see
[Networking](aws-parallelcluster-in-a-single-public-subnet-no-internet-v3.md "aws-parallelcluster-in-a-single-public-subnet-no-internet-v3.md").

###### Note

Every combination of subnets and security groups must provide access to AWS services using one these methods.
Subnets and security groups must be in the same VPC.

For more information, see [VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the _Amazon Virtual Private Cloud User Guide_ and [Internet and service access for VPC-connected functions](../../../lambda/latest/dg/configuration-vpc.md#vpc-internet "../../../lambda/latest/dg/configuration-vpc.md#vpc-internet") in
the _AWS Lambda Developer Guide_.

To configure the use of Lambda functions and VPCs, see [DeploymentSettings](DeploymentSettings-cluster-v3.md "DeploymentSettings-cluster-v3.md") /
[LambdaFunctionsVpcConfig](DeploymentSettings-cluster-v3.md#DeploymentSettings-cluster-v3-LambdaFunctionsVpcConfig "DeploymentSettings-cluster-v3.md#DeploymentSettings-cluster-v3-LambdaFunctionsVpcConfig") for clusters or
[DeploymentSettings](DeploymentSettings-build-image-v3.md "DeploymentSettings-build-image-v3.md") /
[LambdaFunctionsVpcConfig](DeploymentSettings-build-image-v3.md#DeploymentSettings-build-image-v3-LambdaFunctionsVpcConfig "DeploymentSettings-build-image-v3.md#DeploymentSettings-build-image-v3-LambdaFunctionsVpcConfig") for images.
