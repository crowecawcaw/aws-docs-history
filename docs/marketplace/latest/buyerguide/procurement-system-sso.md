

# Configuring single sign-on for procurement system integration

You can enable single sign-on (SSO) for your AWS Marketplace procurement system integration so that users are automatically signed in using your organization's existing identity provider, without needing a separate AWS login. When enabled, users who access AWS Marketplace through your procurement system are redirected to your organization's SSO login page instead of the default AWS sign-in page. You enable SSO by passing your organization's SSO login portal URL as a query parameter in the punchout configuration.

**Note**  
This feature works with any identity provider that federates users into AWS, including IAM Identity Center, Okta, and Microsoft Entra ID.

## Prerequisites
<a name="procurement-system-sso-prereqs"></a>

Before you enable SSO for procurement system integration, you must have the following:
+ An active procurement system integration with AWS Marketplace. For setup instructions, see [Configuring AWS Marketplace to integrate with Coupa](procurement-system-integration-coupa.md) or [Configuring AWS Marketplace to integrate with SAP Ariba](procurement-system-integration-ariba.md).
+ An SSO login portal URL from your identity provider that authenticates users and lands them in an AWS session. For example, an IAM Identity Center access portal URL, an Okta SAML app URL, or any OIDC-compliant login URL configured to federate into AWS.
+ Administrative access to your procurement system (Coupa or SAP Ariba) to modify the punchout supplier URL.

## How SSO for procurement system integration works
<a name="procurement-system-sso-how-it-works"></a>

When you configure SSO for procurement system integration, the authentication flow works as follows:

1. A user in your procurement system initiates a punchout session. The procurement system sends the `start_url` parameter along with the PunchoutURL.

1. AWS Marketplace reads the `start_url` parameter and redirects the user to your organization's SSO login portal instead of the default AWS sign-in page.

1. The user authenticates through your organization's identity provider. This follows your organization's standard authentication policies, including any multi-factor authentication (MFA) requirements.

1. After authentication, your identity provider issues a session and the user is redirected back to the AWS Marketplace punchout session to browse and request products.

Use the `start_url` parameter to set where the buyer lands when the punchout session starts. It isn't a switch that turns SSO on and off. A session that has no usable value for it sends the buyer to the AWS Marketplace home page instead, where they sign in the default way.

## Step 1: Find your SSO login portal URL
<a name="procurement-system-sso-find-url"></a>

Obtain the SSO login portal URL from your identity provider. Consult your identity provider's documentation to find the direct login URL that initiates the SSO authentication flow and lands users in an AWS session after successful authentication.

**Example: IAM Identity Center**

1. Open the IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/).

1. In the navigation pane, choose **Settings**.

1. On the **Identity source** tab, locate the **AWS access portal URL**. Your URL looks similar to `https://d-1234567890.awsapps.com/start`.

**Example: Okta**

1. In the Okta Admin Console, choose **Applications**.

1. Select the application that federates your users into AWS.

1. On the **General** tab, copy the **Embed Link URL**, which is the application's SSO login URL.

## Step 2: Add the SSO URL to your punchout configuration
<a name="procurement-system-sso-add-parameter"></a>

How you configure the SSO URL depends on your procurement system.

**Coupa**  
In Coupa, navigate to **Setup** > **Punchout Sites** > select your punchout site, and update the **Punchout URL** field to append the `start_url` query parameter with your organization's SSO login portal URL.

**Example:**

```
https://eprocurement.marketplace.us-east-1.amazonaws.com/v1/punchout/setup?start_url=https://d-1234567890.awsapps.com/start
```

**SAP Ariba**  
For SAP Ariba, the punchout endpoint is managed on the AWS supplier account in the Ariba Network, so the `start_url` parameter cannot be self-configured. To enable SSO, contact [AWS Marketplace Support on the AWS website](https://aws.amazon.com/marketplace/help/contact-us) with your SSO login portal URL and request that the `start_url` parameter be added to your AWS Marketplace punchout configuration in the Ariba Network.

## Requirements and limitations
<a name="procurement-system-sso-requirements"></a>


| Requirement | Details | 
| --- | --- | 
| URL must federate into AWS | The SSO login URL must complete authentication and federate the user into an AWS session. URLs that authenticate users into non-AWS destinations are not supported. | 
| Parameter is optional | If the start\_url parameter is omitted, users land on the AWS Marketplace home page and sign in the default way. | 
| No domain validation | AWS Marketplace does not validate the domain in the URL parameter, and there is no list of permitted domains. The procurement administrator is responsible for providing the correct SSO login portal URL. | 
| Supported identity providers | Any identity provider that provides a direct login URL for SSO authentication to AWS, including IAM Identity Center, Okta, Microsoft Entra ID, and other SAML or OIDC-compliant providers. | 

For what to do when buyers don't reach your sign-in page, see [Single sign-on](procurement-system-troubleshooting.md#procurement-system-troubleshooting-sso).