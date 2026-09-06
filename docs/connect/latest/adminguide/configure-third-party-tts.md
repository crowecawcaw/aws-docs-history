

# Configure third-party text-to-speech (TTS) providers
<a name="configure-third-party-tts"></a>

Use the following instructions to configure a third-party text-to-speech (TTS) provider.

## Prerequisites
<a name="tts-prerequisites"></a>
+ A contact flow exists (or you have permission to create one).
+ A third-party TTS provider API key stored in AWS Secrets Manager. For more information about storing API keys as secrets in Secrets Manager, see [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html).
+ An Secrets Manager resource policy allowing Connect Customer to retrieve the key. For more information, see [Managing secrets and resource policies](managing-secrets-resource-policies.md).
+ AWS KMS key permissions allowing decryption. For more information, see [Managing secrets and resource policies](managing-secrets-resource-policies.md).
+ Provider-specific model and voice values.

## Step 1: Open the contact flow
<a name="tts-step1"></a>

1. Sign in to the Connect Customer admin website.

1. Choose **Flows**.

1. Choose an existing flow or create a new one.

## Step 2: Add or choose a Set voice block
<a name="tts-step2"></a>

1. In the Flow designer, search for **Set voice**.

1. Drag the block onto the canvas or choose an existing one.

1. Choose the block to open its configuration panel.

## Step 3: Choose a third-party TTS provider
<a name="tts-step3"></a>

In the **Voice provider** dropdown, choose the third-party text-to-speech provider you want to use.

![The Set voice configuration pane showing a drop-down list of voice providers.](http://docs.aws.amazon.com/connect/latest/adminguide/images/Lex/08-set-voice-amazon.png)


## Step 4: Specify model, voice, Secrets Manager ARN, and language
<a name="tts-step4"></a>

1. Under **Model**, choose **Set manually** and enter the provider model.

1. Under **Voice**, choose **Set manually** and enter the provider voice.

1. Under **Secrets Manager ARN**, choose **Set manually** and enter the ARN of the provider secret.
   + The secret must be in the same AWS Region.
   + The secret value must contain your provider API key. To use a specific provider Region, store the key as a JSON object. For more information about the secret value format and supported provider Regions, see [Endpoints and Regions for third-party speech providers](endpoints-regions-third-party-stt.md).
   + AWS Secrets Manager and KMS policies must permit retrieval and decryption. For more information, see [Managing secrets and resource policies](managing-secrets-resource-policies.md).

1. Under **Language**, choose **Set manually** and choose a language that is supported by the provider voice.  
![The Voice provider configuration pane showing the ElevenLabs third-party voice provider.](http://docs.aws.amazon.com/connect/latest/adminguide/images/Lex/09-voice-provider-elevenlabs.png)

## Step 5: Save and publish the flow
<a name="tts-step5"></a>

1. Choose **Save** in the Flow designer.

1. Choose **Publish** to activate the updated flow settings.

## Runtime behavior (TTS)
<a name="tts-runtime-behavior"></a>
+ Connect Customer sends text to the TTS provider for synthesis.
+ Returned audio is played to the customer.
+ Execution logs include provider errors such as invalid credentials or model values.

## Troubleshooting (TTS)
<a name="tts-troubleshooting"></a>
+ **No audio output**: Validate model and voice values.
+ **Authentication errors**: Verify Secrets Manager and KMS permissions.
+ **Dynamic attributes**: Ensure runtime values resolve to valid provider parameters.
+ **High latency**: Validate provider region alignment.