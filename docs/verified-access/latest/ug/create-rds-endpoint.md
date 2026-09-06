

# Create an Amazon Relational Database Service endpoint for Verified Access
<a name="create-rds-endpoint"></a>

Use the following procedure to create an Amazon Relational Database Service (RDS) endpoint.

**Requirements**
+ Only the TCP protocol is supported.
+ Create an RDS instance, RDS cluster, or RDS DB proxy.
+ Before you create a Verified Access endpoint, you must create a Verified Access group. For more information, see [Create a Verified Access group](create-verified-access-group.md#create-group).
+ Create the endpoint and then connect to the application using the [Connectivity Client](connectivity-client.md).

**To create an Amazon Relational Database Service endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access endpoints**.

1. Choose **Create Verified Access endpoint**.

1. (Optional) For **Name tag** and **Description**, enter a name and description for the endpoint.

1. For **Verified Access group**, choose a Verified Access group for the endpoint.

1. For **Endpoint details**, do the following:

   1. For **Protocol**, choose **TCP**.

   1. For **Attachment type**, choose **VPC**.

   1. For **Endpoint type**, choose **Amazon Relational Database Service (RDS)**.

   1. For **RDS target type**, do one of the following:
      + Choose **RDS instance**, and then choose an RDS instance from **RDS instance**.
      + Choose **RDS cluster**, and then choose an RDS cluster from **RDS cluster**.
      + Choose **RDS DB proxy**, and then choose an RDS DB proxy from **RDS DB proxy**.

   1. For **RDS endpoint**, choose an RDS endpoint related to the RDS resource you chose in the previous step.

   1. For **Port**, enter the port number.

   1. For **Subnet**, choose the subnets. You can specify only one subnet per Availability Zone.

   1. For **Security groups**, choose the security groups for the endpoint. These security groups control the inbound and outbound traffic for the Verified Access endpoint.

   1. (Optional) For **Endpoint domain prefix**, enter a custom identifier to prepend to the DNS name that Verified Access generates for the endpoint.

1. (Optional) For **Policy definition**, enter a Verified Access policy for the endpoint.

1. (Optional) To add a tag, choose **Add new tag** and enter the tag key and the tag value.

1. Choose **Create Verified Access endpoint**.

**To create a Verified Access endpoint using the AWS CLI**  
Use the [create-verified-access-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-verified-access-endpoint.html) command.