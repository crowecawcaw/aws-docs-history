# Troubleshooting MSS endpoints in AWS Elemental MediaPackage

This topic helps you identify and resolve common issues with Microsoft Smooth Streaming
(MSS) endpoints in AWS Elemental MediaPackage.

## Resolving common MSS playback issues

If you encounter issues with your MSS endpoints, consider the following common
problems and solutions:

404 errors when requesting segments

This could be due to the LookaheadCount setting. MSS holds back segments
at the live edge until 2 future segments are available (this value is fixed
and not configurable).

**Solution:** Ensure your player is
requesting segments within the available window, accounting for the fixed
2-segment lookahead buffer.

Playback issues on legacy devices

Some older devices may have limitations with certain MSS features.

**Solution:** Try using the
**Full** manifest layout instead of
**Compact**, as it's more widely supported by legacy
players.

DRM issues

MSS only supports PlayReady DRM.

**Solution:** Ensure your SPEKE key provider
is correctly configured to provide PlayReady keys. For more information, see
[Content encryption and DRM in AWS Elemental MediaPackage](using-encryption.md "using-encryption.md").

Manifest not loading

The MSS manifest may not load if the endpoint is not properly
configured.

**Solution:** Verify that you've selected the
ISM container type when creating your endpoint. MSS manifests require the
ISM container type.

Playback stuttering or buffering

This could be due to network issues or segment availability.

**Solution:** Check your network connection
and ensure your CDN is properly configured for MSS content. Also, verify
that your segment duration is appropriate for your content and network
conditions.

For a better understanding of MSS manifest structure to help diagnose issues, see
[MSS manifest structure in AWS Elemental MediaPackage](mss-manifest-structure.md "mss-manifest-structure.md").

## Monitoring MSS streams

Effective monitoring of your MSS streams helps you ensure reliable delivery and quickly identify issues before they impact your viewers. This section provides detailed guidance on setting up comprehensive monitoring for MSS endpoints.

### Key metrics to monitor

When monitoring MSS streams, pay attention to these key metrics:

Request count

Track the number of requests for manifests and segments to understand your audience size and viewing patterns.

**Normal pattern**: MSS clients typically request manifests less frequently than HLS clients, with a ratio of approximately 1 manifest request to 10-20 segment requests.

**Warning signs**: Sudden drops in request count may indicate playback issues or CDN problems.

HTTP response codes

Monitor the distribution of HTTP status codes to identify potential issues.

**Normal pattern**: Primarily 200 OK
responses, with some
412
errors near the live edge due to the lookahead buffer (these are
expected).

**Warning signs**: High rates of 5xx errors, unexpected 403 errors, or 404 errors for established content.

Latency

Track the time it takes to serve manifest and segment requests.

**Normal pattern**: Manifest requests typically have higher latency than segment requests due to dynamic generation.

**Warning signs**: Increasing latency trends or spikes above 500ms for segment delivery.

Egress bytes

Monitor the volume of data being delivered to understand bandwidth usage and costs.

**Normal pattern**: Consistent patterns that align with your audience's viewing habits.

**Warning signs**: Unexpected spikes or drops that don't correlate with audience size changes.

### Setting up a CloudWatch dashboard for MSS

Create a dedicated Amazon CloudWatch dashboard to monitor your MSS endpoints with these recommended widgets:

1. **Request metrics**:

```

{
  "metrics": [
    [ "AWS/MediaPackage", "EgressRequestCount", "Channel", "YourChannelName", "Origin", "YourOriginEndpointName", { "stat": "Sum", "period": 60 } ]
  ],
  "view": "timeSeries",
  "stacked": false,
  "region": "us-west-2",
  "title": "MSS Endpoint Requests",
  "period": 300
}

```

2. **HTTP status code distribution**:

