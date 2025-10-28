# Getting started with user pools

You have an application that requires authentication and access control. You can work within
the OpenID Connect (OIDC) framework for single sign-on (SSO). Amazon Cognito has tools for handling the
logic of authentication in the application back end with an AWS SDK, and for invoking a
browser in your client to access a managed authorization server.

The Amazon Cognito console guides you through the creation of a user pool from the view of your
preferred application framework. From there, you can continue on to add features like federated
sign-in with external [social](tutorial-create-user-pool-social-idp.md "tutorial-create-user-pool-social-idp.md") or
[SAML 2.0](tutorial-create-user-pool-saml-idp.md "tutorial-create-user-pool-saml-idp.md") identity providers (IdPs).
The application models in the Amazon Cognito console lean on the addition of OIDC libraries to your
project and invoking a browser.

As you work to expand your feature set and incorporate more components of Amazon Cognito, read the
[Amazon Cognito user pools](cognito-user-pools.md "cognito-user-pools.md") chapter for full descriptions of everything
you can do with user pools.

The examples in this chapter and in the Amazon Cognito console demonstrate a basic integration of
application resources with Amazon Cognito user pools. Later, you can adjust your user pool to use more of the
options that are available to you. Then you can update your application to adopt new features
and interact with IdPs.

If you don't want to use the [managed login pages](cognito-terms.md#terms-managedlogin "cognito-terms.md#terms-managedlogin"),
you can create an application with custom-built authentication interfaces using an AWS SDK or
AWS Amplify. Applications that you build in this way interact with the [user
pools API](../../../cognito-user-identity-pools/latest/APIReference/Welcome.md "../../../cognito-user-identity-pools/latest/APIReference/Welcome.md") and are suitable only for authenticating [local users](cognito-terms.md#terms-localuser "cognito-terms.md#terms-localuser"). Continue learning about this authentication model at [Other application
options](getting-started-user-pools-application-other-options.md "getting-started-user-pools-application-other-options.md").

###### Topics

- [Create a new application in the Amazon Cognito
  console](getting-started-user-pools-application.md "getting-started-user-pools-application.md")
- [Other application
  options](getting-started-user-pools-application-other-options.md "getting-started-user-pools-application-other-options.md")
- [Add more features and security options to your user
  pool](user-pool-next-steps.md "user-pool-next-steps.md")
