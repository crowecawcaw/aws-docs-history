# Associate a customer gateway using AWS Network Manager

You can associate a customer gateway with a device and link using the Network Manager console on either
of the following pages:

- On the **Transit gateways** page
- On the **Devices** page

Transit gateways page

###### To associate a customer gateway using the Transit gateways

page

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Transit
   gateways**, and then choose the ID of your transit
   gateway.
5. Choose **On-premises associations**.
6. Select your customer gateway and choose
   **Associate**.
7. For **Device**, select the ID of the device to
   associate. For **Link**, select the ID of the link
   to associate.
8. Choose **Edit on-premises association**.

Devices page

###### To associate a customer gateway using the Devices page

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Devices**, and
   then choose the ID of your device.
5. Choose **On-premises associations**.
6. Choose **Associate**.
7. For **Customer gateway**, select the ID of the
   customer gateway to associate. For **Link**, select
   the ID of the link to associate.
8. Choose **Create on-premises association**.

###### Create a customer gateway association using the AWS CLI

You can view and create a customer gateway association using the following
commands.

- To associate a customer gateway with a device and link: [associate-customer-gateway](../../../cli/latest/reference/networkmanager/associate-customer-gateway.md "../../../cli/latest/reference/networkmanager/associate-customer-gateway.md")
- To view your customer gateway associations: [get-customer-gateway-associations](../../../cli/latest/reference/networkmanager/get-customer-gateway-associations.md "../../../cli/latest/reference/networkmanager/get-customer-gateway-associations.md")
