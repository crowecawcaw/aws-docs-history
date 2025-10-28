# Activating your gateway in a virtual private

cloud

You can create a private connection between your on-premises gateway appliance and
cloud-based storage infrastructure. You can use this connection to activate your gateway and
allow it to transfer data to AWS storage services without communicating over the public
internet. Using the Amazon VPC service, you can launch AWS resources, including private network
interface endpoints, in a custom virtual private cloud (VPC). A VPC gives you control over
network settings such as IP address range, subnets, route tables, and network gateways. For
more information about VPCs, see [What is
Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the _Amazon VPC User Guide_.

To activate your gateway in a VPC, use the Amazon VPC Console to create a VPC endpoint for
Storage Gateway and get the VPC endpoint ID, then specify this VPC endpoint ID when you create
and activate the gateway. For more information, see [Connect your Volume Gateway to AWS](create-volume-gateway.md#connect-to-amazon-volume "create-volume-gateway.md#connect-to-amazon-volume").

###### Note

You must activate your gateway in the same region where you create the VPC endpoint
for Storage Gateway

###### Topics

- [Creating a VPC endpoint for Storage Gateway](#create-vpc-endpoint "#create-vpc-endpoint")

## Creating a VPC endpoint for Storage Gateway

Follow these instructions to create a VPC endpoint. If you already have a VPC endpoint
for Storage Gateway, you can use it to activate your gateway.

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
6. Verify that **Enable Private DNS Name** is not
   selected.
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
    specify an Availability Zone. Your DNS name look similar to this:
    `vpce-1234567e1c24a1fe9-62qntt8k.storagegateway.us-east-1.vpce.amazonaws.com`

Now that you have a VPC endpoint, you can create your gateway. For more information,
see [Creating a
Gateway](create-volume-gateway.md "create-volume-gateway.md").
