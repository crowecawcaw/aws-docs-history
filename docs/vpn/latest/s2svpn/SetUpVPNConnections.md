# Get started with AWS Site-to-Site VPN

Use the following procedure to set up an AWS Site-to-Site VPN connection. During creation, you will
specify a virtual private gateway, a transit gateway, a Site-to-Site VPN Concentrator, or "Not associated" as the
target gateway type. If you specify "Not associated", you can choose the target gateway type
at a later time, or you can use it as a VPN attachment for AWS Cloud WAN. This tutorial
helps you create a VPN connection using a virtual private gateway. It assumes that you have
an existing VPC with one or more subnets.

To set up a VPN connection using a virtual private gateway, complete the following steps:

###### Tasks

- [Prerequisites](#vpn-prerequisites "#vpn-prerequisites")
- [Create a customer gateway](#vpn-create-cgw "#vpn-create-cgw")
- [Create a target gateway](#vpn-create-target-gateway "#vpn-create-target-gateway")
- [Configure routing](#vpn-configure-route-tables "#vpn-configure-route-tables")
- [Update your security group](#vpn-configure-security-groups "#vpn-configure-security-groups")
- [Create a VPN connection](#vpn-create-vpn-connection "#vpn-create-vpn-connection")
- [Download the configuration
  file](#vpn-download-config "#vpn-download-config")
- [Configure the customer gateway device](#vpn-configure-customer-gateway-device "#vpn-configure-customer-gateway-device")

###### Related tasks

- To create a VPN connection for AWS Cloud WAN, see
  [Create a VPN Cloud WAN connection
  using the CLI or API](create-cwan-vpn-attachment.md "create-cwan-vpn-attachment.md").
- To create a VPN connection on a transit gateway, see
  [Create a VPN connection](create-vpn-connection.md "create-vpn-connection.md").

## Prerequisites

You need the following information to set up and configure the components of a VPN
connection.

| Item                                                   | Information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer gateway device                                | The physical or software device on your side of the VPN connection.<br>You need the vendor (for example, Cisco), platform (for example, ISR<br>Series Routers), and software version (for example, IOS 12.4).                                                                                                                                                                                                                                                                                                                                             |
| Customer gateway                                       | To create the customer gateway resource in AWS, you need the<br>following information:<br>• The internet-routable IP address for the device's external<br>interface<br>• The type of routing: [static or dynamic](VPNRoutingTypes.md "VPNRoutingTypes.md")<br>• For dynamic routing, the Border Gateway Protocol (BGP)<br>Autonomous System Number (ASN)<br>• (Optional) Private certificate from AWS Private Certificate Authority to<br>authenticate your VPN<br>For more information, see [Customer gateway options](cgw-options.md "cgw-options.md"). |
| (Optional) The ASN for the AWS side of the BGP session | You specify this when you create a virtual private gateway or<br>transit gateway. If you do not specify a value, the default ASN<br>applies. For more information, see [Virtual private gateway](how_it_works.md#VPNGateway "how_it_works.md#VPNGateway").                                                                                                                                                                                                                                                                                                |
| VPN connection                                         | To create the VPN connection, you need the following information:<br>• For static routing, the IP prefixes for your private<br>network.<br>• (Optional) Tunnel options for each VPN tunnel. For more<br>information, see [Tunnel options for your AWS Site-to-Site VPN connection](VPNTunnels.md "VPNTunnels.md").                                                                                                                                                                                                                                        |

## Step 1: Create a customer gateway

A customer gateway provides information to AWS about your customer gateway device or
software application. For more information, see [Customer gateway](how_it_works.md#CustomerGateway "how_it_works.md#CustomerGateway").

If you plan to use a private certificate to authenticate your VPN, create a private
certificate from a subordinate CA using AWS Private Certificate Authority. For information about creating a
private certificate, see [Creating
and managing a private CA](../../../privateca/latest/userguide/creating-managing.md "../../../privateca/latest/userguide/creating-managing.md") in the _AWS Private Certificate Authority User
Guide_.

###### Note

You must specify either an IP address, or the Amazon Resource Name of the private
certificate.

###### To create a customer gateway using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Customer gateways**.
3. Choose **Create customer gateway**.
4. (Optional) For **Name tag**, enter a name for your
   customer gateway. Doing so creates a tag with a key of `Name`
   and the value that you specify.
5. For **BGP ASN**, enter a Border Gateway Protocol
   (BGP) Autonomous System Number (ASN) for your customer gateway.
6. For **IP address type**, select one of the following options:
   - **IPv4** - (Default) Specify an IPv4 address for your customer gateway device.
   - **IPv6** - Specify an IPv6 address for your customer gateway device. This option is required when creating a VPN connection with IPv6 outer tunnel IPs.

7. For **IP address**, enter the static,
   internet-routable IP address for your customer gateway device. If your
   customer gateway device is behind a NAT device that's enabled for NAT-T,
   use the public IP address of the NAT device.
8. (Optional) If you want to use a private certificate, for
   **Certificate ARN**, choose the Amazon Resource
   Name of the private certificate.
9. (Optional) For **Device**, enter a name for the
   customer gateway device associated with this customer gateway.
10. Choose **Create customer gateway**.

###### To create a customer gateway using the command line or API

- [CreateCustomerGateway](../../../AWSEC2/latest/APIReference/API_CreateCustomerGateway.md "../../../AWSEC2/latest/APIReference/API_CreateCustomerGateway.md") (Amazon EC2 Query API)
- [create-customer-gateway](../../../cli/latest/reference/ec2/create-customer-gateway.md "../../../cli/latest/reference/ec2/create-customer-gateway.md") (AWS CLI)

Example for creating an IPv6 customer gateway:

```
aws ec2 create-customer-gateway --ipv6-address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 --bgp-asn 65051 --type ipsec.1 --region us-west-1
```

- [New-EC2CustomerGateway](../../../powershell/latest/reference/items/New-EC2CustomerGateway.md "../../../powershell/latest/reference/items/New-EC2CustomerGateway.md") (AWS Tools for Windows PowerShell)

## Step 2: Create a target gateway

To establish a VPN connection between your VPC and your on-premises network, you must
create a target gateway on the AWS side of the connection. The target gateway can be a
virtual private gateway or a transit gateway.

### Create a virtual private gateway

When you create a virtual private gateway, you can specify a custom private
Autonomous System Number (ASN) for the Amazon side of the gateway, or use the Amazon
default ASN. This ASN must be different from the ASN that you specified for the
customer gateway.

After you create a virtual private gateway, you must attach it to your VPC.

###### To create a virtual private gateway and attach it to your VPC

1. In the navigation pane, choose **Virtual private
   gateways**.
2. Choose **Create virtual private gateway**.
3. (Optional) For **Name tag**, enter a name for your
   virtual private gateway. Doing so creates a tag with a key of
   `Name` and the value that you specify.
4. For **Autonomous System Number (ASN)**, keep the default
   selection, **Amazon default ASN**, to use the default
   Amazon ASN. Otherwise, choose **Custom ASN** and enter a
   value. For a 16-bit ASN, the value must be in the 64512 to 65534 range. For
   a 32-bit ASN, the value must be in the 4200000000 to 4294967294
   range.
5. Choose **Create virtual private gateway**.
6. Select the virtual private gateway you created, then choose
   **Actions**, **Attach to VPC**.
7. For **Available VPCs**, choose your VPC and then choose
   **Attach to VPC**.

###### To create a virtual private gateway using the command line or API

- [CreateVpnGateway](../../../AWSEC2/latest/APIReference/API_CreateVpnGateway.md "../../../AWSEC2/latest/APIReference/API_CreateVpnGateway.md") (Amazon EC2 Query API)
- [create-vpn-gateway](../../../cli/latest/reference/ec2/create-vpn-gateway.md "../../../cli/latest/reference/ec2/create-vpn-gateway.md") (AWS CLI)
- [New-EC2VpnGateway](../../../powershell/latest/reference/items/New-EC2VpnGateway.md "../../../powershell/latest/reference/items/New-EC2VpnGateway.md") (AWS Tools for Windows PowerShell)

###### To attach a virtual private gateway to a VPC using the command line or

API

- [AttachVpnGateway](../../../AWSEC2/latest/APIReference/API_AttachVpnGateway.md "../../../AWSEC2/latest/APIReference/API_AttachVpnGateway.md") (Amazon EC2 Query API)
- [attach-vpn-gateway](../../../cli/latest/reference/ec2/attach-vpn-gateway.md "../../../cli/latest/reference/ec2/attach-vpn-gateway.md") (AWS CLI)
- [Add-EC2VpnGateway](../../../powershell/latest/reference/items/Add-EC2VpnGateway.md "../../../powershell/latest/reference/items/Add-EC2VpnGateway.md") (AWS Tools for Windows PowerShell)

### Create a transit gateway

For more information about creating a transit gateway, see [Transit gateways](../../../vpc/latest/tgw/tgw-transit-gateways.md "../../../vpc/latest/tgw/tgw-transit-gateways.md") in
_Amazon VPC Transit Gateways_.

## Step 3: Configure routing

To enable instances in your VPC to reach your customer gateway, you must configure
your route table to include the routes used by your VPN connection and point them to
your virtual private gateway or transit gateway.

### (Virtual private gateway) Enable route propagation in your

route table

You can enable route propagation for your route table to automatically propagate Site-to-Site VPN
routes.

For static routing, the static IP prefixes that you specify for your VPN configuration are
propagated to the route table when the status of the VPN connection is `UP`.
Similarly, for dynamic routing, the BGP-advertised routes from your customer gateway are
propagated to the route table when the status of the VPN connection is `UP`.

###### Note

If your connection is interrupted but the VPN connection remains UP, any propagated routes
that are in your route table are not automatically removed. Keep this in mind
if, for example, you want traffic to fail over to a static route. In that case,
you might have to disable route propagation to remove the propagated
routes.

###### To enable route propagation using the console

1. In the navigation pane, choose **Route tables**.
2. Select the route table that's associated with the subnet.
3. On the **Route propagation** tab, choose
   **Edit route propagation**. Select the virtual private
   gateway that you created in the previous procedure, and then choose
   **Save**.

###### Note

If you do not enable route propagation, you must manually enter the static
routes used by your VPN connection. To do this, select your route table, choose
**Routes**, **Edit**. For
**Destination**, add the static route used by your Site-to-Site VPN
connection. For **Target**, select the virtual private gateway ID,
and choose **Save**.

###### To disable route propagation using the console

1. In the navigation pane, choose **Route tables**.
2. Select the route table that's associated with the subnet.
3. On the **Route propagation** tab, choose
   **Edit route propagation**. Clear the
   **Propagate** check box for the virtual private gateway.
4. Choose **Save**.

###### To enable route propagation using the command line or API

- [EnableVgwRoutePropagation](../../../AWSEC2/latest/APIReference/API_EnableVgwRoutePropagation.md "../../../AWSEC2/latest/APIReference/API_EnableVgwRoutePropagation.md") (Amazon EC2 Query API)
- [enable-vgw-route-propagation](../../../cli/latest/reference/ec2/enable-vgw-route-propagation.md "../../../cli/latest/reference/ec2/enable-vgw-route-propagation.md") (AWS CLI)
- [Enable-EC2VgwRoutePropagation](../../../powershell/latest/reference/items/Enable-EC2VgwRoutePropagation.md "../../../powershell/latest/reference/items/Enable-EC2VgwRoutePropagation.md") (AWS Tools for Windows PowerShell)

###### To disable route propagation using the command line or API

- [DisableVgwRoutePropagation](../../../AWSEC2/latest/APIReference/API_DisableVgwRoutePropagation.md "../../../AWSEC2/latest/APIReference/API_DisableVgwRoutePropagation.md") (Amazon EC2 Query API)
- [disable-vgw-route-propagation](../../../cli/latest/reference/ec2/disable-vgw-route-propagation.md "../../../cli/latest/reference/ec2/disable-vgw-route-propagation.md") (AWS CLI)
- [Disable-EC2VgwRoutePropagation](../../../powershell/latest/reference/items/Disable-EC2VgwRoutePropagation.md "../../../powershell/latest/reference/items/Disable-EC2VgwRoutePropagation.md") (AWS Tools for Windows PowerShell)

### (Transit gateway) Add a route to your route table

If you enabled route table propagation for your transit gateway, the routes for
the VPN attachment are propagated to the transit gateway route table. For more
information, see [Routing](../../../vpc/latest/tgw/how-transit-gateways-work.md#tgw-routing-overview "../../../vpc/latest/tgw/how-transit-gateways-work.md#tgw-routing-overview") in _Amazon VPC Transit Gateways_.

If you attach a VPC to your transit gateway and you want to enable resources in
the VPC to reach your customer gateway, you must add a route to your subnet route
table to point to the transit gateway.

###### To add a route to a VPC route table

1. On the navigation pane, choose **Route tables**.
2. Choose the route table that is associated with your VPC.
3. On the **Routes** tab, choose **Edit
   routes**.
4. Choose **Add route**.
5. For **Destination**, enter the destination IP
   address range. For **Target**, choose the transit gateway.
6. Choose **Save changes**.

## Step 4: Update your security group

To allow access to instances in your VPC from your network, you must update your
security group rules to enable inbound SSH, RDP, and ICMP access.

###### To add rules to your security group to enable access

1. In the navigation pane, choose **Security groups**.
2. Select the security group for the instances in your VPC that you want to allow access to.
3. On the **Inbound rules** tab, choose **Edit inbound rules**.
4. Add rules that allow inbound SSH, RDP, and ICMP access from your network, and then choose
   **Save rules**. For more information, see
   [Work with security group rules](../../../vpc/latest/userguide/security-group-rules.md#working-with-security-group-rules "../../../vpc/latest/userguide/security-group-rules.md#working-with-security-group-rules") in the _Amazon VPC User Guide_.

## Step 5: Create a VPN connection

Create the VPN connection using the customer gateway in combination with the virtual
private gateway or transit gateway that you created earlier.

###### To create a VPN connection

1. In the navigation pane, choose **Site-to-Site VPN connections**.
2. Choose **Create VPN connection**.
3. (Optional) For **Name tag**, enter a name for your VPN
   connection. Doing so creates a tag with a key of `Name` and the value
   that you specify.
4. For **Target gateway type**, choose either **Virtual
   private gateway** or **Transit gateway**. Then,
   choose the virtual private gateway or transit gateway that you created
   earlier.
5. For **Customer gateway**, select
   **Existing**, then choose the customer gateway that you
   created earlier from **Customer gateway ID**.
6. Select one of the **Routing options** based on whether your
   customer gateway device supports Border Gateway Protocol (BGP):
   - If your customer gateway device supports BGP, choose **Dynamic
     (requires BGP)**.
   - If your customer gateway device does not support BGP, choose
     **Static**. For **Static IP
     Prefixes**, specify each IP prefix for the private network
     of your VPN connection.

7. Choose the Pre-shared key storage type:
   - **Standard** — The pre-shared key is stored directly
     in the Site-to-Site VPN service.
   - **Secrets Manager** — The pre-shared key is stored
     using AWS Secrets Manager. For more information about Secrets Manager, see [Enhanced security features using Secrets Manager](enhanced-security.md "enhanced-security.md").

8. If your target gateway type is transit gateway, for **Tunnel inside IP
   version**, specify whether the VPN tunnels support IPv4 or IPv6
   traffic. IPv6 traffic is only supported for VPN connections on a transit
   gateway.
9. If you specified **IPv4** for **Tunnel inside IP
   version**, you can optionally specify the IPv4 CIDR ranges for the
   customer gateway and AWS sides that are allowed to communicate over the VPN
   tunnels. The default is `0.0.0.0/0`.

If you specified **IPv6** for **Tunnel inside IP
version**, you can optionally specify the IPv6 CIDR ranges for the
customer gateway and AWS sides that are allowed to communicate over the VPN
tunnels. The default for both ranges is `::/0`. 10. For **Outside IP address type**, select one of the following options:

    * **PublicIpv4** - (Default) Use IPv4 addresses for the outer tunnel IPs.
    * **IPv6** - Use IPv6 addresses for the outer tunnel IPs. This option is only available for VPN connections on a transit gateway or Cloud WAN.

11. (Optional) For **Tunnel options**, you can specify the
    following information for each tunnel:
    - A size /30 IPv4 CIDR block from the `169.254.0.0/16` range
      for the inside tunnel IPv4 addresses.
    - If you specified **IPv6** for **Tunnel inside
      IP version**, a /126 IPv6 CIDR block from the
      `fd00::/8` range for the inside tunnel IPv6
      addresses.
    - The IKE pre-shared key (PSK). The following versions are supported:
      IKEv1 or IKEv2.
    - To edit the advanced options for your tunnel, choose **Edit tunnel options**.
      For more information, see [VPN tunnel options](VPNTunnels.md "VPNTunnels.md").

12. Choose **Create VPN connection**. It might take a few minutes
    to create the VPN connection.

###### To create a VPN connection using the command line or API

- [CreateVpnConnection](../../../AWSEC2/latest/APIReference/API_CreateVpnConnection.md "../../../AWSEC2/latest/APIReference/API_CreateVpnConnection.md") (Amazon EC2 Query API)
- [create-vpn-connection](../../../cli/latest/reference/ec2/create-vpn-connection.md "../../../cli/latest/reference/ec2/create-vpn-connection.md") (AWS CLI)

Example for creating a VPN connection with IPv6 outer tunnel IPs and IPv6 inner tunnel IPs:

```
aws ec2 create-vpn-connection --type ipsec.1 --transit-gateway-id tgw-12312312312312312 --customer-gateway-id cgw-001122334455aabbc --options OutsideIPAddressType=IPv6,TunnelInsideIpVersion=ipv6,TunnelOptions=[{StartupAction=start},{StartupAction=start}]
```

Example for creating a VPN connection with IPv6 outer tunnel IPs and IPv4 inner tunnel IPs:

```
aws ec2 create-vpn-connection --type ipsec.1 --transit-gateway-id tgw-12312312312312312 --customer-gateway-id cgw-001122334455aabbc --options OutsideIPAddressType=IPv6,TunnelInsideIpVersion=ipv4,TunnelOptions=[{StartupAction=start},{StartupAction=start}]
```

- [New-EC2VpnConnection](../../../powershell/latest/reference/items/New-EC2VpnConnection.md "../../../powershell/latest/reference/items/New-EC2VpnConnection.md") (AWS Tools for Windows PowerShell)

## Step 6: Download the configuration file

After you create the VPN connection, you can download a sample configuration file to
use for configuring the customer gateway device.

###### Important

The configuration file is an example only and might not match your intended VPN
connection settings entirely. It specifies the minimum requirements for a VPN
connection of AES128, SHA1, and Diffie-Hellman group 2 in most AWS Regions, and
AES128, SHA2, and Diffie-Hellman group 14 in the AWS GovCloud Regions. It also
specifies pre-shared keys for authentication. You must modify the example
configuration file to take advantage of additional security algorithms,
Diffie-Hellman groups, private certificates, and IPv6 traffic.

We have introduced IKEv2 support in the configuration files for many popular
customer gateway devices and will continue to add additional files over time. For a
list of configuration files with IKEv2 support, see [AWS Site-to-Site VPN customer gateway devices](your-cgw.md "your-cgw.md").

###### Permissions

To properly load the download configuration screen from the AWS Management Console, you must
ensure that your IAM role or user has permission for the following Amazon EC2 APIs:
`GetVpnConnectionDeviceTypes` and
`GetVpnConnectionDeviceSampleConfiguration`.

###### To download the configuration file using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN connections**.
3. Select your VPN connection and choose **Download
   configuration**.
4. Select the **Vendor**, **Platform**,
   **Software**, and **IKE version** that
   correspond to your customer gateway device. If your device is not listed, choose
   **Generic**.
5. Choose **Download**.

###### To download a sample configuration file using the command line or API

- [GetVpnConnectionDeviceTypes](../../../AWSEC2/latest/APIReference/API_GetVpnConnectionDeviceTypes.md "../../../AWSEC2/latest/APIReference/API_GetVpnConnectionDeviceTypes.md") (Amazon EC2 API)
- [GetVpnConnectionDeviceSampleConfiguration](../../../AWSEC2/latest/APIReference/API_GetVpnConnectionDeviceSampleConfiguration.md "../../../AWSEC2/latest/APIReference/API_GetVpnConnectionDeviceSampleConfiguration.md") (Amazon EC2 Query API)
- [get-vpn-connection-device-types](../../../cli/latest/reference/ec2/get-vpn-connection-device-types.md "../../../cli/latest/reference/ec2/get-vpn-connection-device-types.md") (AWS CLI)
- [get-vpn-connection-device-sample-configuration](../../../cli/latest/reference/ec2/get-vpn-connection-device-sample-configuration.md "../../../cli/latest/reference/ec2/get-vpn-connection-device-sample-configuration.md") (AWS CLI)

## Step 7: Configure the customer gateway device

Use the sample configuration file to configure your customer gateway device. The customer
gateway device is the physical or software appliance on your side of the VPN connection.
For more information, see [AWS Site-to-Site VPN customer gateway devices](your-cgw.md "your-cgw.md").
