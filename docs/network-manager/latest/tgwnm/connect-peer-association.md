# Add a Connect peer association using AWS Network Manager

Create a transit gateway Connect peer association using the Network Manager console on either of the following
pages:

- On the **Transit gateways** page
- On the **Devices** page

Transit gateways page

###### To associate a Connect peer using the Transit gateways page

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Transit
   gateways**, and then choose the ID of your transit
   gateway.
5. Choose **Connect peer associations**.
6. Select the Connect peer and choose
   **Edit**.
7. For **Device**, select the ID of the device to
   associate. For **Link**, select the ID of the link
   to associate.
8. Choose **Edit Connect peer association**.

Devices page

###### To associate a Connect peer using the Devices page

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Devices**, and
   choose the ID of the device.
5. Choose **Connect peer associations**.
6. Choose **Associate**.
7. For **Connect peer**, choose the
   Connect peer.
8. (Optional) For **Link**, choose the link for the
   Connect peer association.
9. Choose **Create Connect peer
   association**.

###### Working with Connect peer associations using the AWS CLI

You can view and create Connect peer associations using the following commands.

- To associate a Connect peer with a device: [associate-transit-gateway-connect-peer](../../../cli/latest/reference/networkmanager/associate-transit-gateway-connect-peer.md "../../../cli/latest/reference/networkmanager/associate-transit-gateway-connect-peer.md")
- To view your Connect peer associations: [get-transit-gateway-connect-peer-associations](../../../cli/latest/reference/networkmanager/get-transit-gateway-connect-peer-associations.md "../../../cli/latest/reference/networkmanager/get-transit-gateway-connect-peer-associations.md")
