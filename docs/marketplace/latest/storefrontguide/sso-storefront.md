

# Setting up single sign-on for a storefront
<a name="sso-storefront"></a>

You can enable single sign-on (SSO) so that buyers sign in to a storefront with your identity provider. AWS Marketplace Storefront supports Okta and Microsoft Entra ID through OpenID Connect (OIDC). It also supports any SAML 2.0 identity provider, such as Okta.

For Amazon Business Buy button sign-in with SSO, use SAML 2.0 with the same identity provider that you use for Amazon Business. For more information, see [Amazon Business connector](connector-amazon-business.md).

## Configuring OIDC sign-in with Okta or Microsoft Entra ID
<a name="sso-storefront-oidc"></a>

**To configure storefront SSO with OIDC**

1. Open the storefront, and then choose the **SSO Configuration** tab.

1. Turn on **Enable SSO**.

1. For **Identity Provider**, choose **OKTA** or **Azure Entra ID**.

1. Enter the **Client ID** and **Client Secret** from your identity provider application.

1. For Okta, enter the **Domain**. For Microsoft Entra ID, enter the **Tenant ID**.

1. Choose **Save**.

1. To verify the configuration, choose **Test Connection**.

## Configuring SAML 2.0 sign-in
<a name="sso-storefront-saml"></a>

Use the following procedures to set up storefront buyer sign-in with a SAML 2.0 application in your identity provider (IdP). You can use any IdP that supports SAML 2.0 applications. These procedures use Okta as the example. In another IdP, menu and setting names differ, so use the equivalent settings.

If your storefront already has working SAML sign-in through the intended IdP, confirm the user assignments and run the sign-in test at the end.

**SAML 2.0 availability**  
If **SAML 2.0** or **IdP Configuration Values** isn't available on the **SSO Configuration** tab, contact [awsmp-storefront-support@amazon.com](mailto:awsmp-storefront-support@amazon.com).

### Creating the storefront application in your IdP
<a name="sso-storefront-saml-okta-app"></a>

**To create the storefront SAML application**

1. Sign in to the Okta Admin Console. Open **Applications and Resources** > **Applications**. (Some Okta versions name the parent menu **Applications**.)

1. Choose **Create App Integration**. In the **Create app integration** dialog box, under **Sign-in method**, select **SAML 2.0**, and then choose **Next**.

1. On **General Settings**, enter **AWS Marketplace Storefront** as the **App name**, and then choose **Next** to continue to **Configure SAML**.

1. Enter the following initial settings. To display the signing controls, choose **Show Advanced Settings**.


<table>
<thead>
  <tr><th>Setting</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td> <b>Single sign-on URL</b> </td><td>Temporarily use <code>https://example.invalid/pending-storefront-acs</code>.</td></tr>
  <tr><td> <b>Use this for Recipient URL and Destination URL</b> </td><td>Selected</td></tr>
  <tr><td> <b>Audience URI (SP Entity ID)</b> </td><td>Temporarily use <code>https://example.invalid/pending-storefront-audience</code>.</td></tr>
  <tr><td> <b>Default RelayState</b> </td><td>Leave empty.</td></tr>
  <tr><td> <b>Name ID format</b> </td><td> <b>Unspecified</b> </td></tr>
  <tr><td> <b>Application username</b> </td><td> <b>Email</b> </td></tr>
  <tr><td> <b>Update application username on</b> </td><td> <b>Create and update</b> </td></tr>
  <tr><td> <b>Response</b> / <b>Assertion Signature</b> </td><td> <b>Signed</b> / <b>Signed</b> </td></tr>
  <tr><td> <b>Signature Algorithm</b> / <b>Digest Algorithm</b> </td><td> <b>RSA-SHA256</b> / <b>SHA256</b> </td></tr>
  <tr><td> <b>Assertion Encryption</b> </td><td>Keep the default, <b>Unencrypted</b>.</td></tr>
</tbody>
</table>

**Temporary values**  
AWS Marketplace Storefront creates your sign-in connection after you save your IdP's sign-in URL and signing certificate. You then copy the generated **ACS URL** and **Audience** back into your IdP. The temporary values only let you create the app. Replace both before you test sign-in.

1. Choose **Next**, continue past the optional **Feedback** page, and choose **Finish**.

**To add attributes, assign users, and get the sign-in details**

