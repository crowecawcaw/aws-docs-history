# Managing user existence error

responses

Amazon Cognito supports customizing error responses returned by user pools. Custom error responses
are available for user creation and authentication, password recovery, and confirmation
operations.

Use the `PreventUserExistenceErrors` setting of a user pool app client to enable
or disable user existence related errors. When you create a new app client with the Amazon Cognito user pools API,
`PreventUserExistenceErrors` is `LEGACY`, or disabled, by default. In
the Amazon Cognito console, the option **Prevent user existence errors** —a
setting of `ENABLED` for `PreventUserExistenceErrors`—is selected
by default. To update your `PreventUserExistenceErrors` configuration, do one of the
following:

- Change the value of `PreventUserExistenceErrors` between `ENABLED`
  and `LEGACY` in an [UpdateUserPoolClient](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.md") API request.
- Edit your app client in the Amazon Cognito console and change the state of **Prevent user
  existence errors** between selected (`ENABLED`) and deselected
  (`LEGACY`).
  When this property has a value of `LEGACY`, your app client returns a
  `UserNotFoundException` error response when a user attempts to sign in with a
  username that doesn't exist in your user pool.

When this property has a value of `ENABLED`, your app client doesn't disclose the
nonexistence of a user account in your user pool with a `UserNotFoundException`
error. A `PreventUserExistenceErrors` configuration of `ENABLED` has the
following effects when you submit a request for a username that doesn't exist:

- Amazon Cognito responds with nonspecific information to API requests where its response might
  otherwise disclose that a valid user exists.
- Amazon Cognito returns a generic authentication failure response to forgot-password requests, and
  to authentication requests with authentication flows _except_ for [choice-based
  authentication](authentication-flows-selection-sdk.md#authentication-flows-selection-choice "authentication-flows-selection-sdk.md#authentication-flows-selection-choice") (`USER_AUTH`)—for example,
  `USER_SRP_AUTH` or `CUSTOM_AUTH`. The error response tells you the
  user name or password is incorrect.
- Amazon Cognito responds to requests for choice-based authentication with a random selection from
  the challenge types allowed for the user pool. Your user pool might return a passkey,
  one-time password, or password challenge.
- The behavior of Amazon Cognito account confirmation and password recovery APIs alternates between
  returning a response indicating a code was sent to a simulated delivery medium and returning
  an `InvalidParameterException` error.
  The following information details the behaviors of user pool operations when
  `PreventUserExistenceErrors` is set to `ENABLED`.

## Authentication and user creation

operations

You can configure error responses in username-password, and Secure Remote Password (SRP)
authentication.
You can also customize the errors that you return with custom authentication.
Choice-based authentication is unaffected by your
`PreventUserExistenceErrors` configuration.

###### User-existence disclosure details in authentication flows

**Choice-based authentication**

In the `USER_AUTH` choice-based authentication flow, Amazon Cognito returns a
challenge from the primary authentication factors that are available, depending on your
user pool configuration and users' attributes. This authentication flow can return
password, secure remote password (SRP), WebAuthn (passkey), SMS one-time password (OTP),
or email OTP challenges. With `PreventUserExistenceErrors` active, Amazon Cognito
issues a challenge to nonexistent users to complete one or more of the available forms
of authentication. With `PreventUserExistenceErrors` inactive, Amazon Cognito returns
a `UserNotFound` exception.

**Username and password authentication**

The authentication flows `ADMIN_USER_PASSWORD_AUTH`,
`USER_PASSWORD_AUTH`, and the `PASSWORD` flow of
`USER_AUTH` return a `NotAuthorizedException` with the message
`Incorrect username or password` when
`PreventUserExistenceErrors` is active. When
`PreventUserExistenceErrors` is inactive, these flows return
`UserNotFoundException`.

**Secure Remote Password (SRP) based authentication**

As a best practice, only implement `PreventUserExistenceErrors` with
`USER_SRP_AUTH` or the `PASSWORD_SRP` flow of
`USER_AUTH` in user pools without email address, phone number, or preferred
username [alias attributes](user-pool-settings-attributes.md#user-pool-settings-aliases "user-pool-settings-attributes.md#user-pool-settings-aliases"). Users with
alias attributes might not be subject to user-existence suppression in the SRP
authentication flow. Username-password authentication
flows—`ADMIN_USER_PASSWORD_AUTH`, `USER_PASSWORD_AUTH`,
and the `USER_AUTH`
`PASSWORD` challenge—fully suppress the existence of users from alias
attributes.

When someone attempts SRP sign-in with a username that isn't known to your app
client, Amazon Cognito returns a simulated response in the first step as described in [RFC 5054](https://tools.ietf.org/html/rfc5054#section-2.5.1.3 "https://tools.ietf.org/html/rfc5054#section-2.5.1.3"). Amazon Cognito
returns the same salt and an internal user ID in [UUID](cognito-terms.md#terms-uuid "cognito-terms.md#terms-uuid")
format for the same username and user pool combination. When you send a
`RespondToAuthChallenge` API request with proof of password, Amazon Cognito returns
a generic `NotAuthorizedException` error when either username or password is
incorrect. For more information about implementation of SRP authentication, see [Sign-in with
persistent passwords and secure payload](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-srp "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-srp").

###### Note

You can simulate a generic response with username and password authentication if
you are using verification-based alias attributes, and the immutable username isn't
formatted as a [UUID](cognito-terms.md#terms-uuid "cognito-terms.md#terms-uuid").

**Custom authentication challenge Lambda trigger**

Amazon Cognito invokes the [custom authentication
challenge Lambda triggers](user-pool-lambda-challenge.md "user-pool-lambda-challenge.md") when users attempt to sign in with the
`CUSTOM_AUTH` authentication flow, but their username isn't found. The
input event includes a boolean parameter named `UserNotFound` with a value of
`true` for any nonexistent user. This parameter appears in the request
events that your user pool sends to the create, define, and verify auth challenge Lambda
functions that make up the custom-authentication architecture. When you examine this
indicator in the logic of your Lambda function, you can simulate custom authentication
challenges for a user that doesn't exist.

**Pre authentication Lambda trigger**

Amazon Cognito invokes the [pre
authentication trigger](user-pool-lambda-pre-authentication.md "user-pool-lambda-pre-authentication.md") when users attempt to sign in but their username isn't
found. The input event includes a `UserNotFound` parameter with a value of
`true` for any nonexistent user.

The following list describes the effect of `PreventUserExistenceErrors` on user
account creation.

###### User-existence disclosure details in user creation flows

**SignUp**

The `SignUp` operation always returns
`UsernameExistsException` when a username is already taken. If you don't
want Amazon Cognito to return a `UsernameExistsException` error for email addresses
and phone numbers when you sign up users in your app, use verification-based alias
attributes. For more information about aliases, see [Customizing sign-in attributes](user-pool-settings-attributes.md#user-pool-settings-aliases "user-pool-settings-attributes.md#user-pool-settings-aliases").

For an example of how Amazon Cognito can prevent the use of `SignUp` API requests
to discover users in your user pool, see [Preventing
UsernameExistsException errors for email addresses and phone numbers on
sign-up](#cognito-user-pool-managing-errors-prevent-userexistence-errors "#cognito-user-pool-managing-errors-prevent-userexistence-errors").

**Imported users**

If `PreventUserExistenceErrors` is enabled, during authentication of
imported users a generic `NotAuthorizedException` error is returned
indicating either the username or password was incorrect instead of returning
`PasswordResetRequiredException`. See [Requiring imported users
to reset their passwords](cognito-user-pools-using-import-tool.md#cognito-user-pools-using-import-tool-password-reset "cognito-user-pools-using-import-tool.md#cognito-user-pools-using-import-tool-password-reset") for more
information.

**Migrate user Lambda trigger**

Amazon Cognito returns a simulated response for users that don't exist when an empty response
was set in the original event context by the Lambda trigger. For more information, see
[Importing users with a user migration
Lambda trigger](cognito-user-pools-import-using-lambda.md "cognito-user-pools-import-using-lambda.md").

### Preventing

`UsernameExistsException` errors for email addresses and phone numbers on
sign-up

The following example demonstrates how, when you configure alias attributes in your user
pool, you can keep duplicate email addresses and phone numbers from generating
`UsernameExistsException` errors in response to `SignUp` API
requests. You must have created your user pool with email address or phone number as an
alias attribute. For more information, see the _Customizing sign-in
attributes_ section of [User pool attributes](user-pool-settings-attributes.md#user-pool-settings-aliases "user-pool-settings-attributes.md#user-pool-settings-aliases").

1. Jie signs up for a new username, and also provides the email address
   `jie@example.com`. Amazon Cognito sends a code to their email address.

**Example AWS CLI command**

```
aws cognito-idp sign-up --client-id 1234567890abcdef0 --username jie --password PASSWORD --user-attributes Name="email",Value="jie@example.com"
```

**Example response**

```
{
    "UserConfirmed": false,
    "UserSub": "`<subId>`",
    "CodeDeliveryDetails": {
        "AttributeName": "email",
        "Destination": "j****@e****",
        "DeliveryMedium": "EMAIL"
    }
}

```

2. Jie provides the code sent to them to confirm their ownership of the email address.
   This completes their registration as a user.

**Example AWS CLI command**

```
aws cognito-idp confirm-sign-up --client-id 1234567890abcdef0 --username=jie --confirmation-code xxxxxx
```

3. Shirley registers a new user account and provides the email address
   `jie@example.com`. Amazon Cognito doesn't return a
   `UsernameExistsException` error, and sends a confirmation code to Jie's
   email address.

**Example AWS CLI command**

```
aws cognito-idp sign-up --client-id 1234567890abcdef0 --username shirley --password PASSWORD --user-attributes Name="email",Value="jie@example.com"
```

**Example response**

```
{
    "UserConfirmed": false,
    "UserSub": "`<new subId>`",
    "CodeDeliveryDetails": {
        "AttributeName": "email",
        "Destination": "j****@e****",
        "DeliveryMedium": "EMAIL"
    }
}

```

4. In a different scenario, Shirley has ownership of `jie@example.com`.
   Shirley retrieves the code that Amazon Cognito sent to Jie's email address and attempts to
   confirm the account.

**Example AWS CLI command**

```
aws cognito-idp confirm-sign-up --client-id 1234567890abcdef0 --username=shirley --confirmation-code xxxxxx
```

**Example response**

```
An error occurred (AliasExistsException) when calling the ConfirmSignUp operation: An account with the email already exists.
```

Amazon Cognito doesn't return an error to Shirley's `aws cognito-idp sign-up` request,
despite `jie@example.com` being assigned to an existing user. Shirley must
demonstrate ownership of the email address before Amazon Cognito returns an error response. In a user
pool with alias attributes, this behavior prevents use of the public `SignUp` API
to check whether a user exists with a given email address or phone number.

This behavior is different from the response that Amazon Cognito returns to `SignUp`
request with an existing username, as shown in the following example. While Shirley learns
from this response that a user already exists with the username `jie`, they don't
learn about any email addresses or phone numbers associated with the user.

**Example CLI command**

```
aws cognito-idp sign-up --client-id 1example23456789 --username jie --password PASSWORD
      --user-attributes Name="email",Value="shirley@example.com"
```

**Example response**

```
An error occurred (UsernameExistsException) when calling the SignUp operation: User already exists
```

## Password reset

operations

Amazon Cognito returns the following responses to user password reset operations when you prevent
user existence errors.

**ForgotPassword**

When a user isn't found, is deactivated, or doesn't have a verified delivery
mechanism to recover their password, Amazon Cognito returns `CodeDeliveryDetails` with
a simulated delivery medium for a user. The simulated delivery medium is determined by
the input username format and verification settings of the user pool.

**ConfirmForgotPassword**

Amazon Cognito returns the `CodeMismatchException` error for users that don't
exist or are disabled. If a code isn't requested when using `ForgotPassword`,
Amazon Cognito returns the `ExpiredCodeException` error.

## Confirmation

operations

Amazon Cognito returns the following responses to user confirmation and verification operations
when you prevent user existence errors.

**ResendConfirmationCode**

Amazon Cognito returns `CodeDeliveryDetails` for a disabled user or a user that
doesn't exist. Amazon Cognito sends a confirmation code to the existing user's email or phone
number.

**ConfirmSignUp**

`ExpiredCodeException` returns if a code has expired. Amazon Cognito returns
`NotAuthorizedException` when a user isn't authorized. If the code doesn't
match what the server expects Amazon Cognito returns `CodeMismatchException`.
