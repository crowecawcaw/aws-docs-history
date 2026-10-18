

# Caching HTTP responses
<a name="monetization-functions-caching"></a>

By default, every time an `HTTP_REQUEST`, `AWS_SERVICE_REQUEST`, or `VAST_REQUEST` function runs, MediaTailor sends a request to the function's endpoint. When many viewers request the same data, such as content metadata for the ad break that they're all watching, this can multiply the request rate to your endpoint by the number of concurrent sessions.

With response caching, MediaTailor stores the endpoint's response and reuses it for later requests that resolve to the same cache key. A cached response is shared across all sessions of the same playback configuration. Response caching has the following benefits:
+ **Lower request rate to your endpoint.** MediaTailor calls your endpoint only when no cached response is available. You might not need a content delivery network (CDN) in front of your endpoint.
+ **Lower function latency.** A cached response doesn't wait for a network round trip, which leaves more of the hook's time budget for other functions.

Caching is off by default. You turn it on for each function by adding a `Cache` object to the function's configuration. Your `Output` expressions run the same way for cached and uncached responses.

## When to use response caching
<a name="monetization-functions-caching-when"></a>

Use response caching when many requests return the same response for a period of time. Common use cases include the following:
+ Content metadata that is the same for every viewer of a channel at a given point in time, such as Elemental Inference contextual metadata for the current ad break.
+ Lookups that depend on a small set of values, such as audience segments by device type or Region.
+ Configuration or feature-flag data that changes infrequently.
+ House ads or promos fetched with `VAST_REQUEST` from an endpoint that returns the same ads to every viewer.

