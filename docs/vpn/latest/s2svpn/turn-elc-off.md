

# Turn AWS Site-to-Site VPN tunnel endpoint lifecycle control off
<a name="turn-elc-off"></a>

If you no longer want to use the tunnel endpoint lifecycle control feature, you can turn it off using the AWS Management Console or the AWS CLI. When you turn off this feature, AWS will automatically deploy maintenance updates periodically, and these updates might happen during your business hours. To avoid any business impact, we highly recommend that you configure both tunnels in your VPN connection for high availability.

**Note**  
While there is an available pending maintenance, you cannot specify the **skip tunnel replacement** option while turning the feature off. You can always turn the feature off without using the **skip tunnel replacement** option, but AWS will automatically deploy the available pending maintenance updates by initiating a tunnel endpoint replacement immediately.

**To turn off tunnel endpoint lifecycle control using the AWS Management Console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the left-side navigation pane, choose **Site-to-Site VPN Connections**.

1. Select the appropriate connection under **VPN connections**.

1. Choose **Actions**, then **Modify VPN tunnel options**.

1. Select the specific tunnel that you want to modify by choosing the appropriate **VPN tunnel outside IP address**.

1. To turn off tunnel endpoint lifecycle control, under **Tunnel Endpoint Lifecycle Control**, clear the **Enable** check box.

1. (Optional) Select **Skip tunnel replacement**.

1. Choose **Save changes**.

**To turn off tunnel endpoint lifecycle control using the AWS CLI**  
Use the [modify-vpn-tunnel-options](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpn-tunnel-options.html) command to turn off tunnel endpoint lifecycle control.