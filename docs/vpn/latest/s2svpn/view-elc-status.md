# Verify if AWS Site-to-Site VPN tunnel endpoint lifecycle control is

enabled

You can verify whether tunnel endpoint lifecycle control is enabled on an existing
VPN tunnel by using the AWS Management Console or CLI.

- If tunnel endpoint lifecycle control is disabled, and you want to enable it see [Enable tunnel endpoint lifecycle control](enable-elc.md "enable-elc.md").
- If tunnel endpoint lifecycle control is enabled, and you want to disable it, see [Turn tunnel endpoint lifecycle control off](turn-elc-off.md "turn-elc-off.md").

###### To verify if tunnel endpoint lifecycle control is enabled using the

AWS Management Console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the left-side navigation pane, choose **Site-to-Site VPN
   Connections**.
3. Select the appropriate connection under **VPN
   connections**.
4. Select the **Tunnel details** tab.
5. In the tunnel details, look for **Tunnel Endpoint Lifecycle
   Control**, which will report whether the feature is
   **Enabled** or **Disabled**.

###### To verify if tunnel endpoint lifecycle control is enabled using the

AWS CLI

Use the [describe-vpn-connections](../../../cli/latest/reference/ec2/describe-vpn-connections.md "../../../cli/latest/reference/ec2/describe-vpn-connections.md") command to verify if tunnel endpoint
lifecycle control is enabled.
