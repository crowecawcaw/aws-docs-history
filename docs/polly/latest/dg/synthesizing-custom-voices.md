

# Synthesizing speech with a custom voice

To use a custom voice, specify its ID as the `VoiceId` in a `SynthesizeSpeech`, `StartSpeechSynthesisTask`, or `StartSpeechSynthesisStream` request. Set `Engine` to `generative`. The voice must be in `active` status.

To synthesize speech, you must have the permission for the operation that you call: `polly:SynthesizeSpeech`, `polly:StartSpeechSynthesisTask`, or `polly:StartSpeechSynthesisStream`.

In the console, you can synthesize speech on the **Text-to-Speech** tab or on the voice details page. You can also use the AWS CLI.

------
#### [ Console - Text-to-Speech tab ]<a name="synthesizing-custom-voices-console"></a>

**To synthesize speech on the Text-to-Speech tab**

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/).

1. Choose the **Text-to-Speech** tab. The text box contains example text that you can use to try the voice.

1. Under **Engine**, choose **Generative**.

1. Choose the language of your custom voice.

1. For **Voice**, choose your custom voice by its name.

1. To listen to the speech, choose **Listen**.

------
#### [ Console - voice details page ]<a name="synthesizing-custom-voices-console-details"></a>

**To synthesize speech on the voice details page**

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/).

1. Choose the **Voice Cloning** tab.

1. In the list of voices, choose the **Voice ID** of your custom voice. The voice details page opens.

1. Choose the **Synthesize** tab. The text box contains example text that you can use to try the voice.

1. To listen to the speech, choose **Listen**.

------
#### [ AWS CLI ]

The following AWS CLI command synthesizes speech with a custom voice and saves it in `speech.mp3`:

```
aws polly synthesize-speech \
--region us-east-1 \
--voice-id {{vc-9a8fa85dd3}} \
--engine generative \
--output-format mp3 \
--text "Hello from my custom voice." \
speech.mp3
```

------

Custom voices support the same output formats, sample rates, and SSML tags as the other voices of the generative engine. For more information, see [Generative voices](generative-voices.md). The `<phoneme>` tag works with custom voices in English, French, Italian, German, and Spanish.

The same text can sound slightly different from one request to the next. For fixed prompts, such as phone greetings, synthesize the audio once, review it, and store the file.

In the AWS SDKs, the `VoiceId` enumeration contains only the voices that Amazon Polly provides. To use a custom voice, pass its ID as a string. To read the ID from a response, use the string accessor, for example `Voice.idAsString()` in the AWS SDK for Java 2.x.

If the voice uses a customer managed key, you must have the `kms:Decrypt` permission on the key. If Amazon Polly can't use the key, the synthesis request fails. For a `StartSpeechSynthesisTask` request, the task fails, and `TaskStatusReason` describes the problem. For more information, see [Disabling or deleting the key of a voice](encryption-at-rest.md#encryption-at-rest-key-disabled).

## Example: Allowing synthesis with one custom voice
<a name="custom-voices-iam-example"></a>

Custom voices are IAM resources, so you can scope permissions to a single voice. The following policy allows a role to synthesize speech with one custom voice and nothing else. Keep `polly:CreateVoice` and `polly:DeleteVoice` in a separate role that you use to provision voices.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "polly:SynthesizeSpeech",
            "Resource": "arn:aws:polly:{{us-east-1}}:{{111122223333}}:voice/{{vc-9a8fa85dd3}}"
        }
    ]
}
```

A statement that allows `polly:SynthesizeSpeech` on all resources (`"Resource": "*"`) also covers every custom voice in the account. To write one rule for a group of voices, use `aws:ResourceTag` conditions. For more information, see [ABAC with Amazon Polly](security_iam_service-with-iam.md#security_iam_service-with-iam-tags).