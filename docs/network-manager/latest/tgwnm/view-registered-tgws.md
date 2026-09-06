

# View registered transit gateways using AWS Network Manager
<a name="view-registered-tgws"></a>

View a transit gateway registered with your AWS global network using either the Network Manager console or using the CLI. 

**To access your registered transit gateways**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit gateways**.

1. The **Transit gateways** page lists your registered transit gateways. Choose the ID of transit gateway to view its details.

**To view your registered transit gateways using the AWS CLI**  
Use the [get-transit-gateway-registrations](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-transit-gateway-registrations.html) command.