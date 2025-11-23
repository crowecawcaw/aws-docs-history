# Tutorial: Creating and Streaming from Interface VPC Endpoints

You can use an interface VPC endpoint in your Amazon Web Services account to restrict all network
traffic between your Amazon VPC and WorkSpaces Applications to the Amazon network. After you create this
endpoint, you configure your WorkSpaces Applications stack or image builder to use it.

**Prerequisites**

Before you set up interface VPC endpoints for WorkSpaces Applications, be aware of the following prerequisites:

- Internet connectivity is required to authenticate users and deliver the web assets that WorkSpaces Applications
  requires to function. The streaming interface endpoint maintains the streaming
  traffic within your VPC. Streaming traffic includes pixel, USB, user input,
  audio, clipboard, file upload and download, and printer traffic. To allow this
  traffic, you must allow the domains listed in [Allowed Domains](allowed-domains.md "allowed-domains.md"). After creating
  the VPC endpoint, you must allow the WorkSpaces Applications user authentication domains.
  However, for the streaming gateways, you can restrict access to just
  <vpc-endpoint-id>.streaming.appstream.<aws-region>.vpce.amazonaws.com.
  Allow listing to \*.amazonappstream.com is not required. The VPC endpoint fully
  qualified domain name replaces that dependency.
- The network to which your users' devices are connected must be able to route traffic to the interface endpoint.
- The security groups that are associated with the interface endpoint must allow inbound access to port 443 (TCP) and ports 1400-1499 (TCP) from the IP address range from which your users connect.
- The network access control list for the subnets must allow outbound traffic from ephemeral network ports 1024-65535 (TCP) to the IP address range from which your users connect.
- You must have an IAM permissions policy in your AWS account that provides permissions to perform the `ec2:DescribeVpcEndpoints` API action. By default, this permission is defined in the IAM policy that is attached to the AmazonAppStreamServiceAccess role. If you have the required permissions, this service role is automatically created by WorkSpaces Applications, with the required IAM policies attached, when you get started with the WorkSpaces Applications service in an AWS Region. For more information, see [Identity and Access Management for Amazon WorkSpaces Applications](controlling-access.md "controlling-access.md").

###### To create an interface endpoint

1.  Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2.  In the navigation pane, choose **Endpoints**, **Create Endpoint**.
3.  Choose **Create Endpoint**.
4.  For **Service category**, ensure that **AWS services** is selected.
5.  For **Service Name**, choose `com.amazonaws.``<AWS Region>``.appstream.streaming`.
6.  Specify the following information. When you're done, choose **Create endpoint**.

        * For **VPC**, choose a VPC in which to create the interface endpoint. You can choose a different VPC than the VPC with WorkSpaces Applications resources.
        * For **Subnets**, choose the subnets (Availability Zones) in which to create the endpoint network interfaces. We recommend that you choose subnets in at least two Availability Zones.
        * For **IP address type**, choose either IPV6 or IPV4.
        * Ensure that the **Enable Private DNS Name** check box is selected.


        ###### Note

        If your users use a network proxy to access streaming instances, disable any proxy caching on
         the domain and DNS names that are associated with the private
         endpoint. The VPC endpoint DNS name should be allowed through the
         proxy.
        * For **Security group**, choose the security groups to associate with the endpoint network interfaces.


        ###### Note

        The security groups must provide inbound access to the ports from the IP address range from which your users connect.

    While your interface endpoint is being created, the status of the endpoint in the console
    appears as **Pending**. After your endpoint is created, the
    status changes to **Available.**

To update a stack to use the interface endpoint that you created for streaming sessions, perform the following steps.

###### To update a stack to use a new interface endpoint

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home "https://console.aws.amazon.com/appstream2/home").

Ensure that you open the console in the same AWS Region as the interface endpoint that you want to use. 2. In the navigation pane, choose **Stacks**, and then choose the stack that you want. 3. Choose the **VPC Endpoints** tab, and then choose **Edit**. 4. In the **Edit VPC Endpoint** dialog box, for **Streaming
Endpoint**, choose the endpoint through which to stream
traffic. 5. Choose **Update**.
Traffic for new streaming sessions will be routed through this endpoint. However, traffic for current streaming sessions continues to be routed through the previously specified endpoint.

###### Note

Users cannot stream using the internet endpoint when an interface endpoint is specified.
