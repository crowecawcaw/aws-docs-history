# API workflow

## Step 1: CreateContact

Use [CreateContact](../APIReference/API_CreateContact.md "../APIReference/API_CreateContact.md") to create a voice contact in `COMPLETED`
state. The contact represents the call and is the anchor for the recording and
analytics.

Request:

```
aws connect create-contact \
  --instance-id "`instance-id`" \
  --region "`region`" \
  --cli-input-json '{
    "InstanceId": "`instance-id`",
    "ClientToken": "`unique-idempotency-token`",
    "Channel": "VOICE",
    "InitiationMethod": "INBOUND",
    "InitiateAs": "COMPLETED",
    "Name": "`descriptive-contact-name`",
    "Description": "`optional-description`",
    "UserInfo": { "UserId": "`agent-arn`" }
  }'
```

Response:

```
{ "ContactId": "`contact-id`" }
```

Notes:

- `UserInfo.UserId` must be the ARN of an agent that exists in
  your Connect Customer instance.
- You will need the returned `ContactId` in Steps 2 and

3.

## Step 2: CreateAttachedFile

Use [CreateAttachedFile](../APIReference/API_CreateAttachedFile.md "../APIReference/API_CreateAttachedFile.md") to import the recording from your Amazon S3 bucket into
Connect Customer storage. Connect Customer performs an S3-to-S3 copy.

Request:

```
aws connect create-attached-file \
  --instance-id "`instance-id`" \
  --region "`region`" \
  --file-use-case-type "VOICE_RECORDING" \
  --file-source-uri "s3://`source-bucket`/`path-to-recording`.wav" \
  --associated-resource-arn "`contact-arn`" \
  --client-token "`unique-idempotency-token`"
```

Response:

```
{
  "CreationTime": "2026-03-31T00:00:00.000Z",
  "FileId": "`file-id`",
  "FileArn": "arn:aws:connect:`region`:`account-id`:instance/`instance-id`/file/`file-id`",
  "FileStatus": "PROCESSING"
}
```

Notes:

- Construct the `ContactArn` using the `ContactId`
  from Step 1:

```
arn:aws:connect:`region`:`account-id`:instance/`instance-id`/contact/`contact-id`
```

- `ClientToken` enables safe retries — pass the same value
  to retry the request without creating duplicate resources.
- Attempting to attach a second recording to the same contact will be
  rejected.
- `FileStatus` will be `PROCESSING` initially. The
  copy completes asynchronously — monitor your CTR (delivered via Amazon S3
  or Kinesis) for the final attachment status.
- Do not attempt Step 3 until the recording is attached.
- The external voice charge applies once the recording is attached. For
  pricing information, see [Connect Customer
  Pricing](https://aws.amazon.com/connect/pricing/ "https://aws.amazon.com/connect/pricing/").

## Step 3: StartContactConversationalAnalyticsJob

Use [StartContactConversationalAnalyticsJob](../APIReference/API_StartContactConversationalAnalyticsJob.md "../APIReference/API_StartContactConversationalAnalyticsJob.md") to initiate conversational
analytics on the imported recording.

Request:

```
aws connect start-contact-conversational-analytics-job \
  --instance-id "`instance-id`" \
  --contact-id "`contact-id`" \
  --region "`region`" \
  --cli-input-json '{
    "ContactId": "`contact-id`",
    "InstanceId": "`instance-id`",
    "AnalyticsModes": ["PostContact"],
    "LanguageConfiguration": { "LanguageLocale": "en-US" },
    "RedactionConfiguration": { "Behavior": "Enable", "Policy": "RedactedAndOriginal" },
    "SentimentConfiguration": { "Behavior": "Enable" },
    "SummaryConfiguration": { "SummaryModes": ["PostContact"] },
    "RulesConfiguration": { "Behavior": "Enable" }
  }'
```

Response:

```
{ "ContactId": "`contact-id`", "InstanceId": "`instance-id`" }
```

Notes:

- The contact must be in `COMPLETED` state with a recording
  attached.
- `RedactionConfiguration.Policy` options:
  `RedactedOnly`,
  `RedactedAndOriginal`.
- `RulesConfiguration` cannot be disabled — the rules
  configured in your account are executed.
- Analysis runs asynchronously. Results are delivered to your
  Connect Customer-configured Amazon S3 bucket.
- `ContactId` is used as the job identifier — duplicate
  analysis jobs on the same contact are not allowed.
- Subscribe to EventBridge to receive notifications when analysis fails.
  Successful completion is indicated by the conversational analytics output
  file being delivered to your configured Amazon S3 bucket. For more information,
  see [Error notifications: When conversational analytics can't analyze a contact](contact-lens-error-notifications.md "contact-lens-error-notifications.md").
