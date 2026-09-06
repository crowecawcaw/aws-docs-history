

# Register a transit gateway using AWS Network Manager
<a name="register-tgw"></a>

Register a transit gateway created using Amazon Virtual Private Cloud with your AWS global network using either the Network Manager console or using the CLI. You cannot register a transit gateway with more than one global network.

**To register a transit gateway**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit gateways**., and then choose **Register transit gateway**.

1. (Optional) If your account is enabled for multi-account access, from the **Select account** dropdown list choose the account you want to register transit gateways from. 

   The **Select transit gateway to register** section populates with that account's transit gateways.

1. Choose one or more transit gateways, and then choose **Register transit gateway**.

**To register a transit gateway using the AWS CLI**  
Use the [register-transit-gateway](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/register-transit-gateway.html) command.