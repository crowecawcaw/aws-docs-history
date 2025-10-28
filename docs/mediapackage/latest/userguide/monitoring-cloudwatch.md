# Monitoring AWS Elemental MediaPackage with Amazon CloudWatch metrics

You can monitor MediaPackage using CloudWatch, which collects raw data and processes it into readable,
near real-time metrics. These statistics are kept for 15 months, so that you can access
historical information and gain a better perspective on how your web application or service is
performing. You can also set alarms that watch for certain thresholds, and send notifications or
take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

MediaPackage console
MediaPackage displays metrics throughout the console.

###### To view metrics using the MediaPackage console

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/ "https://console.aws.amazon.com/mediapackage/").
2. Navigate to the appropriate page to view metrics:
   - For metrics on all channel groups, go to the **Channel groups**
     page.
   - For metrics on all channels and origin endpoints associated with your channel group in
     the AWS Region, go to the channel group's details page.
   - For metrics on a specific channel and all of its origin endpoints, go to the channel's
     details page.
   - For metrics on a specific origin endpoint, go to the origin endpoint's details
     page.

3. (Optional) To refine the metrics view, choose **Open in CloudWatch**.

CloudWatch consoleMetrics are grouped first by the service namespace, and then by the various dimension
combinations within each namespace.

###### To view metrics using the CloudWatch console

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. Under **All metrics**, choose the **AWS/MediaPackage**
   namespace.
4. Choose the metric dimension to view the metrics (for example, choose `channel`
   to view metrics per channel).

AWS CLI

###### To view metrics using the AWS CLI

At a command prompt, enter the following command:

- ```
  aws cloudwatch list-metrics --namespace "AWS/MediaPackage"
  ```

