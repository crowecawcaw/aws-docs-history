

# Service availability and API metrics
<a name="inference-metrics-global"></a>

## API Latency
<a name="inference-metrics-api-latency"></a>

The duration of API calls from request initiation to response completion. 

****Details****
+ Name: ApiLatency
+ Supported dimension sets: Feed
+ Recommended statistic: p50, p95, p99, Average
+ Units: Milliseconds
+ Meaning of zero: Elemental Inference throttled requests because of request volume was too high. Typically, API requests fail with error code 429.
+ Meaning of no datapoints: There were no API calls on the specified feed.

## API Request Count
<a name="inference-metrics-api-count"></a>

The number of API calls made. 

**Details**
+ Name: ApiRequestCount
+ Supported dimension sets:
  + Feed
  + Feed, StatusCode: to monitor API requests that result in a specific category HTTP response codes.
+ Recommended statistic: Sum
+ Meaning of zero: No API requests were made to the specified feed during the time period.
+ Meaning of no datapoints: There were no API calls on the specified feed.