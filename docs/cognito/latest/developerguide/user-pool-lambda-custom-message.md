# Custom message Lambda trigger

When you have an external standard for the email and SMS messages that you want to send to
your users, or when you want to apply your own logic at runtime to the formatting of user
messages, add a custom message trigger to your user pool. The custom message Lambda receives
the contents of all email and SMS messages before your user pool sends them. Your Lambda
function then has the opportunity to modify the message contents and subject.

Amazon Cognito invokes this trigger before it sends an email or phone verification message or a
multi-factor authentication (MFA) code. You can customize the message dynamically with your
custom message trigger.

The request includes `codeParameter`. This is a string that acts as a
placeholder for the code that Amazon Cognito delivers to the user. Insert the
`codeParameter` string into the message body where you want the verification
code to appear. When Amazon Cognito receives this response, Amazon Cognito replaces the
`codeParameter` string with the actual verification code.

###### Note

The input event for a custom message Lambda function with the
`CustomMessage_AdminCreateUser` trigger source includes a username and
verification code. Because an admin-created user must receive both their user name and
code, the response from your function must include placeholder variables for the
username and code. The placeholders for your message are the values of
`request.usernameParameter` and `request.codeParameter`. These
values are typically `{username}` and `{####}`; as a best
practice, reference the input values instead of hardcoding the variable names.

###### Topics