Don't cache responses that must be unique for each viewer or each request, such as requests with side effects (for example, logging or impression reporting) or per-viewer data that your cache key doesn't distinguish. For details about what makes two requests share a cached response, see [How cache keys work](#monetization-functions-caching-keys).

## Configuration fields
<a name="monetization-functions-caching-fields"></a>

Add the optional `Cache` object to an `HttpRequestConfiguration`, `AwsServiceRequestConfiguration`, or `VastRequestConfiguration`. The `Cache` object has the following fields:
+ **TtlMinimumSeconds** (required) — The lower bound, in seconds, on how long MediaTailor caches a response. MediaTailor also uses this value as the cache duration when a response has no `Cache-Control` `max-age` directive. Valid range: `1`–`300`.
+ **TtlMaximumSeconds** (required) — The upper bound, in seconds, on how long MediaTailor caches a response. This value must be greater than or equal to `TtlMinimumSeconds`. Valid range: `1`–`300`.
+ **Key** (optional) — A JSONata expression, wrapped in `{%...%}`, that produces a custom cache key. When you set a key, it replaces the default cache key. For details, see [Custom cache key](#monetization-functions-caching-keys-custom).

The following example shows the `Cache` object in an `HTTP_REQUEST` function:

```
"HttpRequestConfiguration": {
    ...
    "Cache": {
        "TtlMinimumSeconds": 5,
        "TtlMaximumSeconds": 60
    }
}
```

To turn off caching, remove the `Cache` object from the function's configuration.

## Turning on caching in the console
<a name="monetization-functions-caching-console"></a>

When you create or edit an `HTTP_REQUEST`, `AWS_SERVICE_REQUEST`, or `VAST_REQUEST` function in the MediaTailor console, use the **Response caching** section:

1. Turn on **Enable response caching**. The console fills in default values for the minimum and maximum time to live (TTL).

1. For **Minimum TTL (seconds)** and **Maximum TTL (seconds)**, enter the bounds for how long MediaTailor caches a response.

1. (Optional) For **Cache key**, enter a JSONata expression for a custom cache key.

For more information about creating a function, see [Creating and managing](monetization-functions-managing.md).

## How MediaTailor determines how long to cache a response
<a name="monetization-functions-caching-ttl"></a>

MediaTailor uses your endpoint's `Cache-Control` header together with your TTL bounds to decide how long to keep a response:
+ If the response includes a `Cache-Control` `max-age` directive, MediaTailor uses that value, reduced by the response's `Age` header if present. MediaTailor then clamps the result to the range from `TtlMinimumSeconds` to `TtlMaximumSeconds`.
+ If the response has no `max-age` directive, or the directive is `max-age=0`, MediaTailor caches the response for `TtlMinimumSeconds`.

The following table shows the resulting TTL for a function with `TtlMinimumSeconds` set to `5` and `TtlMaximumSeconds` set to `60`.


| Endpoint response header | Cache TTL | 
| --- | --- | 
| No Cache-Control header | 5 seconds | 
| Cache-Control: max-age=2 | 5 seconds | 
| Cache-Control: max-age=30 | 30 seconds | 
| Cache-Control: max-age=3600 | 60 seconds | 

**Tip**  
To let your endpoint control freshness, set a narrow `TtlMinimumSeconds` and a wider `TtlMaximumSeconds`, and return a `Cache-Control` `max-age` directive from your endpoint. To cache for a fixed duration regardless of response headers, set both values to the same number.

MediaTailor might remove a cached response before its TTL expires. You can't invalidate cached responses directly. A response stays in the cache for at most `TtlMaximumSeconds`, so choose a maximum TTL that you can tolerate as the delay before an endpoint change reaches viewers.

## Which responses are cached
<a name="monetization-functions-caching-status"></a>

MediaTailor caches successful responses with status codes `200`, `203`, and `204`. MediaTailor also caches the following error responses, which HTTP defines as cacheable by default: `404`, `405`, `410`, `414`, and `501`.

MediaTailor doesn't cache the following:
+ Network failures and timeouts.
+ Server errors with status codes `500`, `502`, and `504`.
+ Partial content responses with status code `206`.

## How cache keys work
<a name="monetization-functions-caching-keys"></a>

The cache key determines which requests share a cached response. Requests that produce the same cache key share a response. Cache keys are always scoped to the playback configuration that runs the function, so two playback configurations never share cached responses, even when they use the same function.

### Default cache key
<a name="monetization-functions-caching-keys-default"></a>

If you don't set `Key`, MediaTailor builds the cache key from the following values:
+ The HTTP method
+ The evaluated URL
+ The evaluated request body (for `POST` requests only)

MediaTailor evaluates the URL and body expressions before it builds the key. As a result, sessions that produce the same URL and body share a cached response. If your URL or body includes a per-session value, such as `session.id`, each session gets its own cache entry and caching has little effect.

**Important**  
Request headers aren't part of the default cache key. To cache responses separately by header value, set a custom `Key`. For an example, see [Example: Include a request header in the cache key](#monetization-functions-caching-example-key).

### Custom cache key
<a name="monetization-functions-caching-keys-custom"></a>

Set `Key` when the default key doesn't match how your endpoint's responses vary. For example, your URL might include a value that doesn't affect the response, such as a session ID for request tracing, which would otherwise give each session its own cache entry.

MediaTailor evaluates the `Key` expression against the session state each time the function runs, the same way it evaluates `Url`, `Headers`, and `Body`. When `Key` produces a value, the cache key consists of only the playback configuration and that value. MediaTailor ignores the URL, method, body, headers, and TTL settings when it matches requests to cached responses.

Keep the following in mind when you write a custom key:
+ `Key` must be a JSONata expression wrapped in `{%...%}`. MediaTailor rejects static string values at authoring time.
+ Include every value that changes the endpoint's response. Requests with the same key value receive the same cached response, even if they're sent to different URLs.
+ Custom keys are scoped to the playback configuration, not to a function. Two functions on the same playback configuration that produce the same key share cached responses.
+ If the `Key` expression fails to evaluate or produces an empty value, MediaTailor uses the default cache key for that request. Caching stays on.
+ If the evaluated key exceeds 1,024 characters, MediaTailor doesn't send the request. For all caching limits, see [Response caching limits](monetization-functions-limits.md#monetization-functions-limits-caching).

## Examples
<a name="monetization-functions-caching-examples"></a>

### Example: Cache Elemental Inference contextual metadata
<a name="monetization-functions-caching-example-ei"></a>

The following `AWS_SERVICE_REQUEST` function queries Elemental Inference for contextual metadata at the `PRE_ADS_REQUEST` hook. The request body is built from the ad break's presentation timestamp (PTS) time window, so sessions that reach the same ad break with the same time window send the same body. With the default cache key, MediaTailor calls Elemental Inference about once for each ad break instead of once for each session.

```
{
    "FunctionId": "eiContextualMetadataCached",
    "FunctionType": "AWS_SERVICE_REQUEST",
    "AwsServiceRequestConfiguration": {
        "Runtime": "JSONATA",
        "TargetService": "elemental-inference",
        "TargetRegion": "{%inference.region%}",
        "MethodType": "POST",
        "Url": "{%inference.dataEndpoint & '/v1/feed/' & inference.feedId & '/input/0/metadata'%}",
        "Headers": {
            "Content-Type": "application/json"
        },
        "Body": "{%'{\"outputName\": \"my-contextual-output\", \"timeSpecification\": {\"ptsBased\": {\"startPts\": ' & $string(($exists(inference.previousBreakEndPts) and inference.previousBreakEndPts > inference.pts - 30 * inference.timescale ? inference.previousBreakEndPts : inference.pts - 30 * inference.timescale)) & ', \"endPts\": ' & $string(inference.pts + 1) & ', \"timescale\": ' & $string(inference.timescale) & '}}, \"parameters\": {\"contextualMetadata\": {}}}' %}",
        "RequestTimeoutMilliseconds": 2000,
        "Cache": {
            "TtlMinimumSeconds": 30,
            "TtlMaximumSeconds": 300
        },
        "Output": {
            "player_params.iabCategories": "{%response.statusCode = 200 ? $join($distinct(response.body.items.metadata.contextualMetadata.iabTaxonomy.categories.uniqueId), ',') : ''%}"
        }
    }
}
```

For details about the request body and the time window, see [Elemental Inference integration](monetization-functions-elemental-inference-integration.md).

### Example: Include a request header in the cache key
<a name="monetization-functions-caching-example-key"></a>

Request headers aren't part of the default cache key. If your endpoint returns a different response for each value of a header, add that value to a custom key. The following `HTTP_REQUEST` function fetches localized promo text at the `PRE_SESSION_INITIALIZATION` hook. The endpoint selects the language from the `Accept-Language` header, which the function sets from a player parameter. The custom key combines the URL with the header value, so sessions share a cached response only when they request the same URL in the same language.

```
{
    "FunctionId": "fetchLocalizedPromo",
    "FunctionType": "HTTP_REQUEST",
    "HttpRequestConfiguration": {
        "Runtime": "JSONATA",
        "MethodType": "GET",
        "Url": "{%'https://promos.example.com/v1/promo?channel=' & $encodeUrlComponent(session.player_params.channel)%}",
        "Headers": {
            "Accept": "application/json",
            "Accept-Language": "{%session.player_params.lang%}"
        },
        "RequestTimeoutMilliseconds": 1000,
        "Cache": {
            "TtlMinimumSeconds": 60,
            "TtlMaximumSeconds": 300,
            "Key": "{%'https://promos.example.com/v1/promo?channel=' & $encodeUrlComponent(session.player_params.channel) & '|Accept-Language=' & session.player_params.lang%}"
        },
        "Output": {
            "player_params.promo_text": "{%response.statusCode = 200 ? response.body.text : ''%}"
        }
    }
}
```