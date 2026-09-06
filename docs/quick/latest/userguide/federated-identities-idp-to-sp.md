

# Initiating sign-on from the identity provider (IdP)
<a name="federated-identities-idp-to-sp"></a>


|  | 
| --- |
|    Applies to: Enterprise Edition and Standard Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

**Note**  
IAM identity federation doesn't support syncing identity provider groups with Amazon Quick.

In this scenario, your users initiate the sign-on process from the identity provider's portal. After the users are authenticated, they sign in to Amazon Quick. After Quick checks that they are authorized, your users can access Quick. 

Beginning with a user signing into the IdP, authentication flows through these steps:

1. The user browses to `https://applications.example.com` and signs on to the IdP. At this point, the user isn't signed in to the service provider. 

1. The federation service and the IdP authenticate the user:

   1. The federation service requests authentication from the organization's identity store.

   1. The identity store authenticates the user and returns the authentication response to the federation service.

   1. When authentication is successful, the federation service posts the SAML assertion to the user’s browser.

1. The user opens Amazon Quick:

   1. The user's browser posts the SAML assertion to the AWS Sign-In SAML endpoint (`https://signin.aws.amazon.com/saml`). 

   1. AWS Sign-In receives the SAML request, processes the request, authenticates the user, and forwards the authentication token to the Amazon Quick service.

1. Amazon Quick accepts the authentication token from AWS and presents Amazon Quick to the user.

From the user's perspective, the process happens transparently. The user starts at your organization's internal portal and lands at an Amazon Quick application portal, without ever having to supply any AWS credentials.

In the following diagram, you can find an authentication flow between Amazon Quick and a third-party identity provider (IdP). In this example, the administrator has set up a sign-in page to access Amazon Quick, called `applications.example.com`. When a user signs in, the sign-in page posts a request to a federation service that complies with SAML 2.0. The end user initiates authentication from the sign-on page of the IdP.

![Quick SAML Diagram. The diagram contains two boxes. The first one describes an authentication process inside the enterprise. The second one describes authentication inside AWS. The process is described in the text following the table.](http://docs.aws.amazon.com/quick/latest/userguide/images/SAML-Flow-Diagram.png)


For information from some common providers, see the following third-party documentation:
+ CA – [Enabling SAML 2.0 HTTP Post Binding](https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/siteminder/12-7/configuring/partnership-federation/saml-2-0-only-configurable-features/enable-saml-2-0-http-post-binding.html)
+ Okta – [Planning a SAML deployment](https://developer.okta.com/docs/concepts/saml/)
+ Ping – [Amazon integrations](https://docs.pingidentity.com/bundle/integrations/page/kun1563994988131.html)

Use the following topics to understand using an existing federation with AWS:
+ [Identity federation in AWS](https://aws.amazon.com/identity/federation/) on the AWS website
+ [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*
+ [Enabling SAML 2.0 federated users to access the AWS Management Console](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html) in the *IAM User Guide*