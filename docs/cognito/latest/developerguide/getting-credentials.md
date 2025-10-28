# Getting credentials

You can use Amazon Cognito to deliver temporary, limited-privilege credentials to your application,
so that your users can access AWS resources. This section describes how to get credentials
and how to retrieve an Amazon Cognito identity from an identity pool.

Amazon Cognito supports both authenticated and unauthenticated identities. Unauthenticated users do
not have their identity verified, making this role appropriate for guest users of your app or
in cases when it doesn't matter if users have their identities verified. Authenticated users
log in to your application through a third-party identity provider, or a user pool, that
verifies their identities. Make sure you scope the permissions of resources appropriately so
you don't grant access to them from unauthenticated users.

Amazon Cognito identities are not credentials. They are exchanged for credentials using web
identity federation support in the AWS Security Token Service (AWS STS). The recommended way to obtain AWS
credentials for your app users is to use `AWS.CognitoIdentityCredentials`. The
identity in the credentials object is then exchanged for credentials using AWS STS.

###### Note

If you created your identity pool before February 2015, you must reassociate your roles
with your identity pool to use the `AWS.CognitoIdentityCredentials` constructor
without the roles as parameters. To do so, open the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"), choose **Manage
identity pools**, select your identity pool, choose **Edit
identity Pool**, specify your authenticated and unauthenticated roles, and save
the changes.

Web identity credentials providers are part of the default credential provider chain in
AWS SDKs. To set your identity pool token in a local `config` file for an AWS
SDK or the AWS CLI, add a `web_identity_token_file` profile entry. See [Assume
role credential provider](../../../sdkref/latest/guide/feature-assume-role-credentials.md "../../../sdkref/latest/guide/feature-assume-role-credentials.md") in the AWS SDKs and Tools Reference Guide.

To learn more about how to populate web identity credentials in your SDK, refer to the SDK
developer guide. For best results, start your project with the identity pool integration
that's built in to AWS Amplify.

###### AWS SDK resources for getting and setting credentials with identity pools

