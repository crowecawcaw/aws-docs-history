

# Disassociate a customer gateway using AWS Network Manager
<a name="nm-cgw-diasssociate"></a>

You can disassociate a customer gateway from a device or link using the Network Manager console on either of the following pages:
+ On the **Transit gateways** page
+ On the **Devices** page

------
#### [ Transit gateways page ]

**To disassociate a customer gateway using the Transit gateways page**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit gateways**, and then choose **On-premises associations**.

1. Select your customer gateway and choose **Disassociate**.

------
#### [ Devices page ]

**To disassociate a customer gateway using the Devices page**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**, and then choose the ID of your device.

1. Choose **On-premises associations**.

1. Select your customer gateway and choose **Disassociate**.

------

**Disassociate a customer gateway association using the AWS CLI**  
You can view and disassociate a customer gateway association using the following command.
+ To view your customer gateway associations: [get-customer-gateway-associations](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-customer-gateway-associations.html)
+ To disassociate a customer gateway from a device and link: [disassociate-customer-gateway](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/disassociate-customer-gateway.html)