```



## MediaPackage live content metrics


The `AWS/MediaPackage` namespace includes the following metrics for live
 content. MediaPackage publishes metrics to CloudWatch every minute, if not sooner.




| Metric | Description |
| --- | --- |
| `ChannelMQCS` | Segment-level quality score as calculated by MediaPackage for the active input to this channel.Units: NumericValid statistics: <br>• `Average` – Average bytes (`Sum`/`SampleCount`) that MediaPackage outputs over the configured interval. <br>• `Maximum` – Largest individual output request (in bytes) made to MediaPackage. <br>• `Minimum` – Smallest individual output request (in bytes) made to MediaPackage. <br>• `SampleCount` – Number of requests that's used in the statistical calculation. <br>• `Sum` – Total number of bytes that MediaPackage outputs over the configured interval. Valid dimensions: <br>• `ChannelGroup` <br>• Combination of `ChannelGroup` and `Channel` <br>• Combination of `ChannelGroup`, `Channel`, and `TrackType` <br>• No dimension |
| `ChannelMQCSSequence` | Aggregated quality score for all segments in the sequence for the active input to this channel, as calculated by MediaPackage.Units: NumericValid statistics: <br>• `Average` – Average bytes (`Sum`/`SampleCount`) that MediaPackage outputs over the configured interval. <br>• `Maximum` – Largest individual output request (in bytes) made to MediaPackage. <br>• `Minimum` – Smallest individual output request (in bytes) made to MediaPackage. <br>• `SampleCount` – Number of requests that's used in the statistical calculation. <br>• `Sum` – Total number of bytes that MediaPackage outputs over the configured interval. Valid dimensions: <br>• `ChannelGroup` <br>• Combination of `ChannelGroup` and `Channel` <br>• No dimension |
| `EgressBytes` | Number of bytes that MediaPackage successfully sends for each request. If MediaPackage doesn't receive any requests for output in the specified interval, then no data is given. Units: Bytes Valid statistics: <br>• `Average` – Average bytes (`Sum`/`SampleCount`) that MediaPackage outputs over the configured interval. <br>• `Maximum` – Largest individual output request (in bytes) made to MediaPackage. <br>• `Minimum` – Smallest individual output request (in bytes) made to MediaPackage. <br>• `SampleCount` – Number of requests that's used in the statistical calculation. <br>• `Sum` – Total number of bytes that MediaPackage outputs over the configured interval. Valid dimensions: <br>• `ChannelGroup` <br>• `RequestType` <br>• Combination of `ChannelGroup` and `Channel` <br>• Combination of `ChannelGroup`, `Channel`, and `RequestType` <br>• Combination of `ChannelGroup`, `Channel`, and `OriginEndpoint` <br>• Combination of `ChannelGroup`, `Channel`, `OriginEndpoint`, and `RequestType` <br>• No dimension |
| `EgressRequestCount` | Number of content requests that MediaPackage receives. If MediaPackage doesn't receive any requests for output in the specified interval, then no data is given. Units: Count Valid statistics: <br>• `Sum` – Total number of output requests that MediaPackage receives. Valid dimensions: <br>• `ChannelGroup` <br>• `RequestType` <br>• `StatusCode` <br>• `OuputType` and `StatusCode` <br>• Combination of `ChannelGroup` and `RequestType` <br>• Combination of `ChannelGroup` and `StatusCode` <br>• Combination of `ChannelGroup`, `RequestType`, and `StatusCode` <br>• Combination of `ChannelGroup` and `Channel` <br>• Combination of `ChannelGroup`, `Channel`, and `RequestType` <br>• Combination of `ChannelGroup`, `Channel`, and `OriginEndpoint` <br>• Combination of `ChannelGroup`, `Channel`, and `StatusCode` <br>• Combination of `ChannelGroup`, `Channel`, `OriginEndpoint`, and `RequestType` <br>• Combination of `ChannelGroup`, `Channel`, `RequestType`, and `StatusCode` <br>• Combination of `ChannelGroup`, `Channel`, `OriginEndpoint`, and `StatusCode` <br>• Combination of `ChannelGroup`, `Channel`, `OriginEndpoint`, `RequestType`, and `StatusCode` <br>• No dimension |
| `EgressResponseTime` | The time that it takes MediaPackage to process each output request. If MediaPackage doesn't receive any requests for output in the specified interval, then no data is given. Units: Milliseconds Valid statistics: <br>• `Average` – Average amount of time (`Sum`/`SampleCount`) that it takes MediaPackage to process output requests over the configured interval. <br>• `Maximum` – Longest amount of time (in milliseconds) that it takes MediaPackage to process an output request and provide a response. <br>• `Minimum` – Shortest amount of time (in milliseconds) that it takes MediaPackage to process an output request and provide a response. <br>• `SampleCount` – Number of requests that's used in the statistical calculation. <br>• `Sum` – Total amount of time that it takes MediaPackage to process output requests over the configured interval. Valid dimensions: <br>• `ChannelGroup` <br>• `RequestType` <br>• Combination of `ChannelGroup` and `Channel` <br>• Combination of `ChannelGroup`, `Channel`, and `RequestType` <br>• Combination of `ChannelGroup`, `Channel`, and `OriginEndpoint` <br>• Combination of `ChannelGroup`, `Channel`, `OriginEndpoint`, and `RequestType` <br>• No dimension |
| `IngressBytes` | Number of bytes of content that MediaPackage receives for each input request. If MediaPackage doesn't receive any requests for input in the specified interval, then no data is given. Units: Bytes Valid statistics: <br>• `Average` – Average bytes (`Sum`/`SampleCount`) that MediaPackage receives over the configured interval. <br>• `Maximum` – Largest individual input request (in bytes) made to MediaPackage. <br>• `Minimum` – Smallest individual input request (in bytes) made to MediaPackage. <br>• `SampleCount` – Number of requests that's used in the statistical calculation. <br>• `Sum` – Total number of bytes that MediaPackage receives over the configured interval. Valid dimensions: <br>• `ChannelGroup` <br>• Combination of `ChannelGroup` and `Channel` <br>• Combination of `ChannelGroup`, `Channel`, and `IngestEndpoint` <br>• No dimension |
| `IngressMQCS` | Segment-level quality score as communicated by AWS Elemental MediaLive for this input.Units: NumericValid statistics: <br>• `Average` – Average bytes (`Sum`/`SampleCount`) that MediaPackage outputs over the configured interval. <br>• `Maximum` – Largest individual output request (in bytes) made to MediaPackage. <br>• `Minimum` – Smallest individual output request (in bytes) made to MediaPackage. <br>• `SampleCount` – Number of requests that's used in the statistical calculation. <br>• `Sum` – Total number of bytes that MediaPackage outputs over the configured interval. Valid dimensions: <br>• `ChannelGroup` <br>• Combination of `ChannelGroup` and `Channel` <br>• Combination of `ChannelGroup`, `Channel`, and `IngestEndpoint` <br>• Combination of `ChannelGroup`, `Channel`, `IngestEndpoint`, and `TrackType` <br>• No dimension |
| `IngressMQCSSequence` | Aggregated quality scores for all segments in the sequence, as communicated by AWS Elemental MediaLive.Units: NumericValid statistics: <br>• `Average` – Average bytes (`Sum`/`SampleCount`) that MediaPackage outputs over the configured interval. <br>• `Maximum` – Largest individual output request (in bytes) made to MediaPackage. <br>• `Minimum` – Smallest individual output request (in bytes) made to MediaPackage. <br>• `SampleCount` – Number of requests that's used in the statistical calculation. <br>• `Sum` – Total number of bytes that MediaPackage outputs over the configured interval. Valid dimensions: <br>• `ChannelGroup` <br>• Combination of `ChannelGroup` and `Channel` <br>• Combination of `ChannelGroup`, `Channel`, and `IngestEndpoint` <br>• No dimension |
| `IngressRequestCount` | Number of input requests that MediaPackage receives. If MediaPackage doesn't receive any requests for input in the specified interval, then no data is given. Units: Count Valid statistics: <br>• `Sum` – Total number of input manifest requests that MediaPackage receives. Valid dimensions: <br>• `ChannelGroup` <br>• `StatusCode` <br>• Combination of `ChannelGroup` and `StatusCode` <br>• Combination of `ChannelGroup` and `Channel` <br>• Combination of `ChannelGroup`, `Channel`, and `IngestEndpoint` <br>• Combination of `ChannelGroup`, `Channel`, and `StatusCode` <br>• Combination of `ChannelGroup`, `Channel`, `IngestEndpoint`, and `StatusCode` <br>• No dimension |
| `IngressResponseTime` | The time that it takes MediaPackage to process each input request. If MediaPackage doesn't receive any requests for input in the specified interval, then no data is given. Units: Milliseconds Valid statistics: <br>• `Average` – Average amount of time (`Sum`/`SampleCount`) that it takes MediaPackage to process input requests over the configured interval. <br>• `Maximum` – Longest amount of time (in milliseconds) that it takes MediaPackage to process an input request and provide a response. <br>• `Minimum` – Shortest amount of time (in milliseconds) that it takes MediaPackage to process an input request and provide a response. <br>• `SampleCount` – Number of requests that's used in the statistical calculation. <br>• `Sum` – Total amount of time that it takes MediaPackage to process input requests over the configured interval. Valid dimensions: <br>• `ChannelGroup` <br>• Combination of `ChannelGroup` and `Channel` <br>• Combination of `ChannelGroup`, `Channel`, and `IngestEndpoint` <br>• No dimension | ## MediaPackage live dimensions You can filter the `AWS/MediaPackage` data using the following dimensions.
| Dimension | Description |
| --- | --- |
| No Dimension | Metrics are aggregated and shown for all channels, endpoints, or status codes. |
| `CDNAuthorizationStatus` | Value: `Authorized` or `Unauthorized` Can be used in combination with `ChannelGroup`, `Channel`, `OriginEndpoint`, and `CDNAuthorizationStatusDetails` to show metrics for the CDN authorization requests to the specified endpoint. |
| `CDNAuthorizationStatusDetails` | Value when `CDNAuthorizationStatus` is `Authorized`: `HeaderSecretMatched` Value when `CDNAuthorizationStatus` is `Unauthorized`: `HeaderSecretMismatched`, `MissingCdnAuthHeaderAndConfiguration`, `MissingCdnAuthHeader`, `MissingCdnAuthConfiguration`, `MissingCdnIdentifierSecretArns`, `MissingSecretsRoleArn`, `SecretsManagerInvalidParameterError`, `SecretsManagerInternalServiceError`, `SecretsManagerThrottlingError`, `MediaPackageSecretsValidationError`, or `OtherErrors`. Can be used in combination with `ChannelGroup`, `Channel`, `OriginEndpoint`, and `CDNAuthorizationStatus` to show the CDN authorization request details for the specified endpoint. |
| `Channel` | Metrics are shown only for the specified channel. Value: The auto-generated name of the channel. Can be used alone or with other dimensions: <br>• Alone to show metrics for only the specified channel. <br>• With the `originEndpoint` dimension to show metrics for the specified endpoint that's associated with the specified channel. |
| `ChannelGroup` | Metrics are shown only for the specified channel group. Value: The name of the channel group. Can be used alone or with other dimensions: <br>• Alone to show metrics only for the specified channel group. <br>• With the `channel` dimension to show metrics for the specified channel that's associated with the specified channel group. <br>• With the `statusCode` dimension to show metrics for the specified status code ranges that are associated with the specified channel group. |
| `IngestEndpoint` | Metrics are shown only for the specified ingest endpoint on a channel. Value: The auto-generated GUID of the ingest endpoint. Can be used with the following dimensions: <br>• With the `channel` dimension to show metrics for the specified ingest endpoint that's associated with the specified channel. <br>• With the `originEndpoint` dimension to show metrics for the specified ingest endpoint that's associated with the specified endpoint. |
| `OriginEndpoint` | Metrics are shown for the specified channel and endpoint combination. Value: The auto-generated name of the endpoint. Must be used with the `channel` dimension.  |
| `RequestType` | Metrics are shown only for the specified request type. Value: Either `manifest` or `segment`, signifying the type of content being filtered in the metric. Can be used alone or with other dimensions: <br>• Alone to show metrics only for the specified request type. <br>• With the `statusCode` dimension to show metrics for the specified request type that's associated with the specified status code range. <br>• With the `originEndpoint` dimension to show metrics for the specified request type that's associated with the specified origin endpoint. |
| `StatusCode` | Metrics are shown for the specified status code range. Value: `2xx`, `3xx`, `4xx`, or `5xx`. Can be used alone or with other dimensions: <br>• Alone to show all output requests for the specified status range. <br>• With the `channel` dimension to show output requests for all endpoints that are associated with the specified channel, with the specified status code range. <br>• With the `channel` and `originEndpoint` dimensions to show output requests with a specific status code range on the specified endpoint that's associated with the specified channel. |
| `TrackType` | Metrics are shown for the specified track type. Value: `Video`, `Audio`, or `Subtitle`. Can be used alone or with other dimensions: <br>• Alone to show quality scores for the specified track type. <br>• With the `channel` dimension to show quality scores for all track types that are associated with the specified channel, with the specified track type. <br>• With the `channel` and `IngestEndpoint` dimensions to show quality scores with a specific track type on the specified ingest endpoint that's associated with the specified channel. |
```
