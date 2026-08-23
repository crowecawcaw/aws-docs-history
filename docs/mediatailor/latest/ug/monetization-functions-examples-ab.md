# Example 2: A/B traffic split

## Scenario

A streaming service wants to use a CUSTOM\_OUTPUT function to randomly split ad
request traffic between two ad decision server (ADS) URLs for A/B testing. Half of
the ad requests go to the v1 endpoint and half go to the v2 endpoint.

## Configuration

**A/B traffic split
(CUSTOM\_OUTPUT):**

```
{
    "FunctionId": "abTestAdsUrl",
    "FunctionType": "CUSTOM_OUTPUT",
    "CustomOutputConfiguration": {
        "Runtime": "JSONATA",
        "Output": {
            "adsRequest.url": "{%$random() < 0.5 ? 'https://ads.example.com/v1/decision?session=' & session.id : 'https://ads.example.com/v2/decision?session=' & session.id%}"
        }
    }
}
```

In this configuration:

- `FunctionId` — A unique name for this function.
- `FunctionType` — `CUSTOM_OUTPUT` evaluates
  expressions without making HTTP calls.
- `Output` — Maps `adsRequest.url` to an
  expression that randomly selects one of two ADS URLs.

## Function mapping

```
{
    "FunctionMapping": {
        "PRE_ADS_REQUEST": "abTestAdsUrl"
    }
}
```

## What happens when the function runs

1. An ad break is encountered during playback.
2. MediaTailor runs the `PRE_ADS_REQUEST` lifecycle hook and
   runs `abTestAdsUrl`.
3. The `$random()` function returns a value between 0 and 1.
   If the value is less than 0.5, the function sets the ADS URL to the v1
   endpoint. Otherwise, it sets the URL to the v2
   endpoint.

The `$random()` function is evaluated on each ad break, so the split
is per ad request, not per session.

###### Tip

To adjust the traffic split ratio, change the threshold value. For example,
`$random() < 0.8` sends 80% of traffic to the first URL and 20%
to the second.

###### Note

Writing to `adsRequest.url` overrides the default ADS URL
configured in the playback configuration for the current ad break.

For more information, see [Custom output](monetization-functions-types-custom-output.md "monetization-functions-types-custom-output.md"), [Pre-ads request](monetization-functions-hooks-pre-ads.md "monetization-functions-hooks-pre-ads.md"), and [JSONata expression
reference](monetization-functions-jsonata.md "monetization-functions-jsonata.md").