```

{
  "metrics": [
    [ "AWS/MediaPackage", "EgressRequestCount", "Channel", "YourChannelName", "Origin", "YourOriginEndpointName", "StatusCodeRange", "4xx", { "stat": "Sum", "period": 60 } ],
    [ "AWS/MediaPackage", "EgressRequestCount", "Channel", "YourChannelName", "Origin", "YourOriginEndpointName", "StatusCodeRange", "5xx", { "stat": "Sum", "period": 60 } ],
    [ "AWS/MediaPackage", "EgressRequestCount", "Channel", "YourChannelName", "Origin", "YourOriginEndpointName", { "stat": "Sum", "period": 60 } ]
  ],
  "view": "timeSeries",
  "stacked": true,
  "region": "us-west-2",
  "title": "MSS HTTP Status Codes",
  "period": 300
}

```

3. **Latency tracking**:

```

{
  "metrics": [
    [ "AWS/MediaPackage", "EgressResponseTime", "Channel", "YourChannelName", "Origin", "YourOriginEndpointName", { "stat": "Average", "period": 60 } ],
    [ "AWS/MediaPackage", "EgressResponseTime", "Channel", "YourChannelName", "Origin", "YourOriginEndpointName", { "stat": "p90", "period": 60 } ],
    [ "AWS/MediaPackage", "EgressResponseTime", "Channel", "YourChannelName", "Origin", "YourOriginEndpointName", { "stat": "p99", "period": 60 } ]
  ],
  "view": "timeSeries",
  "stacked": false,
  "region": "us-west-2",
  "title": "MSS Endpoint Latency",
  "period": 300
}

```

4. **Egress tracking**:

```

{
  "metrics": [
    [ "AWS/MediaPackage", "EgressBytes", "Channel", "YourChannelName", "Origin", "YourOriginEndpointName", { "stat": "Sum", "period": 60 } ]
  ],
  "view": "timeSeries",
  "stacked": false,
  "region": "us-west-2",
  "title": "MSS Egress Bytes",
  "period": 300
}

```

Replace `YourChannelName` and `YourOriginEndpointName` with your actual channel and endpoint names, and adjust the region as needed.

### Recommended CloudWatch alarms

Set up these Amazon CloudWatch alarms to proactively detect issues with your MSS streams:

High error rate alarm

Triggers when the percentage of 4xx or 5xx errors exceeds a threshold.

```

aws cloudwatch put-metric-alarm \
  --alarm-name MSS_HighErrorRate \
  --alarm-description "Alarm when MSS endpoint error rate exceeds 5%" \
  --metrics '[
    {
      "Id": "e1",
      "Expression": "(m2+m3)/m1*100",
      "Label": "Error Rate"
    },
    {
      "Id": "m1",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/MediaPackage",
          "MetricName": "EgressRequestCount",
          "Dimensions": [
            { "Name": "Channel", "Value": "YourChannelName" },
            { "Name": "Origin", "Value": "YourOriginEndpointName" }
          ]
        },
        "Period": 300,
        "Stat": "Sum"
      },
      "ReturnData": false
    },
    {
      "Id": "m2",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/MediaPackage",
          "MetricName": "EgressRequestCount",
          "Dimensions": [
            { "Name": "Channel", "Value": "YourChannelName" },
            { "Name": "Origin", "Value": "YourOriginEndpointName" },
            { "Name": "StatusCodeRange", "Value": "4xx" }
          ]
        },
        "Period": 300,
        "Stat": "Sum"
      },
      "ReturnData": false
    },
    {
      "Id": "m3",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/MediaPackage",
          "MetricName": "EgressRequestCount",
          "Dimensions": [
            { "Name": "Channel", "Value": "YourChannelName" },
            { "Name": "Origin", "Value": "YourOriginEndpointName" },
            { "Name": "StatusCodeRange", "Value": "5xx" }
          ]
        },
        "Period": 300,
        "Stat": "Sum"
      },
      "ReturnData": false
    }
  ]' \
  --threshold 5 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2 \
  --alarm-actions [your-sns-topic-arn]

```

Latency spike alarm

Triggers when the average latency exceeds a threshold.

