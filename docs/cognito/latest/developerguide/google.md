# Setting up Google as an identity pool IdP

Amazon Cognito identity pools work with Google to provide federated authentication for your mobile
application users. This section explains how to register and set up your application with
Google as an IdP.

## Android

###### Note

If your app uses Google and is available on multiple mobile platforms, you should
configure it as an [OpenID Connect Provider](open-id.md "open-id.md"). Add all created
client IDs as additional audience values for better integration. To learn more about
Google's cross-client identity model, see [Cross-client
Identity](https://developers.google.com/accounts/docs/CrossClientAuth "https://developers.google.com/accounts/docs/CrossClientAuth").

###### Setting up Google

To activate Google Sign-in for Android, create a Google Developers console project for
your application.

1. Go to the [Google Developers
   console](https://console.developers.google.com/ "https://console.developers.google.com/") and create a new project.
2. Choose **APIs & Services**, then **OAuth consent
   screen**. Customize the information that Google shows to your users when
   Google asks for their consent to share their profile data with your app.
3. Choose **Credentials**, then **Create
   credentials**. Choose **OAuth client ID**. Select
   **Android** as the **Application type**. Create a
   separate client ID for each platform where you develop your app.
4. From **Credentials**, choose **Manage service
   accounts**. Choose **Create service account**. Enter your
   service account details, and then choose **Create and
   continue**.
5. Grant the service account access to your project. Grant users access to the service
   account as your app requires.
6. Choose your new service account, choose the **Keys** tab, and
   **Add key**. Create and download a new JSON key.

For more information about how to use the Google Developers console, see [Creating
and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects "https://cloud.google.com/resource-manager/docs/creating-managing-projects") in the Google Cloud documentation.

For more information about how to integrate Google into your Android app, see [Authenticate
users with Sign in with Google](https://developer.android.com/identity/sign-in/credential-manager-siwg "https://developer.android.com/identity/sign-in/credential-manager-siwg") in the Google Identity documentation.

###### To add a Google identity provider (IdP)

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select an identity
   pool.
2. Choose the **User access** tab.
3. Select **Add identity provider**.
4. Choose **Google**.
5. Enter the **Client ID** of the OAuth project you created at [Google Cloud Platform](https://console.cloud.google.com/ "https://console.cloud.google.com/"). For more
   information, see [Setting up
   OAuth 2.0](https://support.google.com/cloud/answer/6158849 "https://support.google.com/cloud/answer/6158849") in _Google Cloud Platform Console
   Help_.
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

**Use Google**

To enable login with Google in your application, follow the instructions in the [Google documentation
for Android](https://developers.google.com/identity/sign-in/android/start "https://developers.google.com/identity/sign-in/android/start"). When a user signs in, they request an OpenID Connect authentication
token from Google. Amazon Cognito then uses the token to authenticate the user and generate a unique
identifier.

The following example code shows how to retrieve the authentication token from the
Google Play service:

```
GooglePlayServicesUtil.isGooglePlayServicesAvailable(getApplicationContext());
AccountManager am = AccountManager.get(this);
Account[] accounts = am.getAccountsByType(GoogleAuthUtil.GOOGLE_ACCOUNT_TYPE);
String token = GoogleAuthUtil.getToken(getApplicationContext(), accounts[0].name,
        "audience:server:client_id:YOUR_GOOGLE_CLIENT_ID");
Map<String, String> logins = new HashMap<String, String>();
logins.put("accounts.google.com", token);
credentialsProvider.setLogins(logins);

```

## iOS - Objective-C

###### Note

If your app uses Google and is available on multiple mobile platforms, configure
Google as an [OpenID Connect Provider](open-id.md "open-id.md"). Add all created
client IDs as additional audience values for better integration. To learn more about
Google's cross-client identity model, see [Cross-client
Identity](https://developers.google.com/accounts/docs/CrossClientAuth "https://developers.google.com/accounts/docs/CrossClientAuth").

###### Setting up Google

To enable Google Sign-in for iOS, create a Google Developers console project for your
application.

1. Go to the [Google Developers
   console](https://console.developers.google.com/ "https://console.developers.google.com/") and create a new project.
2. Choose **APIs & Services**, then **OAuth consent
   screen**. Customize the information that Google shows to your users when
   Google asks for their consent to share their profile data with your app.
3. Choose **Credentials**, then **Create
   credentials**. Choose **OAuth client ID**. Select
   **iOS** as the **Application type**. Create a
   separate client ID for each platform where you develop your app.
4. From **Credentials**, choose **Manage service
   accounts**. Choose **Create service account**. Enter your
   service account details, and choose **Create and continue**.
5. Grant the service account access to your project. Grant users access to the service
   account as your app requires.
6. Choose your new service account. Choose the **Keys** tab, and
   **Add key**. Create and download a new JSON key.

For more information about how to use the Google Developers console, see [Creating
and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects "https://cloud.google.com/resource-manager/docs/creating-managing-projects") in the Google Cloud documentation.

For more information about how to integrate Google into your iOS app, see [Google Sign-In
for iOS](https://developers.google.com/identity/sign-in/ios/start-integrating "https://developers.google.com/identity/sign-in/ios/start-integrating") in the Google Identity documentation.

###### To add a Google identity provider (IdP)

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select an identity
   pool.
2. Choose the **User access** tab.
3. Select **Add identity provider**.
4. Choose **Google**.
5. Enter the **Client ID** of the OAuth project you created at [Google Cloud Platform](https://console.cloud.google.com/ "https://console.cloud.google.com/"). For more
   information, see [Setting up
   OAuth 2.0](https://support.google.com/cloud/answer/6158849 "https://support.google.com/cloud/answer/6158849") in _Google Cloud Platform Console
   Help_.
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

**Use Google**

To enable login with Google in your application, follow the [Google documentation for
iOS](https://developers.google.com/identity/sign-in/ios/start/ "https://developers.google.com/identity/sign-in/ios/start/"). Successful authentication results in an OpenID Connect authentication token,
which Amazon Cognito uses to authenticate the user and generate a unique identifier.

Successful authentication results in a `GTMOAuth2Authentication` object,
which contains an `id_token`, which Amazon Cognito uses to authenticate the user and
generate a unique identifier:

```
- (void)finishedWithAuth: (GTMOAuth2Authentication *)auth error: (NSError *) error {
        NSString *idToken = [auth.parameters objectForKey:@"id_token"];
        credentialsProvider.logins = @{ @(AWSCognitoLoginProviderKeyGoogle): idToken };
    }

```

## iOS - Swift

###### Note

If your app uses Google and is available on multiple mobile platforms, configure
Google as an [OpenID Connect Provider](open-id.md "open-id.md"). Add all created
client IDs as additional audience values for better integration. To learn more about
Google's cross-client identity model, see [Cross-client
Identity](https://developers.google.com/accounts/docs/CrossClientAuth "https://developers.google.com/accounts/docs/CrossClientAuth").

###### Setting up Google

To enable Google Sign-in for iOS, create a Google Developers console project for your
application.

1. Go to the [Google Developers
   console](https://console.developers.google.com/ "https://console.developers.google.com/") and create a new project.
2. Choose **APIs & Services**, then **OAuth consent
   screen**. Customize the information that Google shows to your users when
   Google asks for their consent to share their profile data with your app.
3. Choose **Credentials**, then **Create
   credentials**. Choose **OAuth client ID**. Select
   **iOS** as the **Application type**. Create a
   separate client ID for each platform where you develop your app.
4. From **Credentials**, choose **Manage service
   accounts**. Choose **Create service account**. Enter your
   service account details, and choose **Create and continue**.
5. Grant the service account access to your project. Grant users access to the service
   account as your app requires.
6. Choose your new service account, choose the **Keys** tab, and
   **Add key**. Create and download a new JSON key.

For more information about how to use the Google Developers console, see [Creating
and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects "https://cloud.google.com/resource-manager/docs/creating-managing-projects") in the Google Cloud documentation.

For more information about how to integrate Google into your iOS app, see [Google Sign-In
for iOS](https://developers.google.com/identity/sign-in/ios/start-integrating "https://developers.google.com/identity/sign-in/ios/start-integrating") in the Google Identity documentation.

Choose **Manage Identity Pools** from the [Amazon Cognito Console home page](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"):

###### Configuring the external provider in the Amazon Cognito Console

1. Choose the name of the identity pool where you want to enable Google as an external
   provider. The **Dashboard** page for your identity pool appears.
2. In the top-right corner of the **Dashboard** page, choose
   **Edit identity pool**. The Edit identity pool page appears.
3. Scroll down and choose **Authentication providers** to expand the
   section.
4. Choose the **Google** tab.
5. Choose **Unlock**.
6. Enter the Google Client ID that you obtained from Google, and then choose
   **Save Changes**.

**Use Google**

To enable login with Google in your application, follow the [Google documentation for
iOS](https://developers.google.com/identity/sign-in/ios/start/ "https://developers.google.com/identity/sign-in/ios/start/"). Successful authentication results in an OpenID Connect authentication token
that Amazon Cognito uses to authenticate the user and generate a unique identifier.

Successful authentication results in a `GTMOAuth2Authentication` object that
contains an `id_token`. Amazon Cognito uses this token to authenticate the user and
generate a unique identifier:

```
func finishedWithAuth(auth: GTMOAuth2Authentication!, error: NSError!) {
    if error != nil {
      print(error.localizedDescription)
    }
    else {
      let idToken = auth.parameters.objectForKey("id_token")
      credentialsProvider.logins = [AWSCognitoLoginProviderKey.Google.rawValue: idToken!]
    }
}
```

## JavaScript

###### Note

If your app uses Google and is available on multiple mobile platforms, you should
configure Google as an [OpenID Connect Provider](open-id.md "open-id.md"). Add all
created client IDs as additional audience values for better integration. To learn more
about Google's cross-client identity model, see [Cross-client
Identity](https://developers.google.com/accounts/docs/CrossClientAuth "https://developers.google.com/accounts/docs/CrossClientAuth").

###### Setting up Google

To enable Google Sign-in for a JavaScript web app, create a Google Developers console
project for your application.

1. Go to the [Google Developers
   console](https://console.developers.google.com/ "https://console.developers.google.com/") and create a new project.
2. Choose **APIs & Services**, then **OAuth consent
   screen**. Customize the information that Google shows to your users when
   Google asks their consent to share their profile data with your app.
3. Choose **Credentials**, then **Create
   credentials**. Choose **OAuth client ID**. Select
   **Web application** as the **Application type**.
   Create a separate client ID for each platform where you develop your app.
4. From **Credentials**, choose **Manage service
   accounts**. Choose **Create service account**. Enter your
   service account details, and choose **Create and continue**.
5. Grant the service account access to your project. Grant users access to the service
   account as your app requires.
6. Choose your new service account, choose the **Keys** tab, and
   **Add key**. Create and download a new JSON key.

For more information about how to use the Google Developers console, see [Creating
and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects "https://cloud.google.com/resource-manager/docs/creating-managing-projects") in the Google Cloud documentation.

For more information about how to integrate Google into your web app, see [Sign in With
Google](https://developers.google.com/identity/gsi/web/guides/overview "https://developers.google.com/identity/gsi/web/guides/overview") in the Google Identity documentation.

**Configure the External Provider in the Amazon Cognito
Console**

###### To add a Google identity provider (IdP)

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select an identity
   pool.
2. Choose the **User access** tab.
3. Select **Add identity provider**.
4. Choose **Google**.
5. Enter the **Client ID** of the OAuth project you created at [Google Cloud Platform](https://console.cloud.google.com/ "https://console.cloud.google.com/"). For more
   information, see [Setting up
   OAuth 2.0](https://support.google.com/cloud/answer/6158849 "https://support.google.com/cloud/answer/6158849") in _Google Cloud Platform Console
   Help_.
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

**Use Google**

To enable login with Google in your application, follow the [Google documentation
for Web](https://developers.google.com/identity/gsi/web/guides/overview "https://developers.google.com/identity/gsi/web/guides/overview").

Successful authentication results in a response object that contains an
`id_token` that Amazon Cognito uses to authenticate the user and generate a unique
identifier:

```
function signinCallback(authResult) {
  if (authResult['status']['signed_in']) {

     // Add the Google access token to the Amazon Cognito credentials login map.
     AWS.config.credentials = new AWS.CognitoIdentityCredentials({
        IdentityPoolId: 'IDENTITY_POOL_ID',
        Logins: {
           'accounts.google.com': authResult['id_token']
        }
     });

     // Obtain AWS credentials
     AWS.config.credentials.get(function(){
        // Access AWS resources here.
     });
  }
}
```
