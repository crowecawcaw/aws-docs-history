

# Example 1: Data enrichment
<a name="monetization-functions-examples-enrichment"></a>

## Scenario
<a name="monetization-functions-examples-enrichment-scenario"></a>

A streaming service wants to fetch audience identity data from an external service (in this case, LiveRamp) at session start and store it in player parameters for ad targeting later in the session. An identity envelope is an encrypted identifier provided by an identity resolution service that allows ad systems to recognize a viewer across devices and platforms without exposing personal information.

## Configuration
<a name="monetization-functions-examples-enrichment-config"></a>

**Fetch LiveRamp envelope (HTTP\_REQUEST):**

```
{
    "FunctionId": "fetchLiveRamp",
    "FunctionType": "HTTP_REQUEST",
    "HttpRequestConfiguration": {
        "Runtime": "JSONATA",
        "MethodType": "GET",
        "Url": "{%'https://api.example-identity.com/v2/envelope?pid=12345&iv=' & player_params.hashedId%}",
        "Headers": {
            "Authorization": "{%'Bearer ramp-token-789'%}"
        },
        "RequestTimeoutMilliseconds": 2000,
        "Output": {
            "player_params.envelope_id": "{%response.body.envelopes[0].value%}"
        }
    }
}
```

**Note**  
Replace `Bearer ramp-token-789` with your own API credentials. Do not store sensitive tokens directly in function configurations in production. Consider using a token rotation strategy.

Set `RequestTimeoutMilliseconds` based on the expected response time of your external service. A lower value reduces latency but increases the chance of timeout errors.

## Function mapping
<a name="monetization-functions-examples-enrichment-mapping"></a>

```
{
    "FunctionMapping": {
        "PRE_SESSION_INITIALIZATION": "fetchLiveRamp"
    }
}
```

## What happens when the function runs
<a name="monetization-functions-examples-enrichment-runtime"></a>

1. A viewer starts a playback session.

1. MediaTailor runs the `PRE_SESSION_INITIALIZATION` lifecycle hook and runs `fetchLiveRamp`.

1. The function builds the request URL using `player_params.hashedId` and calls the LiveRamp API. In the URL, `pid` is the partner ID and `iv` is the hashed viewer identifier.

1. The output expression extracts the value from the first envelope in the response array (`response.body.envelopes[0].value`) and writes it to `player_params.envelope_id`.

**Tip**  
To handle errors explicitly, check `response.statusCode` before accessing response data: `{%response.statusCode = 200 ? response.body.envelopes[0].value : ''%}`

For more information, see [HTTP request](monetization-functions-types-http-request.md), [Pre-session initialization](monetization-functions-hooks-pre-session.md), [Troubleshooting and monitoring](monetization-functions-troubleshooting.md), and [Limits](monetization-functions-limits.md).