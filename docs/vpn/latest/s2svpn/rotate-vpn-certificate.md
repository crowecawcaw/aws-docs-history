# Rotate AWS Site-to-Site VPN tunnel endpoint certificates

You can rotate the certificates on the tunnel endpoints on the AWS side by using the Amazon VPC
console. When a tunnel endpoint’s certificate is close to expiration, AWS automatically
rotates the certificate using the service-linked role. For more information, see [Service-linked
roles for Site-to-Site VPN](security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service-linked "security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service-linked").

###### To rotate the Site-to-Site VPN tunnel endpoint certificate using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN connections**.
3. Select the Site-to-Site VPN connection, and then choose **Actions**,
   **Modify VPN tunnel certificate**.
4. Select the tunnel endpoint.
5. Choose **Save**.

###### To rotate the Site-to-Site VPN tunnel endpoint certificate using the AWS CLI

Use the [modify-vpn-tunnel-certificate](../../../cli/latest/reference/ec2/modify-vpn-tunnel-certificate.md "../../../cli/latest/reference/ec2/modify-vpn-tunnel-certificate.md") command.
