

# Troubleshooting custom voices

The following entries describe common problems with custom voices and how to solve them.

`UnknownOperationException` on `CreateVoice`, or no **Voice Cloning** tab in the console  
Your account isn't approved for the voice cloning preview. To request access, see [Availability, languages, and pricing](custom-voices.md#custom-voices-availability).

The voice status is `failed`  
Amazon Polly couldn't create the voice. Call `GetVoice` and read `StatusReason`. If it doesn't name the cause, check the following:  
+ Each recording is 10 seconds to 15 minutes long.
+ The recordings meet the [Recording requirements](creating-custom-voices.md#creating-custom-voices-recordings).
+ You can read the Amazon S3 objects, including with their SSE-KMS key, if they use one.
+ The key policy of your customer managed key allows the requests that Amazon Polly makes to the key while it creates the voice.
+ The new voice passed the check that it sounds like the speaker in your recordings. The check can fail when the recordings have background noise, music, or more than one speaker. Record again in a quiet room with one speaker.
Then delete the voice and create it again.

`Missing required parameter in input: "TermsAccepted"`  
The AWS CLI or the SDK didn't send the request because it omits `TermsAccepted`. In the AWS CLI, add `--terms-accepted`.

`Invalid base64`  
You set `Bytes` with the `=` operator, for example `Bytes=fileb://speaker-1.wav`. Use the `@=` operator instead: `Bytes@=fileb://speaker-1.wav`.

`ValidationException` on `CreateVoice`  
A parameter is missing or not valid. The error message names the parameter. Common causes are the following:  
+ The request has more than 10 recordings.
+ An Amazon S3 URL isn't in the form `s3://{{bucket}}/{{key}}`.
+ `TermsAccepted` is `false`.
+ The language isn't supported.
For a customer managed key, the `reason` field is one of the following:  
+ `kmsKeyNotFound` – No key with the ARN exists. The key can be in your AWS account or in another AWS account.
+ `fieldValidationFailed` – The key is in a different AWS Region from the voice.
+ `kmsKeyUnusable` – The key is disabled, pending deletion, or not a symmetric encryption key.
In the AWS CLI, add `--cli-error-format json` to see the `reason` and `fields` members.

`ValidationException` on synthesis  
The voice ID isn't valid, or the engine isn't `generative`. Use the voice ID, not its name. If you pass the name, the error message lists the voices that Amazon Polly provides.  
This error also occurs when the customer managed key of the voice is disabled, scheduled for deletion, or deleted. To fix it, enable the key or cancel its scheduled deletion.

`ServiceQuotaExceededException` on `CreateVoice`  
You have the maximum number of custom voices in the Region. Voices in every status count toward the quota. Delete a voice that you don't need, or request a higher quota. For more information, see [Custom voice quotas](limits.md#limits-custom-voices).

`AccessDeniedException`  
You don't have the Amazon Polly permission for the operation, or AWS KMS denied the request to use the customer managed key of the voice. For the Amazon Polly permissions, see [Identity and Access Management in Amazon Polly](security-iam.md). For the key policy, see [Configuring permissions to use a customer managed key](encryption-at-rest.md#encryption-at-rest-key-permissions).

`ConflictException`  
The voice isn't in a status that allows the request. Synthesis needs an `active` voice. `DeleteVoice` fails while the voice is `pending`. Check the status with `GetVoice`.

`ResourceNotFoundException`  
No custom voice with the ID exists in your account and Region. Check the ID, the Region, and the account that you use. A voice that you deleted no longer exists.

`ThrottlingException`  
You sent requests faster than the quota allows, or AWS KMS throttled the requests that Amazon Polly made to the customer managed key. `CreateVoice` and `DeleteVoice` together accept 1 request per second. Retry with a delay. The AWS SDKs retry automatically.