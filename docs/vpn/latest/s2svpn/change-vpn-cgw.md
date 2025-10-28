# Change the customer gateway for an AWS Site-to-Site VPN connection

You can change the customer gateway of your Site-to-Site VPN connection by using the Amazon VPC console or a
command line tool.

After you change the customer gateway, your VPN connection will be temporarily
unavailable for a brief period while we provision the new endpoints.

###### To change the customer gateway using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN connections**.
3. Select the VPN connection.
4. Choose **Actions**, **Modify VPN connection**.
5. For **Target type**, choose **Customer gateway**.
6. For **Target customer gateway**, choose the new customer gateway.
7. Choose **Save changes**.

###### To change the customer gateway using the command line or API

- [ModifyVpnConnection](../../../AWSEC2/latest/APIReference/API_ModifyVpnConnection.md "../../../AWSEC2/latest/APIReference/API_ModifyVpnConnection.md") (Amazon EC2 Query API)
- [modify-vpn-connection](../../../cli/latest/reference/ec2/modify-vpn-connection.md "../../../cli/latest/reference/ec2/modify-vpn-connection.md") (AWS CLI)
