

# VAST request
<a name="monetization-functions-types-vast-request"></a>

## When to use
<a name="monetization-functions-types-vast-request-when"></a>

Use `VAST_REQUEST` when your function needs to fetch ads from a Video Ad Serving Template (VAST) endpoint. MediaTailor sends the request, parses the response as VAST with wrapper redirects resolved, and makes the parsed ads available to your output expressions. Common use cases include fetching ads from a secondary ad server to supplement a short primary response, and retrieving house ads or promos to inject into underfilled ad breaks.

`VAST_REQUEST` functions are supported at the `POST_ADS_RESPONSE` and `PRE_MANIFEST_INSERTION` lifecycle hooks, on their own or as steps inside an executor. Ads parsed by a `VAST_REQUEST` function integrate with those hooks' outputs at full fidelity. For details, see [How parsed ads integrate with hook outputs](#monetization-functions-types-vast-request-store).

## Configuration fields
<a name="monetization-functions-types-vast-request-fields"></a>

A `VAST_REQUEST` function has the following fields:
+ **Runtime** — The expression language. Set this to `JSONATA`.
+ **MethodType** — The HTTP method. Supported values are `GET` (the default) and `POST`.
+ **Url** — The VAST endpoint to send the request to. You can use a static URL or a JSONata expression that builds the URL dynamically. A static URL must use the `https` scheme.
+ **Headers** — The HTTP headers to include in the request, specified as header name and value pairs. Use `{%...%}` expression syntax for dynamic header values.
+ **Body** — The request body to send. Used with `POST` requests, for example to send an OpenRTB bid request. You can use a JSONata expression to build the body dynamically.
+ **RequestTimeoutMilliseconds** (required) — How long to wait for a response.
+ **Output** — Defines the values to produce after the call completes. Each entry maps an output key to an expression that can reference the `response` object, including `response.parsedAds`.

The HTTP request limits that apply to `HTTP_REQUEST` functions also apply here. For details, see [Limits](monetization-functions-limits.md).

## How the request is processed
<a name="monetization-functions-types-vast-request-phases"></a>

1. **Build the request** — MediaTailor evaluates the `Url`, `Headers`, and `Body` expressions against the current session state, then sends the request. `POST` requests are sent with the `application/json` content type.

1. **Parse the response** — MediaTailor parses the response body as VAST. If an ad is a VAST wrapper, MediaTailor follows the redirect chain and resolves it to the final inline ad. Wrapper redirect requests are always sent with `GET`, as the VAST specification requires. If your endpoint returns a document that contains a VAST URL instead of VAST itself (as some bidders do), chain an `HTTP_REQUEST` step that retrieves the URL, followed by a `VAST_REQUEST` step that fetches it.

1. **Process the parsed ads** — MediaTailor evaluates the expressions in the output block. These expressions can reference the original session state and the `response` object.

## Response fields
<a name="monetization-functions-types-vast-request-response"></a>

After the call completes, you can reference the following fields in your Output expressions:


| Field | Type | Description | 
| --- | --- | --- | 
| response.parsedAds | Array | The parsed ads, with wrapper redirects resolved. Each ad has the same shape as the adsResponse.ads entries at the POST\_ADS\_RESPONSE hook: adId, durationSeconds, adSystem, adTitle, creativeId, sequence, mediaFiles, and trackingEvents. Set to an empty array when the call fails or the response is not valid VAST. | 
| response.statusCode | Integer | The HTTP status code returned by the endpoint. Set to null on network failure. | 

Because parsed ads use the same shape as `adsResponse.ads`, you can move expressions between the two surfaces without rewriting field references.

## How parsed ads integrate with hook outputs
<a name="monetization-functions-types-vast-request-store"></a>

Every ad that a `VAST_REQUEST` function parses is retained internally by MediaTailor, keyed by the ad's VAST ad ID, for the duration of the hook invocation. This gives parsed ads first-class treatment in hook outputs:
+ At `POST_ADS_RESPONSE`, appending a parsed ad to `adsResponse.ads` by its `adId` restores the ad's complete parsed VAST data, including the full media file list and tracking events.
+ At `PRE_MANIFEST_INSERTION`, injecting an ad with just its `vastAdId` lets MediaTailor select the best media file and handle transcoding registration automatically.

**Important**  
The retained ads don't carry over between hook invocations. A `VAST_REQUEST` call made at `POST_ADS_RESPONSE` is not available to a later `PRE_MANIFEST_INSERTION` invocation. Call `VAST_REQUEST` in the same hook's function chain where you use its results.

## Failure behavior
<a name="monetization-functions-types-vast-request-failure"></a>

If the call fails due to a network error or timeout, if the endpoint returns an HTTP error, or if the response can't be parsed as VAST, `response.parsedAds` is an empty array and the function chain continues. Check `response.statusCode` to distinguish an HTTP failure from a VAST response that genuinely contains no ads.

**Tip**  
Keep `RequestTimeoutMilliseconds` tight. VAST wrapper resolution can involve multiple network round trips, and all of them count against the hook's timeout and the shared hook budget.

## Example: Fetch ads from a secondary ad server
<a name="monetization-functions-types-vast-request-example"></a>

The following function fetches ads from a backup ad server and stores the parsed ads in temporary data. A `CUSTOM_OUTPUT` step later in the same sequence can append them to `adsResponse.ads`. It is designed for the `POST_ADS_RESPONSE` lifecycle hook.

```
{
    "FunctionId": "fetchBackupAds",
    "FunctionType": "VAST_REQUEST",
    "VastRequestConfiguration": {
        "Runtime": "JSONATA",
        "MethodType": "GET",
        "Url": "{%'https://backup-ads.example.com/vast?sid=' & session.uuid%}",
        "Headers": {
            "Accept": "application/xml"
        },
        "RequestTimeoutMilliseconds": 1000,
        "Output": {
            "temp.backupAds": "{%response.parsedAds%}"
        }
    }
}
```

To send an OpenRTB bid request instead, set `MethodType` to `POST` and provide the bid request in `Body`. The bidder must return VAST in the response body.

For a complete walkthrough of a similar example, see [Function examples](monetization-functions-examples.md).