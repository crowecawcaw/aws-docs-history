This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Step 2: Configure your network

Complete the following procedure to access the AWS Management Console for Wickr, where you can add users,
add security groups, configure SSO, configure data retention, and additional network
settings.

1. On the **Networks** page, select the network name to navigate to that
   network.

You're redirected to the Wickr Admin Console for the selected network. 2. The following user management options are available. For more information about
configuring these settings, see [Manage your AWS Wickr network](managing-network.md "managing-network.md").

    * **Security Group** — Manage security groups and
     their settings, such as password complexity policies, messaging preferences, calling
     features, security features and external federation. For more information, see [Security groups for AWS Wickr](security-groups.md "security-groups.md") .
    * **Single Sign-on (SSO) Configuration** — Configure
     SSO and view the endpoint address for your Wickr network. Wickr supports SSO providers
     who use OpenID Connect (OIDC) only. Providers who use Security Assertion Markup Language
     (SAML) are not supported. For more information, see [Single sign-on configuration for
     AWS Wickr](sso-configuration.md "sso-configuration.md").
