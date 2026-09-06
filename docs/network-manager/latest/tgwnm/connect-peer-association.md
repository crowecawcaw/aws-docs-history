

# Add a Connect peer association using AWS Network Manager
<a name="connect-peer-association"></a>

Create a transit gateway Connect peer association using the Network Manager console on either of the following pages:
+ On the **Transit gateways** page
+ On the **Devices** page

------
#### [ Transit gateways page ]

**To associate a Connect peer using the Transit gateways page**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit gateways**, and then choose the ID of your transit gateway.

1. Choose **Connect peer associations**.

1. Select the Connect peer and choose **Edit**.

1. For **Device**, select the ID of the device to associate. For **Link**, select the ID of the link to associate.

1. Choose **Edit Connect peer association**.

------
#### [ Devices page ]

**To associate a Connect peer using the Devices page**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**, and choose the ID of the device.

1. Choose **Connect peer associations**.

1. Choose **Associate**.

1. For **Connect peer**, choose the Connect peer.

1. (Optional) For **Link**, choose the link for the Connect peer association.

1. Choose **Create Connect peer association**.

------

**Working with Connect peer associations using the AWS CLI**  
You can view and create Connect peer associations using the following commands.
+ To associate a Connect peer with a device: [associate-transit-gateway-connect-peer](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/associate-transit-gateway-connect-peer.html)
+ To view your Connect peer associations: [get-transit-gateway-connect-peer-associations](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-transit-gateway-connect-peer-associations.html)