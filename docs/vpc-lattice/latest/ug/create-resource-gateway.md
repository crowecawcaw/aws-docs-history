# Create a resource gateway in VPC Lattice

Use the console to create a resource gateway.

###### To create a resource gateway using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **PrivateLink and Lattice**, choose
   **Resource gateways**.
3. Choose **Create resource gateway**.
4. For **Resource gateway name**, enter a name that is unique within your
   AWS account.
5. For **IP address type**, choose the IP address type for the resource gateway.
   1. If you selected **IPv4** or **Dualstack** for the
      **IP address type**, you can enter the number of IPv4 addresses per ENI for your resource
      gateway.

   The default is 16 IPv4 addresses per ENI. This is a suitable
   number of IPs to form connections with your backend resources.

6. For **VPC**, choose the VPC and subnets to create your resource gateway
   in.
7. For **Security groups**, choose up to five security groups to control inbound traffic from the VPC to the service
   network.
8. (Optional) To add a tag, choose **Add new tag** and enter the tag key and
   the tag value.
9. Choose **Create resource gateway**.

###### To create a resource gateway using the AWS CLI

Use the [create-resource-gateway](../../../cli/latest/reference/vpc-lattice/create-resource-gateway.md "../../../cli/latest/reference/vpc-lattice/create-resource-gateway.md") command.
