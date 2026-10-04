

End of support notice: Amazon Managed Blockchain (AMB) will stop accepting new customers on October 29, 2026. Existing customers can continue using Amazon Managed Blockchain (AMB) until September 29, 2027. After September 29, 2027 you will no longer be able to access Amazon Managed Blockchain (AMB). For more information, see [Amazon Managed Blockchain (AMB) end of support](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-end-of-support.html).

# Step 2: Create and Configure the Interface VPC Endpoint
<a name="get-started-create-endpoint"></a>

Now that the network is up and running in your VPC, you set up an interface VPC endpoint (AWS PrivateLink) for your member. This allows the Amazon EC2 instance that you use as a Hyperledger Fabric client to interact with the Hyperledger Fabric endpoints that Amazon Managed Blockchain (AMB) exposes for your member and network resources. For more information, see [Interface VPC Endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*. Applicable charges for interface VPC endpoints apply. For more information, see [AWS PrivateLink Pricing](https://aws.amazon.com/privatelink/pricing/).

The AWS Identity and Access Management (IAM) principal (user) identity that you use must have sufficient IAM permissions to create an interface VPC endpoint in your AWS account. For more information, see [Controlling Access - Creating and Managing VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_IAM.html#vpc-endpoints-iam) in the *Amazon VPC User Guide*.

You can create the interface VPC endpoint using a shortcut in the AMB Access console.

**To create an interface VPC endpoint using the AMB Access console**

1. Open the AMB Access console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/).

1. Choose **Networks**, select your network from the list, and then choose **View details**.

1. Choose **Create VPC endpoint**.

1. Choose a **VPC**.

1. For **Subnets**, choose a subnet from the list, and then choose additional subnets as necessary.

1. For **Security groups**, choose an EC2 security group from the list, and then choose additional security groups as necessary. We recommend that you select the same security group that your framework client EC2 instance is associated with.

1. Choose **Create**.