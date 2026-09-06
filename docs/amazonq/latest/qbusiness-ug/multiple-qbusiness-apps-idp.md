

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting multiple Amazon Q Business applications to an Identity Provider
<a name="multiple-qbusiness-apps-idp"></a>

You can connect multiple Amazon Q Business custom applications to a single SAML 2.0 or OIDC based identity provider (IdP) application. Connecting multiple Amazon Q Business applications to a single identity provider enables end users access Amazon Q Business with all their web-based tools and services through a single sign-on (SSO) provided by the IdP.

Most IdPs allow you to configure additional custom web applications alongside existing ones. In this section we use Okta as an example to show you the specific steps to configure a new custom application.

**Important**  
Amazon Q Business supports Microsoft Entra ID with SAML 2.0, but doesn't support OIDC for Google or Microsoft Entra ID.

**Topics**
+ [Using SAML](#multiple-qbusiness-apps-idp-saml)
+ [Using OIDC](#multiple-qbusiness-apps-idp-oidc)

## Using SAML
<a name="multiple-qbusiness-apps-idp-saml"></a>

In this section we use Okta as an example to show you the specific steps to configure a new custom application using SAML 2.0.

**To connect multiple Amazon Q Business custom applications to Okta**

1. Sign into Okta and go to the admin console.

1. In the left navigation pane, choose **Applications**, and then choose your existing SAML 2.0 application.

1. From **General**, choose **SAML settings**.

1. Keep your **General Settings** as is and select **Next**.

1. In **Edit SAML Integration**, for **SAML Settings**, under **General**, make sure you've already entered the **Single sign-on URL** and **Audience URI** for your first SAML application. For steps on how to do this, see [Create and configure an Okta application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html#create-iam-app-okta-1).

1. Then, from **General**, select **Show Advanced Settings**.

1. Scroll down to **Other Requestable SSO URLs** and select **Add Another**.

1. Then, add a **Single sign-on URL** for each additional SAML application you want to configure, and provide an index value for each. Example URL format: {{http://localhost:8000/saml}}.

1. Then, scroll down and select **Next**.

1. On the **Feedback** page, select **Finish**.

You're done with setting up your Okta application for multiple Amazon Q Business applications.

To make a request to this URI, you need to construct a SAML request in the following format:

```
<samlp:AuthnRequest 
    xmlns:samlp="{{urn:oasis:names:tc:SAML:2.0:protocol}}" 
    xmlns:saml="{{urn:oasis:names:tc:SAML:2.0:assertion}}" 
    ID="{{_uniqueID12345}}" 
    Version="{{2.0}}" 
    IssueInstant="{{2024-08-08T12:00:00Z}}" 
    ProtocolBinding="{{urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect}}" 
    Destination="{{https://idp-sso-url/sso}}"  
    AssertionConsumerServiceIndex="{{0}}"
    <saml:Issuer>{{https://sp.example.com/}}</saml:Issuer>
    <samlp:NameIDPolicy Format="{{urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified}}" AllowCreate="{{true}}"
</samlp:AuthnRequest>
```

Then, you send a SAML request to your to your custom web application's URI with index 0. The SAML request is usually sent via HTTP redirect, which requires the XML to be Base64 encoded. This can be done programmatically in various languages. For example, in JavaScript, you would do the following:

```
const samlRequest = '<samlp:AuthnRequest ...>...</samlp:AuthnRequest>'; // Your SAML request
const encodedRequest = btoa(samlRequest); // Base64 encoding
```

After encoding, redirect the user to the IdP with the following SAML request as parameter:

```
window.location.href = `https://idp.example.com/sso?SAMLRequest=$${encodedRequest}`;
```

## Using OIDC
<a name="multiple-qbusiness-apps-idp-oidc"></a>

You can configure multiple redirect URLs for a single OpenID Connect (OIDC) application. In this section we use Okta as an example to show you the specific steps to configure a new custom application using OIDC.

**To connect multiple Amazon Q Business custom applications to Okta**

1. Sign into Okta and go to the admin console.

1. From **General**, scroll down to **General Settings**, and then select **Edit**.

1. From **LOGIN**, for **Sign-in redirect URIs**, and then select **Edit**.

1. In **Sign-in redirect URIs**, choose **Add URI** to add multiple URIs. Then, select **Save**.

You're done with setting up your Okta application for multiple Amazon Q Business applications.