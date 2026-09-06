

# Custom email sender Lambda trigger
<a name="user-pool-lambda-custom-email-sender"></a>

When you assign a custom email sender trigger to your user pool, Amazon Cognito invokes a Lambda function instead of its default behavior when a user event requires that it send an email message. With a custom sender trigger, your AWS Lambda function can send email notifications to your users through a method and provider that you choose. The custom code of your function must process and deliver all email messages from your user pool.

This trigger serves scenarios where you might want to have greater control over how your user pool sends email messages. Your Lambda function can customize the call to Amazon SES API operations, for example when you want to manage multiple verified identities or cross AWS Regions. Your function also might redirect messages to another delivery medium or third-party service.

To learn how to configure a custom email sender trigger, see [Activating custom sender Lambda triggers](user-pool-lambda-custom-sender-triggers.md#enable-custom-sender-lambda-trigger).

## Custom email sender Lambda trigger sources
<a name="trigger-source"></a>

The following table shows the triggering events for custom email trigger sources in your Lambda code.


| `TriggerSource value` | Event | 
| --- | --- | 
| CustomEmailSender\_SignUp | A user signs up and Amazon Cognito sends a welcome message. | 
| CustomEmailSender\_Authentication | A user signs in and Amazon Cognito sends an email OTP or MFA code. | 
| CustomEmailSender\_ForgotPassword | A user requests a code to reset their password. | 
| CustomEmailSender\_ResendCode | A user requests a replacement account-confirmation code. | 
| CustomEmailSender\_UpdateUserAttribute | A user updates an email address or phone number attribute and Amazon Cognito sends a code to verify the attribute. | 
| CustomEmailSender\_VerifyUserAttribute | A user creates a new email address or phone number attribute and Amazon Cognito sends a code to verify the attribute. | 
| CustomEmailSender\_AdminCreateUser | You create a new user in your user pool and Amazon Cognito sends them a temporary password. | 
| CustomEmailSender\_AccountTakeOverNotification | Amazon Cognito detects an attempt to take over a user account and sends the user a notification. | 

## Custom email sender Lambda trigger parameters
<a name="custom-email-sender-parameters"></a>

The request that Amazon Cognito passes to this Lambda function is a combination of the parameters below and the [common parameters](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html#cognito-user-pools-lambda-trigger-syntax-shared) that Amazon Cognito adds to all requests.

------
#### [ JSON ]

```
{
    "request": {
        "type": "customEmailSenderRequestV1",
        "code": "{{string}}",
        "clientMetadata": {
            "{{string}}": "{{string}}",
             . . .
            },
        "userAttributes": {
            "{{string}}": "{{string}}",
            . . .
         }
}
```

------

### Custom email sender request parameters
<a name="custom-email-sender-request-parameters"></a>

**type**  
The request version. For a custom email sender event, the value of this string is always `customEmailSenderRequestV1`.

**code**  
The encrypted code that your function can decrypt and send to your user.

**clientMetadata**  
One or more key-value pairs that you can provide as custom input to the custom email sender Lambda function trigger. To pass this data to your Lambda function, you can use the ClientMetadata parameter in the [AdminRespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.html) and [RespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.html) API actions. Amazon Cognito doesn't include data from the ClientMetadata parameter in [AdminInitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html) and [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html) API operations in the request that it passes to the post authentication function.  
Amazon Cognito sends `ClientMetadata` to custom email trigger functions in events with the following trigger sources:  
+ `CustomEmailSender_ForgotPassword`
+ `CustomEmailSender_SignUp`
+ `CustomEmailSender_Authentication`
Amazon Cognito doesn't send `ClientMetadata` in trigger events with source `CustomEmailSender_AccountTakeOverNotification`.

**userAttributes**  
One or more key-value pairs that represent user attributes.

### Custom email sender response parameters
<a name="custom-email-sender-response-parameters"></a>

Amazon Cognito doesn't expect any additional return information in the custom email sender response. Your Lambda function must interpret the event and decrypt the code, then deliver the message contents. A typical function assembles an email message and directs it to a third-party SMTP relay.

## Code example
<a name="custom-email-sender-code-examples"></a>

The following Node.js example processes an email message event in your custom email sender Lambda function. This example assumes your function has two environment variables defined.

**`KEY_ID`**  
The ID of the KMS key that you want to use to encrypt and decrypt your users' codes.

**`KEY_ARN`**  
The Amazon Resource Name (ARN) of the KMS key that you want to use to encrypt and decrypt your users' codes.

**To deploy this function**

1. Install the latest version of NodeJS in your developer workspace.

1. Create a new NodeJS project in your workspace.

1. Initialize your project with `npm init -y`.

1. Create the script for the Lambda function: `touch index.mjs`.

1. Paste the contents of the below example into `index.mjs`.

1. Download the project dependency, AWS Encryption SDK: `npm install @aws-crypto/client-node`.

1. Zip the project directory into a file: `zip -r my_deployment_package.zip .`.

1. [Deploy the ZIP file to your function](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-package.html).

This example function decrypts the code and, for sign-up events, simulates sending an email message to the user's email address.

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