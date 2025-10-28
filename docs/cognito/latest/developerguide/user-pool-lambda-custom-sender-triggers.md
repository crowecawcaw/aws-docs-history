# Custom sender Lambda

triggers

The Lambda triggers `CustomEmailSender` and `CustomSMSSender` support
third-party email and SMS notifications in user pools. You can choose SMS and email
providers to send notifications to users from within your Lambda function code. When Amazon Cognito
sends invitations, MFA codes, confirmation codes, verification codes, and temporary
passwords to users, the events activate your configured Lambda functions. Amazon Cognito sends the
code and temporary passwords (secrets) to your activated Lambda functions. Amazon Cognito encrypts
these secrets with an AWS KMS customer managed key and the AWS Encryption SDK. The AWS Encryption SDK is a
client-side encryption library that helps you to encrypt and decrypt generic data.

**[CustomEmailSender](user-pool-lambda-custom-email-sender.md "user-pool-lambda-custom-email-sender.md")**

Amazon Cognito invokes this trigger to send email notifications to users.

**[CustomSMSSender](user-pool-lambda-custom-sms-sender.md "user-pool-lambda-custom-sms-sender.md")**

Amazon Cognito invokes this trigger to send SMS notifications to users.

## Encryption

concepts

Amazon Cognito doesn't send users' codes in plaintext in the events that it sends to custom
sender triggers. The Lambda functions must decrypt codes in the events. The following
concepts are the encryption architecture that your function must use to get codes that
it can deliver to users.

**AWS KMS**

AWS KMS is a managed service to create and control AWS KMS keys. These keys
encrypt your data. For more information see, [What is
AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").

**KMS key**

A KMS key is a logical representation of a cryptographic key. The
KMS key includes metadata, such as the key ID, creation date, description,
and key state. The KMS key also contains the key material used to encrypt
and decrypt data. For more information see, [AWS KMS keys](../../../kms/latest/developerguide/concepts.md#kms_keys "../../../kms/latest/developerguide/concepts.md#kms_keys").

**Symmetric KMS key**

A symmetric KMS key is a 256-bit encryption key that doesn't exit AWS KMS
unencrypted. To use a symmetric KMS key, you must call AWS KMS. Amazon Cognito uses
symmetric keys. The same key encrypts and decrypts. For more information
see, [Symmetric KMS keys](../../../kms/latest/developerguide/concepts.md#symmetric-cmks "../../../kms/latest/developerguide/concepts.md#symmetric-cmks").

## Things to know

about custom sender Lambda triggers

- To configure your user pools to use these Lambda triggers, you can use the
  AWS CLI or SDK. These configurations aren't available from Amazon Cognito console.

The `UpdateUserPool` operation sets Lambda configuration. Requests
to this operation require all the parameters of your user pool _and_ the parameters that you want to change. If you
don't provide all relevant parameters, Amazon Cognito sets the values of any missing
parameters to their defaults. As demonstrated in the AWS CLI example that
follows, include entries for all Lambda functions that you want to add to or keep
in your user pool. For more information, see [Updating user pool and app client
configuration](cognito-user-pool-updating.md "cognito-user-pool-updating.md").

```

    #Send this parameter in an 'aws cognito-idp update-user-pool' CLI command, including any existing
    #user pool configurations. This snippet also includes a pre sign-up trigger for syntax reference. The pre sign-up trigger
    #doesn't have a role in custom sender triggers.

      --lambda-config "PreSignUp=`lambda-arn`, \
                       CustomSMSSender={LambdaVersion=V1_0,LambdaArn=`lambda-arn`}, \
                       CustomEmailSender={LambdaVersion=V1_0,LambdaArn=`lambda-arn`}, \
                       KMSKeyID=`key-id`"

```

For requests that use the JSON body of `UpdateUserPool` the
following `LambdaConfig` snippet assigns custom SMS and email sender
functions.

```
"LambdaConfig": {
   "KMSKeyID": "arn:aws:kms:`us-east-1`:`111122223333`:key/`a6c4f8e2-0c45-47db-925f-87854bc9e357`",
   "CustomEmailSender": {
      "LambdaArn": "arn:aws:lambda:`us-east-1`:`111122223333`:function:`MyFunction`",
      "LambdaVersion": "V1_0"
   },
   "CustomSMSSender": {
      "LambdaArn": "arn:aws:lambda:`us-east-1`:`111122223333`:function:`MyFunction`",
      "LambdaVersion": "V1_0"
   }
```

- To remove a custom sender Lambda trigger with an `update-user-pool`
  AWS CLI command, omit the `CustomSMSSender` or
  `CustomEmailSender` parameter from `--lambda-config`,
  and include all other triggers that you want to use with your user pool.

To remove a custom sender Lambda trigger with an `UpdateUserPool`
API request, omit the `CustomSMSSender` or
`CustomEmailSender` parameter from the request body that contains
the rest of your user pool configuration.

- Amazon Cognito HTML-escapes reserved characters like `<`
  (`&lt;`) and `>` (`&gt;`) in your
  user's temporary password. These characters might appear in temporary passwords
  that Amazon Cognito sends to your custom email sender function, but don't appear in
  temporary verification codes. To send temporary passwords, your Lambda function
  must unescape these characters after it decrypts the password, and before it
  sends the message to your user.

## Activating custom sender Lambda

triggers

To use custom logic to send SMS or email messages for your user pool, set up custom
sender triggers. The following procedure assigns a custom SMS trigger, a custom email
trigger, or both to your user pool. After you add your custom sender trigger, Amazon Cognito
always sends user attributes, including the phone number, and the one-time code to your
Lambda function instead of the default behavior that sends an SMS or email
message.

1. Create a [symmetric
   encryption key](../../../kms/latest/developerguide/concepts.md#symmetric-cmks "../../../kms/latest/developerguide/concepts.md#symmetric-cmks") in AWS Key Management Service (AWS KMS). Amazon Cognito generates
   secrets—temporary passwords, verification codes, authentication one-time
   passwords, and confirmation codes—then uses this KMS key to encrypt the
   secrets with [AWS Encryption SDK](../../../encryption-sdk/latest/developer-guide/introduction.md "../../../encryption-sdk/latest/developer-guide/introduction.md"). You can then use the AWS Encryption SDK in your Lambda
   function to decrypt the secrets and send them to the user in plaintext.
2. The IAM principal that creates or updates your user pool creates a one-time
   grant against the KMS key that Amazon Cognito uses to encrypt the code. Grant this
   principal `CreateGrant` permissions for your KMS key. For this
   example KMS key policy to be effective, the administrator who updates the user
   pool must be signed in with an assumed-role session for the IAM role
   `arn:aws:iam::111222333444:role/my-example-administrator-role`.

Apply the following resource-based policy, modified for your environment, to
your KMS key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`my-example-administrator-role`"
 },
 "Action": "kms:CreateGrant",
 "Resource": "arn:aws:kms:us-west-2:`111122223333`:key/`1example-2222-3333-4444-999example`",
 "Condition": {
 "StringEquals": {
 "kms:EncryptionContext:userpool-id": "`us-west-2_EXAMPLE`"
 }
 }
 },
 {
 "Sid": "Allow Lambda to decrypt",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`my-lambda-function-role`"
 },
 "Action": "kms:Decrypt",
 "Resource": "*"
 }]
}`

```

