# Setting up Amazon Quick on desktop for enterprise deployments

|                                           |
| ----------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition |

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

To use Amazon Quick on desktop for enterprise deployments, administrators must
configure enterprise single sign-on (SSO) so that users in the organization can sign in
with their corporate credentials. This setup connects your organization's OpenID Connect
(OIDC) compatible identity provider (IdP) to Amazon Quick.

###### Note

If you are using a Free or Plus account, this section does not apply to you.
Continue to [Getting started](getting-started-desktop.md "getting-started-desktop.md").

## How enterprise sign-in works

The Amazon Quick desktop application uses the OIDC protocol to authenticate users.
When you choose **Continue with SSO**, a browser window
opens to Amazon Quick. Amazon Quick identifies your configured identity
provider and redirects to your IdP's authorization endpoint. The application then
exchanges the resulting authorization code for tokens using Proof Key for Code
Exchange (PKCE).

To identify the configured identity provider, your browser must have an active
Amazon Quick web session. If no session exists, the browser prompts you to sign in
to Amazon Quick before the application redirects to your IdP.

Amazon Quick validates the token and maps the user to an identity in your account.
The email address in your IdP must exactly match the email address of the user
in Amazon Quick.

###### Note

If you sign in for the first time, the browser checks for an active
Amazon Quick web session. If no session exists, the browser opens the
Amazon Quick sign-in page instead of redirecting to your IdP. Sign in to
Amazon Quick in the browser to continue. The desktop application then completes
sign-in through your configured identity provider.

## Prerequisites

Before you begin, verify that you have the following:

- An AWS account with an active Amazon Quick subscription. The
  Amazon Quick account's home region (identity region) must be in a
  supported AWS Region. For a list of supported Regions, see
  [Supported AWS Regions for Amazon Quick](regions.md#regions-qs "regions.md#regions-qs"). All identity
  types are supported, including IAM Identity Center, IAM federation, and native Amazon Quick
  (username/password) users.
- Administrator access to your Amazon Quick account.
- Access to your IdP with permissions to create OIDC application
  registrations.
- In restricted network environments, the ability to reach the required
  Amazon Quick and identity provider domains. For the list of domains to add to
  your allow list, see [Network access and required domains](desktop-security.md#desktop-network-access "desktop-security.md#desktop-network-access").

###### Important

Amazon Quick on desktop is available for Enterprise accounts in
AWS Regions that support the full Amazon Quick feature set. Regions
that support Amazon Quick Sight capabilities only do not include desktop. For
the full list, see [Supported AWS Regions for Amazon Quick](regions.md#regions-qs "regions.md#regions-qs").

## Setup process

Setting up enterprise sign-in involves the same four steps regardless of which
identity provider you use:

1. **Create an OIDC application in your identity
   provider.** Register a public OIDC client and record its Client ID
   and OIDC endpoints. The steps and endpoint formats are specific to your
   identity provider.
2. **Add the extension access in the Amazon Quick administration console.** In the Amazon Quick administration console,
   add an extension access using the Client ID and OIDC endpoints from
   Step 1.
3. **Create the extension in the Amazon Quick console.** On the **Extensions** page
   in the Amazon Quick console, create the extension from the extension access
   you added in Step 2.
4. **Download, verify, and distribute the desktop
   application.** Download and install the application, choose
   **Continue with SSO** to confirm that
   authentication succeeds, and then direct your users to download and sign
   in.

The complete procedure for each of these steps is documented on the page for your
identity provider. Choose your identity provider to get started:

- [Microsoft Entra ID](desktop-enterprise-entra-id.md "desktop-enterprise-entra-id.md") – Microsoft Entra
  ID
- [Google
  Workspace](desktop-enterprise-google-workspace.md "desktop-enterprise-google-workspace.md") – Google
  Workspace
- [Okta](desktop-enterprise-okta.md "desktop-enterprise-okta.md") – Okta
- [Ping Identity](desktop-enterprise-ping-identity.md "desktop-enterprise-ping-identity.md") – Ping Identity
  (PingFederate and PingOne)

If you encounter problems during setup or sign-in, see [Troubleshooting enterprise sign-in for Amazon Quick on desktop](desktop-enterprise-setup-troubleshooting.md "desktop-enterprise-setup-troubleshooting.md").

###### Topics

- [Set up enterprise sign-in with Microsoft Entra ID for Amazon Quick on desktop](desktop-enterprise-entra-id.md "desktop-enterprise-entra-id.md")
- [Set up enterprise sign-in with Google Workspace for Amazon Quick on desktop](desktop-enterprise-google-workspace.md "desktop-enterprise-google-workspace.md")
- [Set up enterprise sign-in with Okta for Amazon Quick on desktop](desktop-enterprise-okta.md "desktop-enterprise-okta.md")
- [Set up enterprise sign-in with Ping Identity for Amazon Quick on desktop](desktop-enterprise-ping-identity.md "desktop-enterprise-ping-identity.md")
- [Troubleshooting enterprise sign-in for Amazon Quick on desktop](desktop-enterprise-setup-troubleshooting.md "desktop-enterprise-setup-troubleshooting.md")
