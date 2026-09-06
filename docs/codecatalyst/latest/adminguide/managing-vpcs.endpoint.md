

Amazon CodeCatalyst will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For more information, see [Migrating from Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html).

# Configuring VPC endpoints for a space
<a name="managing-vpcs.endpoint"></a>

VPCs allow you to define a virtual network that isolates AWS resources, securely connects to remote networks, and safely accesses service endpoints through AWS PrivateLink. AWS PrivateLink is used to generate private endpoints which keep all the network traffic within the AWS network. When connected to a VPC, you can create VPC endpoints that will allow CodeCatalyst to communicate directly with certain services rather than through the internet.

For more information about PrivateLink and VPC endpoints, see [What is AWS PrivateLink?](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html).

Use the following procedure to configure VPC endpoints for a space.

------
#### [ AWS console ]

**To configure VPC endpoints using the AWS console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints** and then choose **Create endpoint**.

1. In **Endpoint settings**, do the following:
   + (Optional) For **Name tag**, enter a reference name for your endpoint.

1. In **Services**, enter your specified service name and then select it. For more information, see [CodeCatalyst VPC endpoint service names](#managing-vpcs.endpoint-service-names).

1. In **VPC**, choose the VPC in which to create your endpoint.
   + For **Additional settings**, leave the default.

1. In **Subnets**, select the same private subnets that you associated with your VPC connection to connect to in each availability zone:
   + In **IP address type**, select **IPv4**. This enables the endpoint service to accept IPv4 requests.

1. In **Security groups**, select the same security groups that you associated with your VPC connection then choose **Create endpoint**.

1. After your VPC endpoint is created, choose that endpoint, and then choose **Modify private DNS name**.

1. In **Enable private DNS names**, select **Enable for this endpoint**.

------
#### [ AWS CLI ]

**To configure VPC endpoints using the AWS CLI**

1. If you haven't done so already, [set up the AWS CLI for CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/set-up-cli.html).

1. Run this command to sign-in to Amazon CodeCatalyst using AWS IAM Identity Center:

   ```
   aws sso login --profile codecatalyst
   ```

1. Create your VPC endpoint:

   ```
   aws ec2 create-vpc-endpoint --vpc-id {{<vpc-id>}} --service-name {{<service-name>}} --subnet-ids {{<subnet-ids>}} --security-group-ids {{<security-group-ids>}} --private-dns-enabled
   ```

   For more information on service names, see [CodeCatalyst VPC endpoint service names](#managing-vpcs.endpoint-service-names).

------

## CodeCatalyst VPC endpoint service names
<a name="managing-vpcs.endpoint-service-names"></a>

You can create VPC endpoints for these services, if you would prefer for CodeCatalyst to utilize these endpoints.
+ Source:
  + Regions: `us-west-2`, `eu-west-1`
  + Service name: `com.amazonaws.{{<region>}}.codecatalyst.git`
+ API:
  + Regions: `us-west-2`, `eu-west-1`
  + Service name: `aws.api.global.codecatalyst`
+ Packages:
  + Regions: `us-west-2`, `eu-west-1`
  + Service name: `com.amazonaws.{{<region>}}.codecatalyst.packages`