3. Create a Lambda function for the custom sender trigger. Amazon Cognito uses the [AWS
   encryption SDK](../../../encryption-sdk/latest/developer-guide/introduction.md "../../../encryption-sdk/latest/developer-guide/introduction.md") to encrypt the secrets, temporary passwords and codes
   that authorize your users' API requests.
   1. Assign a [Lambda
      execution role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md") that has, at minimum,
      `kms:Decrypt` permissions for your KMS key.
   2. Compose Lambda function code to send your messages. The input event to
      your function contains a secret. In your function, decrypt the secret
      with the AWS Encryption SDK and process any relevant metadata. Then send the
      code, your own custom message, and destination phone number to the
      custom API that delivers your message.
   3. Add the AWS Encryption SDK to your Lambda function. For more information, see
      [AWS Encryption SDK programming
      languages](../../../encryption-sdk/latest/developer-guide/programming-languages.md "../../../encryption-sdk/latest/developer-guide/programming-languages.md"). To update the Lambda package, complete the
      following steps.
      1. Export your Lambda function as a .zip file in the
         AWS Management Console.
      2. Open your function and add the AWS Encryption SDK. For more
         information and download links, see [AWS Encryption SDK programming languages](../../../encryption-sdk/latest/developer-guide/programming-languages.md "../../../encryption-sdk/latest/developer-guide/programming-languages.md") in the _AWS Encryption SDK Developer Guide_.
      3. Zip your function with your SDK dependencies, and upload the
         function to Lambda. For more information, see [Deploying Lambda functions as .zip file archives](../../../lambda/latest/dg/configuration-function-zip.md#configuration-function-create "../../../lambda/latest/dg/configuration-function-zip.md#configuration-function-create") in
         the _AWS Lambda Developer
         Guide_.

4. Grant Amazon Cognito service principal `cognito-idp.amazonaws.com` access to
   invoke the Lambda function.

The following AWS CLI command grants Amazon Cognito permission to invoke your Lambda
function:

```
aws lambda add-permission --function-name `lambda_arn` --statement-id "`CognitoLambdaInvokeAccess`" --action lambda:InvokeFunction --principal cognito-idp.amazonaws.com
```

5. Generate an [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md") API request with a `LambdaConfig`
   parameter that adds custom sender Lambda triggers. You can't add triggers of
   this type in the Amazon Cognito console. Custom sender triggers require
   `LambdaConfig` parameters of `KMSKeyID` and
   `CustomSMSSender` or `CustomEmailSender` (or
   both).
