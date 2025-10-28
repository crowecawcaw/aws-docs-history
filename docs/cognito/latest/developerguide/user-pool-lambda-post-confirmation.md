# Post confirmation Lambda trigger

Amazon Cognito invokes this trigger after a signed-up user confirms their user account. In your
post confirmation Lambda function, you can send custom messages or add custom API requests.
For example, you can query an external system and populate additional attributes to the
user. Amazon Cognito invokes this trigger only for user who sign up in your user pool, not for user
accounts that you create with your administrator credentials.

The request contains the current attributes for the confirmed user. Your user pool invokes
your post confirmation function on [ConfirmSignUp](../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmSignUp.md "../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmSignUp.md"), [AdminConfirmSignUp](../../../cognito-user-identity-pools/latest/APIReference/API_AdminConfirmSignUp.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminConfirmSignUp.md"), and [ConfirmForgotPassword](../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmForgotPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmForgotPassword.md"). This trigger also runs when users confirm sign-up or
password reset in [managed
login](cognito-user-pools-managed-login.md "cognito-user-pools-managed-login.md").

###### Topics

- [Post
  confirmation Lambda trigger parameters](#cognito-user-pools-lambda-trigger-syntax-post-confirmation "#cognito-user-pools-lambda-trigger-syntax-post-confirmation")
- [Post confirmation
  example](#aws-lambda-triggers-post-confirmation-example "#aws-lambda-triggers-post-confirmation-example")

## Post

confirmation Lambda trigger parameters

The request that Amazon Cognito passes to this Lambda function is a combination of the parameters below and the
[common parameters](cognito-user-pools-working-with-lambda-triggers.md#cognito-user-pools-lambda-trigger-syntax-shared "cognito-user-pools-working-with-lambda-triggers.md#cognito-user-pools-lambda-trigger-syntax-shared") that Amazon Cognito adds to all requests.

JSON

```
{
    "request": {
            "userAttributes": {
                "`string`": "`string`",
                . . .
            },
            "clientMetadata": {
            	"`string`": "`string`",
            	. . .
            }
        },
    "response": {}
}
```

### Post confirmation request parameters

**userAttributes**

One or more key-value pairs representing user attributes.

**clientMetadata**

One or more key-value pairs that you can provide as custom input to
the Lambda function that you specify for the post confirmation trigger.
You can pass this data to your Lambda function by using the
ClientMetadata parameter in the following API actions: [AdminConfirmSignUp](../../../cognito-user-identity-pools/latest/APIReference/API_AdminConfirmSignUp.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminConfirmSignUp.md"), [ConfirmForgotPassword](../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmForgotPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmForgotPassword.md"), [ConfirmSignUp](../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmSignUp.md "../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmSignUp.md"), and [SignUp](../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md "../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md").

### Post confirmation response parameters

No additional return information is expected in the response.

## Post confirmation

example

This example Lambda function sends a confirmation email message to your user using
Amazon SES. For more information see [Amazon Simple Email Service Developer Guide](../../../ses/latest/DeveloperGuide.md "../../../ses/latest/DeveloperGuide.md").

Node.js

```
// Import required AWS SDK clients and commands for Node.js. Note that this requires
// the `@aws-sdk/client-ses` module to be either bundled with this code or included
// as a Lambda layer.
import { SES, SendEmailCommand } from "@aws-sdk/client-ses";
const ses = new SES();

const handler = async (event) => {
  if (event.request.userAttributes.email) {
    await sendTheEmail(
      event.request.userAttributes.email,
      `Congratulations ${event.userName}, you have been confirmed.`,
    );
  }
  return event;
};

const sendTheEmail = async (to, body) => {
  const eParams = {
    Destination: {
      ToAddresses: [to],
    },
    Message: {
      Body: {
        Text: {
          Data: body,
        },
      },
      Subject: {
        Data: "Cognito Identity Provider registration completed",
      },
    },
    // Replace source_email with your SES validated email address
    Source: "<source_email>",
  };
  try {
    await ses.send(new SendEmailCommand(eParams));
  } catch (err) {
    console.log(err);
  }
};

export { handler };

```

Amazon Cognito passes event information to your Lambda function. The function then returns the same event
object to Amazon Cognito, with any changes in the response. In the Lambda console, you can set up a test
event with data that is relevant to your Lambda trigger. The following is a test event for this code sample:

JSON

```

{
    "request": {
        "userAttributes": {
            "email": "user@example.com",
            "email_verified": true
        }
    },
    "response": {}
}
```