- [Identity Pool Federation](https://docs.amplify.aws/lib/auth/advanced/q/platform/android/#identity-pool-federation "https://docs.amplify.aws/lib/auth/advanced/q/platform/android/#identity-pool-federation") (Android) in the Amplify Dev Center
- [Identity Pool Federation](https://docs.amplify.aws/lib/auth/advanced/q/platform/ios/#identity-pool-federation "https://docs.amplify.aws/lib/auth/advanced/q/platform/ios/#identity-pool-federation") (iOS) in the Amplify Dev Center
- [Using Amazon Cognito Identity to authenticate users](../../../sdk-for-javascript/v3/developer-guide/loading-browser-credentials-cognito.md "../../../sdk-for-javascript/v3/developer-guide/loading-browser-credentials-cognito.md") in the AWS SDK for JavaScript Developer Guide
- [Amazon Cognito credentials
  provider](../../../sdk-for-net/v3/developer-guide/cognito-creds-provider.md "../../../sdk-for-net/v3/developer-guide/cognito-creds-provider.md") in the AWS SDK for .NET Developer Guide
- [Specify Credentials Programmatically](https://aws.github.io/aws-sdk-go-v2/docs/configuring-sdk/#specify-credentials-programmatically "https://aws.github.io/aws-sdk-go-v2/docs/configuring-sdk/#specify-credentials-programmatically") in the AWS SDK for Go Developer Guide
- [Supply temporary
  credentials in code](../../../sdk-for-java/latest/developer-guide/credentials-explicit.md "../../../sdk-for-java/latest/developer-guide/credentials-explicit.md") in the AWS SDK for Java 2.x Developer Guide
- [assumeRoleWithWebIdentityCredentialProvider](../../../sdk-for-php/v3/developer-guide/guide_credentials_provider.md#assume-role-with-web-identity-provider "../../../sdk-for-php/v3/developer-guide/guide_credentials_provider.md#assume-role-with-web-identity-provider") provider in the AWS SDK for PHP Developer
  Guide
- [Assume Role With Web Identity Provider](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#assume-role-with-web-identity-provider "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#assume-role-with-web-identity-provider") in the AWS SDK for Python (Boto3)
  documentation
- [Specifying
  your credentials and default region](../../../sdk-for-rust/latest/dg/credentials.md "../../../sdk-for-rust/latest/dg/credentials.md") in the AWS SDK for Rust Developer Guide
  The following sections provide example code in some legacy AWS SDKs.

You can use Amazon Cognito to deliver temporary, limited-privilege credentials to your
application, so that your users can access AWS resources. Amazon Cognito supports both
authenticated and unauthenticated identities. To provide AWS credentials to your app,
follow the steps below.

To use a Amazon Cognito identity pool in an Android app, set up AWS Amplify. For more
information, see [Authentication](https://docs.amplify.aws/lib/auth/getting-started/q/platform/android/ "https://docs.amplify.aws/lib/auth/getting-started/q/platform/android/") in the _Amplify Dev
Center_.

**Retrieving an Amazon Cognito identity**

If you're allowing unauthenticated users, you can retrieve a unique Amazon Cognito identifier
(identity ID) for your end user immediately. If you're authenticating users, you can
retrieve the identity ID after you've set the login tokens in the credentials
provider:

```
String identityId = credentialsProvider.getIdentityId();
Log.d("LogTag", "my ID is " + identityId);

```

###### Note

Do not call `getIdentityId()`, `refresh()`, or
`getCredentials()` in the main thread of your application. As of Android
3.0 (API Level 11), your app will automatically fail and throw a [NetworkOnMainThreadException](https://developer.android.com/reference/android/os/NetworkOnMainThreadException.html "https://developer.android.com/reference/android/os/NetworkOnMainThreadException.html") if you perform network I/O on the main
application thread. You must move your code to a background thread using
`AsyncTask`. For more information, consult the [Android documentation](https://developer.android.com/training/basics/network-ops/connecting.html#AsyncTask "https://developer.android.com/training/basics/network-ops/connecting.html#AsyncTask"). You can also call `getCachedIdentityId()`
to retrieve an ID, but only if one is already cached locally. Otherwise, the method will
return null.

You can use Amazon Cognito to deliver temporary, limited-privilege credentials to your
application, so that your users can access AWS resources. Amazon Cognito identity pools support
both authenticated and unauthenticated identities. To provide AWS credentials to your
app, complete the following steps.

To use a Amazon Cognito identity pool in an iOS app, set up AWS Amplify. For more
information, see [Swift
Authentication](https://docs.amplify.aws/lib/auth/getting-started/q/platform/ios/ "https://docs.amplify.aws/lib/auth/getting-started/q/platform/ios/") and [Flutter
Authentication](https://docs.amplify.aws/lib/auth/getting-started/q/platform/flutter/ "https://docs.amplify.aws/lib/auth/getting-started/q/platform/flutter/") in the _Amplify Dev
Center_.

**Retrieving an Amazon Cognito identity**

You can retrieve a unique Amazon Cognito identifier (identity ID) for your end user immediately
if you're allowing unauthenticated users or after you've set the login tokens in the
credentials provider if you're authenticating users:

```
// Retrieve your Amazon Cognito ID
[[credentialsProvider getIdentityId] continueWithBlock:^id(AWSTask *task) {
    if (task.error) {
        NSLog(@"Error: %@", task.error);
    }
    else {
        // the task result will contain the identity id
        NSString *cognitoId = task.result;
    }
    return nil;
}];
```

###### Note

`getIdentityId` is an asynchronous call. If an identity ID is already set on
your provider, you can call `credentialsProvider.identityId` to retrieve that
identity, which is cached locally. However, if an identity ID is not set on your
provider, calling `credentialsProvider.identityId` will return
`nil`. For more information, consult the [Amplify iOS SDK reference](https://github.com/aws-amplify/aws-sdk-ios "https://github.com/aws-amplify/aws-sdk-ios").

You can use Amazon Cognito to deliver temporary, limited-privilege credentials to your
application so that your users can access AWS resources. Amazon Cognito supports both
authenticated and unauthenticated identities. To provide AWS credentials to your app,
follow the steps below.

To use a Amazon Cognito identity pool in an iOS app, set up AWS Amplify. For more
information, see [Swift
Authentication](https://docs.amplify.aws/lib/auth/getting-started/q/platform/ios/ "https://docs.amplify.aws/lib/auth/getting-started/q/platform/ios/") in the _Amplify Dev
Center_.

**Retrieving an Amazon Cognito identity**

You can retrieve a unique Amazon Cognito identifier (identity ID) for your end user immediately
if you're allowing unauthenticated users or after you've set the login tokens in the
credentials provider if you're authenticating users:

```
// Retrieve your Amazon Cognito ID
credentialsProvider.getIdentityId().continueWith(block: { (task) -> AnyObject? in
    if (task.error != nil) {
        print("Error: " + task.error!.localizedDescription)
    }
    else {
        // the task result will contain the identity id
        let cognitoId = task.result!
        print("Cognito id: \(cognitoId)")
    }
    return task;
})
```

###### Note

`getIdentityId` is an asynchronous call. If an identity ID is already set on
your provider, you can call `credentialsProvider.identityId` to retrieve that
identity, which is cached locally. However, if an identity ID is not set on your
provider, calling `credentialsProvider.identityId` will return
`nil`. For more information, consult the [Amplify iOS SDK reference](https://github.com/aws-amplify/aws-sdk-ios "https://github.com/aws-amplify/aws-sdk-ios").

If you have not yet created one, create an identity pool in the [Amazon Cognito console](https://console.aws.amazon.com/cognito "https://console.aws.amazon.com/cognito") before using
`AWS.CognitoIdentityCredentials`.

After you configure an identity pool with your identity providers, you can use
`AWS.CognitoIdentityCredentials` to authenticate users. To configure your
application credentials to use `AWS.CognitoIdentityCredentials`, set the
`credentials` property of either `AWS.Config` or a per-service
configuration. The following example uses `AWS.Config`:

```
// Set the region where your identity pool exists (us-east-1, eu-west-1)
AWS.config.region = 'us-east-1';

// Configure the credentials provider to use your identity pool
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: 'IDENTITY_POOL_ID',
    Logins: { // optional tokens, used for authenticated login
        'graph.facebook.com': 'FBTOKEN',
        'www.amazon.com': 'AMAZONTOKEN',
        'accounts.google.com': 'GOOGLETOKEN',
        'appleid.apple.com': 'APPLETOKEN'
    }
});

// Make the call to obtain credentials
AWS.config.credentials.get(function(){

    // Credentials will be available when this function is called.
    var accessKeyId = AWS.config.credentials.accessKeyId;
    var secretAccessKey = AWS.config.credentials.secretAccessKey;
    var sessionToken = AWS.config.credentials.sessionToken;

});
```

The optional `Logins` property is a map of identity provider names to the
identity tokens for those providers. How you get the token from your identity provider
depends on the provider you use. For example, if Facebook is one of your identity
providers, you might use the `FB.login` function from the [Facebook SDK](https://developers.facebook.com/docs/facebook-login/web "https://developers.facebook.com/docs/facebook-login/web") to
get an identity provider token:

```
FB.login(function (response) {
    if (response.authResponse) { // logged in
        AWS.config.credentials = new AWS.CognitoIdentityCredentials({
          IdentityPoolId: 'us-east-1:1699ebc0-7900-4099-b910-2df94f52a030',
          Logins: {
            'graph.facebook.com': response.authResponse.accessToken
          }
        });

        console.log('You are now logged in.');
    } else {
        console.log('There was a problem logging you in.');
    }
});
```

**Retrieving an Amazon Cognito identity**

You can retrieve a unique Amazon Cognito identifier (identity ID) for your end user immediately
if you're allowing unauthenticated users or after you've set the login tokens in the
credentials provider if you're authenticating users:

```
var identityId = AWS.config.credentials.identityId;

```

You can use Amazon Cognito to deliver temporary, limited-privilege credentials to your
application, so that your users can access AWS resources. Amazon Cognito supports both
authenticated and unauthenticated identities. To provide AWS credentials to your app,
follow the steps below.

The [AWS SDK for
Unity](../../../mobile/sdkforunity/developerguide/what-is-unity-plugin.md "../../../mobile/sdkforunity/developerguide/what-is-unity-plugin.md") is now part of the [SDK for .NET](../../../sdk-for-net/v3/developer-guide/welcome.md "../../../sdk-for-net/v3/developer-guide/welcome.md"). To get started with
Amazon Cognito in the SDK for .NET, see [Amazon Cognito credentials
provider](../../../sdk-for-net/v3/developer-guide/cognito-creds-provider.md "../../../sdk-for-net/v3/developer-guide/cognito-creds-provider.md") in the AWS SDK for .NET Developer Guide. Or see [Amplify Dev Center](https://docs.amplify.aws/ "https://docs.amplify.aws/") for options for building an
app with AWS Amplify.

**Retrieving an Amazon Cognito identity**

You can retrieve a unique Amazon Cognito identifier (identity ID) for your end user
immediately if you're allowing unauthenticated users or after you've set the login tokens
in the credentials provider if you're authenticating users:

```
credentials.GetIdentityIdAsync(delegate(AmazonCognitoIdentityResult<string> result) {
    if (result.Exception != null) {
        //Exception!
    }
    string identityId = result.Response;
});
```

You can use Amazon Cognito to deliver temporary, limited-privilege credentials to your
application so that your users can access AWS resources. Amazon Cognito supports both
authenticated and unauthenticated identities. To provide AWS credentials to your app,
follow the steps below.

The [AWS SDK for Xamarin](../../../mobile/sdkforxamarin/developerguide/Welcome.md "../../../mobile/sdkforxamarin/developerguide/Welcome.md") is now part of the [SDK for .NET](../../../sdk-for-net/v3/developer-guide/welcome.md "../../../sdk-for-net/v3/developer-guide/welcome.md"). To get started with
Amazon Cognito in the SDK for .NET, see [Amazon Cognito credentials
provider](../../../sdk-for-net/v3/developer-guide/cognito-creds-provider.md "../../../sdk-for-net/v3/developer-guide/cognito-creds-provider.md") in the AWS SDK for .NET Developer Guide. Or see [Amplify Dev Center](https://docs.amplify.aws/ "https://docs.amplify.aws/") for options for building an
app with AWS Amplify.

###### Note

**Note:** If you created your identity pool before February
2015, you must reassociate your roles with your identity pool in order to use this
constructor without the roles as parameters. To do so, open the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"), choose **Manage
identity pools**, select your identity pool, choose **Edit identity Pool**, specify your authenticated and unauthenticated roles,
and save the changes.

**Retrieving an Amazon Cognito identity**

You can retrieve a unique Amazon Cognito identifier (identity ID) for your end user
immediately if you're allowing unauthenticated users or after you've set the login tokens
in the credentials provider if you're authenticating users:

```
var identityId = await credentials.GetIdentityIdAsync();
```
