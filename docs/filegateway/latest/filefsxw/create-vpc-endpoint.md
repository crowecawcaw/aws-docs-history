Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Create a VPC endpoint for Storage Gateway

Follow these instructions to create a VPC endpoint. If you already have a VPC endpoint
for Storage Gateway, you can use it.

###### To create a VPC endpoint for Storage Gateway

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**, and then choose
   **Create Endpoint**.
3. On the **Create Endpoint** page, choose **AWS
   Services** for **Service category**.
4. For **Service Name**, choose
   `com.amazonaws.`region`.storagegateway`.
   For example `com.amazonaws.us-east-2.storagegateway`.
5. For **VPC**, choose your VPC and note its Availability Zones
   and subnets.
6. Verify that **Enable DNS Name** is not selected.
7. For **Security group**, choose the security group that you
   want to use for your VPC. You can accept the default security group. Verify that
   all of the following TCP ports are allowed in your security group:
   - TCP 443
   - TCP 1026
   - TCP 1027
   - TCP 1028
   - TCP 1031
   - TCP 2222

8. Choose **Create endpoint**. The initial state of the endpoint
   is **pending**. When the endpoint is created, note the ID of
   the VPC endpoint that you just created.
9. When the endpoint is created, choose **Endpoints**, then
   choose the new VPC endpoint.
10. In **Details** tab of the selected storage gateway endpoint,
    under **DNS Names**, use the first DNS name that doesn't
    specify an Availability Zone. Your DNS name should look similar to the following
    example:
    `vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com`
    Now that you have a VPC endpoint, you can create and activate your gateway. For more
    information, see [Create and activate an
    Amazon FSx File Gateway](create-gateway-file.md "create-gateway-file.md").

For information about getting an activation key, see [Getting an activation key for your gateway](get-activation-key.md "get-activation-key.md").
