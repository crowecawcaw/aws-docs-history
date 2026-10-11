

# Choose your authentication approach
<a name="cognito-authentication-approach"></a>

When you authenticate users with an Amazon Cognito user pools, you choose how the sign-in experience is presented. The following three approaches differ in how much of the interface Amazon Cognito provides versus how much you build, and they are not mutually exclusive—you can combine them. They all authenticate against the same user pool and produce the same tokens. The difference is where the sign-in pages live and how much control you have.

**Managed login (Amazon Cognito hosts the pages)**  
Amazon Cognito serves the sign-up, sign-in, multi-factor authentication, and password-reset pages from your user pool domain. You customize their appearance with the branding editor. Choose this when you want a complete, hosted sign-in experience without building UI, and when you want the standards-based OAuth 2.0 and OpenID Connect flows handled for you. Managed login is the current version of these Amazon Cognito-hosted pages; the earlier *classic hosted UI* is a simpler, first-generation alternative that you can still select per app client. See [User pool managed login](cognito-user-pools-managed-login.md).

**User pools API (you build the interface)**  
Your application collects credentials and calls the Amazon Cognito user pools API directly through an AWS SDK. You build and control the entire interface. Choose this when you need a fully custom sign-in experience, or when you are signing in users from a back-end service. See [Authentication with Amazon Cognito user pools](authentication.md).

**Third-party identity providers (federation)**  
Your users sign in through an external provider. This can be a social provider like Google or Apple, or an enterprise SAML or OIDC provider. Amazon Cognito federates their identity into your user pool. You can present federated sign-in through managed login or initiate it through the API. Choose this when your users already have identities elsewhere. See [User pool sign-in with third party identity providers](cognito-user-pools-identity-federation.md).

The following table summarizes when to reach for each approach.


| If you want to | Start with | 
| --- | --- | 
| Ship sign-in fast with no UI to build and maintain | Managed login | 
| Fully control the look and behavior of every sign-in screen | The user pools API | 
| Authenticate requests from a back-end or machine-to-machine caller | The user pools API (and, for M2M, client credentials) | 
| Let users sign in with Google, Apple, or an enterprise directory | Third-party identity providers (federation), presented through managed login or the API | 

**Note**  
Whichever approach you choose, your user pool's [feature plan](cognito-sign-in-feature-plans.md) determines which capabilities are available. The **Lite** plan covers core sign-up and sign-in; **Essentials** adds options such as passwordless and passkey sign-in and managed login; and **Plus** adds advanced threat protection. You select a plan when you create a user pool and can change it later, so you don't have to decide before you start. If a feature you expect isn't available, check your plan first. For a full comparison, see [User pool feature plans](cognito-sign-in-feature-plans.md).

**Note**  
These approaches all answer *who is this user?* (authentication). If you also need to grant users temporary AWS credentials to reach services like Amazon S3, that is a separate question—authorization—answered by identity pools. See [Which parts of Amazon Cognito do you need?](what-is-amazon-cognito.md#what-is-amazon-cognito-choosing).