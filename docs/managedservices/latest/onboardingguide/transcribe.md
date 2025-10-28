# Use AMS SSP to provision Amazon Transcribe in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Transcribe capabilities directly in your AMS managed account. Amazon Transcribe is a fully managed and continuously trained
automatic speech recognition service that automatically generates time-stamped text transcripts
from audio files. Amazon Transcribe makes it easy for developers to add speech-to-text capabilities to their
applications. Audio data is virtually impossible for computers to search and analyze. Therefore,
recorded speech needs to be converted to text before it can be used in applications. Historically,
customers had to work with transcription providers that required them to sign expensive contracts
and were hard to integrate into their technology stacks to accomplish this task. Many of these
providers use outdated technology that does not adapt well to different scenarios, like low-fidelity
phone audio common in contact centers, which results in poor accuracy.

Amazon Transcribe uses a deep learning process called automatic speech recognition (ASR) to convert
speech into text, quickly and accurately. Amazon Transcribe can be used to transcribe customer service calls,
automate closed captioning and subtitling, and generate metadata for media assets to create a fully
searchable archive. You can use Amazon Transcribe Medical to add medical speech-to-text capabilities to clinical
documentation applications. To learn more, see
[Amazon Transcribe](https://aws.amazon.com/transcribe/ "https://aws.amazon.com/transcribe/").

## Amazon Transcribe in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request Amazon Transcribe to be set up in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the
following IAM role to your account: `customer_transcribe_role`. Once
provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon Transcribe in my AMS account?**

You must use 'customer-transcribe\*' as the prefix for your buckets when working with
transcribe, unless RA and specified otherwise.

You are not able to create an IAM role within Amazon transcribe.

You cannot use a service-managed S3 bucket for output data in default SSPS (if this
is needed, please reach out to your account CA).

You must submit Risk Acceptance if you want to use customer-managed KMS Keys
that do not fall under the AMS namespace.

**Q: What are the prerequisites or dependencies to using Amazon Transcribe in my AMS account?**

S3 must have access to the buckets with the name 'customer-transcribe\*'. KMS is
required in order to use Amazon Transcribe if your S3 buckets are encrypted with KMS keys.
If a bucket doesn’t need to be encrypted "KMStranscribeAllow" can be removed.
