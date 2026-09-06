

# Deregister a transit gateway using AWS Network Manager
<a name="deregister-tgw"></a>

Deregister a transit gateway from a global network using either the Network Manager console or using the CLI. Once deregistered, you can re-register this transit gateway with the same global network or with a different global network.

**To deregister a transit gateway**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit gateways**. 

1. Select your transit gateway, and choose **Deregister**.

**To deregister a transit gateway using the AWS CLI**  
Use the [deregister-transit-gateway](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/deregister-transit-gateway.html) command.