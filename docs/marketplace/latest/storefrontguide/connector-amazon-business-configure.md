

# Configuring the Amazon Business connector
<a name="connector-amazon-business-configure"></a>

Add the connector, enter the API credentials, and bind the connector to the storefront that receives Amazon Business products and prices. Unlike other connectors, the Amazon Business connector applies to one storefront.

**United States marketplace only**  
The Amazon Business connector connects to the United States Amazon Business marketplace. The connector has no region or marketplace setting. All catalog lookups and product imports made through this connection resolve against the US catalog.

**To add the Amazon Business connector**

1. In AWS Marketplace Storefront, in the top-right corner, choose your profile, and then choose **Organization Settings**. On the **Connectors** tab, choose **\+ Add Connector**, and then choose **Amazon Business**.

1. Enter the following values:


<table>
<thead>
  <tr><th>Setting</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td> <b>LWA client ID</b> </td><td>Your API application's LWA client ID. Required.</td></tr>
  <tr><td> <b>LWA client secret</b> </td><td>The matching client secret. Required.</td></tr>
  <tr><td> <b>Refresh token</b> </td><td>The refresh token from your business's authorization. Required.</td></tr>
  <tr><td> <b>Storefront</b> </td><td>The storefront that receives these products and prices. Imported listings and pricing appear only in this storefront.</td></tr>
  <tr><td> <b>Set up Amazon Business SSO (optional)</b> </td><td>Select this option only if you set up Amazon Business single sign-on (SSO). If you leave it cleared, buyers sign in to Amazon Business themselves after they choose the Buy button.</td></tr>
  <tr><td> <b>Amazon Business SSO login URL</b> </td><td>Appears when you select the SSO option. Paste the full sign-in start link from Amazon Business. It must be an HTTPS URL on an <code>amazon.com</code> host. Required when shown.</td></tr>
</tbody>
</table>


1. If you selected the SSO option, get the SSO login URL. In Amazon Business, open **Business Settings** > **System integrations** > **Single Sign-On**. Then copy the link that starts an SSO session. It has the following form:

   ```
   https://www.amazon.com/bb/feature/sso/action/start?domain_hint=...
   ```
**Use the SSO start link**  
Enter the `/sso/action/start?domain_hint=...` link in the connector. Don't paste the `/3p_redirect` assertion consumer service (ACS) URL. Also don't paste the app sign-in link from your identity provider (IdP), such as the Okta **App Embed Link**. The ACS receives a SAML assertion. It doesn't start buyer sign-in.

1. If you selected the SSO option, paste the complete link, keeping all supplied parameters. After activation, use the current link from Amazon Business if it has changed.

1. Choose **Test connection**. Wait for the *Connection successful* message. The **Status** changes from **Pending** to **Successful**, and **Save** becomes available.

1. Choose **Save**.

The connector list shows **Connected** and your storefront. This test verifies API access, not browser SSO. Catalog access and the Buy button work without the SSO option. Without it, a buyer who isn't signed in to Amazon Business signs in after choosing the Buy button.

**To update the connector**
**Re-enter all credentials**  
You can't resubmit masked saved values. When you update the connector, re-enter all three credentials.

1. Re-enter all three credentials.

1. Choose **Test connection**.

1. Choose **Update**.

## Related topics
<a name="connector-amazon-business-configure-related"></a>
+  [Getting Amazon Business API credentials](connector-amazon-business-credentials.md) 
+  [Adding Amazon Business products and the Buy button](connector-amazon-business-products.md) 
+  [Connector overview](connectors-overview.md) 