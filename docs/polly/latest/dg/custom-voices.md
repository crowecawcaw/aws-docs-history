

# Voice cloning in Amazon Polly

**Note**  
Voice cloning is in preview release for Amazon Polly and is subject to change. Access is already enabled for select Amazon Polly customers. Others can reach out to their AWS account team or [apply here](https://pages.awscloud.com/amazon-polly-voice-cloning-20261119.html) to get access.

With *voice cloning*, you create a *custom voice* from recordings of one consenting speaker. The speech that you synthesize with the voice sounds similar to that speaker. You use a custom voice with the generative engine, in the same way as the voices that Amazon Polly provides.

This chapter describes how to create, use, and manage custom voices with voice cloning. For the operations, parameters, and errors, see the [CreateVoice](https://docs.aws.amazon.com/polly/latest/APIReference/API_CreateVoice.html), [GetVoice](https://docs.aws.amazon.com/polly/latest/APIReference/API_GetVoice.html), and [DeleteVoice](https://docs.aws.amazon.com/polly/latest/APIReference/API_DeleteVoice.html) pages of the *Amazon Polly API Reference*.

A custom voice is different from a brand voice. You create a custom voice yourself, from your own recordings, with the console or the `CreateVoice` operation. A brand voice is an exclusive voice that the Amazon Polly team builds for your brand persona. You work with the Amazon Polly team to create a brand voice, and you can't create it with `CreateVoice`. For more information about brand voices, see [Brand voices](available-voices.md#brand-voices).

## Why use a custom voice
<a name="custom-voices-benefits"></a>

A custom voice gives your application a voice that you choose, instead of one of the voices that Amazon Polly provides. You might use a custom voice for the following:
+ **One voice for all your content** – Prompts, messages, and narration all sound like the same speaker, and you synthesize new lines from text instead of recording them.
+ **A recognizable voice** – Your application can speak as your spokesperson, host, or product persona.
+ **Quick script changes** – When a script changes, you synthesize the new version. You don't need a new recording session with your voice talent.
+ **Control over the voice** – You choose the speaker and the recordings, and you can delete the voice at any time, for example if the speaker withdraws consent.

A custom voice works best when the recordings capture the speech style that you want the voice to use. For guidance on recordings, see [Recording requirements](creating-custom-voices.md#creating-custom-voices-recordings).

## How custom voices work
<a name="custom-voices-how"></a>

To create a custom voice, you provide one or more recordings of the speaker and choose the language and a name for the voice. Amazon Polly creates the voice in the background. Creation typically takes 5 to 10 minutes.

Before a new voice becomes available, Amazon Polly checks that it sounds like the speaker in your recordings. This is a quality check. It doesn't verify consent.

A custom voice belongs to the AWS account and the AWS Region where you create it. Other accounts can't use it. The voice works only with the generative engine.

Keep the following in mind when you use a custom voice:
+ Custom voices use the same generative model as the voices that Amazon Polly provides. Updates to the model can cause slight variations in the way a custom voice sounds, even when its overall quality improves. This can affect content that you synthesize over a long period, for example a season of podcasts.
+ In rare cases, the generative model can cut off a word or produce speech that you didn't expect. For more information, see [Generative voices](generative-voices.md).

## Your responsibilities
<a name="custom-voices-responsibilities"></a>

You can create a custom voice only from recordings that you have the right to use. When you create a custom voice, you must confirm the following two statements:
+ "I confirm that I have obtained all necessary consents required under any applicable laws and regulations, including biometric privacy laws, from the owner of this voice to clone these voice samples."
+ "I confirm that I will not use the generated content for any illegal, fraudulent, or harmful purpose and reaffirm my obligation to abide by the AWS Service Terms, Biometric Notice and Consent Terms, AWS Responsible AI Policy, and AWS Acceptable Use Policy."

In the Amazon Polly console, you select two check boxes. In the API, you set `TermsAccepted` to `true`.

If your application lets your own users create voices, you confirm these statements for each of them. Collect their consent in your application before you call `CreateVoice`.

We recommend that you do the following:
+ Keep a record of each speaker's consent with the voice ID.
+ Delete the voice if the speaker withdraws consent.
+ Tell listeners when they hear a synthetic voice, where that's appropriate.
+ Grant permissions for custom voices only to the people and systems that need them.

If a custom voice is created or used in violation of the AWS Service Terms or the AWS Acceptable Use Policy, AWS can delete the voice or turn off voice cloning for the account. To report a custom voice that was created without the speaker's consent, see [How do I report abuse of AWS resources?](https://repost.aws/knowledge-center/report-aws-abuse) on the AWS re:Post website.

For the full terms, see the following pages on the AWS website:
+ [AWS Service Terms](https://aws.amazon.com/service-terms/)
+ [Biometric Notice and Consent Terms](https://aws.amazon.com/legal/biometric-notice-and-consent-terms/)
+ [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/)
+ [AWS Acceptable Use Policy](https://aws.amazon.com/aup/)

## Availability, languages, and pricing
<a name="custom-voices-availability"></a>

During the preview, voice cloning is available only to AWS accounts that Amazon Polly has approved for it. To get access, contact your AWS account team or [apply for access](https://pages.awscloud.com/amazon-polly-voice-cloning-20261119.html). After your account is approved, you can create custom voices in the AWS Regions where the generative engine is available. For more information, see [Feature and region compatibility](generative-voices.md#generative-regions).

A custom voice speaks the language that you choose when you create it. You can create custom voices in the following languages:
+ English, US (`en-US`)
+ French (`fr-FR`)
+ German (`de-DE`)
+ Hindi (`hi-IN`)
+ Italian (`it-IT`)
+ Portuguese, Brazilian (`pt-BR`)
+ Spanish, US (`es-US`)

For more information about the number of custom voices that you can have, see [Custom voice quotas](limits.md#limits-custom-voices).

Creating a custom voice is free. Amazon Polly charges for the speech that you synthesize with it, in the same way as for other generative voices. For pricing, see the [Amazon Polly pricing information page](https://aws.amazon.com/polly/pricing/). If you encrypt a custom voice with a customer managed key, you pay AWS Key Management Service (AWS KMS) charges for the key and for the requests that Amazon Polly makes with it. For more information, see [Encryption at rest](encryption-at-rest.md).

## Data that Amazon Polly stores
<a name="custom-voices-data"></a>

Amazon Polly creates the voice by processing your recordings. It accesses the recordings only while it creates the voice, and it doesn't keep a copy of them after creation ends. Amazon Polly doesn't use your recordings to train Amazon Polly models, and it doesn't return the audio of your recordings in any response.

Amazon Polly stores the voice for as long as it exists. You can delete the voice at any time after Amazon Polly creates it. When you delete a voice, Amazon Polly deletes the voice data that it stored, and the voice can no longer be used. You can't restore a deleted voice.

**Tip**  
Keep your original recordings. You need them to create the voice again, for example with a different key, in another Region, or after a failed creation.

Amazon Polly encrypts the voice at rest. By default, it uses an AWS owned key. You can choose a customer managed key instead. For more information, see [Encryption at rest](encryption-at-rest.md).