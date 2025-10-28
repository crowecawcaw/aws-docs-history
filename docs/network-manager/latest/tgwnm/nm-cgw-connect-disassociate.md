# Disassociate a Connect peer using AWS Network Manager

You can disassociate a Connect peer from a device in one of the following
ways:

- On the **Transit gateways** page
- On the **Devices** page

Transit gateways page

###### To disassociate a Connect peer using the Transit gateways

page

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Transit
   gateways**, and then choose **Connect peer
   associations**.
5. Select the Connect peer and choose
   **Disassociate**.

Devices page

###### To disassociate a Connect peer using the Devices page

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Devices**, and
   then choose the ID of your device.
5. Choose **Connect peer associations**.
6. Select the Connect peer and choose
   **Disassociate**.

###### Working with Connect peer associations using the AWS CLI

You can view and disassociate Connect peer associations using the following
commands.

- To view your Connect peer associations: [get-transit-gateway-connect-peer-associations](../../../cli/latest/reference/networkmanager/get-transit-gateway-connect-peer-associations.md "../../../cli/latest/reference/networkmanager/get-transit-gateway-connect-peer-associations.md")
- To disassociate a Connect peer from a device: [disassociate-transit-gateway-connect-peer](../../../cli/latest/reference/networkmanager/disassociate-transit-gateway-connect-peer.md "../../../cli/latest/reference/networkmanager/disassociate-transit-gateway-connect-peer.md")
