# Controlling the interval for re-authenticating a SAML IdP token in Amazon WorkSpaces Secure Browser

When a user visits a WorkSpaces Secure Browser portal, they can sign in to launch a streaming session. Every
sessions begins on the start page, unless they sign in less than 5 minutes ago. The portal checks
for identity provider (IdP) tokens to determine whether to prompt the user for credentials when
it launches a session. A user without a valid IdP token must enter a user name, password, and
(optionally multifactor authentication (MFA) to launch a streaming session. If a user already
generated a SAML IdP token by signing into their IdP or an app protected by the same IdP, they
won't be asked for sign-in credentials.

If a user has a valid SAML IdP token, they can access WorkSpaces Secure Browser. You can control the interval
required for re-authenticating a SAML IdP token.

To control the interval for re-authenticating a SAML IdP token

1. Set the IdP timeout duration with your SAML IdP provider. We recommend configuring your
   IdP timeout duration with the shortest amount of time necessary for a user to complete their
   tasks.
   - For more information about Okta, see [Enforce a limited session lifetime for all policies](https://help.okta.com/en/prod/Content/Topics/Security/healthinsight/session-lifetime.htm "https://help.okta.com/en/prod/Content/Topics/Security/healthinsight/session-lifetime.htm").
   - For more information about Azure AD, see [Configuring authentication session controls](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/howto-conditional-access-session-lifetime#configuring-authentication-session-controls "https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/howto-conditional-access-session-lifetime#configuring-authentication-session-controls").
   - For more information about Ping, see [Sessions](https://docs.pingidentity.com/bundle/pingfederate-93/page/pqn1564002990312.html "https://docs.pingidentity.com/bundle/pingfederate-93/page/pqn1564002990312.html").
   - For more information about AWS IAM Identity Center, see [Set session duration](../../../singlesignon/latest/userguide/howtosessionduration.md "../../../singlesignon/latest/userguide/howtosessionduration.md").

2. Set your WorkSpaces Secure Browser portal's inactivity and idle timeout values. These values controls the
   amount of time between a user’s last interaction and when a WorkSpaces Secure Browser session ends due to
   inactivity. When a session ends, a user will lose their session state (including open tabs,
   unsaved web content, and history), and return to a fresh state at the start of the next
   session. For more information, see step 5 in [Creating a web portal for Amazon WorkSpaces Secure Browser](getting-started-step1.md "getting-started-step1.md").

###### Note

If a user's session times out but the user still has a valid SAML IdP token, they don't
have to enter their user name and password to start a new WorkSpaces Secure Browser session. To control how tokens
are re-authenticated, follow the guides in the previous step.
