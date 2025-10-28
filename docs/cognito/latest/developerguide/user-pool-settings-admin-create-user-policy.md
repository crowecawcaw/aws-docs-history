# Configuring policies for user

creation

Your user pool can allow users to sign up, or you can create them as an administrator. You
can also control how much of the process of verification and confirmation after sign-up is in
the hands of your users. For example, you might want to review sign-ups and accept them based on
an external validation process. This configuration, or _admin create user
policy_, also sets the amount of time before a user can no longer confirm their user
account.

Amazon Cognito can serve the needs of your public customers as the customer identity and access
management (CIAM) platform for your software. A user pool that accepts sign-up and has an app
client, with or without managed login, creates a user profile for anyone on the internet who
knows your publicly-discoverable app client ID and requests to sign up. A signed-up user profile
can receive access and identity tokens and can access resources that you've authorized for your
app. Before you activate sign-up in your user pool, review your options and ensure that your
configuration complies with your security standards. Set **Enable
self-registration** and `AllowAdminCreateUserOnly`, described in the
following procedures, with care.

AWS Management Console
The **Sign-up** menu of your user pool contains some of the settings
for sign-up and administrative creation of users in your user pool.

###### To configure the sign-up experience

1. In **Cognito-assisted verification and confirmation**, choose
   whether you want to **Allow Cognito to automatically send messages to verify
   and confirm**. With this setting enabled, Amazon Cognito sends an email or SMS
   message to new users with a code that they must present to your user pool. This
   confirms their ownership of the email address or phone number, setting the equivalent
   attribute as verified and confirming the user account for sign-in. The
   **Attributes to verify** that you choose determine the delivery
   methods and destinations of the verification messages.
2. **Verifying attribute changes** isn't significant when you're
   creating users, but relates to attribute verification. You can permit users who have
   changed but not yet verified their [sign-in attributes](user-pool-settings-attributes.md#user-pool-settings-aliases.title "user-pool-settings-attributes.md#user-pool-settings-aliases.title") to continue to sign in either with their new attribute
   value or with their original. For more information, see [Verifying when users
   change their email or phone number](signing-up-users-in-your-app.md#verifying-when-users-change-their-email-or-phone-number "signing-up-users-in-your-app.md#verifying-when-users-change-their-email-or-phone-number").
3. **Required attributes** displays the attributes that must be
   provided a value before a user can sign up or you can create a user. You can only set
   required attributes when you create a user pool.
4. **Custom attributes** are important to the user creation and
   sign-up process because you can only set a value for _immutable_ custom attributes when you first create a user. For more
   information about custom attributes, see [Custom attributes](user-pool-settings-attributes.md#user-pool-settings-custom-attributes "user-pool-settings-attributes.md#user-pool-settings-custom-attributes").
5. In **Self-service sign-up**, select **Enable
   self-registration** if you want users to be able to generate a new account
   with the [unauthenticated](user-pools-API-operations.md#user-pool-apis-auth-unauth "user-pools-API-operations.md#user-pool-apis-auth-unauth")
   `SignUp` API. If you disable self-registration, you can only create new
   users as an administrator, in the Amazon Cognito console or with [AdminCreateUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.md") API requests. In a user pool where self-registration is
   inactive, [SignUp](../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md "../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md") API requests return `NotAuthorizedException` and managed
   login doesn't display a **Sign up** link.

For user pools where you plan to create users as an administrator, you can configure
the duration of their temporary passwords in the setting in the **Authentication
methods** menu under **Temporary passwords set by administrators expire
in**.

Another important element of the creation of users as an administrator is the
invitation message. When you create a new user, Amazon Cognito sends them a message with a link to
your app so that they can sign in for the first time. Customize this message template in
the **Authentication methods** menu under **Message
templates**.

You can configure [confidential app clients](user-pool-settings-client-apps.md#user-pool-settings-client-app-client-types.title "user-pool-settings-client-apps.md#user-pool-settings-client-app-client-types.title"), typically web applications, with a client secret that
prevents sign-up without the app client secret. As a security best practice, do not
distribute app client secrets in public app clients, typically mobile apps. You can create
app clients with client secrets in the **App clients** menu of the Amazon Cognito
console.

Amazon Cognito user pools API
You can programmatically set the parameters for creation of users in a user pool in a
[CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") or [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md") API request.

The [AdminCreateUserConfig](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-AdminCreateUserConfig "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-AdminCreateUserConfig") element sets values for the following properties of a
user pool.

1. Enable self-service sign-up
2. The invitation message that you send to new admin-created users

The following example, when added to a full API request body, sets a user pool with
self-service sign-up inactive and a basic invitation email.

```
"AdminCreateUserConfig": {
      "AllowAdminCreateUserOnly": true,
      "InviteMessageTemplate": {
         "EmailMessage": "Your username is {username} and temporary password is {####}.",
         "EmailSubject": "Welcome to ExampleApp",
         "SMSMessage": "Your username is {username} and temporary password is {####}."
      }
   }
```

The following additional parameters of a [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") or [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md") API request govern the creation of new users.

[AutoVerifiedAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-AutoVerifiedAttributes "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-AutoVerifiedAttributes")

The attributes, email addresses or phone numbers, that you want to [automatically send a
message to](user-pool-settings-email-phone-verification.md#user-pool-settings-email-phone-verification.title "user-pool-settings-email-phone-verification.md#user-pool-settings-email-phone-verification.title") when you register a new user.

[Policies](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-Policies "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-Policies")

The user pool [password
policy](managing-users-passwords.md#user-pool-settings-policies.title "managing-users-passwords.md#user-pool-settings-policies.title").

[Schema](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-Schema "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-Schema")

The user pool [custom
attributes](user-pool-settings-attributes.md#user-pool-settings-custom-attributes.title "user-pool-settings-attributes.md#user-pool-settings-custom-attributes.title"). They are important to the user creation and sign-up process
because you can only set a value for _immutable_
custom attributes when you first create a user.

This parameter also sets the required attributes for your user pool. The
following text, when inserted into the `Schema` element of a full API
request body, set the `email` attribute as required.

```
{
            "Name": "email",
            "Required": true
}
```
