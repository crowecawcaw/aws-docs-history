AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Configure authentication for Gapwalk applications

To configure OAuth2 authentication for your Gapwalk application, you need to set up an identity provider (IdP) and integrate it with your application.
This guide covers the steps for using Amazon Cognito or Keycloak as your IdP.
With Amazon Cognito, you can update your application's configuration file with the Cognito user pool details.
With Keycloak, you can control access to your application's APIs and resources based on the user's assigned roles.

###### Topics

- [Configure Gapwalk OAuth2 authentication with Amazon Cognito](ba-runtime-auth-cognito.md "ba-runtime-auth-cognito.md")
- [Configure Gapwalk OAuth2 authentication with
  Keycloak](ba-runtime-auth-keycloak.md "ba-runtime-auth-keycloak.md")
