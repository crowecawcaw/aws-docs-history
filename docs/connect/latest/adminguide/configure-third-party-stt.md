

# Configure third-party speech-to-text (STT) providers
<a name="configure-third-party-stt"></a>

Use the following instructions to configure a third-party speech-to-text (STT) provider.

## Prerequisites
<a name="stt-prerequisites"></a>
+ A bot with an existing locale.
+ A third-party STT provider API key stored in AWS Secrets Manager. For more information about storing API keys as secrets in Secrets Manager, see [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html).
+ An Secrets Manager resource policy allowing Connect Customer to retrieve the secret. For more information, see [Managing secrets and resource policies](managing-secrets-resource-policies.md).
+ AWS KMS key permissions allowing decryption. For more information, see [Managing secrets and resource policies](managing-secrets-resource-policies.md).
+ A provider model ID and Secrets Manager ARN.

## Step 1: Open the speech model configuration panel
<a name="stt-step1"></a>

1. Sign in to the Connect Customer admin website.

1. Choose **Bots**, then choose the bot.

1. Choose the locale.

1. In the **Speech model** section, choose **Edit** to open the configuration modal.  
![The configuration page for your conversational AI bot.](http://docs.aws.amazon.com/connect/latest/adminguide/images/Lex/01-airlinesbot.png)

## Step 2: Choose the model type
<a name="stt-step2"></a>

In the **Model type** dropdown, choose **Speech-to-Text (STT)**. This ensures the locale is configured for transcription rather than speech-to-speech.

![The speech model dialog box.](http://docs.aws.amazon.com/connect/latest/adminguide/images/Lex/02-speech-model.png)


## Step 3: Review the default speech model settings
<a name="stt-step3"></a>

By default, Amazon is selected as the speech-to-text provider. Review the current settings before switching to a third-party provider.

![The speech model dialog box with Amazon selected as the voice provider.](http://docs.aws.amazon.com/connect/latest/adminguide/images/Lex/03-speech-model-amazon.png)


## Step 4: Choose a third-party STT provider
<a name="stt-step4"></a>

Open the **Voice provider** dropdown and choose a supported third-party speech-to-text provider.

![The speech model dialog box with Deepgram selected as the voice provider.](http://docs.aws.amazon.com/connect/latest/adminguide/images/Lex/04-speech-model-deepgram.png)


## Step 5: Enter the model ID and Secrets Manager ARN
<a name="stt-step5"></a>

1. In **Model ID**, enter the provider's model name.
   + Some providers require a minimum or maximum length.
   + Model IDs are case-sensitive and must match provider documentation.

1. In **Secrets Manager ARN**, enter the ARN of the secret that contains the provider API key.
   + The secret must be in the same Region as your Connect Customer instance.
   + Secrets Manager and KMS key policies must permit Connect Customer to access and decrypt the key. For more information, see [Managing secrets and resource policies](managing-secrets-resource-policies.md).

1. Choose **Continue** to save your changes.

## Build and activate the locale
<a name="stt-build-activate"></a>

If the locale shows **Unbuilt changes**, choose **Build language**. The new STT settings become active after a successful build.

## Runtime behavior (STT)
<a name="stt-runtime-behavior"></a>
+ Connect Customer routes audio to the chosen third-party speech-to-text provider.
+ No changes to flows or Lambda functions are required.
+ Errors such as invalid credentials or invalid model IDs appear in logs.
+ Metrics and analytics continue to function normally.

## Troubleshooting (STT)
<a name="stt-troubleshooting"></a>
+ **Invalid model ID**: Confirm the value with provider documentation.
+ **Access denied**: Verify Secrets Manager and KMS permissions.
+ **Locale build fails**: Ensure required fields are valid.
+ **High latency**: Validate the provider region configuration.