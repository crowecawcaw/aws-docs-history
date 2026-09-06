

# Step 1: Configure a gateway VPC endpoint to reach S3 Express One Zone directory buckets
<a name="s3-express-tutorial-endpoints"></a>

 You can access both Zonal and Regional API operations through gateway virtual private cloud (VPC) endpoints. Gateway endpoints can allow traffic to reach S3 Express One Zone without traversing a NAT Gateway. We strongly recommend using gateway endpoints as they provide the most optimal networking path when working with S3 Express One Zone. You can access S3 Express One Zone directory buckets from your VPC without an internet gateway or NAT device for your VPC, and at no additional cost. Use the following procedure to configure a gateway endpoint that connects to S3 Express One Zone storage class objects and directory buckets.

To access S3 Express One Zone, you use Regional and Zonal endpoints that are different from standard Amazon S3 endpoints. Depending on the Amazon S3 API operation that you use, either a Zonal or Regional endpoint is required. For a complete list of supported API operations by endpoint type, see [API operations supported by S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-differences.html#s3-express-differences-api-operations). You must access both Zonal and Regional endpoints through a gateway virtual private cloud (VPC) endpoint. 

 Use the following procedure to create a gateway endpoint that connects to S3 Express One Zone storage class objects and directory buckets.

**To configure a gateway VPC endpoint**

1. Open the Amazon VPC Console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the side navigation pane under **Virtual private cloud**, choose **Endpoints**.

1. Choose **Create endpoint**.

1. Create a name for your endpoint.

1. For **Service category**, choose **AWS services**. 

1. Under **Services**, search using the filter **Type=Gateway** and then choose the option button next to **com.amazonaws.{{region}}.s3express**. 

1. For **VPC**, choose the VPC in which to create the endpoint.

1. For **Route tables**, choose the route table on your Local Zone to be used by the endpoint. After the endpoint is created, a route record will be added to the route table that you select in this step.

1. For **Policy**, choose **Full access** to allow all operations by all principals on all resources over the VPC endpoint. Otherwise, choose **Custom** to attach a VPC endpoint policy that controls the principals' permissions to perform actions on resources over the VPC endpoint.

1. For **IP address type**, choose from the following options:
   +  **IPv4** – Assign IPv4 addresses to the endpoint network interfaces. This option is supported only if all selected subnets have IPv4 address ranges and the service accepts IPv4 requests. 
   +  **IPv6** – Assign IPv6 addresses to the endpoint network interfaces. This option is supported only if all selected subnets are IPv6 only subnets and the service accepts IPv6 requests.
   +  **Dualstack** – Assign both IPv4 and IPv6 addresses to the endpoint network interfaces. This option is supported only if all selected subnets have both IPv4 and IPv6 address ranges and the service accepts both IPv4 and IPv6 requests.

1. (Optional) To add a tag, choose **Add new tag**, and enter the tag key and the tag value.

1. Choose **Create endpoint**.

After creating a gateway endpoint, you can use Regional API endpoints and Zonal API endpoints to access Amazon S3 Express One Zone storage class objects and directory buckets.