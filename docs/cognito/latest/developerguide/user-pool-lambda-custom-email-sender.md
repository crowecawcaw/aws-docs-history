# Custom email sender Lambda

trigger

When you assign a custom email sender trigger to your user pool, Amazon Cognito invokes a Lambda
function instead of its default behavior when a user event requires that it send an email
message. With a custom sender trigger, your AWS Lambda function can send email notifications
to your users through a method and provider that you choose. The custom code of your
function must process and deliver all email messages from your user pool.

This trigger serves scenarios where you might want to have greater control over how your
user pool sends email messages. Your Lambda function can customize the call to Amazon SES API
operations, for example when you want to manage multiple verified identities or cross
AWS Regions. Your function also might redirect messages to another delivery medium or
third-party service.

To learn how to configure a custom email sender trigger, see [Activating custom sender Lambda
triggers](user-pool-lambda-custom-sender-triggers.md#enable-custom-sender-lambda-trigger "user-pool-lambda-custom-sender-triggers.md#enable-custom-sender-lambda-trigger").

## Custom email sender Lambda trigger sources

The following table shows the triggering events for custom email trigger sources in
your Lambda code.

| `TriggerSource value`                           | Event                                                                                                                    |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `CustomEmailSender_SignUp`                      | A user signs up and Amazon Cognito sends a welcome message.                                                              |
| `CustomEmailSender_Authentication`              | A user signs in and Amazon Cognito sends an email OTP or MFA code.                                                       |
| `CustomEmailSender_ForgotPassword`              | A user requests a code to reset their password.                                                                          |
| `CustomEmailSender_ResendCode`                  | A user requests a replacement account-confirmation code.                                                                 |
| `CustomEmailSender_UpdateUserAttribute`         | A user updates an email address or phone number attribute and Amazon Cognito<br>sends a code to verify the attribute.    |
| `CustomEmailSender_VerifyUserAttribute`         | A user creates a new email address or phone number attribute and<br>Amazon Cognito sends a code to verify the attribute. |
| `CustomEmailSender_AdminCreateUser`             | You create a new user in your user pool and Amazon Cognito sends them a<br>temporary password.                           |
| `CustomEmailSender_AccountTakeOverNotification` | Amazon Cognito detects an attempt to take over a user account and sends the<br>user a notification.                      |

## Custom email sender Lambda trigger

parameters

The request that Amazon Cognito passes to this Lambda function is a combination of the parameters below and the
[common parameters](cognito-user-pools-working-with-lambda-triggers.md#cognito-user-pools-lambda-trigger-syntax-shared "cognito-user-pools-working-with-lambda-triggers.md#cognito-user-pools-lambda-trigger-syntax-shared") that Amazon Cognito adds to all requests.

JSON

```
{
    "request": {
        "type": "customEmailSenderRequestV1",
        "code": "`string`",
        "clientMetadata": {
            "`string`": "`string`",
             . . .
            },
        "userAttributes": {
            "`string`": "`string`",
            . . .
         }
}
```

### Custom email sender request parameters

**type**

The request version. For a custom email sender event, the value of
this string is always `customEmailSenderRequestV1`.

**code**

The encrypted code that your function can decrypt and send to your
user.

**clientMetadata**

One or more key-value pairs that you can provide as custom input to
the custom email sender Lambda function trigger. To pass this data to
your Lambda function, you can use the ClientMetadata parameter in the
[AdminRespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md") and [RespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md") API actions. Amazon Cognito doesn't include
data from the ClientMetadata parameter in [AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md") and [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md") API
operations in the request that it passes to the post authentication
function.

###### Note

Amazon Cognito sends `ClientMetadata` to custom email trigger
functions in events with the following trigger sources:

- `CustomEmailSender_ForgotPassword`
- `CustomEmailSender_SignUp`
- `CustomEmailSender_Authentication`
  Amazon Cognito doesn't send `ClientMetadata` in trigger events
  with source
  `CustomEmailSender_AccountTakeOverNotification`.

**userAttributes**

One or more key-value pairs that represent user attributes.

### Custom email sender

response parameters

Amazon Cognito doesn't expect any additional return information in the custom email sender
response. Your Lambda function must interpret the event and decrypt the code, then
deliver the message contents. A typical function assembles an email message and
directs it to a third-party SMTP relay.

## Code example

The following Node.js example processes an email message event in your custom email
sender Lambda function. This example assumes your function has two environment variables
defined.

**`KEY_ID`**

The ID of the KMS key that you want to use to encrypt and decrypt your
users' codes.

**`KEY_ARN`**

The Amazon Resource Name (ARN) of the KMS key that you want to use to
encrypt and decrypt your users' codes.

###### To deploy this function

1. Install the latest version of NodeJS in your developer workspace.
2. Create a new NodeJS project in your workspace.
3. Initialize your project with `npm init -y`.
4. Create the script for the Lambda function: `touch index.mjs`.
5. Paste the contents of the below example into `index.mjs`.
6. Download the project dependency, AWS Encryption SDK: `npm install
@aws-crypto/client-node`.
7. Zip the project directory into a file: `zip -r my_deployment_package.zip
.`.
8. [Deploy
   the ZIP file to your function](../../../lambda/latest/dg/nodejs-package.md "../../../lambda/latest/dg/nodejs-package.md").

This example function decrypts the code and, for sign-up events, simulates sending an
email message to the user's email address.

```
import { KmsKeyringNode, buildClient, CommitmentPolicy } from '@aws-crypto/client-node';

// Configure the encryption SDK client with the KMS key from the environment variables
const { encrypt, decrypt } = buildClient(
    CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT
);

const generatorKeyId = process.env.KEY_ID;
const keyIds = [process.env.KEY_ARN];
const keyring = new KmsKeyringNode({ generatorKeyId, keyIds });

// Example function to simulate sending email.
// This example logs message details to CloudWatch Logs from your Lambda function.
// Update this function with custom logic that sends an email message to 'emailaddress' with body 'message'.
const sendEmail = async (emailAddress, message) => {
    // Log the destination with the email address masked.
    console.log(`Simulating email send to ${emailAddress.replace(/[^@.]/g, '*')}`);
    // Log the message with the code masked.
    console.log(`Message content: ${message.replace(/\b\d{6,8}\b/g, '********')}`);
    // Simulate API delay
    await new Promise(resolve => setTimeout(resolve, 100));
    console.log('Email sent successfully');
    return true;
};

export const handler = async (event) => {
    try {
        // Decrypt the secret code using encryption SDK
        let plainTextCode;
        if (event.request.code) {
            const { plaintext, messageHeader } = await decrypt(keyring, Buffer.from(event.request.code, 'base64'));
            plainTextCode = Buffer.from(plaintext).toString('utf-8');
        }

        // Handle different trigger sources
        if (event.triggerSource == 'CustomEmailSender_SignUp') {
            const emailAddress = event.request.userAttributes.email;
            const message = `Welcome! Your verification code is: ${plainTextCode}`;
            await sendEmail(emailAddress, message);
        }
        else if (event.triggerSource == 'CustomEmailSender_ResendCode') {
            // Handle resend code
        }
        else if (event.triggerSource == 'CustomEmailSender_ForgotPassword') {
            // Handle forgot password
        }
        else if (event.triggerSource == 'CustomEmailSender_UpdateUserAttribute') {
            // Handle update attribute
        }
        else if (event.triggerSource == 'CustomEmailSender_VerifyUserAttribute') {
            // Handle verify attribute
        }
        else if (event.triggerSource == 'CustomEmailSender_AdminCreateUser') {
            // Handle admin create user
        }
        else if (event.triggerSource == 'CustomEmailSender_Authentication') {
            // Handle authentication
        }
        else if (event.triggerSource == 'CustomEmailSender_AccountTakeOverNotification') {
            // Handle account takeover notification
        }

        return;
    } catch (error) {
        console.error('Error in custom email sender:', error);
        throw error;
    }
};
```
