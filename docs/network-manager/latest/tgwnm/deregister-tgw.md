# Deregister a transit gateway using AWS Network Manager

Deregister a transit gateway from a global network using either the Network Manager console or using the CLI.
Once deregistered, you can re-register this transit gateway with the same global network or with
a different global network.

###### To deregister a transit gateway

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Transit gateways**.
5. Select your transit gateway, and choose
   **Deregister**.

###### To deregister a transit gateway using the AWS CLI

Use the [deregister-transit-gateway](../../../cli/latest/reference/networkmanager/deregister-transit-gateway.md "../../../cli/latest/reference/networkmanager/deregister-transit-gateway.md") command.
