# Step 1: Configure a gateway VPC endpoint to reach S3 Express One Zone directory buckets

You can access both Zonal and Regional API operations through gateway virtual
private cloud (VPC) endpoints. Gateway endpoints can allow traffic to reach S3 Express One Zone
without traversing a NAT Gateway. We strongly recommend using gateway endpoints as they
provide the most optimal networking path when working with S3 Express One Zone. You can
access S3 Express One Zone directory buckets from your VPC without an internet gateway
or NAT device for your VPC, and at no additional cost. Use the following procedure to
configure a gateway endpoint that connects to S3 Express One Zone storage class objects and
directory buckets.

To access S3 Express One Zone, you use Regional and Zonal endpoints that are different from
standard Amazon S3 endpoints. Depending on the Amazon S3 API operation that you use,
either a Zonal or Regional endpoint is required. For a complete list of supported API
operations by endpoint type, see [API operations supported by S3 Express One Zone](s3-express-differences.md#s3-express-differences-api-operations "s3-express-differences.md#s3-express-differences-api-operations"). You must access both Zonal and
Regional endpoints through a gateway virtual private cloud (VPC) endpoint.

Use the following procedure to create a gateway endpoint that connects to S3 Express One Zone
storage class objects and directory buckets.

###### To configure a gateway VPC endpoint

1. Open the Amazon VPC Console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the side navigation pane under **Virtual private cloud**, choose
   **Endpoints**.
3. Choose **Create endpoint**.
4. Create a name for your endpoint.
5. For **Service category**, choose
   **AWS services**.
6. Under **Services**, search using the filter
   **Type=Gateway** and then choose the option button next to
   **com.amazonaws.`region`.s3express**.
7. For **VPC**, choose the VPC in which to create the
   endpoint.
8. For **Route tables**, select the route tables to be used
   by the endpoint. Amazon VPC automatically adds a route that points traffic
   destined for the service to the endpoint network interface.
9. For **Policy**, choose **Full access** to
   allow all operations by all principals on all resources over the VPC endpoint.
   Otherwise, choose **Custom** to attach a VPC endpoint policy
   that controls the permissions that principals have to perform actions on
   resources over the VPC endpoint.
10. Choose **Create endpoint**.
    After creating a gateway endpoint, you can use Regional API endpoints and Zonal API
    endpoints to access Amazon S3 Express One Zone storage class objects and directory buckets.
