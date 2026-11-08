

# Verifying and troubleshooting the Amazon Business connector
<a name="connector-amazon-business-verify"></a>

Test the buyer journey after you publish the storefront. If you use single sign-on (SSO), first configure storefront SAML sign-in, activate Amazon Business SSO, and enter the SSO login URL in the connector. For SSO, use a buyer account that's assigned in your identity provider (IdP).

## Verifying the buyer experience
<a name="connector-amazon-business-verify-buyer"></a>

**To verify the buyer experience**

1. Sign in to the hosted storefront as the test buyer.

1. Open an imported product, and check the details that Amazon Business supplies:


<table>
<thead>
  <tr><th>Detail</th><th>What to verify</th></tr>
</thead>
<tbody>
  <tr><td> <b>Price</b> </td><td>The imported Amazon Business offer price</td></tr>
  <tr><td> <b>List price and discount</b> </td><td>A list price comparison and discount, when supplied and applicable</td></tr>
  <tr><td> <b>Quantity tiers</b> </td><td>Prices or discounts for the displayed purchase quantities, when available</td></tr>
  <tr><td> <b>Other offers</b> </td><td>Available alternative sellers, prices, or conditions</td></tr>
</tbody>
</table>


1. Choose **Buy on Amazon Business**, or your custom label. Amazon opens in a new tab. With SSO, Amazon starts SSO, with the product as the return destination.

1. Confirm that you reach the intended Amazon Business account and product. Without SSO, sign in with the buyer's Amazon Business credentials. With SSO and an active session in the same IdP, an assigned buyer can continue without entering credentials again. Otherwise, complete sign-in or multi-factor authentication (MFA) as prompted.

1. To confirm the expected sign-in prompts and account access, repeat these steps in a new private window. You don't need to place an order to verify the handoff.

**Offer details vary**  
Not every product has a list price discount, quantity tiers, or other offers. Buyers review the current offer and complete purchases in Amazon Business.

## Troubleshooting
<a name="connector-amazon-business-troubleshooting"></a>

Use the following table to resolve common issues.


| Symptom | What to check | 
| --- | --- | 
|  **SAML 2.0** or the connection values are missing in AWS Marketplace Storefront | Confirm that you opened the storefront's **SSO Configuration** tab. To turn on SAML 2.0 for your storefront or to get its assertion consumer service (ACS) URL and Audience, contact [awsmp-storefront-support@amazon.com](mailto:awsmp-storefront-support@amazon.com). | 
| Storefront sign-in fails after saving | In your IdP, replace both temporary values with the exact storefront **ACS URL** and **Audience**. Keep the ACS `connection` query parameter. Confirm the active signing certificate and the populated `email` and `name` attribute statements. | 
|  **Test Connection** doesn't open or stays **Pending validation**  | Allow pop-ups, use an assigned active user, complete MFA, and reopen the **SSO Configuration** tab. Verify the buyer's email and access to the intended storefront. | 
| Your IdP reports that the user isn't assigned (in Okta, 403 or *user is not assigned*) | Assign the user or their group to the application that you're testing. For the full buyer journey, assign them to both SAML applications. | 
| Repeated redirects between your IdP and Amazon | In the Amazon Business application, use Amazon's exact `/3p_redirect` ACS and the audience `https://www.amazon.com`. If those are correct, retry in a private window with no existing Amazon session. | 
| Amazon shows 404 after the assertion | Set **Name ID format** to **Unspecified**, sign both the response and the assertion, and set **Assertion Encryption** to **Encrypted** with Amazon's service provider (SP) certificate. Recheck the ACS. | 
| Okta rejects `user.email` with *Invalid property email*  | Use **Sign On** > **Show legacy configuration** > **Profile attribute statements** > **Edit**, not **Add expression**. Use the correct attributes for each application. | 
| Certificate rejected | Use the complete PEM certificate, including the `BEGIN` and `END` lines. Your IdP's signing certificate goes to the service provider. Amazon's encryption certificate goes into the Amazon Business application in your IdP. | 
| Connector **Test connection** fails or **Save** is unavailable | Re-enter the matching Login with Amazon (LWA) client ID, client secret, and refresh token. Confirm authorization for the intended business. Choose **Test connection** before you save. | 
| The Buy button opens the consumer Amazon site | Without SSO, have the buyer sign in with their Amazon Business credentials. With SSO, confirm that Amazon Business SSO is active and that the connector uses the current `/sso/action/start?domain_hint=...` link. Also confirm that you assigned the buyer in the same IdP that you use for storefront sign-in. A product URL alone doesn't start business SSO. | 
| Publishing fails or the Buy setting is unavailable | Add a notification receiver, and confirm that you bound a **Connected** Amazon Business connector to this storefront. | 

If the issue continues, contact [awsmp-storefront-support@amazon.com](mailto:awsmp-storefront-support@amazon.com). Don't include credentials or certificates in your message.

## Related topics
<a name="connector-amazon-business-verify-related"></a>
+  [Amazon Business connector](connector-amazon-business.md) 
+  [Configuring SAML 2.0 sign-in](sso-storefront.md#sso-storefront-saml) 
+  [Setting up Amazon Business SSO](connector-amazon-business-sso.md) 