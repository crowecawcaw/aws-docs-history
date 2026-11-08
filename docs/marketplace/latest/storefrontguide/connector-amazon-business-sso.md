

# Setting up Amazon Business SSO
<a name="connector-amazon-business-sso"></a>

Complete this page only if you want the Buy button to sign buyers in to Amazon Business with single sign-on (SSO).

If buyers sign in to Amazon Business themselves, skip to [Getting Amazon Business API credentials](connector-amazon-business-credentials.md).

Create a SAML application in your identity provider (IdP) that signs buyers in to Amazon Business. Then exchange metadata with Amazon Business to complete the SSO trust. Your IdP administrator and Amazon Business administrator complete these procedures together. Use the same IdP that you use for storefront sign-in.

**Identity providers for SSO**  
You can use any IdP that supports SAML 2.0 applications. This page uses Okta as the example. In another IdP, menu and setting names differ, so use the equivalent settings.

## Creating the Amazon Business application in your IdP
<a name="connector-amazon-business-sso-okta"></a>

**To create and configure the Amazon Business SAML application**

1. In the Okta Admin Console, open **Applications**, choose **Create App Integration**, select **SAML 2.0**, and then choose **Next**.

1. Enter **Amazon Business** as the **App name**, and then choose **Next** to continue to **Configure SAML**.

1. Configure the following values. To display the signing and encryption settings, choose **Show Advanced Settings**.


<table>
<thead>
  <tr><th>Setting</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td> <b>Single sign-on URL</b> </td><td>Amazon's HTTP-POST <b>AssertionConsumerService</b> <code>Location</code> from its service provider (SP) metadata. Copy the whole URL, including the query string. Its path contains <code>/bb/feature/sso/action/3p_redirect</code>. Amazon Business also shows this value as <b>SSO URL</b> on its <b>Amazon connection data</b> page.</td></tr>
  <tr><td> <b>Use this for Recipient URL and Destination URL</b> </td><td>Selected</td></tr>
  <tr><td> <b>Audience URI (SP Entity ID)</b> </td><td> <code>https://www.amazon.com</code>. Confirm that it matches the <code>entityID</code> in Amazon's metadata.</td></tr>
  <tr><td> <b>Default RelayState</b> </td><td>Leave empty.</td></tr>
  <tr><td> <b>Name ID format</b> </td><td> <b>Unspecified</b> </td></tr>
  <tr><td> <b>Application username</b> </td><td> <b>Email</b> </td></tr>
  <tr><td> <b>Update application username on</b> </td><td> <b>Create and update</b> </td></tr>
  <tr><td> <b>Response</b> / <b>Assertion Signature</b> </td><td> <b>Signed</b> / <b>Signed</b> </td></tr>
  <tr><td> <b>Signature Algorithm</b> / <b>Digest Algorithm</b> </td><td> <b>RSA-SHA256</b> / <b>SHA256</b> </td></tr>
  <tr><td> <b>Assertion Encryption</b> </td><td> <b>Encrypted</b>, using Amazon's SP encryption certificate (<b>Encryption Certificate</b>). Leave <b>Encryption Algorithm</b> and <b>Key Transport Algorithm</b> at the values that Okta shows.</td></tr>
</tbody>
</table>


   If Amazon's metadata isn't available yet, temporarily use `https://example.invalid/pending-amazon-acs` as the **Single sign-on URL** and keep the Amazon audience. Leave encryption at its initial setting until you get Amazon's certificate. Save the app so that you can download the IdP metadata. Then replace the temporary URL with Amazon's assertion consumer service (ACS) URL, and turn on encryption before you test.

1. Choose **Next**, continue past the optional **Feedback** page, and choose **Finish**.

**To add the attribute statements**
+ On the **Sign On** tab, open **Show legacy configuration**. Next to **Profile attribute statements**, choose **Edit**. Add the following rows, and then choose **Save**.


<table>
<thead>
  <tr><th>Name</th><th>Name format</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td> <code>email</code> </td><td> <b>Unspecified</b> </td><td> <code>user.email</code> </td></tr>
  <tr><td> <code>firstName</code> </td><td> <b>Unspecified</b> </td><td> <code>user.firstName</code> </td></tr>
  <tr><td> <code>lastName</code> </td><td> <b>Unspecified</b> </td><td> <code>user.lastName</code> </td></tr>
</tbody>
</table>


**To assign users and download the identity provider metadata**

1. On the **Assignments** tab, assign the same test user and buyer groups that you assigned to the storefront application. Keep each application username equal to the user's email address.

1. On the **Sign On** tab, in the **Settings** section, download the **Identity Provider metadata** as XML. Give this file to your Amazon Business administrator.

## Configuring SSO in Amazon Business
<a name="connector-amazon-business-sso-configure"></a>

**To configure Amazon Business SSO**

