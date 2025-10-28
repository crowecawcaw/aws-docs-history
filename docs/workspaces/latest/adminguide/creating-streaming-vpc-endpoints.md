# Create and Stream from Interface VPC Endpoints

A virtual private cloud (VPC) is a virtual network in your own logically isolated
area in the Amazon Web Services Cloud. If you use Amazon Virtual Private Cloud to
host your AWS resources, you can establish a private connection between your VPC and
WorkSpaces. You can use this connection to enable WorkSpaces to communicate with your
resources on your VPC without going through the public internet.

Interface endpoints are powered by AWS PrivateLink, a technology that lets you keep
streaming traffic within a VPC that you specify by using private IP addresses. When you
use the VPC with an AWS Direct Connect or AWS Virtual Private Network tunnel, you can
keep the streaming traffic within your network.

You can use a VPC endpoint in your AWS account to restrict all streaming traffic between your Amazon VPC
and WorkSpaces to the AWS network. After you create the endpoint, configure your WorkSpaces directory to use it.

## Prerequisites and limitations

Before you set up VPC endpoints for WorkSpaces, be aware of the following prerequisites and limitations.

- The feature currently supports IPv4 or IPv6 DNS record IP type. Dualstack DNS record IP type is not
  supported.
- You can only configure VPC endpoints that are in the same AWS account as your directory.
  VPC endpoints in other AWS accounts are not supported, including endpoints in shared VPCs.
- The feature currently only support private DNS name for VPC endpoints. The private DNS name
  for a VPC endpoint is not publicly resolvable.
- The feature is currently available for WorkSpaces Personal only. WorkSpaces
  Pools does not support VPC endpoints for streaming.
- The VPC endpoint feature is available exclusively for WorkSpaces using Amazon DCV. When you
  configure a VPC endpoint for a directory, users cannot stream from Amazon DCV over the internet. However,
  you can enable internet streaming for PCoIP WorkSpaces in the same directory during VPC
  endpoint configuration.
