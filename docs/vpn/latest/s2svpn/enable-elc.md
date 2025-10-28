# Enable AWS Site-to-Site VPN tunnel endpoint lifecycle control

Endpoint lifecycle control can be enabled on an existing or new VPN connection. This can be done using either the AWS Management Console or AWS CLI.

###### Note

By default when you turn on the feature for an existing VPN connection, a
tunnel endpoint replacement will be initiated at the same time. If you want to
turn the feature on, but not initiate an tunnel endpoint replacement
immediately, you can use the **skip tunnel replacement** option.

Existing VPN connection
The following steps demonstrate how to enable tunnel endpoint
lifecycle control on an existing VPN connection.

###### To enable tunnel endpoint lifecycle control using the

AWS Management Console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the left-side navigation pane, choose **Site-to-Site VPN
   Connections**.
3. Select the appropriate connection under **VPN
   connections**.
4. Choose **Actions**, then **Modify VPN
   tunnel options**.
5. Select the specific tunnel that you want to modify by choosing
   the appropriate **VPN tunnel outside IP
   address**.
6. Under **Tunnel Endpoint Lifecycle Control**,
   select the **Enable** check box.
7. (Optional) Select **Skip tunnel
   replacement**.
8. Choose **Save changes**.

###### To enable tunnel endpoint lifecycle control using the

AWS CLI

Use the [modify-vpn-tunnel-options](../../../cli/latest/reference/ec2/modify-vpn-tunnel-options.md "../../../cli/latest/reference/ec2/modify-vpn-tunnel-options.md") command to turn on tunnel
endpoint lifecycle control.

New VPN connection
The following steps demonstrate how to enable tunnel endpoint
lifecycle control during creation of a new VPN connection.

###### To enable tunnel endpoint lifecycle control during creation of a

new VPN connection using the AWS Management Console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN
   Connections**.
3. Choose **Create VPN connection**.
4. In the sections for **Tunnel 1 options** and
   **Tunnel 2 options**, under
   **Tunnel Endpoint Lifecycle Control**,
   select **Enable**.
5. Choose **Create VPN Connection**.

###### To enable tunnel endpoint lifecycle control during creation of a

new VPN connection using the AWS CLI

Use the [create-vpn-connection](../../../cli/latest/reference/ec2/create-vpn-connection.md "../../../cli/latest/reference/ec2/create-vpn-connection.md") command to turn on tunnel
endpoint lifecycle control.
