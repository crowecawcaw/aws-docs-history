

# Amazon Business connector
<a name="connector-amazon-business"></a>

Use the Amazon Business connector to offer Amazon Business products in your AWS Marketplace Storefront and send buyers to Amazon Business with a **Buy** button. When a buyer chooses the Buy button, the buyer signs in to Amazon Business in one of two ways:
+ Without single sign-on (SSO), buyers sign in to Amazon Business themselves with their Amazon Business credentials. You don't set up SSO.
+ With SSO, the Buy button signs buyers in to Amazon Business through your identity provider (IdP), so an assigned buyer doesn't enter credentials again. This option requires SAML 2.0 sign-in for your storefront and Amazon Business SSO, both through the same IdP.

**Identity providers for SSO**  
For the SSO option, you can use any IdP that supports SAML 2.0 applications. These procedures use Okta as the example. In another IdP, menu and setting names differ, so use the equivalent settings.

## What you set up
<a name="connector-amazon-business-components"></a>

You set up the following components.


| Component | What it does | 
| --- | --- | 
|  **AWS Marketplace Storefront** SAML application | SSO option only. Signs buyers in to your storefront with SAML 2.0. For instructions, see [Configuring SAML 2.0 sign-in](sso-storefront.md#sso-storefront-saml). | 
|  **Amazon Business** SAML application | SSO option only. Signs buyers in to Amazon Business with SAML 2.0. It has its own metadata, attributes, and certificate settings. | 
|  **Amazon Business SSO**  | SSO option only. Trusts the Amazon Business SAML application in your IdP for your business account. | 
|  **Amazon Business connector**  | Gives one storefront API access to Amazon Business products and prices. | 
|  **Buy** button | Sends buyers from a storefront product to the same product in Amazon Business. | 

For the SSO option, the two SAML applications are separate trusts. Don't reuse one for the other. The connector's API access is also separate from browser sign-in. A successful connector test doesn't prove that buyer SSO works. A successful SSO test doesn't prove that API access works.

## Prerequisites
<a name="connector-amazon-business-prerequisites"></a>

Before you begin, make sure that you have the following:
+ Access to your Amazon Business API application in the Solution Provider Portal, including its credentials and registered redirect URI. Business administrator access alone doesn't provide developer portal access.
+ An Amazon Business administrator who can authorize the API application for your business.
+ An AWS Marketplace Storefront organization **Owner** account with access to the storefront that you configure.
+ Your target storefront and the Amazon product identifiers (ASINs) that you want to offer.

For the SSO option, you also need the following:
+ An administrator for your IdP who can create SAML 2.0 applications and assign users or groups.
+ An Amazon Business administrator with access to **Business Settings** > **System integrations** > **Single Sign-On** and self-service SSO.
+ An active test user with a real email address, first name, last name, and display name populated in your IdP.
+ The same IdP for storefront buyer sign-in and Amazon Business sign-in, with the intended buyers assigned to both applications. In Okta, use the same Okta organization for both.

**Use the same IdP**  
With the SSO option, a shared IdP session lets an assigned buyer continue from your storefront into Amazon Business without entering credentials again. Your authentication policy still applies.  
Amazon Business supports one SSO identity provider for each business account. Coordinate with the current administrator before you replace an existing integration.

These procedures use Amazon Business in the US (`amazon.com`).

## Setup overview
<a name="connector-amazon-business-setup-overview"></a>

Complete these tasks in order:

1. If you use SSO, configure storefront sign-in with SAML 2.0. See [Configuring SAML 2.0 sign-in](sso-storefront.md#sso-storefront-saml).

1. If you use SSO, create the Amazon Business SAML application in your IdP, then configure and activate Amazon Business SSO. See [Setting up Amazon Business SSO](connector-amazon-business-sso.md).

1. Get the Amazon Business API credentials. See [Getting Amazon Business API credentials](connector-amazon-business-credentials.md).

1. Add the connector and bind it to a storefront. See [Configuring the Amazon Business connector](connector-amazon-business-configure.md).

1. Import products, choose the display template, turn on the Buy button, and publish. See [Adding Amazon Business products and the Buy button](connector-amazon-business-products.md).

1. Verify the buyer experience. See [Verifying and troubleshooting the Amazon Business connector](connector-amazon-business-verify.md).

For help, contact [awsmp-storefront-support@amazon.com](mailto:awsmp-storefront-support@amazon.com).

**Topics**
+ [What you set up](#connector-amazon-business-components)
+ [Prerequisites](#connector-amazon-business-prerequisites)
+ [Setup overview](#connector-amazon-business-setup-overview)
+ [Setting up Amazon Business SSO](connector-amazon-business-sso.md)
+ [Getting Amazon Business API credentials](connector-amazon-business-credentials.md)
+ [Configuring the Amazon Business connector](connector-amazon-business-configure.md)
+ [Adding Amazon Business products and the Buy button](connector-amazon-business-products.md)
+ [Verifying and troubleshooting the Amazon Business connector](connector-amazon-business-verify.md)