```

aws cloudwatch put-metric-alarm \
  --alarm-name MSS_HighLatency \
  --alarm-description "Alarm when MSS endpoint latency exceeds 500ms" \
  --metric-name EgressResponseTime \
  --namespace AWS/MediaPackage \
  --statistic Average \
  --period 300 \
  --threshold 500 \
  --comparison-operator GreaterThanThreshold \
  --dimensions Name=Channel,Value=YourChannelName Name=Origin,Value=YourOriginEndpointName \
  --evaluation-periods 3 \
  --alarm-actions [your-sns-topic-arn]

```

Request drop alarm

Triggers when request count drops significantly, which could indicate delivery issues.

```

aws cloudwatch put-metric-alarm \
  --alarm-name MSS_RequestDrop \
  --alarm-description "Alarm when MSS requests drop by more than 50%" \
  --metric-name EgressRequestCount \
  --namespace AWS/MediaPackage \
  --statistic Sum \
  --period 300 \
  --threshold 0 \
  --comparison-operator LessThanThreshold \
  --dimensions Name=Channel,Value=YourChannelName Name=Origin,Value=YourOriginEndpointName \
  --evaluation-periods 2 \
  --alarm-actions [your-sns-topic-arn] \
  --treat-missing-data breaching

```

### Interpreting monitoring data

Understanding common patterns in your monitoring data can help you quickly identify and resolve issues:

Pattern: Spike in 404 errors

**Possible causes**:

- Segment duration too short relative to the fixed 2-fragment
  lookahead buffer
- Input stream interruption causing gaps in available
  segments
- CDN cache configuration issues

**Recommended action**: Check input
stream health, ensure segment duration works well with the fixed
2-fragment lookahead buffer, and review CDN cache settings.

Pattern: Increasing latency trend

**Possible causes**:

- Growing audience size exceeding capacity
- CDN origin shield not properly configured
- Network congestion between CDN and origin

**Recommended action**: Review your CDN configuration, consider implementing or optimizing origin shield settings, and check for network bottlenecks.

Pattern: Cyclical spikes in request count

**Possible causes**:

- Normal audience behavior patterns (e.g., primetime viewing)
- CDN cache expiration causing request floods

**Recommended action**: If these align with expected audience patterns, this is normal. If not, review your CDN TTL settings to ensure they're appropriate for your content type.

For comprehensive information about MediaPackage monitoring capabilities, see [Logging and monitoring in MediaPackage](monitoring.md "monitoring.md").

## Common MSS error codes

Understanding the specific HTTP error codes returned by MSS endpoints helps you diagnose and resolve issues more effectively:

404 Not Found

Occurs when the player requests a segment that cannot be found. This typically happens when the requested segment is not available or the URL is incorrect.

**Common causes**:

- Player requesting segments beyond the available window
- LookaheadCount settings causing segments to be held back
- Input stream interruptions creating gaps in available content

412 Precondition Failed

Occurs when lookahead fragments are not available for the requested segment. This indicates that MediaPackage does not have the lookahead fragments internally available.

**Common causes**:

- Player requesting segments too close to the live edge
- Input stream issues preventing lookahead fragments from being
  generated
- Network delays affecting fragment availability

403 Forbidden

Occurs when access to the requested resource is denied.

**Common causes**:

- CDN authentication or authorization issues
- Incorrect endpoint permissions or access policies
- Geographic restrictions or IP blocking

5xx Server Errors

Indicates server-side issues with the MSS endpoint or underlying infrastructure.

**Common causes**:

- Service capacity issues or overload
- Backend service failures or timeouts
- Configuration errors in the endpoint setup

## Using diagnostic tools to identify MSS

issues

The following tools can help you troubleshoot MSS streaming issues:

- Browser developer tools to inspect network requests and responses
- Dash.js or Bitmovin player to verify playback and DRM functionality
- Amazon CloudWatch to monitor endpoint metrics and logs

If you continue to experience issues with your MSS endpoints after trying these solutions,
contact AWS Support for assistance.
