

# Configuring a user pool domain
<a name="cognito-user-pools-assign-domain"></a>

Configuring a domain is an optional part of setting up a user pool. A user pool domain hosts features for user authentication, federation with third-party providers, and OpenID Connect (OIDC) flows. It has *managed login*, a prebuilt interface for key operations like signing up, signing in, and password recovery. It also hosts the standard OpenID Connect (OIDC) endpoints like [authorize](authorization-endpoint.md), [userInfo](userinfo-endpoint.md), and [token](token-endpoint.md), for machine-to-machine (M2M) authorization and other OIDC and OAuth 2.0 authentication and authorization flows.

M2M authorization is also available without a domain. You can request client-credentials access tokens with the [GetClientToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetClientToken.html) API operation, which uses the Amazon Cognito API instead of the token endpoint.

Users authenticate with managed login pages at the domain associated with your user pool. You have two options for configuring this domain: you can either use the default Amazon Cognito hosted domain, or you can configure a custom domain that you own.

The custom domain option has more options for flexibility, security and control. For example, a familiar, organization-owned domain can encourage user trust and make the sign-in process more intuitive. However, the custom domain approach requires some additional overhead, like managing the SSL certificate and DNS configuration.

The OIDC discovery endpoints, `/.well-known/openid-configuration` for endpoint URLs and `/.well-known/jwks.json` for token signing keys, aren't hosted on your domain. For more information, see [Identity provider and relying party endpoints](federation-endpoints.md).

Understanding how to configure and manage the domain for your user pool is an important step in integrating authentication into your application. Sign-in with the user pools API and an AWS SDK can be an alternative to configuring a domain. The API-based model delivers tokens directly in an API response, but for implementations that use the extended capabilities of user pools as an OIDC IdP, you must configure a domain. For more information about the authentication models that are available in user pools, see [Understanding API, OIDC, and managed login pages authentication](authentication-flows-public-server-side.md#user-pools-API-operations).

**Topics**
+ [Things to know about user pool domains](#cognito-user-pools-assign-domain-things-to-know)
+ [Using the Amazon Cognito prefix domain for managed login](cognito-user-pools-assign-domain-prefix.md)
+ [Using your own domain for managed login](cognito-user-pools-add-custom-domain.md)

## Things to know about user pool domains
<a name="cognito-user-pools-assign-domain-things-to-know"></a>

User pool domains are a point of service for OIDC relying parties in your applications and for UI elements. Consider the following details when you're planning your implementation of a domain for your user pool.

**Reserved terms**  
You can't use the text `aws`, `amazon`, or `cognito` in the name of an Amazon Cognito prefix domain.

**Discovery endpoints are on a different domain**  
The user pool [discovery endpoints](federation-endpoints.md) `.well-known/openid-configuration` and `.well-known/jwks.json` aren't on your user pool custom or prefix domain. The path to these endpoints is as follows.
+ `https://cognito-idp.{{Region}}.amazonaws.com/{{your user pool ID}}/.well-known/openid-configuration`
+ `https://cognito-idp.{{Region}}.amazonaws.com/{{your user pool ID}}/.well-known/jwks.json`

**Effective time of domain changes**  
It can take Amazon Cognito up to a minute to launch or update the branding version of a prefix domain. Changes to a custom domain can take up to five minutes to propagate. New custom domains can take up to one hour to propagate.

**Custom and prefix domains at the same time**  
You can set up a user pool with both a custom domain and a prefix domain that's owned by AWS. Because the user pool [discovery endpoints](federation-endpoints.md) are hosted at a different domain, they only serve the *custom domain*. For example, your `openid-configuration` will provide a single value for `"authorization_endpoint"` of `"https://auth.example.com/oauth2/authorize"`.

When you have both custom and prefix domains in a user pool, you can use the custom domain with the full features of an OIDC provider. The prefix domain in a user pool with this configuration doesn't have discovery or token-signing-key endpoints and should be used accordingly.

**Custom domains preferred as relying party ID for passkey**  
When you set up user pool authentication with [passkeys](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passkey), you must set a relying party (RP) ID. When you have a custom domain and a prefix domain, you can set the RP ID only as your custom domain. To set a prefix domain as the RP ID in the Amazon Cognito console, delete your custom domain or enter the fully-qualified domain name (FQDN) of the prefix domain as a **Third-party domain**.

**Don't use custom domains at different levels of your domain hierarchy**  
You can configure separate user pools to have custom domains in the same top-level domain (TLD), for example *auth.example.com* and *auth2.example.com*. The managed login session cookie is valid for a custom domain and all subdomains, for example *\*.auth.example.com*. Because of this, no user of your applications should access managed login for any parent domain *and* subdomain. Where custom domains use the same TLD, keep them at the same subdomain level.

Say you have a user pool with the custom domain *auth.example.com*. Then you create another user pool and assign the custom domain *uk.auth.example.com.*. A user signs in with *auth.example.com.* and gets a cookie that their browser presents to any website in the wildcard path *\*.auth.example.com*. They then try to sign in to *uk.auth.example.com.*. They pass an invalid cookie to your user pool domain and receive an error instead of a sign-in prompt. By contrast, a user with a cookie for *\*.auth.example.com* has no issues starting a sign-in session at *auth2.example.com*.

**Branding version**  
When you create a domain, you set a **Branding version**. Your options are the newer managed-login experience and the classic hosted UI experience. This choice applies to all app clients that host services at your domain.