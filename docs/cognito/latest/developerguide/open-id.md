

# Setting up an OIDC provider as an identity pool IdP
<a name="open-id"></a>

[OpenID Connect](http://openid.net/connect/) is an open standard for authentication that a number of login providers support. With Amazon Cognito, you can link identities with OpenID Connect providers that you configure through [AWS Identity and Access Management](http://aws.amazon.com/iam/).

**Adding an OpenID Connect provider**

For information about how to create an OpenID Connect provider, see [Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/identity-providers-oidc.html) in the *AWS Identity and Access Management User Guide*.

**Associating a provider with Amazon Cognito**

**To add an OIDC identity provider (IdP)**

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home). Select an identity pool.

1. Choose the **User access** tab.

1. Select **Add identity provider**.

1. Choose **OpenID Connect (OIDC)**.

1. Choose an **OIDC identity provider** from the IAM IdPs in your AWS account. If you want to add a new SAML provider, choose **Create new provider** to navigate to the IAM console.

1. To set the role that Amazon Cognito requests when it issues credentials to users who have authenticated with this provider, configure **Role settings**.

   1. You can assign users from that IdP the **Default role** that you set up when you configured your **Authenticated role**, or you can **Choose role with rules**.

     1. If you chose **Choose role with rules**, enter the source **Claim** from your user's authentication, the **Operator** that you want to compare the claim by, the **Value** that will cause a match to this role choice, and the **Role** that you want to assign when the **Role assignment** matches. Select **Add another** to create an additional rule based on a different condition.

     1. Choose a **Role resolution**. When your user's claims don't match your rules, you can deny credentials or issue credentials for your **Authenticated role**.

1. To change the principal tags that Amazon Cognito assigns when it issues credentials to users who have authenticated with this provider, configure **Attributes for access control**.

   1. To apply no principal tags, choose **Inactive**.

   1. To apply principal tags based on `sub` and `aud` claims, choose **Use default mappings**.

   1. To create your own custom schema of attributes to principal tags, choose **Use custom mappings**. Then enter a **Tag key** that you want to source from each **Claim** that you want to represent in a tag.

1. Select **Save changes**.

You can associate multiple OpenID Connect providers with a single identity pool.

**Using OpenID Connect**

Refer to your provider's documentation for how to sign in and receive an ID token.

After you have a token, add the token to the logins map. Use the URI of your provider as the key.

**Validating an OpenID Connect token**

When you first integrate with Amazon Cognito, you might receive an `InvalidToken` exception. It is important to understand how Amazon Cognito validates OpenID Connect (OIDC) tokens.

**Note**  
As specified here ([https://tools.ietf.org/html/rfc7523](https://tools.ietf.org/html/rfc7523)), Amazon Cognito provides a grace period of 5 minutes to handle any clock skew between systems.

1. The `iss` parameter must match the key that the logins map uses (such as login.provider.com).

1. The signature must be valid. The signature must be verifiable via an RSA public key.
**Note**  
Identity pools maintain a cache of the OIDC IdP signing key for a brief period. If your provider changes their signing key, Amazon Cognito might return a `NoKeyFound` error until this cache refreshes. If you encounter this error, wait about ten minutes for your identity pool to refresh the signing key.

1. The fingerprint of the certificate public key matches the fingerprint that you set in IAM when you created your OIDC provider.

1. If the `azp` parameter is present, check this value against listed client IDs in your OIDC provider.

1. If the `azp` parameter isn't present, check the `aud` parameter against listed client IDs in your OIDC provider.

The website [jwt.io](http://jwt.io/) is a valuable resource that you can use to decode tokens and verify these values.

## Android
<a name="set-up-open-id-1.android"></a>

```
Map<String, String> logins = new HashMap<String, String>();
logins.put("login.provider.com", token);
credentialsProvider.setLogins(logins);
```

## iOS - Objective-C
<a name="set-up-open-id-1.ios-objc"></a>

```
credentialsProvider.logins = @{ "login.provider.com": token }
```

## JavaScript
<a name="set-up-open-id-1.javascript"></a>

```
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
 IdentityPoolId: 'IDENTITY_POOL_ID',
 Logins: {
    'login.provider.com': token
 }
});
```