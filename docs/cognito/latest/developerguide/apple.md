# Setting up Sign in with Apple as an identity pool IdP

Amazon Cognito identity pools work with Sign in with Apple to provide federated authentication for
your mobile application and web application users. This section explains how to register and
set up your application using Sign in with Apple as an identity provider (IdP).

To add Sign in with Apple as an authentication provider to an identity pool, you must
complete two procedures. First, integrate Sign in with Apple in an application, and then
configure Sign in with Apple in identity pools. For the most up-to-date information about
setting up Sign in with Apple, see [Configuring Your Environment for Sign in with Apple](https://developer.apple.com/documentation/signinwithapple/configuring-your-environment-for-sign-in-with-apple "https://developer.apple.com/documentation/signinwithapple/configuring-your-environment-for-sign-in-with-apple") in the Apple Developer
documentation.

## Set up Sign in with Apple

To configure Sign in with Apple as an IdP, register your application with the Apple to
receive client ID.

1. Create a [developer account
   with Apple](https://developer.apple.com/programs/enroll/ "https://developer.apple.com/programs/enroll/").
2. [Sign in](https://developer.apple.com/account/#/welcome "https://developer.apple.com/account/#/welcome") with your
   Apple credentials.
3. In the left navigation pane, choose **Certificates, IDs &
   Profiles**.
4. In the left navigation pane, choose **Identifiers**.
5. On the **Identifiers** page, choose the
   **+**icon.
6. On the **Register a New Identifier** page, choose **App
   IDs**, and then choose **Continue**.
7. On the **Register an App ID** page, do the following:
   1. Under **Description**, type a description.
   2. Under **Bundle ID,** type an identifier. Make a note of this
      **Bundle ID** as you need this value to configure Apple as a
      provider in the identity pool.
   3. Under **Capabilities**, choose **Sign In with
      Apple**, and then choose **Edit**.
   4. On the **Sign in with Apple: App ID Configuration** page,
      select the appropriate setting for your app. Then choose
      **Save**.
   5. Choose **Continue**.

8. On the **Confirm your App ID** page, choose
   **Register**.
9. Proceed to step 10 if you want to integrate Sign in with Apple with a native iOS
   application. Step 11 is for applications that you want to integrate with Sign in with
   Apple JS.
10. On the **Identifiers** page, choose the **App
    IDs** menu, then **Services IDs**. Choose the
    **+** icon.
11. On the **Register a New Identifier** page, choose
    **Services IDs**, and then choose
    **Continue**.
12. On the **Register a Services ID** page, do the following:
    1. Under **Description**, type a description.
    2. Under **Identifier**, type an identifier. Make a note of the
       services ID as you need this value to configure Apple as a provider in your identity
       pool.
    3. Select **Sign In with Apple** and then choose
       **Configure**.
    4. On the **Web Authentication Configuration** page, choose a
       **Primary App ID**. Under **Website URLs**,
       choose the **+** icon. For **Domains and
       Subdomains**, enter the domain name of your app. In **Return
       URLs,** enter the callback URL where the authorization redirects the user
       after they authenticate through Sign in with Apple.
    5. Choose **Next**.
    6. Choose **Continue**, and then choose
       **Register**.

13. In the left navigation pane, choose **Keys**.
14. On the **Keys** page, choose the **+**
    icon.
15. On the **Register a New Key** page, do the following:
    1. Under **Key Name**, type a key name.
    2. Choose **Sign In with Apple**, and then choose
       **Configure**.
    3. On the **Configure Key** page, choose a **Primary App
       ID** and then choose **Save**.
    4. Choose **Continue**, and then choose
       **Register**.

###### Note

To integrate Sign in with Apple with a native iOS application, see [Implementing User Authentication with Sign in with Apple.](https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple "https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple")

To integrate Sign in with Apple in a platform other than native iOS, see [Sign in with Apple JS.](https://developer.apple.com/documentation/signinwithapplejs/ "https://developer.apple.com/documentation/signinwithapplejs/")

## Configure the external provider in the

Amazon Cognito federated identities console

Use the following procedure to configure your external provider.

###### To add a Sign in with Apple identity provider (IdP)

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select an identity
   pool.
2. Choose the **User access** tab.
3. Select **Add identity provider**.
4. Choose **Sign in with Apple**.
5. Enter the **Services ID** of the OAuth project you created with
   [Apple Developer](https://developer.apple.com "https://developer.apple.com"). For more
   information, see [Authenticating users with Sign in with Apple](https://developer.apple.com/documentation/signinwithapple/authenticating-users-with-sign-in-with-apple "https://developer.apple.com/documentation/signinwithapple/authenticating-users-with-sign-in-with-apple") in _Sign
   in with Apple Documentation_.
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

## Sign in with Apple as a provider in the

Amazon Cognito federated identities CLI examples

This example creates an identity pool named `MyIdentityPool` with Sign in
with Apple as an IdP.

`aws cognito-identity create-identity-pool --identity-pool-name MyIdentityPool
 --supported-login-providers appleid.apple.com="sameple.apple.clientid"`

For more information, see [Create identity pool](../../../cli/latest/reference/cognito-identity/create-identity-pool.md "../../../cli/latest/reference/cognito-identity/create-identity-pool.md")

###### Generate an Amazon Cognito identity ID

This example generates (or retrieves) an Amazon Cognito ID. This is a public API so you don't
need any credentials to call this API.

`aws cognito-identity get-id --identity-pool-id SampleIdentityPoolId --logins
 appleid.apple.com="SignInWithAppleIdToken"`

For more information, see [get-id.](../../../cli/latest/reference/cognito-identity/get-id.md "../../../cli/latest/reference/cognito-identity/get-id.md")

###### Get credentials for an Amazon Cognito identity ID

This example returns credentials for the provided identity ID and Sign in with Apple
login. This is a public API so you don't need any credentials to call this API.

`aws cognito-identity get-credentials-for-identity --identity-id SampleIdentityId
 --logins appleid.apple.com="SignInWithAppleIdToken"`

For more information, see [get-credentials-for-identity](../../../cli/latest/reference/cognito-identity/get-credentials-for-identity.md "../../../cli/latest/reference/cognito-identity/get-credentials-for-identity.md")

## Use Sign in with Apple: Android

Apple doesn't provide an SDK that supports Sign in with Apple for Android. You can use
the web flow in a web view instead.

- To configure Sign in with Apple in your application, follow [Configuring Your Web page for Sign In with Apple](https://developer.apple.com/documentation/signinwithapple/configuring-your-webpage-for-sign-in-with-apple "https://developer.apple.com/documentation/signinwithapple/configuring-your-webpage-for-sign-in-with-apple") in the Apple
  documentation.
- To add a **Sign in with Apple** button to your Android user
  interface, follow [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web "https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web") in the Apple
  documentation.
- To securely authenticate users with Sign in with Apple, follow [Authenticating Users with Sign in with Apple](https://developer.apple.com/documentation/signinwithapple/authenticating-users-with-sign-in-with-apple "https://developer.apple.com/documentation/signinwithapple/authenticating-users-with-sign-in-with-apple") in the Apple
  documentation.

Sign in with Apple uses a session object to track its state. Amazon Cognito uses the ID token
from this session object to authenticate the user, generate the unique identifier, and, if
needed, grant the user access to other AWS resources.

```
@Override
public void onSuccess(Bundle response) {
    String token = response.getString("id_token");
    Map<String, String> logins = new HashMap<String, String>();
    logins.put("appleid.apple.com", token);
    credentialsProvider.setLogins(logins);
}
```

## Use Sign in with Apple: iOS - Objective-C

Apple provided SDK support for Sign in with Apple in native iOS applications. To
implement user authentication with Sign in with Apple in native iOS devices, follow [Implementing User Authentication with Sign in with Apple](https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple "https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple") in the Apple
documentation.

Amazon Cognito uses the ID token to authenticate the user, generate the unique identifier, and,
if needed, grant the user access to other AWS resources.

```
(void)finishedWithAuth: (ASAuthorizationAppleIDCredential *)auth error: (NSError *) error {
        NSString *idToken = [ASAuthorizationAppleIDCredential objectForKey:@"identityToken"];
        credentialsProvider.logins = @{ "appleid.apple.com": idToken };
    }
```

## Use Sign in with Apple: iOS - Swift

Apple provided SDK support for Sign in with Apple in native iOS applications. To
implement user authentication with Sign in with Apple in native iOS devices, follow [Implementing User Authentication with Sign in with Apple](https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple "https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple") in the Apple
documentation.

Amazon Cognito uses the ID token to authenticate the user, generate the unique identifier, and,
if needed, grant the user access to other AWS resources.

For more information about how to set up Sign in with Apple in iOS, see [Set up Sign in with Apple](https://docs.amplify.aws/sdk/auth/federated-identities/q/platform/ios#set-up-sign-in-with-apple "https://docs.amplify.aws/sdk/auth/federated-identities/q/platform/ios#set-up-sign-in-with-apple")

```
func finishedWithAuth(auth: ASAuthorizationAppleIDCredential!, error: NSError!) {
    if error != nil {
      print(error.localizedDescription)
    }
    else {
      let idToken = auth.identityToken,
      credentialsProvider.logins = ["appleid.apple.com": idToken!]
    }
}
```

## Use Sign in with Apple: JavaScript

Apple doesn’t provide an SDK that supports Sign in with Apple for JavaScript. You can
use the web flow in a web view instead.

- To configure Sign in with Apple in your application, follow [Configuring Your Web page for Sign In with Apple](https://developer.apple.com/documentation/signinwithapple/configuring-your-webpage-for-sign-in-with-apple "https://developer.apple.com/documentation/signinwithapple/configuring-your-webpage-for-sign-in-with-apple") in the Apple
  documentation.
- To add a **Sign in with Apple** button to your JavaScript user
  interface, follow [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web "https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web") in the Apple
  documentation.
- To securely authenticate users with Sign in with Apple, follow [Authenticating Users with Sign in with Apple](https://developer.apple.com/documentation/signinwithapple/authenticating-users-with-sign-in-with-apple "https://developer.apple.com/documentation/signinwithapple/authenticating-users-with-sign-in-with-apple") in the Apple
  documentation.

Sign in with Apple uses a session object to track its state. Amazon Cognito uses the ID token
from this session object to authenticate the user, generate the unique identifier, and, if
needed, grant the user access to other AWS resources.

```
function signinCallback(authResult) {
     // Add the apple's id token to the Amazon Cognito credentials login map.
     AWS.config.credentials = new AWS.CognitoIdentityCredentials({
        IdentityPoolId: 'IDENTITY_POOL_ID',
        Logins: {
           'appleid.apple.com': authResult['id_token']
        }
     });

     // Obtain AWS credentials
     AWS.config.credentials.get(function(){
        // Access AWS resources here.
     });
}
```
