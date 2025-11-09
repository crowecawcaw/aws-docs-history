# Create a new application in the Amazon Cognito

console

User pools add authentication options to software applications. For the easiest
getting-started experience, step into the Amazon Cognito console and follow the instructions there. The
creation process there guides you not only through setup of user pool resources, but through
setting up the initial pieces of your application.

When you're ready to begin, navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/v2/idp/user-pools "https://console.aws.amazon.com/cognito/v2/idp/user-pools") and select the button to create a new
user pool. The setup process will guide you through your configuration and
programming-language options.

###### Additional resources for authentication concepts

- [Authentication with Amazon Cognito user pools](authentication.md "authentication.md")
- [Understanding API, OIDC, and managed login pages
  authentication](authentication-flows-public-server-side.md#user-pools-API-operations "authentication-flows-public-server-side.md#user-pools-API-operations")
- [How authentication works with Amazon Cognito](cognito-how-to-authenticate.md "cognito-how-to-authenticate.md")
- [Integrating Amazon Cognito authentication and authorization with
  web and mobile apps](cognito-integrate-apps.md "cognito-integrate-apps.md")

###### To create Amazon Cognito resources for your application

1. Navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/ "https://console.aws.amazon.com/cognito/"). To assign
   permissions to your IAM principal so that they can create and manage Amazon Cognito resources,
   refer to [AWS managed policies for Amazon Cognito](security-iam-awsmanpol.md "security-iam-awsmanpol.md").
   The `AmazonCognitoPowerUser` policy is sufficient for the creation of user
   pools.
2. Select **Create user pool** from the **User pools**
   menu, or select **Get started for free in less than five
   minutes**.
3. Under **Define your application**, choose the **Application
   type** that best fits the application scenario that you want to create
   authentication and authorization services for.
4. In **Name your application**, enter a descriptive name or proceed
   with the default name.
5. You must make some basic choices under **Configure options** that
   support settings that you can't change after you create your user pool.
   1. Under **Options for sign-in identifiers**, tell us how you want
      to identify users when they sign in. You can prefer user-generated usernames, email
      addresses, or phone numbers. You can also allow a combination of multiple options.
      Amazon Cognito accepts the options that you configure here in the username field of [managed login](cognito-user-pools-managed-login.md "cognito-user-pools-managed-login.md") sign-in
      forms.
   2. Under **Required attributes for sign-up**, tell us what user
      information you want to collect when users register for a new account. In managed
      login pages, Amazon Cognito presents prompts for all required attributes.

   **Options for sign-in identifiers** influences your required
   attributes. **Username** requires email or phone attributes for each
   user so that they can receive a password-reset code in an email or SMS message.
   **Email** requires the email attribute, and **Phone
   number** requires the phone number attribute.

6. Under **Add a return URL**, enter a redirect path to your application
   for after users complete authentication. This location should be a route in your
   application that uses OpenID Connect (OIDC) libraries to process user-authentication
   outcomes. An example of a return URL for a test application is
   `https://localhost:3000/callback`. In the example NodeJS application in the
   Amazon Cognito console, this route employs [openid-client](https://www.npmjs.com/package/openid-client "https://www.npmjs.com/package/openid-client") to collect the access token and redeem it for user information.
   You'll be able to browse examples for your development platform after you create your
   resources.
7. Choose **Create your application**. Amazon Cognito creates a user pool and app
   client with default settings for your application type. You can configure additional
   options like [external identity
   providers](cognito-user-pools-identity-federation.md "cognito-user-pools-identity-federation.md") and [multi-factor
   authentication (MFA)](user-pool-settings-mfa.md#user-pool-configuring-mfa "user-pool-settings-mfa.md#user-pool-configuring-mfa") after you create your initial resources.
8. On the **Set up your application** page, you can immediately get code
   examples for your application. To explore your new user pool, scroll down and select
   **Go to overview**.
9. To add more applications in the same user pool, navigate to the **App
   clients** menu and add a new app client. This will repeat the process of
   application-focused creation, but only add a new app client to the existing user
   pool.
   After you create a user pool and one or more app clients with this process, you can start
   testing authentication operations with managed login. These quick-start options are open to
   public self sign-up. We recommend that you create a testing environment with the console
   process, then move your finalized design to production. Spend time familiarizing yourself with
   the capabilities of Amazon Cognito. Then, to move to production workloads, craft custom configurations
   and deploy them with automation tools like AWS CloudFormation and the AWS Cloud Development Kit (AWS CDK).

Amazon Cognito makes some default configurations in this process that you can't reverse. For more
information about user pool settings that you can't change and those options that you can
choose in the console, see [Updating user pool and app client
configuration](cognito-user-pool-updating.md "cognito-user-pool-updating.md").

| Setting            | Effect                                                                                                         | How to change                                                                                                         | More information                                                                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Client secret      | Requires a client secret hash in authentication requests.                                                      | Create a new app client with a **Traditional web application**<br>or \*_Machine-to-machine application_<br>• profile. | [Application-specific settings with app<br>clients](user-pool-settings-client-apps.md "user-pool-settings-client-apps.md")                                  |
| Preferred username | User pool doesn't accept the `preferred_username` attribute as an<br>alias.                                    | Create a user pool programmatically with an AWS SDK.                                                                  | [Customizing sign-in attributes](user-pool-settings-attributes.md#user-pool-settings-aliases "user-pool-settings-attributes.md#user-pool-settings-aliases") |
| Case sensitivity   | User pool usernames are case insensitive, for example `JohnD` is<br>considered to be the same user as `johnd`. | Create a user pool programmatically with an AWS SDK.                                                                  | [User pool case sensitivity](user-pool-case-sensitivity.md "user-pool-case-sensitivity.md")                                                                 |
