# Amazon Kinesis Video Streams service quotas

Kinesis Video Streams has the following service quotas:

###### Important

The following service quotas are either soft **[s]**,
which can be upgraded by submitting a support ticket, or hard **[h]**, which can't be increased. You will see [s] and [h] next to
individual service quota in the tables below.

## Control plane API service quotas

The following section describes service quotas for control plane APIs. TPS stands for
_transactions per second_.

When an account-level or resource-level request limit is reached, a
`ClientLimitExceededException` is thrown.

| API                                      | Account limit: Request | Account limit: Streams                                                                                                                                                                                                                                                                                                               | Stream-level limit | Relevant exceptions and notes                                                                                                                                                        |
| ---------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **CreateStream**                         | 50 TPS [s]             | 10,000 streams per account [s] in all supported Regions. NoteThis limit can be increased up to 100,000 (or more) streams<br>per account [s]. Sign in to the AWS Management Console at [https://console.aws.amazon.com/](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") and request an increase of this<br>limit. |                    | Devices, CLIs, SDK-driven access, and the console can all invoke this<br>API. Only one API call succeeds if the stream doesn’t already<br>exist.                                     |
| **DeleteEdgeConfiguration**              | 10 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | 1 TPS [h]          |                                                                                                                                                                                      |
| **DeleteStream**                         | 50 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | 5 TPS [h]          |                                                                                                                                                                                      |
| **DescribeEdgeConfiguration**            | 50 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | 5 TPS [h]          |                                                                                                                                                                                      |
| **DescribeImageGenerationConfiguration** | 50 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | 5 TPS [h]          |                                                                                                                                                                                      |
| **DescribeMappedResourceConfiguration**  | 50 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | 5 TPS [h]          |                                                                                                                                                                                      |
| **DescribeNotificationConfiguration**    | 50 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | 5 TPS [h]          |                                                                                                                                                                                      |
| **DescribeStream**                       | 300 TPS [h]            | N/A                                                                                                                                                                                                                                                                                                                                  | 5 TPS [h]          |                                                                                                                                                                                      |
| **GetDataEndpoint**                      | 300 TPS [h]            | N/A                                                                                                                                                                                                                                                                                                                                  | 5 TPS [h]          | Called every 45 minutes to refresh the streaming token for most<br>`PutMedia`/`GetMedia` use cases.<br>Caching data endpoints is safe if the application reloads them on<br>failure. |
| **ListEdgeAgentConfigurations**          | 50 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | N/A                |                                                                                                                                                                                      |
| **ListStreams**                          | 50 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  |                    |                                                                                                                                                                                      |
| **ListTagsForStream**                    | 50 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | 5 TPS [h]          |                                                                                                                                                                                      |
| **StartEdgeConfigurationUpdate**         | 10 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | 1 TPS [h]          |                                                                                                                                                                                      |
| **TagStream**                            | 50 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | 5 TPS [h]          |                                                                                                                                                                                      |
| **UntagStream**                          | 50 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | 5 TPS [h]          |                                                                                                                                                                                      |
| **UpdateDataRetention**                  | 50 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | 5 TPS [h]          |                                                                                                                                                                                      |
| **UpdateImageGenerationConfiguration**   | 50 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | 5 TPS [h]          |                                                                                                                                                                                      |
| **UpdateNotificationConfiguration**      | 50 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | 5 TPS [h]          |                                                                                                                                                                                      |
| **UpdateStream**                         | 50 TPS [h]             | N/A                                                                                                                                                                                                                                                                                                                                  | 5 TPS [h]          |                                                                                                                                                                                      |

## Media and archived-media API service quotas

The following section describes service quotas for media and archived media
APIs.

When an account-level or resource-level request limit is reached, a
`ClientLimitExceededException` is thrown.

When a connection-level limit is reached, a
`ConnectionLimitExceededException` is thrown.

The following errors or acks are thrown when a fragment-level limit is reached:

- A `MIN_FRAGMENT_DURATION_REACHED` ack is returned for a fragment
  below the minimum duration.
- A `MAX_FRAGMENT_DURATION_REACHED` ack is returned for a fragment
  above the maximum duration.
- A `MAX_FRAGMENT_SIZE` ack is returned for a fragment above the
  maximum data size.
- A `FragmentLimitExceeded` exception is thrown if a fragment limit
  is reached in a `GetMediaForFragmentList` operation.

**Data plane API service quotas**

| API                            | Stream-level limit | Connection-level limit | Bandwidth limit                                   | Fragment-level limit                                                                                                                                                                                                                                                | Relevant exceptions and notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------ | ------------------ | ---------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PutMedia**                   | 5 TPS [h]          | 1 [h]                  | 12.5 MB/second, or 100 Mbps [s] **per<br>stream** | • Minimum fragment duration: 1 second [h]<br>• Maximum fragment duration: 20 seconds [h]<br>• Maximum fragment size: 50 MB [h]<br>• Maximum number of tracks: 3 [s]<br>• Maximum fragments sent per second: 5 [h]<br>• Maximum fragment metadata limit: 10 tags [h] | [PutMedia](API_dataplane_PutMedia.md "API_dataplane_PutMedia.md") requests are streaming, long-running connections.<br>You don't need to open a new connection for each piece of data because<br>you can send multiple fragments in a single persistent connection. If<br>you attempt more than one concurrent `PutMedia` connection,<br>Kinesis Video Streams throttles the latest connections with a<br>`ConnectionLimitExceededException` error message.                                                                                                                                                                                                                                                            |
| **GetClip**                    | N/A                | N/A                    | 100 MB size limit [h]                             | Maximum number of fragments: 200 [h]                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **GetDASHStreamingSessionURL** | 25 TPS [h]         | N/A                    | N/A                                               | N/A                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **GetHLSStreamingSessionURL**  | 25 TPS [h]         | N/A                    | N/A                                               | N/A                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **GetImages**                  | N/A                | N/A                    | 100 MB [h]                                        | N/A                                                                                                                                                                                                                                                                 | Maximum number of images per request is 100 [h].<br>NoteThe minimum value for `SamplingInterval` is 200<br>milliseconds (ms), which is 5 images per second.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **GetMedia**                   | 5 TPS [h]          | 3 [h]                  | 25 MB/s or 200 Mbps [s]                           | Maximum of 5 fragments sent per second [h]                                                                                                                                                                                                                          | [GetMedia](API_dataplane_GetMedia.md "API_dataplane_GetMedia.md") requests are streaming, long-running connections. You don't<br>need to open a new connection for each piece of data because you can<br>send multiple fragments in a single persistent connection. If you<br>attempt more than three concurrent `GetMedia` connections,<br>Kinesis Video Streams throttles the latest connections with a<br>`ConnectionLimitExceededException` error message.<br>If a typical fragment is approximately 5 MB, this limit means<br>~75 MBps per Kinesis video stream. Such a stream would have an outgoing<br>bitrate of 2x the streams' maximum incoming bitrate.<br>Note`GetMedia` isn't used for HLS/DASH playback. |
| **GetMediaForFragmentList**    | N/A                | 5 [s]                  | 25 MB/s or 200 Mbps [s]                           | Maximum number of fragments: 1000 [h]                                                                                                                                                                                                                               | Five fragment-based consuming applications can concurrently invoke<br>`GetMediaForFragmentList`. Further connections are<br>rejected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

**Video playback protocol API service quotas**

| API                         | Session-level limit | Fragment-level limit                                |
| --------------------------- | ------------------- | --------------------------------------------------- |
| **GetDASHManifestPlaylist** | 5 TPS [h]           | Maximum number of fragments per playlist: 5,000 [h] |
| **GetHLSMasterPlaylist**    | 5 TPS [h]           | N/A                                                 |
| **GetHLSMediaPlaylist**     | 5 TPS [h]           | Maximum number of fragments per playlist: 5,000 [h] |
| **GetMP4InitFragment**      | 5 TPS [h]           | N/A                                                 |
| **GetMP4MediaFragment**     | 20 TPS [h]          | N/A                                                 |
| **GetTSFragment**           | 20 TPS [h]          | N/A                                                 |

## Fragment-metadata and fragment-media

quotas

Kinesis Video Streams [APIs for accessing archived media](API_Reference.md "API_Reference.md") are throttled based on the number of
fragments requested rather than the number of API calls. APIs are rate-limited by both
the number of fragment metadata and the number of fragment media that's requested. The
fragment metadata and fragment media quotas are applied per stream. In other words,
requests for fragment metadata or media in one stream don't apply to the quotas of
another stream. However, within a given stream, each quota is shared across multiple
APIs. This means that, for a given stream, requests for fragments across different APIs
consume from the same quota. When either the fragment metadata or fragment media quota
for a stream is exceeded, the API returns a `ClientLimitExceededException`.
The following tables show how the APIs consume from each of the two types of quota. For
the second column in these tables, assume that if a stream has a quota of N, that means
the APIs have N points to consume from that quota type for that stream. The
`GetClip` API appears in both tables.

**Fragment-metadata quota consumption**

| API                   | Number of quota points consumed per request                 | Shared quota (N)                               |
| --------------------- | ----------------------------------------------------------- | ---------------------------------------------- |
| `ListFragments`       | Value of the `MaxResults` parameter                         | 10,000 quota points per second, per stream [h] |
| `GetClip`             | Number of fragments in the resulting clip                   |
| `GetHLSMediaPlaylist` | Value of the `MaxMediaPlaylistFragmentResults`<br>parameter |
| `GetDASHManifest`     | Value of the `MaxManifestFragmentResults`<br>parameter      |
| `GetImages`           | Value of 400 + max number of images requested               |

**Fragment-media quota consumption**

| API                       | Number of quota points consumed per request    | Shared quota (N)                            |
| ------------------------- | ---------------------------------------------- | ------------------------------------------- |
| `GetMediaForFragmentList` | Number of fragments in the Fragments parameter | 500 quota points per second, per stream [h] |
| `GetClip`                 | Number of fragments in the resulting clip      |
| `GetMP4MediaFragment`     | 1                                              |
| `GetTSFragment`           | 1                                              |
| `GetImages`               | Max number of images requested                 |

For example, with a quota of 500 fragment media per second, the following call
patterns for a particular stream are supported:

- 5 requests per second to `GetClip` with 100 fragments in each
  clip.
- 100 requests per second to `GetClip` with 5 fragments in each
  clip.
- 2 requests per second to `GetClip` with 100 fragments in each clip
  and 3 requests per second to `GetMediaForFragmentList` in each
  clip.
- 400 requests per second to `GetMP4MediaFragment` and 100 requests
  per second to `GetTSFragment`.

These quotas have an important implication regarding the number of HLS and MPEG-DASH
sessions that can be supported per stream. There's no limit to the number of HLS and
DASH sessions that can be in use by media players at a given time. Therefore, it's
important that the playback application doesn't allow too many sessions to be in use
concurrently. The following two examples describe how to determine the number of
concurrent playback sessions that can be supported:

_Example 1: Live streaming_

In a live streaming scenario with HLS with 1 second duration fragments, an audio and
video track, and `MaxMediaPlaylistFragmentResults` set to five, a media
player typically makes two calls to `GetHLSMediaPlaylist` per second. One
call is for the latest video metadata and another for the corresponding audio metadata.
The two calls consume five fragment metadata quota points each. It also makes two calls
to `GetMP4MediaFragment` per second: one call for the latest video and
another for the corresponding audio. Each call consumes a single fragment media token,
so two tokens are consumed in total.

In this scenario, up to 250 concurrent playback sessions can be supported. With 250
sessions, this scenario consumes 2,500 fragment metadata quota points per second (well
below the 10,000 quota) and 500 fragment media quota points per second.

_Example 2: On-demand playback_

In an on-demand playback scenario of a past event with MPEG-DASH, an audio and video
track and `MaxManifestFragmentResults` set to 1,000, a media player typically
calls `GetDASHManifest` once at the start of the session (consuming 1,000
fragment metadata quota points) and it calls `GetMP4MediaFragment` at a rate
of up to 5 times per second (consuming 5 fragment media quota points) until all
fragments are loaded. In this scenario, up to 10 new sessions can be started per second
(right at the 10,000 fragment metadata per second quota), and up to 100 sessions can be
actively loading fragment media at a rate of 5 per second (right at the 500 fragment
media per second quota).

You can use `ArchivedFragmentsConsumed.Metadata` and
`ArchivedFragmentsConsumed.Media` to monitor the consumption of fragment
metadata and fragment media quota points, respectively. For information about
monitoring, see [Monitoring Amazon Kinesis Video Streams](monitoring.md "monitoring.md").

## Streaming metadata service quotas

The following service quotas apply to adding streaming metadata to a
Kinesis video stream:

- You can prepend up to 10 metadata items to a fragment.
- A fragment metadata _name_ can be up to 128 bytes in
  length.
- A fragment metadata _value_ can be up to 256 bytes in
  length.
- A fragment metadata _name_ can't begin with the string
  "`AWS`". If such a metadata item is added, the
  `putFragmentMetadata` method in the PIC returns a
  `STATUS_INVALID_METADATA_NAME` error (error code
  `0x52000077`). Your application can then either ignore the error
  (the PIC doesn't add the metadata item), or respond to the error.

## Producer SDK quotas

The following table contains the current quotas for values in the SDK. See [Upload to Kinesis Video Streams](producer-sdk.md "producer-sdk.md") for more information.

###### Note

Before setting these values, you must validate your inputs. The SDK doesn't
validate these limits, and a runtime error occurs if the limits are exceeded.

| Value                           | Limit                                                 | Notes                                                                                                                                                                                                       |
| ------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Max stream count                | 128                                                   | The maximum number of streams that a producer object can create. This<br>is a soft limit (you can request an increase). It guarantees that the<br>producer doesn't accidentally create streams recursively. |
| Max device name length          | 128 characters                                        |                                                                                                                                                                                                             |
| Max tag count                   | 50 per stream                                         |                                                                                                                                                                                                             |
| Max stream name length          | 256 characters                                        |                                                                                                                                                                                                             |
| Min storage size                | 10 MiB = 10 \<br>• 1024 \<br>• 1024 bytes             |                                                                                                                                                                                                             |
| Max storage size                | 10 GiB = 10 \<br>• 1024 \<br>• 1024 \<br>• 1024 bytes |                                                                                                                                                                                                             |
| Max root directory path length  | 4,096 characters                                      |                                                                                                                                                                                                             |
| Max auth info length            | 10,000 bytes                                          |                                                                                                                                                                                                             |
| Max URI string length           | 10,000 characters                                     |                                                                                                                                                                                                             |
| Max tag name length             | 128 characters                                        |                                                                                                                                                                                                             |
| Max tag value length            | 1,024 characters                                      |                                                                                                                                                                                                             |
| Min security token period       | 30 seconds                                            |                                                                                                                                                                                                             |
| Security token grace period     | 40 minutes                                            | If the specified duration is longer, it's limited to this<br>value.                                                                                                                                         |
| Retention period                | 0 or greater than one hour                            | 0 indicates no retention.                                                                                                                                                                                   |
| Min cluster duration            | 1 second                                              | The value is specified in 100 ns units, which is the SDK<br>standard.                                                                                                                                       |
| Max cluster duration            | 30 seconds                                            | The value is specified in 100 ns units, which is the SDK standard.<br>The backend API can enforce a shorter cluster duration.                                                                               |
| Max fragment size               | 50 MB                                                 | For more information, see [Amazon Kinesis Video Streams service quotas](limits.md "limits.md").                                                                                                             |
| Max fragment duration           | 20 seconds                                            | For more information, see [Amazon Kinesis Video Streams service quotas](limits.md "limits.md").                                                                                                             |
| Max connection duration         | 45 minutes                                            | The backend closes the connection after this time. The SDK rotates<br>the token and establishes a new connection within this time.                                                                          |
| Max ACK segment length          | 1,024 characters                                      | Maximum segment length of the acknowledgement sent to the ACK parser<br>function.                                                                                                                           |
| Max content type string length  | 128 characters                                        |                                                                                                                                                                                                             |
| Max codec ID string length      | 32 characters                                         |                                                                                                                                                                                                             |
| Max track name string length    | 32 characters                                         |                                                                                                                                                                                                             |
| Max codec private data length   | 1 MiB = 1 \<br>• 1024 \<br>• 1024 bytes               |                                                                                                                                                                                                             |
| Min timecode scale value length | 100 ns                                                | The minimum timecode scale value to represent the frame timestamps in<br>the resulting MKV cluster. The value is specified in increments of 100<br>ns, which is the SDK standard.                           |
| Max timecode scale value length | 1 second                                              | The maximum timecode scale value to represent the frame timestamps in<br>the resulting MKV cluster. The value is specified in increments of 100<br>ns, which is the SDK standard.                           |
| Min content view item count     | 10                                                    |                                                                                                                                                                                                             |
| Min buffer duration             | 20 seconds                                            | The value is specified in increments of 100 ns, which is the SDK<br>standard.                                                                                                                               |
| Max update version length       | 128 characters                                        |                                                                                                                                                                                                             |
| Max ARN length                  | 1024 characters                                       |                                                                                                                                                                                                             |
| Max fragment sequence length    | 128 characters                                        |                                                                                                                                                                                                             |
| Max retention period            | 10 years                                              |                                                                                                                                                                                                             |
