

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Troubleshoot SSO and authentication issues
<a name="troubleshoot-sso"></a>

This section helps administrators troubleshoot single sign-on (SSO) and authentication issues with AWS Wickr. If the steps in this section don't resolve your issue, open a case in the [AWS Support Center](https://console.aws.amazon.com/support/home).

**Important**  
Wickr supports **OpenID Connect (OIDC) only**. SAML-based identity providers are not supported. If your organization uses a SAML-only identity provider, you must configure an OIDC-compatible alternative or implement an OIDC bridge.

**Topics**
+ [Before you begin](#troubleshoot-sso-before)
+ [Common SSO issues](#troubleshoot-sso-common)
+ [Additional resources](#troubleshoot-sso-more-info)

## Before you begin
<a name="troubleshoot-sso-before"></a>

Verify the following before troubleshooting:
+ You have administrator access to the Wickr Admin Console.
+ You have access to your organization's identity provider (IdP) configuration.
+ SSO is enabled in your Wickr network settings.
+ Your identity provider is OIDC-compliant. Wickr does not support SAML.

## Common SSO issues
<a name="troubleshoot-sso-common"></a>

### Supported identity providers
<a name="troubleshoot-sso-supported"></a>

Wickr provides configuration guidance for the following OIDC-compliant identity providers:
+ Microsoft Entra ID (formerly Azure AD)
+ Okta
+ Amazon Cognito
+ AWS Identity and Access Management Identity Center

Any OIDC-compliant identity provider can be used with Wickr. For providers not listed above, use the general OIDC configuration parameters in the [ Configure SSO](https://docs.aws.amazon.com/wickr/latest/adminguide/configure-sso.html) documentation.

### Users cannot sign in with SSO
<a name="troubleshoot-sso-users-cant-sign-in"></a>

When users report they cannot sign in using SSO, work through the following checks.

#### Verify Wickr SSO configuration
<a name="troubleshoot-sso-verify-config"></a>

1. In the Wickr Admin Console, choose **Network Settings**, then **Single Sign-On**.

1. Confirm SSO is enabled.

1. Verify the **Issuer URL**, **Client ID**, and **Client Secret** match your identity provider configuration.

1. Verify the **Redirect URI** in your identity provider matches the value shown in the Wickr Admin Console.

#### Common SSO errors
<a name="troubleshoot-sso-common-errors"></a>

"User not found"  
The user does not exist in your identity provider or has not been assigned to the Wickr application. Verify the user exists in your IdP and has the correct group assignments.

"Invalid response" or "Configuration error"  
The OIDC metadata or endpoints are misconfigured. Verify the Issuer URL, Client ID, and redirect URIs match between Wickr and your identity provider.

"Access denied"  
The user lacks the required group membership or application assignment in your identity provider. Check your IdP's application assignment settings.

User not prompted for Company ID  
If users are not prompted to enter a Company ID during SSO registration, verify the Company ID is configured in **Network Settings**, **Network Profile** in the Wickr Admin Console.

### Determine if the issue is with Wickr or your identity provider
<a name="troubleshoot-sso-determine-scope"></a>

Use the following questions to determine where the issue lies:
+ **Can users authenticate to other applications using the same IdP?** If no, the issue is with your identity provider, not Wickr.
+ **Are all users affected, or only specific users?** If only specific users, check their group assignments and application access in your IdP.
+ **Were there recent changes to your IdP configuration?** Certificate rotations, policy changes, or endpoint updates can break the OIDC connection.
+ **Does the error occur in the Wickr client or in the IdP login page?** If the error appears on the IdP login page, the issue is with your identity provider.

## Additional resources
<a name="troubleshoot-sso-more-info"></a>
+ [ Configure SSO in AWS Wickr](https://docs.aws.amazon.com/wickr/latest/adminguide/configure-sso.html)
+ [ Microsoft Entra ID SSO setup](https://docs.aws.amazon.com/wickr/latest/adminguide/entra-ad-sso.html) (includes Entra-specific troubleshooting)