1. In the intended business account, open **Business Settings** > **System integrations** > **Single Sign-On**.

1. Choose **Set up SSO**, and configure the following:


<table>
<thead>
  <tr><th>Setting</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td> <b>Identity provider</b> </td><td>Your IdP. In this example, choose <b>Okta</b>.</td></tr>
  <tr><td> <b>Default Group</b> </td><td>Your intended group for newly provisioned SSO buyers. Search for it under <b>Select a default group</b>.</td></tr>
  <tr><td> <b>Default Buying Role</b> </td><td> <b>Buyer</b> (some setup versions call this <i>Requisitioner</i>). Don't choose <b>Punchout user</b>; it's a different purchasing flow.</td></tr>
</tbody>
</table>


1. Choose **Next**. Under **Upload your metadata file**, choose **Upload XML File**, choose **Browse**, select the IdP metadata file for the Amazon Business application, and then choose **Upload**.

1. Review **Connection data**. The **EntityID**, **IssuerUrl**, **HTTP-Redirect** and **HTTP-Post** endpoints, and **Signing Certificate Public Key** must all come from the Amazon Business application in your IdP. Don't use values from the AWS Marketplace Storefront application. Choose **Next**.

1. Set **Attribute mapping** as follows, and then choose **Next**. Check that each **SAML AttributeName** matches the attribute name in your IdP exactly, including capitalization.


<table>
<thead>
  <tr><th>Amazon data</th><th>SAML AttributeName</th></tr>
</thead>
<tbody>
  <tr><td> <b>Email</b> </td><td> <code>email</code>. Also select <b>Email</b> as <b>Unique Id</b>. The page might combine these as <b>Email &amp; Unique ID</b>.</td></tr>
  <tr><td> <b>First Name</b> </td><td> <code>firstName</code> </td></tr>
  <tr><td> <b>Last Name</b> </td><td> <code>lastName</code> </td></tr>
</tbody>
</table>


1. On **Amazon connection data**, download the SP metadata (**Metadata XML file**) and the **Amazon SSO Certificate**. Leave the confirmation check box cleared until you save these values in your IdP.

**To update the IdP application and confirm the setup**

1. In Okta, open the **Amazon Business** application. On the **General** tab, next to **SAML Settings**, choose **Edit**, and then choose **Next**. Replace any temporary **Single sign-on URL** with Amazon's exact HTTP-POST ACS (the **SSO URL** on the **Amazon connection data** page). Confirm the audience, the **Unspecified** Name ID format, and the signed response and assertion settings.

1. Set **Assertion Encryption** to **Encrypted**, and upload Amazon's SP encryption certificate as the **Encryption Certificate**. This certificate is different from the IdP signing certificate that Amazon received. Choose **Next**, and then choose **Finish**.

1. Recheck the three saved attribute statements. To confirm the buyer's email NameID and the populated `email`, `firstName`, and `lastName` attributes, choose **Preview the SAML Assertion**.

1. Return to Amazon Business. Select **I confirm that Amazon's metadata has been configured on my IDP**, and then choose **Continue**. Review **SSO Connection Details** and the **Testing** status.

## Testing with a clean browser
<a name="connector-amazon-business-sso-test"></a>

**To test Amazon Business SSO**

1. Open a new private browser window with no existing Amazon session. Sign in to your IdP as your assigned test buyer and complete multi-factor authentication (MFA).

1. In that window, start sign-in from the Amazon Business application in your IdP. In Okta, open the application's **General** > **App Embed Link**.

1. Verify that you reach the intended Amazon Business account as that buyer, with the expected group and role. If Amazon requests an account link, merge, or conversion, have the account owner review the choice before you continue.

1. Return to the Amazon Business SSO page. A successful test shows **Testing verified** and makes **Activate** available.

## Activating SSO
<a name="connector-amazon-business-sso-activate"></a>

**Activate only when you're ready**  
Activation is account-wide and is your final SSO go-live step. To turn SSO off after activation, you must contact Amazon Business support. Don't use activation as a troubleshooting step.

You can finish the connector and storefront setup while Amazon Business SSO remains in **Testing**.

**To activate Amazon Business SSO**

1. Confirm that your buyer assignments, storefront sign-in, and support arrangements are ready.

1. On the Amazon Business SSO page, choose **Activate**, and then complete Amazon's confirmation.

1. Revisit the SSO page and copy its current sign-in link. You need this link when you configure the connector.

After activation, Amazon Business reports SSO as active. A **Testing** status alone doesn't establish that the test or activation succeeded.

## Related topics
<a name="connector-amazon-business-sso-related"></a>
+  [Amazon Business connector](connector-amazon-business.md) 
+  [Configuring SAML 2.0 sign-in](sso-storefront.md#sso-storefront-saml) 
+  [Configuring the Amazon Business connector](connector-amazon-business-configure.md) 