# Setting up Deepgram speech model preference

Deepgram is a third-party speech recognition service that provides advanced AI-powered speech-to-text capabilities with support for real-time and batch processing. Deepgram offers enhanced accuracy across various audio conditions, multiple languages, and specialized models for different use cases. For more information about Deepgram's offerings, see [https://deepgram.com/](https://deepgram.com/ "https://deepgram.com/"). To use Deepgram as your speech recognition model preference, you need to complete a one-time setup process to configure your Deepgram API key and store it securely in AWS Secrets Manager.

###### Important

Deepgram is a third-party service and may not comply with certain regulatory frameworks such as GDPR, FedRAMP, or other compliance standards that AWS services adhere to. Review Deepgram's compliance documentation and your organization's requirements before using this integration.

## Creating a Deepgram API key

Before you can use Deepgram with Amazon Lex V2, you need to obtain an API key from Deepgram.

To create a Deepgram API key:

1. Log into the Deepgram console at [https://console.deepgram.com/](https://console.deepgram.com/ "https://console.deepgram.com/").
2. In the left navigation pane, choose **API Keys**.
3. Choose **Create a New API Key**.
4. Follow the instructions to create the API key and copy it for use in the next section.

###### Important

Store your API key securely. You'll need it to configure AWS Secrets Manager in the next section.

## Storing the API key in AWS Secrets Manager

You must store your Deepgram API key in AWS Secrets Manager for Amazon Lex V2 to access it securely. The secret must contain a single key-value pair with `apiToken` as the key and your Deepgram API key as the value.

###### Important

You must create a symmetric KMS key to use with the secret. The default AWS managed KMS key will not work with Amazon Lex V2.

To store your Deepgram API key in Secrets Manager:

1. Open the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. Choose **Store a new secret**.
3. For **Secret type**, choose **Other type of secret**.
4. Configure the secret using one of the following methods:
   - **Key/value pairs method:** Under **Key/value pairs**, add a single key-value pair with `apiToken` as the key and your Deepgram API key as the value.
   - **Plaintext method:** Under **Plaintext**, enter a JSON object with the following structure:

   ```

   {
     "apiToken": "your-deepgram-api-key-here"
   }

   ```

5. Choose **Next**.
6. Enter a name for your secret and choose **Next**.
7. (Optional) Configure secret rotation if needed, then choose **Next**.
8. Review your secret configuration and choose **Store**.
9. After the secret is created, navigate to your secret and copy the ARN. You'll need this ARN when configuring your bot.

## Configuring resource policy for Secrets Manager

To allow Amazon Lex V2 to retrieve your Deepgram API key, you need to attach a resource policy to your secret.

The following is a sample resource policy that allows Amazon Lex V2 to retrieve the secret:

```

{
  "Version": "2012-10-17"		 	 	 ,
  "Statement": [
    {
      "Sid": "LexTrust",
      "Effect": "Allow",
      "Principal": {
        "Service": "lex.amazonaws.com"
      },
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<YOUR_ACCOUNT_ID>"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:lex:us-east-1:<YOUR_ACCOUNT_ID>:bot-alias/*/*"
        }
      }
    }
  ]
}

```

Replace `<YOUR_ACCOUNT_ID>` with your actual AWS account ID and adjust the region in the ARN pattern as needed for your deployment.

## Configuring your bot to use Deepgram

After setting up your Deepgram API key in Secrets Manager, you can configure your Amazon Lex V2 bot to use Deepgram for speech recognition.

To configure Deepgram for your bot:

1. In the Amazon Lex V2 console, navigate to your bot and select the locale you want to configure.
2. For **Speech model preference**, choose **Deepgram**.
3. Additional fields will appear for Deepgram configuration:
   - **Model ID** (optional) - Specify a Deepgram model ID if you want to use a specific model. For available models, see the [Deepgram model documentation](https://developers.deepgram.com/docs/model "https://developers.deepgram.com/docs/model"). If left blank, the API's default model will be used.
   - **Secret ARN** (required) - Enter the ARN of the secret you created in AWS Secrets Manager that contains your Deepgram API key.

4. Save your changes to apply the Deepgram speech model preference to your bot locale.

Your bot is now configured to use Deepgram for speech recognition. Test your bot to ensure that speech recognition is working as expected with the Deepgram integration.

## Troubleshooting Deepgram integration

If you encounter issues with your Deepgram integration, check the following:

- **API key validity:** Ensure your Deepgram API key is valid and has not expired.
- **Secret configuration:** Verify that your secret in AWS Secrets Manager contains the correct key name (`apiToken`) and API key value.
- **Resource policy:** Confirm that the resource policy on your secret allows Amazon Lex V2 to access it with the correct account ID and ARN pattern.
- **KMS key:** Ensure you're using a customer-managed symmetric KMS key, not the default AWS managed key.
- **Model ID:** If you specified a model ID, verify that it's a valid Deepgram model identifier.

For additional support, consult the Amazon Lex V2 CloudWatch logs or contact AWS Support.
