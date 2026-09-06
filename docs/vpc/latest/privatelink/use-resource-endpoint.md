

# Access a resource through a resource VPC endpoint
<a name="use-resource-endpoint"></a>

You can access a VPC resource such as a domain name, an IP address, or Amazon RDS database using a resource endpoint. A resource endpoint provides private access to a resource. When you create the resource endpoint, you specify a resource configuration of type single, group, or ARN. A resource endpoint can be associated with only one resource configuration. The resource configuration can represent a single resource or a group of resources.

## Prerequisites
<a name="prerequisites-resource-endpoints"></a>

To create a resource endpoint, you must meet the following prerequisites.
+ You must have a resource configuration that you created or another account created and shared with you through AWS RAM.
+ If a resource configuration is shared with you from another account, you must review and accept the resource share that contains the resource configuration. For more information, see [Accepting and rejecting invitations](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared-invitations.html) in the *AWS RAM User Guide*.

VPC Lattice does not create a resource endpoint if the following are true:
+ Resource gateway is in the same VPC as the resource endpoint.
+ For domain-name targets
  + DNS resolution is set to IN\_VPC on the resource gateway.
  + The custom domain name or group domain is the same or higher-level domain of the domain-name target.

## Create a VPC resource endpoint
<a name="create-resource-endpoint-aws"></a>

Use the following procedure to create a VPC resource endpoint. After you create a resource endpoint, you can only modify its security groups or tags.

**To create a VPC resource endpoint**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Choose **Create endpoint**.

1. You can specify a name to make it easier to find and manage the endpoint.

1. For **Type**, choose **Resources**.

1. For **Resource configurations**, select the resource configuration.

1. For **Network settings**, select the VPC from which you'll access the resource.

1. If, you want to configure private DNS support for resource configurations, select **Additional settings**, **Enable DNS name**. To use this feature, ensure that the attributes **Enable DNS hostnames** and **Enable DNS support** are enabled for your VPC. For more information, see [Custom domain names for resource consumers](resource-configuration.md#custom-domain-name-resource-consumers).

1. For **Subnets**, select a subnet to create the endpoint network interface in.

   In a production environment, for high availability and resiliency, we recommend configuring at least two Availability Zones for each VPC endpoint.

1. For **Security groups**, select a security group.

   If you do not specify a security group, we associate the default security group for the VPC.

1. Choose **Create endpoint**.

**To create a resource endpoint using the command line**
+ [create-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint.html) (AWS CLI)
+ [New-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2VpcEndpoint.html) (Tools for Windows PowerShell)