1. On the app's **Sign On** tab, open **Show legacy configuration**. Next to **Profile attribute statements**, choose **Edit**. Add the following rows (choose **Add Another** for the second row), and then choose **Save**.


<table>
<thead>
  <tr><th>Name</th><th>Name format</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td> <code>email</code> </td><td> <b>Unspecified</b> </td><td> <code>user.email</code> </td></tr>
  <tr><td> <code>name</code> </td><td> <b>Unspecified</b> </td><td> <code>user.displayName</code> </td></tr>
</tbody>
</table>


   Storefront sign-in requires both email and name. Populate each user's email and display name in your IdP. In Okta, use the legacy attribute grid instead of **Add expression**.

1. On the **Assignments** tab, choose **Assign**, and then choose **Assign to People** or **Assign to Groups**. Assign your test user and buyer groups, and verify that each application username is the user's email. For a person, choose **Save and Go Back**, and then choose **Done**.

1. On the **Sign On** tab, copy the app's **Sign-On URL** and download its active **SHA-2** signing certificate. Use the complete PEM certificate, including its `BEGIN` and `END` lines.

### Saving the connection in AWS Marketplace Storefront
<a name="sso-storefront-saml-save"></a>

**To save the SAML connection**

1. Open the storefront, and then choose the **SSO Configuration** tab.

1. Turn on **Enable SSO**. For **Identity Provider**, choose **SAML 2.0**, and then enter the following values:


<table>
<thead>
  <tr><th>Setting</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td> <b>IdP sign-in URL</b> </td><td>The sign-in URL of the <i>AWS Marketplace Storefront</i> application in your IdP. In Okta, this is the <b>Sign-On URL</b>. Required.</td></tr>
  <tr><td> <b>IdP signing certificate (PEM)</b> </td><td>That application's complete active signing certificate. Paste it, or choose <b>Upload PEM file</b>. Required.</td></tr>
</tbody>
</table>


1. Choose **Save**. Saving provisions the storefront sign-in connection. The message *SSO configuration updated* appears, and the new connection shows **Pending validation**.

1. Under **IdP Configuration Values**, copy the **ACS URL** and **Audience**.

**Copy the exact values**  
Copy the entire **ACS URL**, including its `connection` query parameter, and the entire **Audience**. Don't construct these values yourself.

### Finishing the IdP application and testing sign-in
<a name="sso-storefront-saml-finish"></a>

**To finish and test SAML sign-in**

1. Return to the *AWS Marketplace Storefront* application in your IdP. In Okta, on the **General** tab, next to **SAML Settings**, choose **Edit**. Keep the app name, and choose **Next** to continue to **Configure SAML**.

1. Replace the temporary values:


<table>
<thead>
  <tr><th>Setting</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td> <b>Single sign-on URL</b> </td><td>The exact <b>ACS URL</b> from AWS Marketplace Storefront. It has the form <code>https://auth-domain/login/callback?connection=connection-name</code>.</td></tr>
  <tr><td> <b>Recipient URL</b> / <b>Destination URL</b> </td><td>Keep <b>Use this for Recipient URL and Destination URL</b> selected.</td></tr>
  <tr><td> <b>Audience URI (SP Entity ID)</b> </td><td>The exact <b>Audience</b> from AWS Marketplace Storefront. It has the form <code>urn:auth0:tenant:connection-name</code>.</td></tr>
</tbody>
</table>


   Choose **Next**, and then choose **Finish**.

1. Verify the saved `email` and `name` attribute statements and the test user's assignment.

1. In AWS Marketplace Storefront, choose **Test Connection**. Allow the pop-up, sign in as a user who is assigned in your IdP, and complete your multi-factor authentication (MFA) requirements.

1. Return to **SSO Configuration**. Confirm that the status is **Connected** and that the **Last connection check** value updates. If needed, reopen the tab to refresh the status.

1. Open the hosted storefront as the assigned buyer and verify that sign-in reaches the correct storefront with the expected access.

A saved connection alone isn't a successful sign-in test. Both the connection test and the buyer's hosted storefront sign-in must succeed.

## Related topics
<a name="sso-storefront-related"></a>
+  [Deployment](storefronts-creating-deploying.md#deployment) 
+  [Setting up single sign-on for your organization](setting-up-sso.md) 
+  [Amazon Business connector](connector-amazon-business.md) 