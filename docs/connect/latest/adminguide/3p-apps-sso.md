# Set up SSO Federation for third-party apps in your

Amazon Connect instance

A user can use Single-Sign-On to federate into multiple third-party applications
that have been setup within their Amazon Connect instance without the need to
authenticate separately for each application.

###### Note

Your third-party (3P) application can seamlessly complete the Sign-On flow
within an iframe, provided that the Identity Provider supports iframing their
sign-in page. Refer to the Identity Provider guides for detailed information on
iframing capabilities.

###### Setup SSO for third-party apps that exist within your Amazon Connect

instances

1. Set up an Identity Provider or use an existing Identity Provider.
2. Set up users within the Identity Provider.
3. Set up an Amazon Connect instance and [Configure SAML with IAM for Amazon Connect](configure-saml.md "configure-saml.md").
4. Set up other applications within your Identity Provider which you will be
   integrating with your Amazon Connect instance.
5. Attach each individual user identity to any applications within the
   Identity Provider that will be integrated with your Amazon Connect instance. You can
   control which agent has access to an application on the Amazon Connect agent
   workspace by providing more granular application specific permissions in
   security profiles. For more information, see [Security profile permissions for
   using third-party applications in Amazon Connect](assign-security-profile-3p-apps.md "assign-security-profile-3p-apps.md").
6. After a user has signed into their Identity Provider, they can federate
   into their Amazon Connect instance which has third-party applications configured and
   they can federate into each application (if the application has been setup
   for SSO) without the need of their username and password.
