

# Set up SSO federation for third-party applications
<a name="3p-apps-sso"></a>

With single sign-on (SSO), a user can federate into multiple third-party applications set up in the agent workspace, without having to authenticate separately for each application.

**Note**  
Your third-party application can complete the sign-in flow in an iframe if your identity provider supports iframing its sign-in page. See your identity provider's documentation for its iframing capabilities.

**Set up SSO for third-party applications in your Connect Customer instances**

1. Set up an identity provider, or use an existing one.

1. Set up users in the identity provider.

1. Set up a Connect Customer instance and [Configure SAML with IAM for Connect Customer](configure-saml.md).

1. Set up the other applications within your identity provider that you plan to integrate with your Connect Customer instance.

1. Attach each user identity to the applications in your identity provider that you integrate with your Connect Customer instance. To control which agents can access an application in the agent workspace, set application-specific permissions in security profiles. For more information, see [Assign permissions to use third-party applications](assign-security-profile-3p-apps.md).

1. After a user signs in to their identity provider, they can federate into their Connect Customer instance. If an application is set up for SSO, the user can also federate into it without entering a username and password.