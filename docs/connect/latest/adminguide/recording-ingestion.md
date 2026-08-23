# Recording ingestion and conversational analytics

This guide provides instructions for importing voice recordings from third-party voice
systems into Connect Customer and generating conversational analytics.

###### Note

Recording ingestion is only available in [Amazon
Connect Customer](enable-nextgeneration-amazonconnect.md "enable-nextgeneration-amazonconnect.md") instances.

## Common use cases

Recording ingestion and conversational analytics help address several customer
needs:

- **Migration acceleration** – Customers
  moving to Connect Customer can ingest recordings from their existing voice system and start
  using conversational analytics insights without changing their voice traffic or
  agent experience.
- **Continuity during migration** – Customers
  actively migrating to Connect Customer can import recordings so that agents can find
  historical contacts directly in Connect Customer, without switching to the older
  system.
- **Unified analytics across systems** –
  Existing Connect Customer customers who also operate branch voice systems, meeting
  applications, or other telephony systems can import recordings from those
  systems for centralized and consistent contact tracking and conversational
  analytics within Connect Customer.

## Getting started

Before using recording ingestion, complete the following configuration steps:

- **Service quotas** – Request increases
  for required API quotas
- **Prerequisites** – Verify your instance
  setup and permissions

### Service quotas

The following service quotas apply to recording ingestion.

- **Rate of CreateAttachedFile API
  requests** – The default quota is 0 and must be
  increased before you can create contacts for recording ingestion.
- **Rate of StartContactConversationalAnalyticsJob API
  requests** – The default quota is 0 and must be
  increased before you can start analytics jobs.
- **Concurrent analysis jobs** – The
  default quota is 200 per account and can be increased upon request.

### Prerequisites

- An Amazon Connect Customer instance.
- Conversational analytics enabled on your instance. To enable, open your
  instance in the AWS Console and navigate to **Applications**,
  **Analytics tools**.
- At least one active agent in your Connect Customer instance to associate with
  imported contacts. Depending on your requirements, you might want to do one of
  the following:

  - Assign all contacts to a single logical agent
  - Assign contacts to a single logical agent per line of
    business
  - Assign each contact to a specific individual agent

- Call recordings must be provided in the Connect Customer native format:

  - Format: Linear16 PCM WAV, 8 kHz, stereo, 16-bit
  - Channels: right = agent audio, left = customer audio (including
    conferenced participants)
  - Maximum recording duration: 4 hours

- Your recording source Amazon S3 bucket must be in the same AWS account and
  AWS Region as your Connect Customer instance.

The recording Amazon S3 bucket is configured in your instance's
**Data storage** settings. In the AWS Console, select
your instance and navigate to **Data storage**,
**Call recordings**.

- If call recording encryption is enabled, you must use a customer-managed
  AWS KMS key (CMK) — service-managed keys are not supported.
  Alternatively, you can disable call recording encryption.

### Known limitations

- A contact can only have a recording attached to it once. Recordings cannot
  be replaced once attached to a contact.
- CreateAttachedFile and StartContactConversationalAnalyticsJob only operate
  on imported contacts. You cannot use these APIs on other Connect Customer
  contacts.
- A contact can only have conversational analytics processing performed
  once. If a contact already has conversational analytics results, initiating
  a new processing request will fail.
- Connect Customer does not transcode recordings. Recordings not matching the required
  format will be rejected.
- Contact timestamps (`InitiationTimestamp`,
  `DisconnectTimestamp`,
  `ConnectedToAgentTimestamp`) reflect the time the
  CreateContact API was called, not the original call time from the source
  system. You can use custom contact attributes to store original timestamps
  if needed.

### Best practices

- Test the end-to-end workflow in a non-production Connect Customer instance before
  using in production.
- Ensure WAV files meet the format requirements before ingestion —
  invalid formats are rejected.
- Wait for the recording attachment to complete before calling
  StartContactConversationalAnalyticsJob. Monitor your contact trace record
  (CTR) delivery through Amazon Kinesis Data Stream or Amazon Kinesis Data
  Firehose to confirm attachment status. For more information, see [Enable data streaming for your Connect Customer instance](data-streaming.md "data-streaming.md").
- Configure EventBridge to receive analytics job failure notifications. For
  more information, see [Error notifications: When conversational analytics can't analyze a contact](contact-lens-error-notifications.md "contact-lens-error-notifications.md").

## Verification

To confirm the workflow completed successfully, check the following in the Connect Customer
console:

- The contact appears in the **Contact search** results with
  the expected name and description.
- The recording is playable in the **Contact Details**
  page.
- Conversational analytics (transcript, sentiment, categories, summary) are
  visible in the **Contact Details** page.
