# Modify the target gateway of an AWS Site-to-Site VPN connection

You can modify the target gateway of an AWS Site-to-Site VPN connection. The following
migration options are available:

- An existing virtual private gateway to a transit gateway
- An existing virtual private gateway to another virtual private gateway
- An existing transit gateway to another transit gateway
- An existing transit gateway to a virtual private gateway
  After you modify the target gateway, your Site-to-Site VPN connection will be temporarily unavailable
  for a brief period while we provision the new endpoints.

The following tasks help you complete the migration to a new gateway.

###### Tasks

- [Step 1: Create the new target gateway](#step-create-gateway "#step-create-gateway")
- [Step 2: Delete your static routes (conditional)](#step-update-staic-route "#step-update-staic-route")
- [Step 3: Migrate to a new gateway](#step-migrate-gateway "#step-migrate-gateway")
- [Step 4: Update VPC route tables](#step-update-routing "#step-update-routing")
- [Step 5: Update the target gateway routing
  (conditional)](#step-update-transit-gateway-routing "#step-update-transit-gateway-routing")
- [Step 6: Update the customer gateway ASN
  (conditional)](#step-update-customer-gateway-asn "#step-update-customer-gateway-asn")

## Step 1: Create the new target gateway

Before you perform the migration to the new target gateway, you must first configure the new gateway. For
information about adding a virtual private gateway, see [Create a virtual private gateway](SetUpVPNConnections.md#vpn-create-vpg "SetUpVPNConnections.md#vpn-create-vpg").
For more information about adding a transit gateway, see [Create a transit gateway](../../../vpc/latest/tgw/tgw-transit-gateways.md#create-tgw "../../../vpc/latest/tgw/tgw-transit-gateways.md#create-tgw") in
_Amazon VPC Transit Gateways_.

If the new target gateway is a transit gateway, attach the VPCs to the transit gateway. For information about
VPC attachments, see [Transit gateway
attachments to a VPC](../../../vpc/latest/tgw/tgw-vpc-attachments.md "../../../vpc/latest/tgw/tgw-vpc-attachments.md") in _Amazon VPC Transit Gateways_.

When you modify the target from a virtual private gateway to a transit gateway, you can optionally set
the transit gateway ASN to be the same value as the virtual private gateway ASN. If you choose to
have a different ASN, then you must set the ASN on your customer gateway device to the
transit gateway ASN. For more information, see [Step 6: Update the customer gateway ASN
(conditional)](#step-update-customer-gateway-asn "#step-update-customer-gateway-asn").

## Step 2: Delete your static routes (conditional)

This step is required when you migrate from a virtual private gateway with static routes to
a transit gateway.

You must delete the static routes before you migrate to the new gateway.

###### Tip

Keep a copy of the static route before you delete it. You will need to add back these
routes to the transit gateway after the VPN connection migration is complete.

###### To delete a route from a route table

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Route tables**, and then select
   the route table.
3. On the **Routes** tab, choose **Edit routes**.
4. Choose **Remove** for the static route to the virtual private
   gateway.
5. Choose **Save changes**.

## Step 3: Migrate to a new gateway

###### To change the target gateway

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN connections**.
3. Select the VPN connection and choose **Actions**,
   **Modify VPN connection**.
4. For **Target type**, choose the gateway type.
   1. If the new target gateway is a virtual private gateway, choose
      **VPN gateway**.
   2. If the new target gateway is transit gateway, choose **Transit
      gateway**.

5. Choose **Save changes**.

###### To modify a Site-to-Site VPN connection using the command line or API

- [ModifyVpnConnection](../../../AWSEC2/latest/APIReference/API_ModifyVpnConnection.md "../../../AWSEC2/latest/APIReference/API_ModifyVpnConnection.md") (Amazon EC2 Query API)
- [modify-vpn-connection](../../../cli/latest/reference/ec2/modify-vpn-connection.md "../../../cli/latest/reference/ec2/modify-vpn-connection.md") (AWS CLI)

## Step 4: Update VPC route tables

After you migrate to the new gateway, you might need to modify your VPC route table. For
more information, see [Route tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md")
in the _Amazon VPC User Guide_.

The following table provides information about the VPC route table updates to make
after you modify the VPN gateway target.

| Existing gateway                               | New gateway                                    | VPC route table change                                                                                             |
| ---------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Virtual private gateway with propagated routes | Transit gateway                                | Add a route that contains the ID of the transit gateway.                                                           |
| Virtual private gateway with propagated routes | Virtual private gateway with propagated routes | There is no action required.                                                                                       |
| Virtual private gateway with propagated routes | Virtual private gateway with static route      | Add a route that contains the ID of the new virtual private gateway.                                               |
| Virtual private gateway with static routes     | Transit gateway                                | Update the route that contains the ID of the virtual private gateway to the ID of the transit gateway.             |
| Virtual private gateway with static routes     | Virtual private gateway with static routes     | Update the route that contains the ID of the virtual private gateway to the ID of the new virtual private gateway. |
| Virtual private gateway with static routes     | Virtual private gateway with propagated routes | Delete the route that contains the ID of the virtual private gateway.                                              |
| Transit gateway                                | Virtual private gateway with static routes     | Update the route that contains the ID of the transit gateway to the ID of the virtual private gateway.             |
| Transit gateway                                | Virtual private gateway with propagated routes | Delete the route that contains the ID of the transit gateway.                                                      |
| Transit gateway                                | Transit gateway                                | Update the route that contains the ID of the transit gateway to the ID of the new transit gateway.                 | ## Step 5: Update the target gateway routing (conditional) When the new gateway is a transit gateway, modify the transit gateway route table to allow traffic between the VPC and the Site-to-Site VPN. For more information, see [Transit gateway route tables](../../../vpc/latest/tgw/tgw-route-tables.md "../../../vpc/latest/tgw/tgw-route-tables.md") in _Amazon VPC Transit Gateways_. If you deleted VPN static routes, you must add the static routes to the transit gateway route table. Unlike a virtual private gateway, a transit gateway sets the same value for the multi-exit discriminator (MED) across all the tunnels on a VPN attachment. If you are migrating from a virtual private gateway to a transit gateway and relied on the MED value for tunnel selection, we recommend that you make routing changes to avoid connection issues. For example, you can advertise more specific routes on your transit gateway. For more information, see [Route tables and AWS Site-to-Site VPN route priority](vpn-route-priority.md "vpn-route-priority.md"). ## Step 6: Update the customer gateway ASN (conditional) When the new gateway has a different ASN from the old gateway, you must update the ASN on your customer gateway device to point to the new ASN. See [Customer gateway options for your AWS Site-to-Site VPN connection](cgw-options.md "cgw-options.md") for more information. |
