# SMS and email message

MFA

SMS and email MFA messages confirm that users have access to a message destination
before they can sign in. They confirm that they not only have access to a password, but to
the SMS messages or the email inbox of the original user. Amazon Cognito requests that users provide
a short code that your user pool sent after they successfully provide a username and
password.

SMS and email message MFA require no additional configuration after your user adds an
email address or phone number to their profile. Amazon Cognito can send messages to unverified email
addresses and phone numbers. When a user completes their first MFA, Amazon Cognito marks their email
address or phone number as verified.

MFA authentication begins when a user with MFA enters their username and password in
your application. Your application submits these initial parameters in an SDK method that
invokes an [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md") or [AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md") API request. The `ChallengeParameters` in the API
response includes a `CODE_DELIVERY_DESTINATION` value that indicates where the
authorization code was sent. In your application, display a form that prompts the user to
check their phone and includes an input element for the code. When they enter their code,
submit it in a challenge-response API request to complete the sign-in process.

After a user with MFA signs in with username and password in the [managed login](cognito-user-pools-managed-login.md "cognito-user-pools-managed-login.md") pages, they're
automatically prompted for the MFA code.

User pools send SMS messages for MFA and other Amazon Cognito notifications with Amazon Simple Notification Service
(Amazon SNS) resources in your AWS account. Similarly, users pools send email messages with
Amazon Simple Email Service (Amazon SES) resources in your account. These linked services incur their own costs on
your AWS bill for message delivery. They also have additional requirements for sending
messages at production volumes. See the following links for more information:

- [SMS message settings for Amazon Cognito user pools](user-pool-sms-settings.md "user-pool-sms-settings.md")
- [Worldwide SMS Pricing](https://aws.amazon.com/sns/sms-pricing/ "https://aws.amazon.com/sns/sms-pricing/")
- [Email settings for Amazon Cognito user pools](user-pool-email.md "user-pool-email.md")
- [Amazon SES pricing](https://aws.amazon.com/ses/pricing "https://aws.amazon.com/ses/pricing")

## Considerations

for SMS and email message MFA

- To permit users to sign in with email MFA, your user pool must have the following
  configuration options:
  1.  You have the Plus or Essentials feature plan in your user pool. For more
      information, see [User pool feature plans](cognito-sign-in-feature-plans.md "cognito-sign-in-feature-plans.md").
  2.  Your user pool sends email messages with your own Amazon SES resources. For more
      information, see [Amazon SES email configuration](user-pool-email.md#user-pool-email-developer "user-pool-email.md#user-pool-email-developer").

- The MFA code is valid for the **Authentication flow session
  duration** that you set for your app client.

Set the duration of an authentication flow session in the Amazon Cognito console in the
**App clients** menu when you **Edit** your app
client. You can also set the authentication flow session duration in a
`CreateUserPoolClient` or `UpdateUserPoolClient` API request.
For more information, see [An example authentication
session](authentication.md#amazon-cognito-user-pools-authentication-flow "authentication.md#amazon-cognito-user-pools-authentication-flow").

- When a user successfully provides a code from an SMS or email message that Amazon Cognito
  sent to an unverified phone number or email address, Amazon Cognito marks the corresponding
  attribute as verified.
- For a user to make a self-service change to the value of a phone number or email
  address that's associated with MFA, they must sign in and authorize the request with
  an access token. If they can't access their current phone number or email address,
  they can't sign in. Your team must change these values with administrator AWS
  credentials in [AdminUpdateUserAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md") API requests.
- After you [configure SMS](user-pool-sms-settings.md "user-pool-sms-settings.md") in your user
  pool, you can't disable SMS messages as an available MFA factor.