- [Custom message Lambda trigger sources](#cognito-user-pools-lambda-trigger-syntax-custom-message-trigger-source "#cognito-user-pools-lambda-trigger-syntax-custom-message-trigger-source")
- [Custom message
  Lambda trigger parameters](#cognito-user-pools-lambda-trigger-syntax-custom-message "#cognito-user-pools-lambda-trigger-syntax-custom-message")
- [Custom message for sign-up
  example](#aws-lambda-triggers-custom-message-example "#aws-lambda-triggers-custom-message-example")
- [Custom message for
  admin create user example](#aws-lambda-triggers-custom-message-admin-example "#aws-lambda-triggers-custom-message-admin-example")

## Custom message Lambda trigger sources

| triggerSource value                 | Event                                                                                                                                                                         |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CustomMessage_SignUp`              | Custom message – To send the confirmation code post sign-up.                                                                                                                  |
| `CustomMessage_AdminCreateUser`     | Custom message – To send the temporary password to a new<br>user.                                                                                                             |
| `CustomMessage_ResendCode`          | Custom message – To resend the confirmation code to an existing<br>user.                                                                                                      |
| `CustomMessage_ForgotPassword`      | Custom message – To send the confirmation code for Forgot Password<br>request.                                                                                                |
| `CustomMessage_UpdateUserAttribute` | Custom message – When a user's email or phone number is changed, this<br>trigger sends a verification code automatically to the user. Cannot be<br>used for other attributes. |
| `CustomMessage_VerifyUserAttribute` | Custom message – This trigger sends a verification code to the user<br>when they manually request it for a new email or phone number.                                         |
| `CustomMessage_Authentication`      | Custom message – To send MFA code during authentication.                                                                                                                      |

## Custom message

Lambda trigger parameters

The request that Amazon Cognito passes to this Lambda function is a combination of the parameters below and the
[common parameters](cognito-user-pools-working-with-lambda-triggers.md#cognito-user-pools-lambda-trigger-syntax-shared "cognito-user-pools-working-with-lambda-triggers.md#cognito-user-pools-lambda-trigger-syntax-shared") that Amazon Cognito adds to all requests.

JSON

```
{
    "request": {
        "userAttributes": {
            "`string`": "`string`",
            . . .
        }
        "codeParameter": "`####`",
        "usernameParameter": "`string`",
        "clientMetadata": {
            "`string`": "`string`",
            . . .
        }
    },
    "response": {
        "smsMessage": "`string`",
        "emailMessage": "`string`",
        "emailSubject": "`string`"
    }
}
```

### Custom message request parameters

**userAttributes**

One or more name-value pairs representing user attributes.

**codeParameter**

A string for you to use as the placeholder for the verification code
in the custom message.

**usernameParameter**

The user name. Amazon Cognito includes this parameter in requests that result
from admin-created users.

**clientMetadata**

One or more key-value pairs that you can provide as custom input to
the Lambda function that you specify for the custom message trigger. The
request that invokes a custom message function doesn't include data
passed in the ClientMetadata parameter in [AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md") and [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md") API
operations. To pass this data to your Lambda function, you can use the
ClientMetadata parameter in the following API actions:

- [AdminResetUserPassword](../../../cognito-user-identity-pools/latest/APIReference/API_AdminResetUserPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminResetUserPassword.md")
- [AdminRespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md")
- [AdminUpdateUserAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.md")
- [ForgotPassword](../../../cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.md")
- [GetUserAttributeVerificationCode](../../../cognito-user-identity-pools/latest/APIReference/API_GetUserAttributeVerificationCode.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetUserAttributeVerificationCode.md")
- [ResendConfirmationCode](../../../cognito-user-identity-pools/latest/APIReference/API_ResendConfirmationCode.md "../../../cognito-user-identity-pools/latest/APIReference/API_ResendConfirmationCode.md")
- [SignUp](../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md "../../../cognito-user-identity-pools/latest/APIReference/API_SignUp.md")
- [UpdateUserAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.md")

### Custom message response parameters

In the response, specify the custom text to use in messages to your users. For the
string constraints that Amazon Cognito applies to these parameters, see [MessageTemplateType](../../../cognito-user-identity-pools/latest/APIReference/API_MessageTemplateType.md "../../../cognito-user-identity-pools/latest/APIReference/API_MessageTemplateType.md").

**smsMessage**

The custom SMS message to be sent to your users. Must include the
`codeParameter` value that you received in the
request.

**emailMessage**

The custom email message to send to your users. You can use HTML
formatting in the `emailMessage` parameter. Must include the
`codeParameter` value that you received in the request as
the variable `{####}`. Amazon Cognito can use the
`emailMessage` parameter only if the
`EmailSendingAccount` attribute of the user pool is
`DEVELOPER`. If the `EmailSendingAccount`
attribute of the user pool isn't `DEVELOPER` and an
`emailMessage` parameter is returned, Amazon Cognito generates a
400 error code
`com.amazonaws.cognito.identity.idp.model.InvalidLambdaResponseException`.
When you choose Amazon Simple Email Service (Amazon SES) to send email messages, the
`EmailSendingAccount` attribute of a user pool is
`DEVELOPER`. Otherwise, the value is
`COGNITO_DEFAULT`.

**emailSubject**

The subject line for the custom message. You can only use the
`emailSubject` parameter if the EmailSendingAccount
attribute of the user pool is `DEVELOPER`. If the
`EmailSendingAccount` attribute of the user pool isn't
`DEVELOPER` and Amazon Cognito returns an
`emailSubject` parameter, Amazon Cognito generates a 400 error
code
`com.amazonaws.cognito.identity.idp.model.InvalidLambdaResponseException`.
The `EmailSendingAccount` attribute of a user pool is
`DEVELOPER` when you choose to use Amazon Simple Email Service (Amazon SES) to
send email messages. Otherwise, the value is
`COGNITO_DEFAULT`.

## Custom message for sign-up

example

This example Lambda function customizes an email or SMS message when the service
requires an app to send a verification code to the user.

Amazon Cognito can invoke a Lambda trigger at multiple events: post-registration, resending a
verification code, recovering a forgotten password, or verifying a user attribute. The
response includes messages for both SMS and email. The message must include the code
parameter `"####"`. This parameter is the placeholder for the verification
code that the user receives.

The maximum length for an email message is 20,000 UTF-8 characters,. This length
includes the verification code. You can use HTML tags in these email messages.

The maximum length of SMS messages is 140 UTF-8 characters. This length includes the
verification code.

Node.js

```
const handler = async (event) => {
  if (event.triggerSource === "CustomMessage_SignUp") {
    const message = `Thank you for signing up. Your confirmation code is ${event.request.codeParameter}.`;
    event.response.smsMessage = message;
    event.response.emailMessage = message;
    event.response.emailSubject = "Welcome to the service.";
  }
  return event;
};

export { handler };

```

Amazon Cognito passes event information to your Lambda function. The function then returns the same event
object to Amazon Cognito, with any changes in the response. In the Lambda console, you can set up a test
event with data that is relevant to your Lambda trigger. The following is a test event for this code sample:

JSON

```
{
	"version": "1",
	"region": "us-west-2",
	"userPoolId": "us-west-2_EXAMPLE",
	"userName": "test-user",
	"callerContext": {
		"awsSdkVersion": "aws-sdk-unknown-unknown",
		"clientId": "1example23456789"
	},
	"triggerSource": "CustomMessage_SignUp",
	"request": {
		"userAttributes": {
			"sub": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
			"cognito:user_status": "CONFIRMED",
			"email_verified": "true",
			"phone_number_verified": "true",
			"phone_number": "+12065551212",
			"email": "test-user@example.com"
		},
		"codeParameter": "{####}",
		"linkParameter": "{##Click Here##}",
		"usernameParameter": "None"
	},
	"response": {
		"smsMessage": "None",
		"emailMessage": "None",
		"emailSubject": "None"
	}
}
```

## Custom message for

admin create user example

The request that Amazon Cognito sent to this example custom message Lambda function has a
`triggerSource` value of `CustomMessage_AdminCreateUser` and a
username and temporary password. The function populates
`${event.request.codeParameter}` from the temporary password in the
request, and `${event.request.usernameParameter}` from the username in the
request.

Your custom messages must insert the values of `codeParameter` and
`usernameParameter` into `smsMessage` and
`emailMessage` in the response object. In this example, the function
writes the same message to the response fields `event.response.smsMessage`
and `event.response.emailMessage`.

The maximum length of an email message is 20,000 UTF-8 characters. This length
includes the verification code. You can use HTML tags in these emails. The maximum
length of SMS messages is 140 UTF-8 characters. This length includes the verification
code.

The response includes messages for both SMS and email.

Node.js

```
const handler = async (event) => {
  if (event.triggerSource === "CustomMessage_AdminCreateUser") {
    const message = `Welcome to the service. Your user name is ${event.request.usernameParameter}. Your temporary password is ${event.request.codeParameter}`;
    event.response.smsMessage = message;
    event.response.emailMessage = message;
    event.response.emailSubject = "Welcome to the service";
  }
  return event;
};

export { handler };

```

Amazon Cognito passes event information to your Lambda function. The function then returns the same event
object to Amazon Cognito, with any changes in the response. In the Lambda console, you can set up a test
event with data that is relevant to your Lambda trigger. The following is a test event for this code sample:

JSON

```
{
  "version": 1,
  "triggerSource": "CustomMessage_AdminCreateUser",
  "region": "`<region>`",
  "userPoolId": "`<userPoolId>`",
  "userName": "`<userName>`",
  "callerContext": {
      "awsSdk": "`<calling aws sdk with version>`",
      "clientId": "`<apps client id>`",
      ...
  },
  "request": {
      "userAttributes": {
          "phone_number_verified": false,
          "email_verified": true,
           ...
      },
      "codeParameter": "####",
      "usernameParameter": "username"
  },
  "response": {
      "smsMessage": "`<custom message to be sent in the message with code parameter and username parameter>`"
      "emailMessage": "`<custom message to be sent in the message with code parameter and username parameter>`"
      "emailSubject": "`<custom email subject>`"
  }
}
```
