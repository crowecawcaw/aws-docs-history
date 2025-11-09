# Access a resource through a resource VPC endpoint

You can access a VPC resource such as a domain name, an IP address, or Amazon RDS database using
a resource endpoint. A resource endpoint provides private access to a resource. When you create
the resource endpoint, you specify a resource configuration of type single, group, or ARN. A
resource endpoint can be associated with only one resource configuration. The resource
configuration can represent a single resource or a group of resources.

## Prerequisites

To create a resource endpoint, you must meet the following prerequisites.

- You must have a resource configuration that you created or another account created and shared with you through AWS RAM.
- If a resource configuration is shared with you from another account, you must review and
  accept the resource share that contains the resource configuration. For more information, see
  [Accepting and rejecting invitations](../../../ram/latest/userguide/working-with-shared-invitations.md "../../../ram/latest/userguide/working-with-shared-invitations.md") in the _AWS RAM User Guide_.

## Create a VPC resource endpoint

Use the following procedure to create a VPC resource endpoint. After you create a resource endpoint, you can only modify its security groups or tags.

###### To create a VPC resource endpoint

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Choose **Create endpoint**.
4. You can specify a name to make it easier to find and manage the endpoint.
5. For **Type**, choose **Resources**.
6. For **Resource configurations**, select the resource configuration.
7. For **Network settings**, select the VPC from which you'll access the
   resource.
8. If, you want to configure private DNS support for resource configurations,
   select **Additional
   settings**, **Enable DNS name**. To use this feature, ensure that
   the attributes **Enable DNS hostnames** and **Enable DNS
   support** are enabled for your VPC. For more information, see [Custom domain names for resource consumers](resource-configuration.md#custom-domain-name-resource-consumers "resource-configuration.md#custom-domain-name-resource-consumers").
9. For **Subnets**, select a subnet to create the endpoint network interface in.

In a production environment, for high availability and resiliency, we recommend configuring at least two Availability Zones for each VPC endpoint. 10. For **Security groups**, select a security group.

If you do not specify a security group, we associate the default security group for the VPC. 11. Choose **Create endpoint**.

###### To create a resource endpoint using the command line

- [create-vpc-endpoint](../../../cli/latest/reference/ec2/create-vpc-endpoint.md "../../../cli/latest/reference/ec2/create-vpc-endpoint.md")
  (AWS CLI)
- [New-EC2VpcEndpoint](../../../powershell/latest/reference/items/New-EC2VpcEndpoint.md "../../../powershell/latest/reference/items/New-EC2VpcEndpoint.md")
  (Tools for Windows PowerShell)
