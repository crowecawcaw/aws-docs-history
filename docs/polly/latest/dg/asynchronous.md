# Long audio files

To create TTS files for large passages of text, use Amazon Polly's _asynchronous
synthesis_ functionality. This uses the three `SpeechSynthesisTask`
APIs:

- `StartSpeechSynthesisTask`: starts a new synthesis task.
- `GetSpeechSynthesisTask`: returns details about a previously submitted
  synthesis task.
- `ListSpeechSynthesisTasks`: lists all submitted synthesis tasks.
  The `SynthesizeSpeech` operation produces audio in near-real time, with
  relatively little latency in most cases. To do this, the operation can only synthesize 3000
  characters.

Amazon Polly's Asynchronous Synthesis feature overcomes the challenge of processing a larger text
document by changing the way the document is both synthesized and returned. When a synthesis
request is made by submitting input text using the `StartSpeechSynthesisTask`,
Amazon Polly queues the requests, and then asynchronously processes them in the background as soon
as the system resources are available. Amazon Polly then uploads the resulting speech or speech
marks stream directly to your (required) Amazon Simple Storage Service (Amazon S3) bucket, and notifies you about the
completed file's availability through your (optional) SNS topic.

In this way, all of the functionality except near-real time processing is available for
texts of up to 100,000 billable characters (or 200,000 total characters) in length.

To synthesize a document using this method, you must have an Amazon S3 bucket that is writable
to which the audio file can be saved. You can be notified when the synthesized audio is
ready by providing an optional SNS Topic identifier. When the synthesis task is complete,
Amazon Polly will publish a message on that topic. This message may also contain useful error
information in cases where the synthesis task didn't succeed. To do this, make sure that the
user creating the synthesis task can also publish to the SNS Topic. See the [Amazon SNS
documentation](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md") for more information on how to create and subscribe to an SNS
Topic.

**Encryption**

You can store the output file in an encrypted form in your S3 bucket if desired. To do
this, you enable [Amazon S3
bucket encryption](../../../AmazonS3/latest/dev/bucket-encryption.md "../../../AmazonS3/latest/dev/bucket-encryption.md"), which use one of the strongest block ciphers available,
256-bit Advanced Encryption Standard (AES-256).

###### Topics

- [Setting up the IAM policy for asynchronous
  synthesis](asynchronous-iam.md "asynchronous-iam.md")
- [Creating long audio files](longer-console.md "longer-console.md")
