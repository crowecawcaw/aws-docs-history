# Change the Secrets Manager pre-shared key in AWS Site-to-Site VPN

If your tunnel is inaccessible in Secrets Manager, you can change the pre-shared key for
that tunnel.

###### Note

- When changing the pre-shared key, ensure you have the necessary IAM
  permissions for both the Secrets Manager service.
- After changing the pre-shared key for a VPN tunnel, connectivity is
  interrupted for up to several minutes. Ensure that you plan for expected
  downtime.

###### To change the Secrets Manager pre-shared key for a VPN tunnel

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN connections**.
3. Select the Site-to-Site VPN connection, and choose **Actions**, **Modify VPN
   tunnel options**.
4. For **VPN tunnel outside IP address**, choose the tunnel endpoint
   IP of the VPN tunnel.
5. In the **New pre-shared key**, choose a new pre-shared
   key.

###### Note

This option is only available for keys stored in Secrets
Manager. 6. Choose **Save changes**. 7. Repeat these steps for any other tunnel.
