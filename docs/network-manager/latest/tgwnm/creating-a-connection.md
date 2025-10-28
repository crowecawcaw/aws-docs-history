# Create a connection using AWS Network Manager

Create a connection between two existing devices in your global network.

###### To create a connection

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Devices**, and choose
   the ID of the device.
5. Choose **Connections**, and then choose **Create
   connection**.
6. For **Name** and **Description**, enter
   a name and description for the connection.
7. (Optional) For **Link**, choose a link to associate with
   the first device in the connection.
8. For **Connected device**, choose the ID of the second
   device in the connection.
9. (Optional) For **Connected link**, choose a link to
   associate with the second device in the connection.
10. Choose **Create connection**.

###### To create a connection using the AWS CLI

Use the [create-connection](../../../cli/latest/reference/networkmanager/create-connection.md "../../../cli/latest/reference/networkmanager/create-connection.md") command.
