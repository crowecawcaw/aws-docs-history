# Using social identity providers with a

user pool

Your web and mobile app users can sign in through social identity providers (IdP) like
Facebook, Google, Amazon, and Apple. With the built-in hosted web UI, Amazon Cognito provides
token handling and management for all authenticated users. This way, your backend
systems can standardize on one set of user pool tokens. You must enable managed login to
integrate with supported social identity providers. When Amazon Cognito builds your managed login
pages, it creates OAuth 2.0 endpoints that Amazon Cognito and your OIDC and social IdPs use to
exchange information. For more information, see the [Amazon Cognito user pools Auth API reference](cognito-userpools-server-contract-reference.md "cognito-userpools-server-contract-reference.md").

You can add a social IdP in the AWS Management Console, or you can use the AWS CLI or Amazon Cognito API.

###### Note

Sign-in through a third party (federation) is available in Amazon Cognito user pools. This
feature is independent of federation through Amazon Cognito identity pools (federated
identities).

###### Topics

- [Set up a social IdP developer
  account and application](#cognito-user-pools-social-idp-step-1 "#cognito-user-pools-social-idp-step-1")
- [Configure your user pool with
  a social IdP](#cognito-user-pools-social-idp-step-2 "#cognito-user-pools-social-idp-step-2")
- [Test your social IdP
  configuration](#cognito-user-pools-social-idp-step-3 "#cognito-user-pools-social-idp-step-3")

## Set up a social IdP developer

account and application

Before you create a social IdP with Amazon Cognito, you must register your application with
the social IdP to receive a client ID and client secret.

Facebook
For the latest information about configuration of Meta developer
accounts and authentication, see [Meta App
Development](https://developers.facebook.com/docs/development "https://developers.facebook.com/docs/development").

###### How to register an application with Facebook/Meta

1. Create a [developer account with Facebook](https://developers.facebook.com/docs/facebook-login "https://developers.facebook.com/docs/facebook-login").
2. [Sign in](https://developers.facebook.com/ "https://developers.facebook.com/")
   with your Facebook credentials.
3. From the **My Apps** menu, choose
   **Create New App**.
4. Enter a name for your Facebook app, and then choose
   **Create App ID**.
5. On the left navigation bar, choose
   **Settings**, and then
   **Basic**.
6. Note the **App ID** and the **App
   Secret**. You will use them in the next
   section.
7. Choose **+ Add Platform** from the bottom of
   the page.
8. Choose **Website**.
9. Under **Website**, enter the path to the
   sign-in page for your app into **Site
   URL**.

```

https://`mydomain.auth.us-east-1.amazoncognito.com`/login?response_type=code&client_id=`1example23456789`&redirect_uri=`https://www.example.com`

```

10. Choose **Save changes**.
11. Enter the path to the root of your user pool domain into
    **App Domains**.

```
`https://`mydomain.auth.us-east-1.amazoncognito.com``
```

12. Choose **Save changes**.
13. From the navigation bar choose **Add
    Product** and choose **Set up**
    for the **Facebook Login** product.
14. From the navigation bar choose **Facebook
    Login** and then
    **Settings**.

Enter the path to the `/oauth2/idpresponse`
endpoint for your user pool domain into **Valid OAuth
Redirect URIs**.

```

`https://`mydomain.auth.us-east-1.amazoncognito.com`/oauth2/idpresponse`

```

15. Choose **Save changes**.

Login with Amazon
For the latest information about configuration of Login with Amazon
developer accounts and authentication, see [Login with Amazon Documentation](https://developer.amazon.com/docs/login-with-amazon/documentation-overview.html "https://developer.amazon.com/docs/login-with-amazon/documentation-overview.html").

###### How to register an application with Login with Amazon

1. Create a [developer account with Amazon](https://developer.amazon.com/login-with-amazon "https://developer.amazon.com/login-with-amazon").
2. [Sign in](https://developer.amazon.com/lwa/sp/overview.html "https://developer.amazon.com/lwa/sp/overview.html") with your Amazon credentials.
3. You need to create an Amazon security profile to receive the
   Amazon client ID and client secret.

Choose **Apps and Services** from navigation
bar at the top of the page and then choose **Login with
Amazon**. 4. Choose **Create a Security Profile**. 5. Enter a **Security Profile Name**, a
**Security Profile Description**, and a
**Consent Privacy Notice URL**. 6. Choose **Save**. 7. Choose **Client ID** and **Client
Secret** to show the client ID and secret. You will
use them in the next section. 8. Hover over the gear icon and choose **Web
Settings**, and then choose
**Edit**. 9. Enter your user pool domain into **Allowed
Origins**.

```
`https://`mydomain.auth.us-east-1.amazoncognito.com``
```

10. Enter your user pool domain with the
    `/oauth2/idpresponse` endpoint into
    **Allowed Return URLs**.

```
`https://`mydomain.auth.us-east-1.amazoncognito.com`/oauth2/idpresponse`
```

11. Choose **Save**.

Google
For more information about OAuth 2.0 in the Google Cloud platform, see
[Learn about authentication & authorization](https://developers.google.com/workspace/guides/auth-overview "https://developers.google.com/workspace/guides/auth-overview") in the
Google Workspace for Developers documentation.

###### How to register an application with Google

1. Create a [developer account with Google](https://developers.google.com/identity "https://developers.google.com/identity").
2. Sign in to the [Google
   Cloud Platform console](https://console.cloud.google.com/home/dashboard "https://console.cloud.google.com/home/dashboard").
3. From the top navigation bar, choose **Select a
   project**. If you already have a project in the
   Google platform, this menu displays your default project
   instead.
4. Select **NEW PROJECT**.
5. Enter a name for your product and then choose
   **CREATE**.
6. On the left navigation bar, choose **APIs and
   Services**, then **Oauth consent
   screen**.
7. Enter App information, an **App domain**,
   **Authorized domains**, and
   **Developer contact information**. Your
   **Authorized domains** must include
   `amazoncognito.com` and the root of your custom
   domain, for example `example.com`. Choose
   **SAVE AND CONTINUE**.
8. 1. Under **Scopes**, choose **Add or
      remove scopes**, and choose, at minimum, the
      following OAuth scopes.

   1. `.../auth/userinfo.email`
   1. `.../auth/userinfo.profile`
   1. openid

9. Under **Test users**, choose **Add
   users**. Enter your email address and any other
   authorized test users, then choose **SAVE AND
   CONTINUE**.
10. Expand the left navigation bar again, and choose
    **APIs and Services**, then
    **Credentials**.
11. Choose **CREATE CREDENTIALS**, then
    **OAuth client ID**.
12. Choose an **Application type** and give your
    client a **Name**.
13. Under **Authorized JavaScript origins**,
    choose **ADD URI**. Enter your user pool
    domain.

```
`https://`mydomain.auth.us-east-1.amazoncognito.com``
```

14. Under **Authorized redirect URIs**, choose
    **ADD URI**. Enter the path to the
    `/oauth2/idpresponse` endpoint of your user pool
    domain.

```
`https://`mydomain.auth.us-east-1.amazoncognito.com`/oauth2/idpresponse`
```

15. Choose **CREATE**.
16. Securely store the values the Google displays under
    **Your client ID** and **Your
    client secret**. Provide these values to Amazon Cognito when
    you add a Google IdP.

Sign in with Apple
For the most up-to-date information about setting up Sign in with
Apple, see [Configuring Your Environment for Sign in with Apple](https://developer.apple.com/documentation/signinwithapple/configuring-your-environment-for-sign-in-with-apple "https://developer.apple.com/documentation/signinwithapple/configuring-your-environment-for-sign-in-with-apple") in the
Apple Developer documentation.

###### How to register an application with Sign in with Apple

(SIWA)

1. Create a [developer
   account with Apple](https://developer.apple.com/programs/enroll/ "https://developer.apple.com/programs/enroll/").
2. [Sign in](https://developer.apple.com/account/#/welcome "https://developer.apple.com/account/#/welcome") with your Apple credentials.
3. On the left navigation bar, choose **Certificates,
   Identifiers & Profiles**.
4. On the left navigation bar, choose
   **Identifiers**.
5. On the **Identifiers** page, choose the
   **+** icon.
6. On the **Register a New Identifier** page,
   choose **App IDs**, and then choose
   **Continue**.
7. On the **Select a type** page, choose
   **App**, then choose
   **Continue**.
8. On the **Register an App ID** page, do the
   following:
   1. Under **Description**, enter a
      description.
   2. Under **App ID Prefix**, enter a
      **Bundle ID**. Make a note of the
      value under **App ID Prefix**. You will
      use this value after you choose Apple as your identity
      provider in [Configure your user pool with
      a social IdP](#cognito-user-pools-social-idp-step-2 "#cognito-user-pools-social-idp-step-2").
   3. Under **Capabilities**, choose
      **Sign In with Apple**, and then
      choose **Edit**.
   4. On the **Sign in with Apple: App ID
      Configuration** page, choose to set up the
      app as either primary or grouped with other App IDs, and
      then choose **Save**.
   5. Choose **Continue**.

9. On the **Confirm your App ID** page, choose
   **Register**.
10. On the **Identifiers** page, choose the
    **+** icon.
11. On the **Register a New Identifier** page,
    choose **Services IDs**, and then choose
    **Continue**.
12. On the **Register a Services ID** page, do
    the following:
    1. Under **Description**, type a
       description.
    2. Under **Identifier**, type an
       identifier. Make a note of this Services ID as you will
       need this value after you choose Apple as your identity
       provider in [Configure your user pool with
       a social IdP](#cognito-user-pools-social-idp-step-2 "#cognito-user-pools-social-idp-step-2").
    3. Choose **Continue**, then
       **Register**.

13. Choose the Services ID you just create from the Identifiers
    page.
    1. Select **Sign In with Apple**, and
       then choose **Configure**.
    2. On the **Web Authentication
       Configuration** page, select the app ID
       that you created earlier as the **Primary App
       ID**.
    3. Choose the **+** icon next to
       **Website URLs**.
    4. Under **Domains and subdomains**,
       enter your user pool domain without an
       `https://` prefix.

    ```
    ``mydomain.auth.us-east-1.amazoncognito.com``
    ```

    5. Under **Return URLs**, enter the path
       to the `/oauth2/idpresponse` endpoint of your
       user pool domain.

    ```
    `https://`mydomain.auth.us-east-1.amazoncognito.com`/oauth2/idpresponse`
    ```

    6. Choose **Next**, and then
       **Done**. You don't need to verify
       the domain.
    7. Choose **Continue**, and then choose
       **Save**.

14. On the left navigation bar, choose
    **Keys**.
15. On the **Keys** page, choose the
    **+** icon.
16. On the **Register a New Key** page, do the
    following:
    1. Under **Key Name**, enter a key name.
    2. Choose **Sign In with Apple**, and
       then choose **Configure**.
    3. On the **Configure Key** page and
       select the app ID that you created earlier as the
       **Primary App ID**. Choose
       **Save**.
    4. Choose **Continue**, and then choose
       **Register**.

17. On the **Download Your Key** page, choose
    **Download** to download the private key
    and note the **Key ID** shown, and then choose
    **Done**. You will need this private key
    and the **Key ID** value shown on this page
    after you choose Apple as your identity provider in [Configure your user pool with
    a social IdP](#cognito-user-pools-social-idp-step-2 "#cognito-user-pools-social-idp-step-2").

## Configure your user pool with

a social IdP

###### To configure a user pool social IdP with the AWS Management Console

1. Go to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). If prompted, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list or create a user pool.
4. Choose the **Social and external providers** menu and
   then select **Add an identity provider**.
5. Choose a social IdP: **Facebook**,
   **Google**, **Login with Amazon**, or
   **Sign in with Apple**.
6. Choose from the following steps, based on your choice of social
   IdP:
   - **Google** and **Login with Amazon** — Enter the **app
     client ID** and **app client secret**
     generated in the previous section.
   - **Facebook** — Enter the
     **app client ID** and **app client
     secret** generated in the previous section, and then
     choose an API version (for example, version 2.12). We recommend that
     you choose the latest possible version, as each Facebook API has a
     lifecycle and discontinuation date. Facebook scopes and attributes
     can vary between API versions. We recommend that you test your
     social identity log in with Facebook to make sure that federation
     works as you intend.
   - **Sign In with Apple** — Enter
     the **Services ID**, **Team ID**,
     **Key ID**, and **private
     key** generated in the previous section.

7. Enter the names of the **Authorized scopes**
   you want to use. Scopes define which user attributes (such as
   `name` and `email`) you want to access with your
   app. For Facebook, these should be separated by commas. For Google and Login
   with Amazon, they should be separated by spaces. For Sign in with Apple,
   select the check boxes for the scopes you want access to.

| Social identity provider | Example scopes          |
| ------------------------ | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | --------------- | ----------------------------------------------------------------------------------------------------------- |
| Facebook                 | `public_profile, email` |
| Google                   | `profile email openid`  |
| Login with Amazon        | `profile postal_code`   |
| Sign in with Apple       | `email name`            | Your app user is prompted to consent to providing these attributes to your app. For more information about social provider scopes, see the documentation from Google, Facebook, Login with Amazon, or Sign in with Apple. With Sign in with Apple, the following are user scenarios where scopes might not be returned: <br>• An end user encounters failures after leaving Apple’s sign in page (can be from Internal failures within Amazon Cognito or anything written by the developer) <br>• The service ID identifier is used across user pools and/or other authentication services <br>• A developer adds additional scopes after the end user has signed in before (no new information is retrieved) <br>• A developer deletes the user and then the user signs in again without removing the app from their Apple ID profile 8. Map attributes from your IdP to your user pool. For more information, see [Specifying Identity Provider Attribute Mappings for Your User Pool](cognito-user-pools-specifying-attribute-mapping.md "cognito-user-pools-specifying-attribute-mapping.md"). 9. Choose **Create**. 10. From the **App clients** menu, select an app client from the list. To add the new social identity provider to the app client, navigate to the **Login pages** tab and select **Edit** on **Managed login pages configuration**. 11. Choose **Save changes**. ## Test your social IdP configuration In your application, you must invoke a browser in the user's client so that they can sign in with their social provider. Test sign-in with your social provider after you have completed the setup procedures in the preceding sections. The following example URL loads the sign-in page for your user pool with a prefix domain. `` https://`mydomain.auth.us-east-1.amazoncognito.com`/oauth2/authorize?response_type=code&client_id=`1example23456789`&redirect_uri=`https://www.example.com` `` This link is the page that Amazon Cognito directs you to when you go to the **App clients** menu, select an app client, navigate to the **Login pages** tab, and select **View login page**. For more information about user pool domains, see [Configuring a user pool domain](cognito-user-pools-assign-domain.md "cognito-user-pools-assign-domain.md"). For more information about app clients, including client IDs and callback URLs, see [Application-specific settings with app clients](user-pool-settings-client-apps.md "user-pool-settings-client-apps.md"). The following example link sets up silent redirect to a social provider from the [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md") with an `identity_provider` query parameter. This URL bypasses interactive user pool sign-in with managed login and goes directly to the IdP sign-in page. ``` https://`mydomain.auth.us-east-1.amazoncognito.com`/oauth2/authorize?identity_provider=`Facebook | Google | LoginWithAmazon | SignInWithApple`&response_type=code&client_id=`1example23456789`&redirect_uri=`https://www.example.com` ``` |
