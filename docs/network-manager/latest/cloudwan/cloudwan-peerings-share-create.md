# Create a shared peering in an AWS Cloud WAN global
 network

The following steps guide you through creating a shared peering in your core network.

###### Important

Before creating a peering, make sure that the account you use to create the
 peering has the following permissions:


* `ec2:CreateTransitGatewayPolicyTable`
* `ec2:AcceptTransitGatewayPeering`
* `ec2:AssociateTransitGatewayPolicyTable`
###### To create a shared peering

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, under **Shared by me**, choose
 **Peerings**.
5. Choose **Create peering**.
6. Enter a `name` to identify the attachment.
7. From the **Core network** dropdown list, choose the core network
 that is shared with you and that is where you want to create the peering.
8. From the **Edge location** dropdown list, choose the location
 where the attachment is located.
9. In the **Transit gateway** section, choose the transit gateway used for
 the peering.
10. Choose one of the following **Associate policy table**
 options:




	* **New** — Creates a new policy routing table.
	* **Existing** — Allows you to associate this peering with
	 an existing policy route table. If you choose this option, choose an
	 existing **Transit gateway policy table** from the
	 dropdown list to associate with the peering.
11. (Optional) In the **Tags** section, add **Key**
 and **Value** pairs to help identify this resource. You can
 add multiple tags by choosing **Add tag**, or remove any tag by
 choosing **Remove tag**.
12. Choose **Create peering**.
