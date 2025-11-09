# Add social sign-in to your user

pool

Providing users with the ability to sign in to your application through their existing
public, or social, identity providers can improve their authentication experience. Amazon Cognito user pools
integrate with popular social identity providers (IdPs) like Facebook, Google, Amazon, and
Apple, giving your users convenient sign-in options that they are already familiar
with.

When you set up social sign-in, you are giving your users an alternative to creating a
dedicated account just for your application. This can improve conversion rates and make the
sign-up process more seamless. From the user's perspective, they can apply their existing
social credentials to quickly authenticate, without the friction of remembering another
username and password.

Configuring a social IdP in your user pool involves a few key steps. You must register
your application with the social provider to obtain a client ID and secret. Then you can add
the social IdP configuration to your user pool, specifying the scopes that you want to
request and the user pool attributes that you want to map from IdP attributes. At runtime,
Amazon Cognito handles the token exchange with the provider, maps user attributes, and issues tokens
to your application in the shared user pool format.

## Register with a social IdP

Before you create a social IdP with Amazon Cognito, you must register your application with the
social IdP to receive a client ID and client secret.

1. Create a [developer account with Facebook](https://developers.facebook.com/docs/facebook-login "https://developers.facebook.com/docs/facebook-login").
2. [Sign in](https://developers.facebook.com/ "https://developers.facebook.com/") with your
   Facebook credentials.
3. From the **My Apps** menu, choose **Create New
   App**.

If you don't have an existing Facebook app, you will see a different option.
Choose **Create App**. 4. On the **Create an app** page, choose a use case for your
app, and then choose **Next**. 5. Enter a name for your Facebook app and choose **Create
App**. 6. On the left navigation bar, choose **App Settings**, and then
choose **Basic**. 7. Note the **App ID** and the **App Secret**.
You will use them in the next section. 8. Choose **+ Add platform** from the bottom of the page. 9. On the **Select Platform** screen, select your platforms, and
then choose **Next**. 10. Choose **Save changes**. 11. For **App Domains**, enter your user pool domain.

```
https://`your_user_pool_domain`
```

12. Choose **Save changes**.
13. From the navigation bar, choose **Products**, and then choose
    **Configure** from **Facebook Login**.
14. From the **Facebook Login**
    **Configure** menu, choose **Settings**.

Enter your redirect URL into **Valid OAuth Redirect URIs**.
The redirect URL consists of your user pool domain with the
`/oauth2/idpresponse` endpoint.

```
https://`your_user_pool_domain`/oauth2/idpresponse
```

15. Choose **Save changes**.
1. Create a [developer
   account with Amazon](https://developer.amazon.com/login-with-amazon "https://developer.amazon.com/login-with-amazon").
1. [Sign in](https://developer.amazon.com/lwa/sp/overview.html "https://developer.amazon.com/lwa/sp/overview.html")
   with your Amazon credentials.
1. You need to create an Amazon security profile to receive the Amazon client ID
   and client secret.

Choose **Apps and Services** from the navigation bar at the
top of the page, and then choose **Login with Amazon**. 4. Choose **Create a Security Profile**. 5. Enter a **Security Profile Name**, a **Security
Profile Description**, and a **Consent Privacy Notice
URL**. 6. Choose **Save**. 7. Choose **Client ID** and **Client Secret**
to show the client ID and secret. You will use them in the next section. 8. Hover over the gear icon and choose **Web Settings**, and
then choose **Edit**. 9. Enter your user pool domain into **Allowed Origins**.

```
`https://`<your-user-pool-domain>``
```

10. Enter your user pool domain with the `/oauth2/idpresponse`
    endpoint into **Allowed Return URLs**.

```
`https://`<your-user-pool-domain>`/oauth2/idpresponse`
```

11. Choose **Save**.
    For more information about OAuth 2.0 in the Google Cloud platform, see [Learn about
    authentication & authorization](https://developers.google.com/workspace/guides/auth-overview "https://developers.google.com/workspace/guides/auth-overview") in the Google Workspace for Developers
    documentation.

1. Create a [developer account
   with Google](https://developers.google.com/identity "https://developers.google.com/identity").
1. Sign in to the [Google Cloud Platform console](https://console.cloud.google.com/home/dashboard "https://console.cloud.google.com/home/dashboard").
1. From the top navigation bar, choose **Select a project**. If
   you already have a project in the Google platform, this menu displays your default
   project instead.
1. Select **NEW PROJECT**.
1. Enter a name for your product and then choose
   **CREATE**.
1. On the left navigation bar, choose **APIs and Services**, and
   then choose **Oauth consent screen**.
1. Enter the app information, an **App domain**,
   **Authorized domains**, and **Developer contact
   information**. Your **Authorized domains** must
   include `amazoncognito.com` and the root of your custom domain. For
   example: `example.com`. Choose **SAVE AND
   CONTINUE**.
1. 1. Under **Scopes**, choose **Add or remove
      scopes**, and then choose, at a minimum, the following OAuth
      scopes.

   1. `.../auth/userinfo.email`
   1. `.../auth/userinfo.profile`
   1. openid

1. Under **Test users**, choose **Add users**.
   Enter your email address and any other authorized test users, and then choose
   **SAVE AND CONTINUE**.
1. Expand the left navigation bar again, choose **APIs and
   Services**, and then choose **Credentials**.
1. Choose **CREATE CREDENTIALS**, and then choose
   **OAuth client ID**.
1. Choose an **Application type** and give your client a
   **Name**.
1. Under **Authorized JavaScript origins**, choose **ADD
   URI**. Enter your user pool domain.

```
`https://`<your-user-pool-domain>``
```

14. Under **Authorized redirect URIs**, choose **ADD
    URI**. Enter the path to the `/oauth2/idpresponse` endpoint
    of your user pool domain.

```
`https://`<your-user-pool-domain>`/oauth2/idpresponse`
```

15. Choose **CREATE**.
16. Securely store the values that Google displays under **Your client
    ID** and **Your client secret**. Provide these values
    to Amazon Cognito when you add a Google IdP.
    For more information about setting up Sign in with Apple, see [Configuring Your Environment for Sign in with Apple](https://developer.apple.com/documentation/signinwithapple/configuring-your-environment-for-sign-in-with-apple "https://developer.apple.com/documentation/signinwithapple/configuring-your-environment-for-sign-in-with-apple") in the Apple Developer
    documentation.

17. Create a [developer
    account with Apple](https://developer.apple.com/programs/enroll/ "https://developer.apple.com/programs/enroll/").
18. [Sign in](https://developer.apple.com/account/#/welcome "https://developer.apple.com/account/#/welcome")
    with your Apple credentials.
19. On the left navigation bar, choose **Certificates, Identifiers &
    Profiles**.
20. On the left navigation bar, choose **Identifiers**.
21. On the **Identifiers** page, choose the
    **+** icon.
22. On the **Register a New Identifier** page, choose
    **App IDs**, and then choose
    **Continue**.
23. On the **Select a type** page, choose
    **App**, and then choose **Continue**.
24. On the **Register an App ID** page, do the following:
    1.  Under **Description**, enter a description.
    2.  Under **App ID Prefix**, enter a **Bundle
        ID**. Make a note of the value under **App ID
        Prefix**. You will use this value after you choose Apple as your
        identity provider in [Configure your user pool with
        a social IdP](cognito-user-pools-social-idp.md#cognito-user-pools-social-idp-step-2 "cognito-user-pools-social-idp.md#cognito-user-pools-social-idp-step-2").
    3.  Under **Capabilities**, choose **Sign In with
        Apple**, and then choose **Edit**.
    4.  On the **Sign in with Apple: App ID Configuration** page,
        choose to set up the app as either primary or grouped with other App IDs, and
        then choose **Save**.
    5.  Choose **Continue**.

25. On the **Confirm your App ID** page, choose
    **Register**.
26. On the **Identifiers** page, choose the
    **+** icon.
27. On the **Register a New Identifier** page, choose
    **Services IDs**, and then choose
    **Continue**.
28. On the **Register a Services ID** page, do the
    following:
    1.  Under **Description**, enter a description.
    2.  Under **Identifier**, enter an identifier. Make a note of
        this Services ID because you'll need this value after you choose Apple as your
        identity provider in [Configure your user pool with
        a social IdP](cognito-user-pools-social-idp.md#cognito-user-pools-social-idp-step-2 "cognito-user-pools-social-idp.md#cognito-user-pools-social-idp-step-2").
    3.  Choose **Continue** and then choose
        **Register**.

29. Choose the Services ID that you just created from the Identifiers page.
    1.  Select **Sign In with Apple**, and then choose
        **Configure**.
    2.  On the **Web Authentication Configuration** page, select
        the app ID that you created earlier as the **Primary App
        ID**.
    3.  Choose the **+** icon next to **Website
        URLs**.
    4.  Under **Domains and subdomains**, enter your user pool
        domain without an `https://` prefix.

    ```
    ``<your-user-pool-domain>``
    ```

    5.  Under **Return URLs**, enter the path to the
        `/oauth2/idpresponse` endpoint of your user pool domain.

    ```
    `https://`<your-user-pool-domain>`/oauth2/idpresponse`
    ```

    6.  Choose **Next**, and then choose
        **Done**. You don't need to verify the domain.
    7.  Choose **Continue**, and then choose
        **Save**.

30. On the left navigation bar, choose **Keys**.
31. On the **Keys** page, choose the **+**
    icon.
32. On the **Register a New Key** page, do the following:
    1.  Under **Key Name**, enter a key name.
    2.  Choose **Sign In with Apple**, and then choose
        **Configure**.
    3.  On the **Configure Key** page, select the app ID that you
        created earlier as the **Primary App ID**. Choose
        **Save**.
    4.  Choose **Continue**, and then choose
        **Register**.

33. On the **Download Your Key** page, choose
    **Download** to download the private key, note the
    **Key ID** shown, and then choose **Done**.
    You will need this private key and the **Key ID** value shown on
    this page after you choose Apple as your identity provider in [Configure your user pool with
    a social IdP](cognito-user-pools-social-idp.md#cognito-user-pools-social-idp-step-2 "cognito-user-pools-social-idp.md#cognito-user-pools-social-idp-step-2").

## Add a social IdP to your user

pool

In this section, you configure a social IdP in your user pool using the client ID and
client secret from the previous section.

###### To configure a user pool social identity provider with the AWS Management Console

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). You
   might be prompted for your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list, or [create a user
   pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md").
4. Choose the **Social and external providers** menu. Locate
   **Federated sign-in** and select **Add an identity
   provider**.
5. Choose a social identity provider: **Facebook**,
   **Google**, **Login with Amazon**, or
   **Sign in with Apple**.
6. Choose from the following steps, based on your choice of social identity
   provider:
   - **Google** and **Login with
     Amazon** – Enter the **app client ID** and
     **app client secret** that was generated in the previous
     section.
   - **Facebook** – Enter the **app
     client ID** and **app client secret** that was
     generated in the previous section, and then choose an API version (for example,
     version 2.12). We recommend choosing the latest possible version—each
     Facebook API has a lifecycle and deprecation date. Facebook scopes and attributes
     can vary between API versions. We recommend testing your social identity log in
     with Facebook to ensure that federation works as intended.
   - **Sign in with Apple** – Enter the
     **Services ID**, **Team ID**, **Key
     ID**, and **private key** that was generated in the
     previous section.

7. Enter the names of the **Authorized scopes** that you
   want to use. Scopes define which user attributes (such as `name` and
   `email`) you want to access with your app. For Facebook, these should be
   separated by commas. For Google and Login with Amazon, they should be separated by
   spaces. For Sign in with Apple, select the check boxes for the scopes you want access
   to.

| Social identity provider | Example scopes          |
| ------------------------ | ----------------------- |
| Facebook                 | `public_profile, email` |
| Google                   | `profile email openid`  |
| Login with Amazon        | `profile postal_code`   |
| Sign in with Apple       | `email name`            |

Your app user is prompted to consent to providing these attributes to your app.
For more information about social provider scopes, see the documentation from Google,
Facebook, Login with Amazon, or Sign in with Apple.

With Sign in with Apple, the following are user scenarios where scopes might not
be returned:

    * An end user encounters failures after leaving Apple’s sign in page (these can
     be from internal failures within Amazon Cognito or anything written by the
     developer).
    * The service ID identifier is used across user pools and/or other
     authentication services.
    * A developer adds additional scopes after the user signs in. Users only
     retrieve new information when they authenticate and when they refresh their
     tokens.
    * A developer deletes the user and then the user signs in again without removing
     the app from their Apple ID profile.

8. Map attributes from your identity provider to your user pool. For more
   information, see [Things to know about mappings](cognito-user-pools-specifying-attribute-mapping.md#cognito-user-pools-specifying-attribute-mapping-requirements "cognito-user-pools-specifying-attribute-mapping.md#cognito-user-pools-specifying-attribute-mapping-requirements").
9. Choose **Create**.
10. From the **App clients** menu, choose one of the app clients in
    the list and **Edit hosted UI settings**. Add the new social identity
    provider to the app client under **Identity providers**.
11. Choose **Save changes**.

## Test your social IdP

configuration

You can create a login URL by using the elements from the previous two sections.
Use it to test your social IdP configuration.

```

https://`mydomain.auth.us-east-1.amazoncognito.com`/login?response_type=code&client_id=`1example23456789`&redirect_uri=`https://www.example.com`

```

You can find your domain on the user pool **Domain name** console
page. The client_id is on the **App client settings** page. Use
your callback URL for the **redirect_uri** parameter. This is the
URL of the page where your user will be redirected after a successful
authentication.

###### Note

Amazon Cognito cancels authentication requests that do not complete within 5
minutes, and redirects the user to managed login. The page displays a
`Something went wrong` error message.
