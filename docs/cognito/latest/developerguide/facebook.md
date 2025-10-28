# Setting up Facebook as an identity pools IdP

Amazon Cognito identity pools work with Facebook to provide federated authentication for your
application users. This section explains how to register and set up your application with
Facebook as an IdP.

## Set up Facebook

Register your application with Facebook before you authenticate Facebook users and
interact with Facebook APIs.

The [Facebook Developers portal](https://developers.facebook.com/ "https://developers.facebook.com/")
helps you to set up your application. Do this procedure before you integrate Facebook in
your Amazon Cognito identity pool:

###### Note

Amazon Cognito identity pools federation isn't compatible with [Facebook Limited
Login](https://developers.facebook.com/docs/facebook-login/limited-login "https://developers.facebook.com/docs/facebook-login/limited-login"). For more information about how to set up Facebook Login for iOS without
exceeding the permissions set for Limited Login, see [Facebook Login for iOS -
Quickstart](https://developers.facebook.com/docs/facebook-login/ios "https://developers.facebook.com/docs/facebook-login/ios") at _Meta for Developers_.

###### Setting up Facebook

1. At the [Facebook Developers
   portal](https://developers.facebook.com/ "https://developers.facebook.com/"), log in with your Facebook credentials.
2. From the **Apps** menu, select **Add a New App**.
3. Select a platform and complete the quick start process.

### Android

For more information about how to integrate Android apps with Facebook Login, see the
[Facebook
Getting Started Guide](https://developers.facebook.com/docs/android/getting-started "https://developers.facebook.com/docs/android/getting-started").

### iOS - Objective-C

For more information about how to integrate iOS Objective-C apps with Facebook Login,
see the [Facebook
Getting Started Guide](https://developers.facebook.com/docs/ios/getting-started/ "https://developers.facebook.com/docs/ios/getting-started/").

### iOS - Swift

For more information about how to integrate iOS Swift apps with Facebook Login, see
the [Facebook
Getting Started Guide](https://developers.facebook.com/docs/ios/getting-started/ "https://developers.facebook.com/docs/ios/getting-started/").

### JavaScript

For more information about how to integrate JavaScript web apps with Facebook Login,
see the [Facebook Getting Started Guide](https://developers.facebook.com/docs/facebook-login/login-flow-for-web/v2.3 "https://developers.facebook.com/docs/facebook-login/login-flow-for-web/v2.3").

## Configure an

identity provider in the Amazon Cognito identity pools console

Use the following procedure to configure your identity provider.

###### To add a Facebook identity provider (IdP)

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select an identity
   pool.
2. Choose the **User access** tab.
3. Select **Add identity provider**.
4. Choose **Facebook**.
5. Enter the **App ID** of the OAuth project that you created at
   [Meta for Developers](https://developers.facebook.com/ "https://developers.facebook.com/"). For more
   information, see [Facebook Login](https://developers.facebook.com/docs/facebook-login/ "https://developers.facebook.com/docs/facebook-login/") in the _Meta for Developers
   Docs_.
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

## Using Facebook

### Android

To add Facebook authentication, first follow the [Facebook guide](https://developers.facebook.com/docs/android "https://developers.facebook.com/docs/android") and integrate
the Facebook SDK into your application. Then add a [**Login with
Facebook** button](https://developers.facebook.com/docs/facebook-login/android "https://developers.facebook.com/docs/facebook-login/android") to your Android user interface. The Facebook SDK
uses a session object to track its state. Amazon Cognito uses the access token from this session
object to authenticate the user, generate the unique identifier, and, if needed, grant the
user access to other AWS resources.

After you authenticate your user with the Facebook SDK, add the session token to the
Amazon Cognito credentials provider.

Facebook SDK 4.0 or later:

```
Map<String, String> logins = new HashMap<String, String>();
logins.put("graph.facebook.com", AccessToken.getCurrentAccessToken().getToken());
credentialsProvider.setLogins(logins);

```

Facebook SDK before 4.0:

```
Map<String, String> logins = new HashMap<String, String>();
logins.put("graph.facebook.com", Session.getActiveSession().getAccessToken());
credentialsProvider.setLogins(logins);

```

The Facebook login process initializes a singleton session in its SDK. The Facebook
session object contains an OAuth token that Amazon Cognito uses to generate AWS credentials for
your authenticated end user. Amazon Cognito also uses the token to check against your user database
for the existence of a user that matches this particular Facebook identity. If the user
already exists, the API returns the existing identifier. Otherwise, the API returns a new
identifier. The client SDK automatically caches identifiers on the local device.

###### Note

After you set the logins map, make a call to `refresh` or
`get` to retrieve the AWS credentials.

### iOS - Objective-C

To add Facebook authentication, first follow the [Facebook guide](https://developers.facebook.com/docs/ios "https://developers.facebook.com/docs/ios") and integrate the
Facebook SDK into your application. Then add a [Login with Facebook
button](https://developers.facebook.com/docs/facebook-login/ios "https://developers.facebook.com/docs/facebook-login/ios") to your user interface. The Facebook SDK uses a session object to track
its state. Amazon Cognito uses the access token from this session object to authenticate the user
and bind them to a unique Amazon Cognito identity pools (federated identities).

To provide the Facebook access token to Amazon Cognito, implement the [AWSIdentityProviderManager](https://github.com/aws-amplify/aws-sdk-ios "https://github.com/aws-amplify/aws-sdk-ios") protocol.

When you implement the `logins` method, return a dictionary that contains
`AWSIdentityProviderFacebook`. This dictionary acts as the key, and the
current access token from the authenticated Facebook user acts as the value, as shown in
the following code example.

```
- (AWSTask<NSDictionary<NSString *, NSString *> *> *)logins {
    FBSDKAccessToken* fbToken = [FBSDKAccessToken currentAccessToken];
    if(fbToken){
        NSString *token = fbToken.tokenString;
        return [AWSTask taskWithResult: @{ AWSIdentityProviderFacebook : token }];
    }else{
            return [AWSTask taskWithError:[NSError errorWithDomain:@"Facebook Login"
                                                          code:-1
                                                      userInfo:@{@"error":@"No current Facebook access token"}]];
    }
}

```

When you instantiate the `AWSCognitoCredentialsProvider`, pass the class
that implements `AWSIdentityProviderManager` as the value of
`identityProviderManager` in the constructor. For more information, go to the
[AWSCognitoCredentialsProvider](https://github.com/aws-amplify/aws-sdk-ios "https://github.com/aws-amplify/aws-sdk-ios")
reference page and choose
**initWithRegionType:identityPoolId:identityProviderManager**.

### iOS - Swift

To add Facebook authentication, first follow the [Facebook guide](https://developers.facebook.com/docs/ios "https://developers.facebook.com/docs/ios") and integrate the
Facebook SDK into your application. Then add a [Login with Facebook
button](https://developers.facebook.com/docs/facebook-login/ios "https://developers.facebook.com/docs/facebook-login/ios") to your user interface. The Facebook SDK uses a session object to track
its state. Amazon Cognito uses the access token from this session object to authenticate the user
and bind them to a unique Amazon Cognito identity pools (federated identities).

###### Note

Amazon Cognito identity pools federation isn't compatible with [Facebook
Limited Login](https://developers.facebook.com/docs/facebook-login/limited-login "https://developers.facebook.com/docs/facebook-login/limited-login"). For more information about how to set up Facebook Login for iOS
without exceeding the permissions set for Limited Login, see [Facebook Login for iOS -
Quickstart](https://developers.facebook.com/docs/facebook-login/ios "https://developers.facebook.com/docs/facebook-login/ios") at _Meta for Developers_.

To provide the Facebook access token to Amazon Cognito, implement the [AWSIdentityProviderManager](https://github.com/aws-amplify/aws-sdk-ios "https://github.com/aws-amplify/aws-sdk-ios") protocol.

When you implement the `logins` method, return a dictionary containing
`AWSIdentityProviderFacebook`. This dictionary acts as the key, and the
current access token from the authenticated Facebook user acts as the value, as shown in
the following code example.

```
class FacebookProvider: NSObject, AWSIdentityProviderManager {
    func logins() -> AWSTask<NSDictionary> {
        if let token = AccessToken.current?.authenticationToken {
            return AWSTask(result: [AWSIdentityProviderFacebook:token])
        }
        return AWSTask(error:NSError(domain: "Facebook Login", code: -1 , userInfo: ["Facebook" : "No current Facebook access token"]))
    }
}
```

When you instantiate the `AWSCognitoCredentialsProvider`, pass the class
that implements `AWSIdentityProviderManager` as the value of
`identityProviderManager` in the constructor. For more information, go to the
[AWSCognitoCredentialsProvider](https://github.com/aws-amplify/aws-sdk-ios "https://github.com/aws-amplify/aws-sdk-ios") reference page and choose
**initWithRegionType:identityPoolId:identityProviderManager**.

### JavaScript

To add Facebook authentication, follow the [Facebook Login for the Web](https://developers.facebook.com/docs/facebook-login/login-flow-for-web/v2.3 "https://developers.facebook.com/docs/facebook-login/login-flow-for-web/v2.3") and add the **Login with Facebook**
button on your website. The Facebook SDK uses a session object to track its state. Amazon Cognito
uses the access token from this session object to authenticate the user, generate the
unique identifier, and, if needed, grant the user access to other AWS resources.

After you authenticate your user with the Facebook SDK, add the session token to the
Amazon Cognito credentials provider.

```
FB.login(function (response) {

  // Check if the user logged in successfully.
  if (response.authResponse) {

    console.log('You are now logged in.');

    // Add the Facebook access token to the Amazon Cognito credentials login map.
    AWS.config.credentials = new AWS.CognitoIdentityCredentials({
      IdentityPoolId: 'IDENTITY_POOL_ID',
      Logins: {
        'graph.facebook.com': response.authResponse.accessToken
      }
    });

    // Obtain AWS credentials
    AWS.config.credentials.get(function(){
        // Access AWS resources here.
    });

  } else {
    console.log('There was a problem logging you in.');
  }

});

```

The Facebook SDK obtains an OAuth token that Amazon Cognito uses to generate AWS credentials
for your authenticated end user. Amazon Cognito also uses the token to check against your user
database for the existence of a user matching this particular Facebook identity. If the
user already exists, the API returns the existing identifier. Otherwise a new identifier
is returned. Identifiers are automatically cached by the client SDK on the local
device.

###### Note

After you set the logins map, make a call to `refresh` or
`get` to get the credentials. For a code example, see "Use Case 17,
Integrating User Pools with Cognito Identity," in the [JavaScript README file](https://github.com/amazon-archives/amazon-cognito-identity-js/blob/master/README.md "https://github.com/amazon-archives/amazon-cognito-identity-js/blob/master/README.md").

### Unity

To add Facebook authentication, first follow the [Facebook guide](https://developers.facebook.com/docs/unity "https://developers.facebook.com/docs/unity") and integrate
the Facebook SDK into your application. Amazon Cognito uses the Facebook access token from the
`FB` object to generate a unique user identifier that is associated with an
Amazon Cognito identity.

After you authenticate your user with the Facebook SDK, add the session token to the
Amazon Cognito credentials provider:

```
void Start()
{
    FB.Init(delegate() {
        if (FB.IsLoggedIn) { //User already logged in from a previous session
            AddFacebookTokenToCognito();
        } else {
            FB.Login ("email", FacebookLoginCallback);
        }
    });
}

void FacebookLoginCallback(FBResult result)
{
    if (FB.IsLoggedIn)
    {
        AddFacebookTokenToCognito();
    }
    else
    {
        Debug.Log("FB Login error");
    }
}

void AddFacebookTokenToCognito()
{
    credentials.AddLogin ("graph.facebook.com", AccessToken.CurrentAccessToken.TokenString);
}

```

Before you use `FB.AccessToken`, call `FB.Login()` and make sure
`FB.IsLoggedIn` is true.

### Xamarin

**Xamarin for Android:**

```
public void InitializeFacebook() {
    FacebookSdk.SdkInitialize(this.ApplicationContext);
    callbackManager = CallbackManagerFactory.Create();
    LoginManager.Instance.RegisterCallback(callbackManager, new FacebookCallback &lt; LoginResult &gt; () {
      HandleSuccess = loginResult = &gt; {
        var accessToken = loginResult.AccessToken;
        credentials.AddLogin("graph.facebook.com", accessToken.Token);
        //open new activity
      },
      HandleCancel = () = &gt; {
        //throw error message
      },
      HandleError = loginError = &gt; {
        //throw error message
      }
    });
    LoginManager.Instance.LogInWithReadPermissions(this, new List &lt; string &gt; {
      "public_profile"
    });
  }

```

**Xamarin for iOS:**

```
public void InitializeFacebook() {
  LoginManager login = new LoginManager();
  login.LogInWithReadPermissions(readPermissions.ToArray(), delegate(LoginManagerLoginResult result, NSError error) {
    if (error != null) {
      //throw error message
    } else if (result.IsCancelled) {
      //throw error message
    } else {
      var accessToken = loginResult.AccessToken;
      credentials.AddLogin("graph.facebook.com", accessToken.Token);
      //open new view controller
    }
  });
}

```
