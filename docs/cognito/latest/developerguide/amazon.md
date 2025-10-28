# Setting up Login with Amazon as an identity pools IdP

Amazon Cognito identity pools work with Login with Amazon to provide federated authentication for
your mobile and web app users. This section explains how to register and set up your
application with Login with Amazon as an identity provider (IdP).

Set up Login with Amazon to work with Amazon Cognito in the [Developer Portal](https://developer.amazon.com/login-with-amazon "https://developer.amazon.com/login-with-amazon"). For more
information, see [Setting Up Login with Amazon](https://developer.amazon.com/docs/login-with-amazon/faq.html#setting-up-login-with-amazon "https://developer.amazon.com/docs/login-with-amazon/faq.html#setting-up-login-with-amazon") in the Login with Amazon FAQ.

###### Note

To integrate Login with Amazon into a Xamarin application, follow the [Xamarin Getting
Started Guide](https://developer.xamarin.com/guides/cross-platform/getting_started/ "https://developer.xamarin.com/guides/cross-platform/getting_started/").

###### Note

You can't natively integrate Login with Amazon on the Unity platform. Instead, use a web
view and go through the browser sign-in flow.

## Setting up Login with Amazon

**Implement Login with Amazon**

In the [Amazon
developer portal](https://developer.amazon.com/apps-and-games/login-with-amazon "https://developer.amazon.com/apps-and-games/login-with-amazon"), you can set up an OAuth application to integrate with your
identity pool, find Login with Amazon documentation, and download SDKs. Choose
**Developer console**, then **Login with Amazon** in the
developer portal. You can create a security profile for your application and then build
Login with Amazon authentication mechanisms into your app. See [Getting credentials](getting-credentials.md "getting-credentials.md") for more information
about how to integrate Login with Amazon authentication with your app.

Amazon issues an OAuth 2.0 **client ID** for your new security profile.
You can find the **client ID** on the security profile **Web
Settings** tab. Enter the **Security Profile ID** in the
**App ID** field of the Login with Amazon IdP in your identity
pool.

###### Note

You enter the **Security Profile ID** in the **App
ID** field of the Login with Amazon IdP in your identity pool. This differs
from user pools, which use **client ID**.

## Configure the external provider in

the Amazon Cognito console

###### To add a Login with Amazon identity provider (IdP)

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select an identity
   pool.
2. Choose the **User access** tab.
3. Select **Add identity provider**.
4. Choose **Login with Amazon**.
5. Enter the **App ID** of the OAuth project that you created at
   [Login with
   Amazon](https://developer.amazon.com/apps-and-games/login-with-amazon "https://developer.amazon.com/apps-and-games/login-with-amazon"). For more information, see [Login with Amazon Documentation](https://developer.amazon.com/docs/login-with-amazon/documentation-overview.html "https://developer.amazon.com/docs/login-with-amazon/documentation-overview.html").
6. To set the role that Amazon Cognito requests when it issues credentials to users who have
   authenticated with this provider, configure **Role settings**.
   1. You can assign users from that IdP the **Default role** that
      you set up when you configured your **Authenticated role**, or you
      can **Choose role with rules**.
      1. If you chose **Choose role with rules**, enter the source
         **Claim** from your user's authentication, the
         **Operator** that you want to compare the claim by, the
         **Value** that will cause a match to this role choice, and
         the **Role** that you want to assign when the **Role
         assignment** matches. Select **Add another** to
         create an additional rule based on a different condition.
      2. Choose a **Role resolution**. When your user's claims don't
         match your rules, you can deny credentials or issue credentials for your
         **Authenticated role**.

7. To change the principal tags that Amazon Cognito assigns when it issues credentials to users
   who have authenticated with this provider, configure **Attributes for access
   control**.
   1. To apply no principal tags, choose **Inactive**.
   2. To apply principal tags based on `sub` and `aud` claims,
      choose **Use default mappings**.
   3. To create your own custom schema of attributes to principal tags, choose
      **Use custom mappings**. Then enter a **Tag
      key** that you want to source from each **Claim** that
      you want to represent in a tag.

8. Select **Save changes**.

## Use Login with Amazon: Android

After you authenticate Amazon login, you can pass the token to the Amazon Cognito credentials
provider in the onSuccess method of the TokenListener interface. The code looks like
this:

```
@Override
public void onSuccess(Bundle response) {
    String token = response.getString(AuthzConstants.BUNDLE_KEY.TOKEN.val);
    Map<String, String> logins = new HashMap<String, String>();
    logins.put("www.amazon.com", token);
    credentialsProvider.setLogins(logins);
}

```

## Use Login with Amazon: iOS - Objective-C

After you authenticate Amazon login, you can pass the token to the Amazon Cognito credentials
provider in the requestDidSucceed method of the AMZNAccessTokenDelegate:

```
- (void)requestDidSucceed:(APIResult \*)apiResult {
    if (apiResult.api == kAPIAuthorizeUser) {
        [AIMobileLib getAccessTokenForScopes:[NSArray arrayWithObject:@"profile"] withOverrideParams:nil delegate:self];
    }
    else if (apiResult.api == kAPIGetAccessToken) {
        credentialsProvider.logins = @{ @(AWSCognitoLoginProviderKeyLoginWithAmazon): apiResult.result };
    }
}}
```

## Use Login with Amazon: iOS - Swift

After you authenticate Amazon login, you can pass the token to the Amazon Cognito credentials
provider in the `requestDidSucceed` method of the
`AMZNAccessTokenDelegate`:

```
func requestDidSucceed(apiResult: APIResult!) {
    if apiResult.api == API.AuthorizeUser {
        AIMobileLib.getAccessTokenForScopes(["profile"], withOverrideParams: nil, delegate: self)
    } else if apiResult.api == API.GetAccessToken {
        credentialsProvider.logins = [AWSCognitoLoginProviderKey.LoginWithAmazon.rawValue: apiResult.result]
    }
}
```

## Use Login with Amazon: JavaScript

After the user authenticates with Login with Amazon and is redirected back to your
website, the Login with Amazon access_token is provided in the query string. Pass that token
into the credentials login map.

```
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
   IdentityPoolId: 'IDENTITY_POOL_ID',
   Logins: {
       'www.amazon.com': 'Amazon Access Token'
   }
});
```
