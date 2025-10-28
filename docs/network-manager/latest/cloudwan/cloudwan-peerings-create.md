# Create a peering in an AWS Cloud WAN core

network

Create a transit gateway peering.

###### Important

Before creating a peering, make sure that the account you use to create the
peering has the following permissions:

- `ec2:CreateTransitGatewayPolicyTable`
- `ec2:AcceptTransitGatewayPeeringAttachment`
- `ec2:AssociateTransitGatewayPolicyTable`

###### To create a peering

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network ID.
4. Under **Core network** in the navigation pane, choose **Peerings**.
5. Choose **Create peering**.
6. (Optional) Enter a `name` identifying the peering.
7. From the **Edge location** dropdown list, choose the edge
   location where the peering is located.
8. From the **Transit gateway** dropdown list, choose a transit gateway to
   be used for the peering.

###### Note

The core ASN and the transit gateway ASN must be unique. ASNs must be unique for
peerings to succeed. 9. Choose one of the following **Associate policy table**
options:

    * **New** — Creates a new policy routing table.
    * **Existing** — Allows you to associate this peering
     with an existing policy table. If you choose this option, you'll be
     prompted to choose an existing **Transit gateway policy
     table** to associate with the peering. For information on
     creating a transit gateway policy table, see [Transit Gateway policy
     tables](../../../vpc/latest/tgw/tgw-policy-tables.md "../../../vpc/latest/tgw/tgw-policy-tables.md") in the *AWS Transit Gateway
     Guide*.

10. (Optional) If the transit gateway is not registered in your global network, choose
    **Register the specific transit gateway to the global network** to
    simultaneously register the transit gateway to the global network. If your transit gateway is
    already registered, this option does not display.
11. (Optional) In the **Tags** section, add
    **Key** and **Value** tags to help
    identify this resource. You can add multiple tags by choosing **Add
    tag**, or remove any tag by choosing **Remove
    tag**.
12. Choose **Create peering**.

The **Create peering progress** displays the current status
of the peering deployment. When deployment is complete, the
**State** of the peering on the
**Peerings** page displays **Available**.
You can then use this peering to create a transit gateway route table attachment. See
[Transit gateway route table attachments in AWS Cloud WAN](cloudwan-tgw-attachment.md "cloudwan-tgw-attachment.md")
