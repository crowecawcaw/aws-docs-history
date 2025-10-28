# Connecting your CMA with Transit Gateway

AMS does not manage the network setup of Customer Managed accounts (CMAs). You have the option of
managing your own network using AWS APIs (see [Networking Solutions](https://aws.amazon.com/solutionspace/networking/ "https://aws.amazon.com/solutionspace/networking/"))
or connecting to the multi-account landing zone network managed by AMS, using the existing Transit Gateway (TGW) deployed in AMS MALZ.

###### Note

You can only have a VPC attached to the TGW if the CMA is in the same AWS Region. For more information see
[Transit gateways](../../../vpc/latest/tgw/tgw-transit-gateways.md "../../../vpc/latest/tgw/tgw-transit-gateways.md").

To add your CMA to Transit Gateway, request a new route with the
[Networking account | Add static route (ct-3r2ckznmt0a59)](../ctref/deployment-managed-networking-account-add-static-route.md "../ctref/deployment-managed-networking-account-add-static-route.md") change type and include this information:

- **Blackhole**: True to indicate that the route's target isn't available. Do this when the traffic
  for the static route is to be dropped by the Transit Gateway. False to route the traffic to the specified TGW attachment ID. Default value is false.
- **DestinationCidrBlock**: The IPV4 CIDR range used for destination matches. Routing decisions are based on the
  most specific match. Example: `10.0.2.0/24`.
- **TransitGatewayAttachmentId**: The TGW Attachment ID that will serve as route table target. If **Blackhole** is
  false, this parameter is required, otherwise leave this parameter blank. Example: `tgw-attach-04eb40d1e14ec7272`.
- **TransitGatewayRouteTableId**: The ID of the TGW route table. Example: `tgw-rtb-06ddc751c0c0c881c`.
  **Connecting a new customer-managed VPC to the AMS Multi-Account Landing Zone network (creating a TGW VPC attachment)**:

1. In your multi-account landing zone Networking account, open the [Amazon VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit Gateways**. Record the TGW ID of the transit gateway you see.
3. In your Customer Managed account, open the [Amazon VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
4. In the navigation pane, choose **Transit Gateway Attachments** >
   **Create Transit Gateway Attachment**. Make these choices:
   1. For the **Transit Gateway ID**, choose the transit gateway ID you recorded in Step 2.
   2. For **Attachment type**, choose **VPC**.
   3. Under **VPC Attachment**, optionally type a name for **Attachment name tag**.
   4. Choose whether to enable **DNS Support** and **IPv6 Support**.
   5. For **VPC ID**, choose the VPC to attach to the transit gateway. This VPC must have at least one subnet associated with it.
   6. For **Subnet IDs**, select one subnet for each Availability Zone to be used by the transit gateway to route traffic.
      You must select at least one subnet. You can select only one subnet per Availability Zone.

5. Choose **Create attachment**. Record the ID of the newly created TGW Attachment.

 

**Associating the TGW attachment to a route table**:

Decide which TGW route table you want to associate the VPC with. We recommend creating a
new application route table for Customer Managed VPCs by submitting a
Deployment | Managed landing zone | Networking account | Create transit gateway route table (ct-3dscwaeyi6cup) RFC. To associate the VPC or TGW attachment to the route
table you select, submit a Deployment | Managed landing zone | Networking account | Associate TGW attachment (ct-3nmhh0qr338q6) RFC on the Networking account.

 

**Create routes in the TGW route tables to connect to this VPC**:

1. By default, this VPC will not be able to communicate with any of the other VPCs in your Multi-Account Landing Zone network.
2. Decide with your solutions architect what VPCs you want this customer-managed VPC to
   communicate with. Submit a
   Deployment | Managed landing zone | Networking account | Add static route (ct-3r2ckznmt0a59) RFC against the networking
   account to create the TGW routes you need.

###### Note

This CT (ct-3r2ckznmt0a59) does not allow adding static routes to core route table EgressRouteDomain; if your CMA needs to allow egress traffic,
submit a Management | Other | Other (MOO) RFC with ct-0xdawir96cy7k.

 

**Configuring your VPC Route tables to point at the AMS Multi-Account Landing Zone transit gateway**:

Decide with your solutions architect what traffic you want to send to the AMS Multi-Account Landing Zone transit gateway.

Update your VPC route tables to send traffic to TGW attachment created earlier
