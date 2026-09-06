

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Step 3: Configure VPC settings
<a name="create-cluster-step3"></a>

You connect to your cluster using q IPC through an AWS PrivateLink VPC endpoint. The endpoint resides in a subnet that you specify in the AWS account where you created your Managed kdb environment. Each cluster that you create has its own AWS PrivateLink endpoint, with an elastic network interface that resides in the subnet you specify. You can specify a security group to be applied to the VPC endpoint.

Connect a cluster to a VPC in your account. On the **Configure VPC settings** page, do the following: 

1. Choose the VPC that you want to access.

1. Choose the VPC subnets that the cluster will use to set up your VPC configuration.

1. Choose the security group.

1. Choose **Next**.