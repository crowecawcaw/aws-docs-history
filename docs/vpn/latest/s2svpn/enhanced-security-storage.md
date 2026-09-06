

# Change the pre-shared key storage mode in AWS Site-to-Site VPN
<a name="enhanced-security-storage"></a>

Change the pre-shared key storage mode for an existing VPN tunnel.

**Note**  
When changing storage modes, ensure you have the necessary IAM permissions for both the Site-to-Site VPN and Secrets Manager services.
After changing the storage mode for a VPN tunnel, connectivity is interrupted for up to several minutes. Ensure that you plan for expected downtime.

**To change the pre-shared key storage mode**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Site-to-Site VPN connections**.

1. Select the Site-to-Site VPN connection, and choose **Actions**, **Modify VPN tunnel options**.

1. For **VPN tunnel outside IP address**, choose the tunnel endpoint IP of the VPN tunnel.

1. Under **Pre-shared key storage**, choose one of the following pre-shared key storage types.
   + **Standard** — The pre-shared key is stored directly in the Site-to-Site VPN service.
   + **Secrets Manager ** — The pre-shared key is stored using AWS Secrets Manager. For more information about Secrets Manager, see [Enhanced security features using Secrets Manager](enhanced-security.md).

1. Choose **Save changes**.

When changing the storage mode from Secrets Manager to Standard:
+ The pre-shared key is removed from Secrets Manager and moved to the Site-to-Site VPN service.
+ The tunnel's entry is removed from the Secrets Manager secret.

When changing the storage mode from Standard to Secrets Manager:
+ The pre-shared key is removed from the Site-to-Site VPN service 
+ A new Secrets Manager secret is created, if one doesn't already exist.
+ The new pre-shared key is stored in Secrets Manager.