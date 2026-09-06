

# Monitor Amazon Kinesis Video Streams metrics with CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor a Kinesis video stream using Amazon CloudWatch, which collects and processes raw data from Amazon Kinesis Video Streams into readable, near real-time metrics. These statistics are recorded for a period of 15 months so that you can access historical information and gain a better perspective on how your web application or service is performing. 

In the [Amazon Kinesis Video Streams console](https://console.aws.amazon.com/kinesisvideo/home/), you can view CloudWatch metrics for a Amazon Kinesis video stream in two ways: 
+ In the **Dashboard** page, choose the **Video streams** tab in the **Account-level metrics for Current Region** section.
+ Choose the **Monitoring** tab in the video stream's details page.

Amazon Kinesis Video Streams provides the following metrics:


| Metric | Description | 
| --- | --- | 
| ArchivedFragmentsConsumed.Media | The number of fragment media quota points that were consumed by all of the APIs. For an explanation of the concept of quota points, see [Fragment-metadata and fragment-media quotas](limits.md#fragment_based_throttling).Units: Count | 
| ArchivedFragmentsConsumed.Metadata | The number of fragments metadata quota points that were consumed by all of the APIs. For an explanation of the concept of quota points, see [Fragment-metadata and fragment-media quotas](limits.md#fragment_based_throttling).Units: Count | 
| `PutMedia.Requests` | The number of `PutMedia` API requests for a given stream.<br />Units: Count | 
| `PutMedia.IncomingBytes` | The number of bytes received as part of `PutMedia` for the stream.<br />Units: Bytes | 
| `PutMedia.IncomingFragments` | The number of complete fragments received as part of `PutMedia` for the stream.<br />Units: Count | 
| `PutMedia.IncomingFrames` | The number of complete frames received as part of `PutMedia` for the stream.<br />Units: Count | 
| `PutMedia.ActiveConnections` | The total number of connections to the service host.<br />Units: Count | 
| `PutMedia.ConnectionErrors` | The errors while establishing `PutMedia` connection for the stream.<br />Units: Count | 
| `PutMedia.FragmentIngestionLatency` | The time difference between when the first and last bytes of a fragment are received by Amazon Kinesis Video Streams.<br />Units: Milliseconds | 
| `PutMedia.FragmentPersistLatency` | The time taken from when the complete fragment data is received and archived.<br />Units: Count | 
| `PutMedia.Latency` | The time difference between the request and the HTTP response from InletService while establishing the connection.<br />Units: Count | 
| `PutMedia.BufferingAckLatency` | The time difference between when the first byte of a new fragment is received by Amazon Kinesis Video Streams and when the Buffering ACK is sent for the fragment.<br />Units: Milliseconds | 
| `PutMedia.ReceivedAckLatency` | The time difference between when the last byte of a new fragment is received by Amazon Kinesis Video Streams and when the Received ACK is sent for the fragment.<br />Units: Milliseconds | 
| `PutMedia.PersistedAckLatency` | The time difference between when the last byte of a new fragment is received by Amazon Kinesis Video Streams and when the Persisted ACK is sent for the fragment.<br />Units: Milliseconds | 
| `PutMedia.ErrorAckCount` | The number of Error ACKs sent while doing `PutMedia` for the stream.<br />Units: Count | 
| `PutMedia.Success` | 1 for each fragment successfully written; 0 for every failed fragment. The average value of this metric indicates how many complete, valid fragments are sent.<br />Units: Count | 
| `GetMedia.Requests` | The number of `GetMedia` API requests for a given stream.<br />Units: Count | 
| `GetMedia.OutgoingBytes` | The total number of bytes sent out from the service as part of the `GetMedia` API for a given stream.<br />Units: Bytes | 
| `GetMedia.OutgoingFragments` | The number of fragments sent while doing `GetMedia` for the stream.<br />Units: Count | 
| `GetMedia.OutgoingFrames` | The number of frames sent during `GetMedia` on the given stream.<br />Units: Count | 
| `GetMedia.MillisBehindNow` | The time difference between the current server timestamp and the server timestamp of the last fragment sent.<br />Units: Milliseconds | 
| `GetMedia.ConnectionErrors` | The number of connections that were not successfully established.<br />Units: Count | 
| `GetMedia.Success` | 1 for every fragment successfully sent; 0 for every failure. The average value indicates the rate of success. Failures include both 400 (user) errors and 500 (system) errors. For more information about enabling a summary of requests and responses, including AWS request IDs, see [Request/Response Summary Logging](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html#sdk-net-logging-request-response). <br />Units: Count | 
| `GetMediaForFragmentList.OutgoingBytes` | The total number of bytes sent out from the service as part of the `GetMediaForFragmentList` API for a given stream.<br />Units: Bytes | 
| `GetMediaForFragmentList.OutgoingFragments` | The total number of fragments sent out from the service as part of the `GetMediaForFragmentList` API for a given stream.<br />Units: Count | 
| `GetMediaForFragmentList.OutgoingFrames` | The total number of frames sent out from the service as part of the `GetMediaForFragmentList` API for a given stream.<br />Units: Count | 
| `GetMediaForFragmentList.Requests` | The number of `GetMediaForFragmentList` API requests for a given stream.<br />Units: Count | 
| `GetMediaForFragmentList.Success` | 1 for every fragment successfully sent; 0 for every failure. The average value indicates the rate of success. Failures include both 400 (user) errors and 500 (system) errors. For more information about enabling a summary of requests and responses, including AWS request IDs, see [Request/Response Summary Logging](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html#sdk-net-logging-request-response). <br />Units: Count | 
| `ListFragments.Latency` | The latency of the `ListFragments` API calls for the given stream name.<br />Units: Milliseconds | 
| `ListFragments.Requests` | The number of `ListFragments` API requests for a given stream.<br />Units: Count | 
| `ListFragments.Success` | 1 for every successful request; 0 for every failure. The average value indicates the rate of success. Failures include both 400 (user) errors and 500 (system) errors. For more information about enabling a summary of requests and responses, including AWS request IDs, see [Request/Response Summary Logging](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html#sdk-net-logging-request-response). <br />Units: Count | 
| `GetHLSStreamingSessionURL.Latency` | The latency of the `GetHLSStreamingSessionURL` API calls for the given stream name.<br />Units: Milliseconds | 
| `GetHLSStreamingSessionURL.Requests` | The number of `GetHLSStreamingSessionURL` API requests for a given stream.<br />Units: Count | 
| `GetHLSStreamingSessionURL.Success` | 1 for every successful request; 0 for every failure. The average value indicates the rate of success. Failures include both 400 (user) errors and 500 (system) errors. For more information about enabling a summary of requests and responses, including AWS request IDs, see [Request/Response Summary Logging](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html#sdk-net-logging-request-response). <br />Units: Count | 
| `GetHLSMasterPlaylist.Latency` | The latency of the `GetHLSMasterPlaylist` API calls for the given stream name.<br />Units: Milliseconds | 
| `GetHLSMasterPlaylist.Requests` | The number of `GetHLSMasterPlaylist` API requests for a given stream.<br />Units: Count | 
| `GetHLSMasterPlaylist.Success` | 1 for every successful request; 0 for every failure. The average value indicates the rate of success. Failures include both 400 (user) errors and 500 (system) errors. For more information about enabling a summary of requests and responses, including AWS request IDs, see [Request/Response Summary Logging](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html#sdk-net-logging-request-response). <br />Units: Count | 
| `GetHLSMediaPlaylist.Latency` | The latency of the `GetHLSMediaPlaylist` API calls for the given stream name.<br />Units: Milliseconds | 
| `GetHLSMediaPlaylist.Requests` | The number of `GetHLSMediaPlaylist` API requests for a given stream.<br />Units: Count | 
| `GetHLSMediaPlaylist.Success` | 1 for every successful request; 0 for every failure. The average value indicates the rate of success. Failures include both 400 (user) errors and 500 (system) errors. For more information about enabling a summary of requests and responses, including AWS request IDs, see [Request/Response Summary Logging](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html#sdk-net-logging-request-response). <br />Units: Count | 
| `GetMP4InitFragment.Latency` | The latency of the `GetMP4InitFragment` API calls for the given stream name.<br />Units: Milliseconds | 
| `GetMP4InitFragment.Requests` | The number of `GetMP4InitFragment` API requests for a given stream.<br />Units: Count | 
| `GetMP4InitFragment.Success` | 1 for every successful request; 0 for every failure. The average value indicates the rate of success. Failures include both 400 (user) errors and 500 (system) errors. For more information about enabling a summary of requests and responses, including AWS request IDs, see [Request/Response Summary Logging](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html#sdk-net-logging-request-response). <br />Units: Count | 
| `GetMP4MediaFragment.Latency` | The latency of the `GetMP4MediaFragment` API calls for the given stream name.<br />Units: Milliseconds | 
| `GetMP4MediaFragment.Requests` | The number of `GetMP4MediaFragment` API requests for a given stream.<br />Units: Count | 
| `GetMP4MediaFragment.Success` | 1 for every successful request; 0 for every failure. The average value indicates the rate of success. Failures include both 400 (user) errors and 500 (system) errors. For more information about enabling a summary of requests and responses, including AWS request IDs, see [Request/Response Summary Logging](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html#sdk-net-logging-request-response). <br />Units: Count | 
| `GetMP4MediaFragment.OutgoingBytes` | The total number of bytes sent out from the service as part of the `GetMP4MediaFragment` API for a given stream.<br />Units: Bytes | 
| `GetTSFragment.Latency` | The latency of the `GetTSFragment` API calls for the given stream name.<br />Units: Milliseconds | 
| `GetTSFragment.Requests` | The number of `GetTSFragment` API requests for a given stream.<br />Units: Count | 
| `GetTSFragment.Success` | 1 for every successful request; 0 for every failure. The average value indicates the rate of success. Failures include both 400 (user) errors and 500 (system) errors. For more information about enabling a summary of requests and responses, including AWS request IDs, see [Request/Response Summary Logging](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html#sdk-net-logging-request-response). <br />Units: Count | 
| `GetTSFragment.OutgoingBytes` | The total number of bytes sent out from the service as part of the `GetTSFragment` API for a given stream.<br />Units: Bytes | 
| `GetDASHStreamingSessionURL.Latency` | The latency of the `GetDASHStreamingSessionURL` API calls for the given stream name.<br />Units: Milliseconds | 
| `GetDASHStreamingSessionURL.Requests` | The number of `GetDASHStreamingSessionURL` API requests for a given stream.<br />Units: Count | 
| `GetDASHStreamingSessionURL.Success` | 1 for every successful request; 0 for every failure. The average value indicates the rate of success. Failures include both 400 (user) errors and 500 (system) errors. For more information about enabling a summary of requests and responses, including AWS request IDs, see [Request/Response Summary Logging](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html#sdk-net-logging-request-response). <br />Units: Count | 
| `GetDASHManifest.Latency` | The latency of the `GetDASHManifest` API calls for the given stream name.<br />Units: Milliseconds | 
| `GetDASHManifest.Requests` | The number of `GetDASHManifest` API requests for a given stream.<br />Units: Count | 
| `GetDASHManifest.Success` | 1 for every successful request; 0 for every failure. The average value indicates the rate of success. Failures include both 400 (user) errors and 500 (system) errors. For more information about enabling a summary of requests and responses, including AWS request IDs, see [Request/Response Summary Logging](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html#sdk-net-logging-request-response). <br />Units: Count | 
| `GetClip.Latency` | The latency of the GetClip API calls for the given video stream name. <br />Units: Milliseconds | 
| `GetClip.Requests` | The number of GetClip API requests for a given video stream. <br />Units: Count | 
| `GetClip.Success` | 1 for every successful request; 0 for every failure. The average value indicates the rate of success.  Failures include both 400 (user) errors and 500 (system) errors. For more information about enabling a summary of requests and responses, including AWS request IDs, see [Request/Response Summary Logging](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html#sdk-net-logging-request-response). <br />Units: Count | 
| `GetClip.OutgoingBytes` | The total number of bytes sent out from the service as part of the GetClip API for a given video stream. <br />Units: Bytes | 

## CloudWatch metrics guidance
<a name="monitoring-cloudwatch-guidance"></a>

CloudWatch metrics can help find answers to the following questions: 

**Topics**
+ [Is data reaching the Amazon Kinesis Video Streams service?](#monitoring-cloudwatch-guidance-incoming)
+ [Why is data not being successfully ingested by the Amazon Kinesis Video Streams service?](#monitoring-cloudwatch-guidance-errors)
+ [Why can't the data be read from the Amazon Kinesis Video Streams service at the same rate as it's being sent from the producer?](#monitoring-cloudwatch-guidance-rate)
+ [Why is there no video in the console, or why is the video being played with a delay?](#monitoring-cloudwatch-guidance-novideo)
+ [What is the delay in reading real-time data, and why is the client lagging behind the head of the stream?](#monitoring-cloudwatch-guidance-delay)
+ [Is the client reading data out of the Kinesis video stream, and at what rate?](#monitoring-cloudwatch-guidance-isread)
+ [Why can't the client read data out of the Kinesis video stream?](#monitoring-cloudwatch-guidance-noread)

### Is data reaching the Amazon Kinesis Video Streams service?
<a name="monitoring-cloudwatch-guidance-incoming"></a>

**Relevant metrics:** 
+ `PutMedia.IncomingBytes`
+ `PutMedia.IncomingFragments`
+ `PutMedia.IncomingFrames`

**Action items:**
+ If there's a drop in these metrics, check if your application is still sending data to the service.
+ Check the network bandwidth. If your network bandwidth is insufficient, it could be slowing down the rate the service is receiving the data.

### Why is data not being successfully ingested by the Amazon Kinesis Video Streams service?
<a name="monitoring-cloudwatch-guidance-errors"></a>

**Relevant metrics:** 
+ `PutMedia.Requests`
+ `PutMedia.ConnectionErrors`
+ `PutMedia.Success`
+ `PutMedia.ErrorAckCount`

**Action items:**
+ If there's an increase in `PutMedia.ConnectionErrors`, look at the HTTP response and error codes received by the producer client to see what errors are occurring while establishing the connection.
+ If there's a drop in `PutMedia.Success` or increase in `PutMedia.ErrorAckCount`, look at the ack error code in the ack responses sent by the service to see why ingestion of data is failing. For more information, see [AckErrorCode.Values](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/kinesisvideo/model/AckErrorCode.Values.html).

### Why can't the data be read from the Amazon Kinesis Video Streams service at the same rate as it's being sent from the producer?
<a name="monitoring-cloudwatch-guidance-rate"></a>

**Relevant metrics:** 
+ `PutMedia.FragmentIngestionLatency`
+ `PutMedia.IncomingBytes`

**Action items:**
+ If there's a drop in these metrics, check the network bandwidth of your connections. Low-bandwidth connections could cause the data to reach the service at a lower rate. 

### Why is there no video in the console, or why is the video being played with a delay?
<a name="monitoring-cloudwatch-guidance-novideo"></a>

**Relevant metrics:** 
+ `PutMedia.FragmentIngestionLatency`
+ `PutMedia.FragmentPersistLatency`
+ `PutMedia.Success`
+ `ListFragments.Latency`
+ `PutMedia.IncomingFragments`

**Action items:**
+ If there's an increase in `PutMedia.FragmentIngestionLatency` or a drop in `PutMedia.IncomingFragments`, check the network bandwidth and whether the data is still being sent.
+ If there's a drop in `PutMedia.Success`, check the ack error codes. For more information, see [AckErrorCode.Values](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/kinesisvideo/model/AckErrorCode.Values.html).
+ If there's an increase in `PutMedia.FragmentPersistLatency` or `ListFragments.Latency`, you're most likely experiencing a service issue. If the condition persists for an extended period of time, check with your customer service contact to see if there's an issue with your service.

### What is the delay in reading real-time data, and why is the client lagging behind the head of the stream?
<a name="monitoring-cloudwatch-guidance-delay"></a>

**Relevant metrics:** 
+ `GetMedia.MillisBehindNow`
+ `GetMedia.ConnectionErrors`
+ `GetMedia.Success`

**Action items:**
+ If there's an increase in `GetMedia.ConnectionErrors`, then the consumer might be falling behind in reading the stream, due to frequent attempts to re-connect to the stream. Look at the HTTP response/error codes returned for the `GetMedia` request.
+ If there's a drop in `GetMedia.Success`, it’s likely due to the service being unable to send the data to the consumer, which would result in dropped connection, and reconnects from consumers, which would result in the consumer lagging behind the head of the stream.
+ If there's an increase in `GetMedia.MillisBehindNow`, look at your bandwidth limits to see if you're receiving the data at a slower rate because of lower bandwidth.

### Is the client reading data out of the Kinesis video stream, and at what rate?
<a name="monitoring-cloudwatch-guidance-isread"></a>

**Relevant metrics:** 
+ `GetMedia.OutgoingBytes`
+ `GetMedia.OutgoingFragments`
+ `GetMedia.OutgoingFrames`
+ `GetMediaForFragmentList.OutgoingBytes`
+ `GetMediaForFragmentList.OutgoingFragments`
+ `GetMediaForFragmentList.OutgoingFrames`

**Action items:**
+ These metrics indicate the rate at which real-time and archived data is being read.

### Why can't the client read data out of the Kinesis video stream?
<a name="monitoring-cloudwatch-guidance-noread"></a>

**Relevant metrics:** 
+ `GetMedia.ConnectionErrors`
+ `GetMedia.Success`
+ `GetMediaForFragmentList.Success`
+ `PutMedia.IncomingBytes`

**Action items:**
+ If there's an increase in `GetMedia.ConnectionErrors`, look at the HTTP response and error codes returned by the `GetMedia` request. For more information, see [AckErrorCode.Values](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/kinesisvideo/model/AckErrorCode.Values.html).
+ If you're trying to read the latest or live data, check `PutMedia.IncomingBytes` to see if there's data coming into the stream for the service to send to the consumers.
+ If there's a drop in `GetMedia.Success` or `GetMediaForFragmentList.Success`, it’s likely due to the service being unable to send the data to the consumer. If the condition persists for an extended period of time, check with your customer service contact to see if there's an issue with your service.