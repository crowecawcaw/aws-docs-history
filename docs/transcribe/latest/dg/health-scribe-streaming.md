# AWS HealthScribe streaming

With AWS HealthScribe streaming, you can transcribe medical conversations in real-time. AWS HealthScribe streaming is a real-time
HTTP2 based bi-directional service that accepts audio stream on one channel and vends an audio transcription on the other
channel. After streaming is complete, AWS HealthScribe analyzes the stream contents and produces a transcript JSON file and a clinical note JSON file.

To start streaming, use the [StartMedicalScribeStream](../APIReference/API_streaming_StartMedicalScribeStream.md "../APIReference/API_streaming_StartMedicalScribeStream.md") API
operation. This API starts an HTTP2 based bi-directional channel that you use to stream audio events.

When you start a stream, first specify the stream configuration in a `MedicalScribeConfigurationEvent`.
This event includes channel definitions, encryption settings, and post-stream analytics settings, such as the output configuration for aggregated transcript and clinical note generation.

After you start streaming audio, you manage the stream as follows:

- When you are finished, to start processing the results with post-stream analytics, send a `MedicalScribeSessionControlEvent` with a `Type` of
  `END_OF_SESSION` and AWS HealthScribe starts the analytics.
- To pause streaming, complete the input stream without sending the
  `MedicalScribeSessionControlEvent`.
- To resume a paused stream, use the `StartMedicalScribeStream` API operation and specify the
  same `SessionId`. This is the `SessionId` you used when you originally started the stream.

###### Topics

- [Guidelines and requirements](#health-scribe-streaming-requirements "#health-scribe-streaming-requirements")
- [ResourceAccessRoleArn role permissions](#health-scribe-data-access-role "#health-scribe-data-access-role")
- [Starting AWS HealthScribe streaming transcription](health-scribe-streaming-setting-up.md "health-scribe-streaming-setting-up.md")

## Guidelines and requirements

The following are guidelines and requirements for AWS HealthScribe streaming:

- Before you send audio events, you must first specify the stream configuration in a `MedicalScribeConfigurationEvent`.
- To run post-stream analytics, the `ResourceAccessRoleArn` in your
  `MedicalScribeConfigurationEvent` must have the correct permissions. For more information, see
  [ResourceAccessRoleArn role permissions](#health-scribe-data-access-role "#health-scribe-data-access-role").
- You can resume a session any number of times within 5 hours from the initial stream creation.
- You can stream at most 2 hours of audio over a session across all streaming requests.
- By default, AWS HealthScribe provides encryption at rest to protect sensitive customer data using Amazon S3-managed keys. When you start a stream, you can specify a AWS KMS key for a second layer of encryption. Your
  `ResourceAccessRoleArn` must have permission to use your AWS KMS key. For more information, see [Data Encryption at rest for AWS HealthScribe](health-scribe-encryption.md "health-scribe-encryption.md").
- You can use AWS HealthScribe streaming with the AWS SDKs, excluding the SDK for Python (Boto3) and SDK for PHP.
- If a `LimitExceededException` exception occurs after you end a stream, you can restart the session and still generate post-stream analytics.
  To restart the stream, use the [StartMedicalScribeStream](../APIReference/API_streaming_StartMedicalScribeStream.md "../APIReference/API_streaming_StartMedicalScribeStream.md") API and use same `SessionID`. Then send a `MedicalScribeSessionControlEvent` with a `Type` of
  `END_OF_SESSION` and AWS HealthScribe starts the analytics.

## ResourceAccessRoleArn role permissions

To run post-stream analytics, the `ResourceAccessRoleArn` in your `MedicalScribeConfigurationEvent` must be able to access your Amazon S3 output bucket
and, if you provide it, your AWS KMS key. Also, the role's trust policy must grant the `transcribe.streaming.amazonaws.com` service permission to assume the role.

The following is an example IAM policy that grants Amazon S3 bucket permissions and AWS KMS key permissions. For more information, see [Data Encryption at rest for AWS HealthScribe](health-scribe-encryption.md "health-scribe-encryption.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "kms:DescribeKey",
 "kms:Decrypt",
 "kms:Encrypt",
 "kms:GenerateDataKey*"
 ],
 "Resource": "arn:aws:kms:us-west-2:`123456789012`:key/`1234abcd-12ab-34cd-56ef-123456SAMPLE`",
 "Effect": "Allow"
 }
 ]
}`

```

The following is an example trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "transcribe.streaming.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
