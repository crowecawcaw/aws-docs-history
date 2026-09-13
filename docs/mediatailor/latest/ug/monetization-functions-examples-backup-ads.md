

# Example 4: Secondary ad server fallback
<a name="monetization-functions-examples-backup-ads"></a>

## Scenario
<a name="monetization-functions-examples-backup-ads-scenario"></a>

Your primary ADS sometimes returns fewer ads than the ad break can hold. When that happens, you want to fetch additional ads from a secondary ad server and append them to the ad list, so the extra ads can fill the remaining time.

This example uses the `POST_ADS_RESPONSE` lifecycle hook. A `VAST_REQUEST` function fetches the secondary ads, and a `SEQUENTIAL_EXECUTOR` orchestrates the process. The executor's output block appends the fetched ads to the ad list, and its `RunCondition` skips the secondary fetch entirely when the primary response already has enough ads.

## Function configuration
<a name="monetization-functions-examples-backup-ads-config"></a>

**Fetch function (`fetchBackupAds`):**

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

**Sequence (`backupAdsFallback`):**

```
{
    "FunctionId": "backupAdsFallback",
    "FunctionType": "SEQUENTIAL_EXECUTOR",
    "SequentialExecutorConfiguration": {
        "Runtime": "JSONATA",
        "TimeoutMilliseconds": 2000,
        "FunctionList": [
            { "FunctionId": "fetchBackupAds", "RunCondition": "{%$count(adsResponse.ads) < 3%}" }
        ],
        "Output": {
            "adsResponse.ads": "{%$count(adsResponse.ads) < 3 ? $append(adsResponse.ads, temp.backupAds)[] : adsResponse.ads[]%}"
        }
    }
}
```

## Function mapping
<a name="monetization-functions-examples-backup-ads-mapping"></a>

```
{
    "FunctionMapping": {
        "POST_ADS_RESPONSE": "backupAdsFallback"
    }
}
```

## What happens at runtime
<a name="monetization-functions-examples-backup-ads-runtime"></a>

1. MediaTailor receives and parses the primary ADS response, then fires the `POST_ADS_RESPONSE` lifecycle hook.

1. If the primary response contains fewer than 3 ads, the `RunCondition` evaluates to `true` and `fetchBackupAds` calls the secondary ad server. MediaTailor then parses the response as VAST, resolves wrapper redirects, and writes the parsed ads to `temp.backupAds`.

1. If the primary response already has 3 or more ads, the fetch is skipped and `temp.backupAds` is not set.

1. The sequence's output block writes the combined ad list to `adsResponse.ads`. When the fetch was skipped, the condition takes the `else` branch and returns the original ads unchanged. Because the secondary ads were parsed by a `VAST_REQUEST` function in the same hook invocation, MediaTailor restores each appended ad's complete VAST data before ad selection.

1. Ad selection proceeds with the combined list. If the secondary fetch failed, `temp.backupAds` is an empty array and the original ad list is used unchanged.

**Note**  
The trailing `[]` in the output expression is required. Without array coercion, an expression that produces zero or one ad doesn't produce an array, and the output is discarded or misapplied. For more information, see [Post-ads response](monetization-functions-hooks-post-ads.md).

For more information about the fields used in this example, see [VAST request](monetization-functions-types-vast-request.md) and [Post-ads response](monetization-functions-hooks-post-ads.md).