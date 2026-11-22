

# Configuring dynamic avail sizing

To turn on dynamic avail sizing, add its parameters to your manifest request.

## Requirements
<a name="das-enable-requirements"></a>

Before you enable dynamic avail sizing, confirm the following:
+ Your stream is a live or live-to-VOD HLS stream. Dynamic avail sizing doesn't apply to VOD, DASH, or Low-Latency HLS (LL-HLS) workflows.
+ Your playback configuration uses server-side ad insertion. Dynamic avail sizing doesn't apply to server-guided ad insertion (SGAI). For more information, see [Server-guided ad insertion overview](server-guided.md).
+ Your origin manifest window is large enough to hold the content reserve. The reserve can't be larger than the origin manifest window minus 60 seconds. If you request a larger reserve, MediaTailor reduces it to that limit. For example, a 180-second reserve needs an origin manifest window of at least 240 seconds.

## Parameters
<a name="das-enable-parameters"></a>

You enable dynamic avail sizing by adding parameters to your manifest request. Dynamic avail sizing is active for a session when `aws.contentReserveSeconds` is present. There's no separate on/off flag.

The following table describes the three dynamic avail sizing parameters. Each parameter is an integer, in seconds.


**Dynamic avail sizing parameters**  

| Parameter | Description | 
| --- | --- | 
| aws.contentReserveSeconds | Size of the content reserve. Dynamic avail sizing is active when this parameter is present. The reserve can't be larger than the origin manifest window minus 60 seconds; MediaTailor reduces a larger value to that limit.<br />**Values:** Integer, at least `1`<br />**Default:** Not set (dynamic avail sizing off) | 
| aws.maxAvailInflationSeconds | Maximum time that MediaTailor adds to a single avail when it inflates. MediaTailor inflates by the smaller of the deficit and this value.<br />**Values:** `0` to `120` (`0` turns inflation off)<br />**Default:** `120` | 
| aws.replenishmentThresholdSeconds | Minimum deficit that triggers inflation. A value of `0` inflates on any deficit. If you set it higher than the deficit your sessions typically reach, MediaTailor never inflates avails.<br />**Values:** `0` up to the value of `aws.contentReserveSeconds`<br />**Default:** `0` | 

For a full description of each parameter, see [aws.contentReserveSeconds](variables-service.md#variables-service-contentreserveseconds), [aws.maxAvailInflationSeconds](variables-service.md#variables-service-maxavailinflationseconds), and [aws.replenishmentThresholdSeconds](variables-service.md#variables-service-replenishmentthresholdseconds).

## Best practices
<a name="das-enable-best-practices"></a>

We recommend the following settings:
+ Set the content reserve to at least twice your longest ad break. For example, for 90-second ad breaks, use `aws.contentReserveSeconds=180`.
+ Set your origin manifest window at least 120 seconds longer than the content reserve, so the personalized manifest holds at least 120 seconds of content.
+ Leave inflation on so that the reserve refills over long sessions. Either omit `aws.maxAvailInflationSeconds` to use the default of 120 seconds, or set it to a value greater than `0`.

## Example configurations
<a name="das-enable-examples"></a>

The following examples show three ways to configure dynamic avail sizing in the manifest request.

To absorb underfill without inflation, set `aws.maxAvailInflationSeconds` to `0`. The reserve absorbs underfill but doesn't refill.

```
GET /v1/master/{hashed-account-id}/{origin-id}/{asset}.m3u8?aws.contentReserveSeconds=180&aws.maxAvailInflationSeconds=0
```

To absorb underfill and inflate later avails on any deficit, set `aws.maxAvailInflationSeconds` to a value greater than `0`. This approach keeps the reserve healthy over long sessions. For more information, see [Best practices](#das-enable-best-practices).

```
GET /v1/master/{hashed-account-id}/{origin-id}/{asset}.m3u8?aws.contentReserveSeconds=180&aws.maxAvailInflationSeconds=120
```

To inflate only after the deficit reaches a threshold, set `aws.replenishmentThresholdSeconds`. MediaTailor doesn't inflate an avail until the deficit reaches the threshold, so the reserve absorbs small or infrequent underfills without changing avail lengths.

```
GET /v1/master/{hashed-account-id}/{origin-id}/{asset}.m3u8?aws.contentReserveSeconds=180&aws.maxAvailInflationSeconds=60&aws.replenishmentThresholdSeconds=90
```