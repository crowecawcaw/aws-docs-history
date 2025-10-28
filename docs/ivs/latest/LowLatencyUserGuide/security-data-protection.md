# IVS Data Protection

For data sent to Amazon Interactive Video Service (IVS), the following data
protections are in place:

- Amazon IVS encrypts data in transit via HTTPS API endpoints, RTMPS ingest, and
  HTTPS playback. No configuration is required for the API endpoints.
  - For ingest, streamers can secure their content by using RTMPS. This is
    available by default. See [Getting Started with IVS Low-Latency Streaming](getting-started.md "getting-started.md").
  - IVS channels can be configured to allow insecure RTMP ingest, though
    we recommend using RTMPS unless you have specific and verified use cases
    that require RTMP.
  - For transcoding/transmuxing, data may be transmitted unencrypted on
    internal Amazon networks.
  - For playback, data is served over HTTPS.

- Live-video content is not stored and is ephemeral. It simply travels through
  the system and is cached (on internal systems) while being viewed.
- For the auto-record-to-S3 feature, video content is written to Amazon S3. For
  more information, see [data protection in Amazon
  S3](../../../AmazonS3/latest/userguide/DataDurability.md "../../../AmazonS3/latest/userguide/DataDurability.md").
- All stored, customer-input metadata is in AWS-managed services using
  server-side encryption.
- To improve quality of service, Amazon IVS stores customer (end user) metadata
  (for example, buffer rates for a particular region). This metadata cannot be
  used to personally identify your end users.
- Public encryption keys (which you manage) can be used with the
  `ImportPlaybackKeyPair` API operation. See the [IVS Low-Latency
  Streaming API Reference](../LowLatencyAPIReference/Welcome.md "../LowLatencyAPIReference/Welcome.md"). _Do not share these
  encryption keys_.
  Amazon IVS does not require that you supply any customer (end user) data. There are no
  fields in channels, inputs, or input security groups where there is an expectation that
  you will provide customer (end user) data.

Do not put sensitive identifying information such as your customer (end user) account
numbers into free-form fields such as a Name field. This includes when you work with the
Amazon IVS console or API, AWS CLI, or AWS SDKs. Any piece of data that you enter
into Amazon IVS might be included in diagnostic logs.

Streams are not end-to-end encrypted; a stream may be transmitted unencrypted
internally in the IVS network, for processing.