- To maintain streaming traffic within your VPC, use a streaming VPC endpoint. Your WorkSpaces clients
  require internet connectivity for user authentication. Enable outbound access on port 443 (both UDP and TCP)
  for authentication traffic. Additionally, you must add the required domains and IP addresses to your allow
  list based on your chosen authentication method. For a complete list of domains for each category, refer to
  [Domains and IP addresses to add to your allow list](workspaces-port-requirements.md#whitelisted_ports "workspaces-port-requirements.md#whitelisted_ports").
  - CAPTCHA
  - Directory Settings
  - Pre-session Smart Card Authentication Endpoints, if you are using Smart Card
  - User Login Pages
  - WS Broker
  - WorkSpaces Endpoints for SAML Single Sign-On (SSO)

- The network that your users' devices are connected must be able to route
  traffic to the VPC endpoint.
- You must have an IAM permissions policy for the IAM user or IAM role in your
  AWS account to perform the `ec2:DescribeVpcEndpoints` API action.
- WorkSpaces streaming VPC endpoints currently do not support FIPS encryption.
  If you already enabled FIPS encryption for a directory, you need to disable FIPS
  encryption before configuring a VPC endpoint.
- AWS Global Accelerator (AGA) integration is
  not available when streaming through a VPC endpoint.
- When a VPC endpoint is configured for a directory, IP access control groups specified
  for the directory no longer apply.

## Setting up VPC endpoint for WorkSpaces streaming

To set up a VPC endpoint for WorkSpaces streaming, complete the following steps:

### Step 1: Create the security group

In this step, you create a security group that lets WorkSpaces clients communicate with VPC endpoint you'll be creating.

1. In the navigation pane of the Amazon EC2 console, go to **Network & Security**, then **Security Groups**.
2. Select **Create security group**.
3. Under **Basic details**, enter the following:
   - For **Security group name** – Enter a unique name that identifies the security group.
   - For **Description** – Enter some text that describes the purpose of the security group.
   - For **VPC** – Choose the VPC that your VPC endpoint is in.

4. Go to **Inbound rules** and select **Add rule** to create inbound rules for TCP traffic.
5. Enter the following:
   - For **Type** – Choose Custom TCP.
   - For **Port range** – Enter the following port numbers: `443`, `4195`.
   - For **Source type** – Choose Custom.
   - For **Source** – Enter the private IP CIDR range or other Security Group IDs from which your users connect
     to the VPC endpoint. Make sure to allow inbound traffic from an IPv4 or IPv6 address source.

6. Repeat steps 4 and 5 for each CIDR range or Security Group.
7. Go to **Inbound rules**, select **Add rule** to create inbound rules for UDP traffic.
8. Enter the following:
   - For **Type** – Choose **Custom UDP**.
   - For **Port range** – Enter the following port numbers: 443, 4195.
   - For **Source type** – Choose **Custom**.
   - For **Source** – Enter the same private IP CIDR range or Security Group IDs entered in Step 5.
     Make sure to allow inbound traffic from an IPv4 or IPv6 address source.

9. Repeat steps 7 and 8 for each CIDR range or Security Group.
10. Select **Create security group**.

### Step 2: Create the VPC endpoint

In Amazon VPC, a VPC endpoint lets you connect your VPC to supported AWS services. In this example,
you configure Amazon VPC so that your WorkSpaces users can stream from WorkSpaces.

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, go to **Endpoints**, then **Create Endpoint**.
3. Select **Create Endpoint**.
4. Ensure the following:
   - **Service category** – Make sure that **AWS services** is selected.
   - **Service Name** – Choose **com.amazonaws.`Region`.highlander**.
   - **VPC** – Choose a VPC in which to create the interface endpoint. You can choose a different VPC than the VPC with WorkSpaces
     resources as long as the network routes traffic to the VPC endpoint.
   - **Enable Private DNS Name** – The check box is selected. If your users use a network proxy to access streaming instances,
     disable any proxy caching on the domain and DNS names that are associated with the private endpoint.
     The VPC endpoint DNS name should be allowed through the proxy. For successful DNS name resolution, it is essential to use the private DNS servers within the VPC,
     this is because public DNS servers will not resolve the VPC endpoint DNS name.
   - **DNS record IP type** – Choose IPv4 or IPv6. Dualstack DNS record IP type is currently not supported. If you choose Dualstack,
     you won’t be able to stream from WorkSpaces using the VPC endpoint.
   - **Subnets** – Choose the subnets (Availability Zones) to create the VPC endpoint. It is recommended that you choose at least two subnets.
   - **IP address type** – Choose IPv4, IPv6 or Dualstack depending on what the Subnets you chose support.
   - **Security groups panel** – Select the security group you created earlier.

5. (Optional) In the **Tags** panel, you can create one or more tags.
6. Select **Create endpoint**.

When the endpoint is ready to use, the value in the **Status** column changes to **Available**.

### Step 3: Configure WorkSpaces directory to use the VPC endpoint

You need to configure the WorkSpaces directory to use the VPC endpoint that you created for streaming.

1. Open the [WorkSpaces console](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home") in the same AWS Region as the VPC endpoint.
2. In the **Navigation** pane, select **Directories**, and then .
3. Select the directory that you want to use.
4. Go to the **VPC Endpoints** section, then **Edit**.
5. In the **Edit VPC Endpoint** dialog box, under **Streaming Endpoint**, select the VPC endpoint you created.
6. Optionally, you can enable **Allow users with PCoIP WorkSpaces to stream from the internet**.

###### Note

When enabled, your users are able to stream from their PCoIP WorkSpaces through public internet. Otherwise, the PCoIP WorkSpaces in the directory will become unreachable since PCoIP WorkSpaces don’t support VPC endpoint for streaming. 7. Select **Save**.

Traffic for new streaming sessions will be routed through this VPC endpoint. However, traffic for current streaming sessions continues to be routed through the previously specified endpoint.

###### Note

Users with DCV WorkSpaces cannot stream using the public internet when a VPC endpoint is specified.
