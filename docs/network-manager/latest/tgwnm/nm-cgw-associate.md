

# Associate a customer gateway using AWS Network Manager
<a name="nm-cgw-associate"></a>

You can associate a customer gateway with a device and link using the Network Manager console on either of the following pages:
+ On the **Transit gateways** page
+ On the **Devices** page

------
#### [ Transit gateways page ]

**To associate a customer gateway using the Transit gateways page**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit gateways**, and then choose the ID of your transit gateway.

1. Choose **On-premises associations**.

1. Select your customer gateway and choose **Associate**.

1. For **Device**, select the ID of the device to associate. For **Link**, select the ID of the link to associate.

1. Choose **Edit on-premises association**.

------
#### [ Devices page ]

**To associate a customer gateway using the Devices page**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**, and then choose the ID of your device.

1. Choose **On-premises associations**.

1. Choose **Associate**.

1. For **Customer gateway**, select the ID of the customer gateway to associate. For **Link**, select the ID of the link to associate.

1. Choose **Create on-premises association**.

------

**Create a customer gateway association using the AWS CLI**  
You can view and create a customer gateway association using the following commands.
+ To associate a customer gateway with a device and link: [associate-customer-gateway](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/associate-customer-gateway.html)
+ To view your customer gateway associations: [get-customer-gateway-associations](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-customer-gateway-associations.html)