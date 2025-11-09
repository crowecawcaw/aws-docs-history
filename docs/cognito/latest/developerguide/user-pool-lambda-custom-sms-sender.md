# Custom SMS sender Lambda trigger

When you assign a custom SMS sender trigger to your user pool, Amazon Cognito invokes a Lambda
function instead of its default behavior when a user event requires that it send an SMS
message. With a custom sender trigger, your AWS Lambda function can send SMS notifications to
your users through a method and provider that you choose. The custom code of your function
must process and deliver all SMS messages from your user pool.

This trigger serves scenarios where you might want to have greater control over how your
user pool sends SMS messages. Your Lambda function can customize the call to Amazon SNS API
operations, for example when you want to manage multiple origination IDs or cross
AWS Regions. Your function also might redirect messages to another delivery medium or
third-party service.

To learn how to configure a custom email sender trigger, see [Activating custom sender Lambda
triggers](user-pool-lambda-custom-sender-triggers.md#enable-custom-sender-lambda-trigger "user-pool-lambda-custom-sender-triggers.md#enable-custom-sender-lambda-trigger").

## Custom SMS sender Lambda trigger sources

The following table shows the triggering event for custom SMS trigger sources in your
Lambda code.

| `TriggerSource value`                 | Event                                                                                                                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `CustomSMSSender_SignUp`              | A user signs up and Amazon Cognito sends a welcome message.                                                              |
| `CustomSMSSender_ForgotPassword`      | A user requests a code to reset their password.                                                                          |
| `CustomSMSSender_ResendCode`          | A user requests a new code to confirm their registration.                                                                |
| `CustomSMSSender_VerifyUserAttribute` | A user creates a new email address or phone number attribute and<br>Amazon Cognito sends a code to verify the attribute. |
| `CustomSMSSender_UpdateUserAttribute` | A user updates an email address or phone number attribute and Amazon Cognito<br>sends a code to verify the attribute.    |
| `CustomSMSSender_Authentication`      | A user signs in and Amazon Cognito sends an SMS OTP or MFA code.                                                         |
| `CustomSMSSender_AdminCreateUser`     | You create a new user in your user pool and Amazon Cognito sends them a<br>temporary password.                           |

## Custom SMS sender Lambda trigger

parameters

The request that Amazon Cognito passes to this Lambda function is a combination of the parameters below and the
[common parameters](cognito-user-pools-working-with-lambda-triggers.md#cognito-user-pools-lambda-trigger-syntax-shared "cognito-user-pools-working-with-lambda-triggers.md#cognito-user-pools-lambda-trigger-syntax-shared") that Amazon Cognito adds to all requests.

JSON

```
{
    "request": {
        "type": "customSMSSenderRequestV1",
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

### Custom SMS sender request

parameters

**type**

The request version. For a custom SMS sender event, the value of this
string is always `customSMSSenderRequestV1`.

**code**

The encrypted code that your function can decrypt and send to your
user.

**clientMetadata**

One or more key-value pairs that you can provide as custom input to
the custom SMS sender Lambda function trigger. To pass this data to your
Lambda function, you can use the ClientMetadata parameter in the [AdminRespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md") and [RespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md") API actions. Amazon Cognito doesn't include
data from the ClientMetadata parameter in [AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md") and [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md") API
operations in the request that it passes to the post authentication
function.

**userAttributes**

One or more key-value pairs that represent user attributes.

### Custom SMS sender response

parameters

Amazon Cognito doesn't expect any additional return information in the response. Your
function can use API operations to query and modify your resources, or record event
metadata to an external system.

## Code example

The following Node.js example processes an SMS message event in your custom SMS sender
Lambda function. This example assumes your function has two environment variables
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

```
import { KmsKeyringNode, buildClient, CommitmentPolicy } from '@aws-crypto/client-node';

// Configure the encryption SDK client with the KMS key from the environment variables
const { encrypt, decrypt } = buildClient(
    CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT
);

const generatorKeyId = process.env.KEY_ID;
const keyIds = [process.env.KEY_ARN];
const keyring = new KmsKeyringNode({ generatorKeyId, keyIds });

// Example function to simulate sending SMS.
// This example logs message details to CloudWatch Logs from your Lambda function.
// Update this function with custom logic that sends an SMS message to 'phoneNumber' with body 'message'.
const sendSMS = async (phoneNumber, message) => {
    // Log the destination with the phone number masked.
    console.log(`Simulating SMS send to ${phoneNumber.replace(/[^+]/g, '*')}`);
    // Log the message with the code masked.
    console.log(`Message content: ${message.replace(/\b\d{6,8}\b/g, '********')}`);
    // Simulate API delay
    await new Promise(resolve => setTimeout(resolve, 100));
    console.log('SMS sent successfully');
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
        if (event.triggerSource == 'CustomSMSSender_SignUp') {
            const phoneNumber = event.request.userAttributes.phone_number;
            const message = `Welcome! Your verification code is: ${plainTextCode}`;
            await sendSMS(phoneNumber, message);
        }
        else if (event.triggerSource == 'CustomSMSSender_ResendCode') {
            // Handle resend code
        }
        else if (event.triggerSource == 'CustomSMSSender_ForgotPassword') {
            // Handle forgot password
        }
        else if (event.triggerSource == 'CustomSMSSender_UpdateUserAttribute') {
            // Handle update attribute
        }
        else if (event.triggerSource == 'CustomSMSSender_VerifyUserAttribute') {
            // Handle verify attribute
        }
        else if (event.triggerSource == 'CustomSMSSender_AdminCreateUser') {
            // Handle admin create user
        }
        return;
    } catch (error) {
        console.error('Error in custom SMS sender:', error);
        throw error;
    }
};
```

###### Topics

- [Evaluate SMS message capabilities with a custom
  SMS sender function](#sms-to-email-example "#sms-to-email-example")

## Evaluate SMS message capabilities with a custom

SMS sender function

A custom SMS sender Lambda function accepts the SMS messages that your user pool would
send, and the function delivers the content based on your custom logic. Amazon Cognito sends the
[Custom SMS sender Lambda trigger
parameters](#custom-sms-sender-parameters "#custom-sms-sender-parameters") to your function. Your function can
do what you want with this information. For example, you can send the code to an
Amazon Simple Notification Service (Amazon SNS) topic. An Amazon SNS topic subscriber can be an SMS message, an HTTPS
endpoint, or an email address.

To create a test environment for Amazon Cognito SMS messaging with a custom SMS sender Lambda
function, see [amazon-cognito-user-pool-development-and-testing-with-sms-redirected-to-email](https://github.com/aws-samples/amazon-cognito-user-pool-development-and-testing-with-sms-redirected-to-email "https://github.com/aws-samples/amazon-cognito-user-pool-development-and-testing-with-sms-redirected-to-email")
in the [aws-samples library on
GitHub](https://github.com/aws-samples "https://github.com/aws-samples"). The repository contains AWS CloudFormation templates that can
create a new user pool, or work with a user pool that you already have. These templates
create Lambda functions and an Amazon SNS topic. The Lambda function that the template assigns
as a custom SMS sender trigger, redirects your SMS messages to the subscribers to the
Amazon SNS topic.

When you deploy this solution to a user pool, all messages that Amazon Cognito usually sends
through SMS messaging, the Lambda function instead sends to a central email address. Use
this solution to customize and preview SMS messages, and to test the user pool events
that cause Amazon Cognito to send an SMS message. After you complete your tests, roll back the
CloudFormation stack, or remove the custom SMS sender function assignment from your user
pool.

###### Important

Don't use the templates in [amazon-cognito-user-pool-development-and-testing-with-sms-redirected-to-email](https://github.com/aws-samples/amazon-cognito-user-pool-development-and-testing-with-sms-redirected-to-email "https://github.com/aws-samples/amazon-cognito-user-pool-development-and-testing-with-sms-redirected-to-email")
to build a production environment. The custom SMS sender Lambda function in the
solution _simulates_ SMS messages, but the Lambda
function sends them all to a single central email address. Before you can send SMS
messages in a production Amazon Cognito user pool, you must complete the requirements shown
at [SMS message settings for Amazon Cognito user pools](user-pool-sms-settings.md "user-pool-sms-settings.md").
