

# AWS Elemental MediaTailor manifest logs description and event types
<a name="log-types"></a>

The following sections describe the logs that MediaTailor emits to describe events with the origin server when requesting and receiving a manifest. These are `ManifestService` logs.

**Topics**
+ [ManifestService events](#log-types-origininteraction)
+ [Manifest logs properties](#manifest-logs-main)

## ManifestService events
<a name="log-types-origininteraction"></a>

The following events are emitted during MediaTailor interactions with the origin. 


| Log | Description | 
| --- | --- | 
| CONFIG\_SECURITY\_ERROR | The MediaTailor configuration has a security issue.  | 
| CONFIG\_SYNTAX\_ERROR | The origin and asset path result in a malformed URL. | 
| CONNECTION\_ERROR | The MediaTailor connection to the origin was refused or failed. | 
| GENERATED\_MANIFEST | MediaTailor generated a manifest. You must have debug mode enabled to receive these logs. For information about debug log mode, including how to enable it, see [Generating debug logs](debug-log-mode.md). | 
| HOST\_DISALLOWED | MediaTailor does not allow HTTP requests to this host. | 
| INCOMPATIBLE\_HLS\_VERSION | The manifest uses an incompatible HLS version. MediaTailor requires version 3 or greater. | 
| INVALID\_SINGLE\_PERIOD\_DASH\_MANIFEST | The single-period DASH manifest is invalid. MediaTailor is passing through single-period DASH manifest. | 
| IO\_ERROR | MediaTailor encountered an IO error during communication with the origin. | 
| LAST\_PERIOD\_MISSING\_AUDIO | The last period in the DASH manifest is missing all audio AdaptationSets because of origin audio or video misalignment. To avoid playback issues, delay publishing the last period until at least the next request. | 
| LAST\_PERIOD\_MISSING\_AUDIO\_WARNING | The last period in the DASH manifest is missing all audio AdaptationSets because of origin audio or video misalignment. Choosing to publish (not delay) the last period. Missing audio might cause playback issues. | 
| MANIFEST\_ERROR | The MediaTailor manifest request failed. | 
| NO\_MASTER\_OR\_MEDIA\_PLAYLIST | The origin response doesn't contain a primary playlist or media playlist. | 
| NO\_MASTER\_PLAYLIST | The origin response doesn't contain the expected primary playlist. | 
| NO\_MEDIA\_PLAYLIST | The origin response doesn't contain the expected media playlist. | 
| ORIGIN\_MANIFEST | MediaTailor fetched an origin manifest. You must have debug mode enabled to receive these logs. For information about debug log mode, including how to enable it, see [Generating debug logs](debug-log-mode.md). | 
| PARSING\_ERROR | The origin is unable to parse the manifest request. | 
| PRE\_SESSION\_INIT\_FUNCTION\_COMPLETED | An individual function in the pre-session initialization hook completed. This is an opt-in event type. | 
| PRE\_SESSION\_INIT\_FUNCTION\_ERROR | An individual function in the pre-session initialization hook failed. | 
| PRE\_SESSION\_INIT\_HOOK\_ERROR | The pre-session initialization hook execution failed. | 
| PRE\_SESSION\_INIT\_HOOK\_SUMMARY | Summary of the pre-session initialization hook execution, including success or error status. This is an opt-in event type. | 
| SCTE35\_PARSING\_ERROR | MediaTailor is unable to parse Signal Binary element in the manifest. | 
| SESSION\_INITIALIZED | A session was initialized. You must have debug mode enabled to receive these logs. For information about debug log mode, including how to enable it, see [Generating debug logs](debug-log-mode.md). | 
| TIMEOUT\_ERROR | The MediaTailor manifest request timed out. | 
| TRACKING\_RESPONSE | MediaTailor served a tracking response. You must have debug mode enabled to receive these logs. For information about debug log mode, including how to enable it, see [Generating debug logs](debug-log-mode.md). | 
| UNKNOWN\_ERROR | MediaTailor encountered an unknown error. | 
| UNKNOWN\_HOST | The host is unknown. | 
| UNSUPPORTED\_SINGLE\_PERIOD\_DASH\_MANIFEST | The single-period DASH manifest is unsupported. MediaTailor is passing through single-period DASH manifest. | 

## Manifest logs properties
<a name="manifest-logs-main"></a>

This section describes the properties of the manifest logs.


| Property | Type | Required | 
| --- | --- | --- | 
| awsAccountId | string | true | 
| eventTimestamp | string | true | 
| originId | string | true | 
| customerId | string | false | 
| eventType | string | false | 
| sessionId | string | false | 
| originRequestUrl | string | false | 
| mediaTailorPath | string | false | 
| requestId | string | false | 
| responseBody | string | false | 
| sessionType | string (legal values: [DASH, HLS]) | false | 
| requestNextToken | string | false | 
| eventDescription | string | false | 
| errorType | string | false | 
| eventId | string | false | 
| executionTimeMs | integer | false | 
| functionId | string | false | 
| functionType | string | false | 
| http | object | false | 
| input | object | false | 
| output | object | false | 
| status | string | false | 
| assetPath | string | false | 
| originFullUrl | string | false | 
| originPrefixUrl | string | false | 
| additionalInfo | string | false | 
| cause | string | false | 
| response | string | false | 
| httpCode | string | false | 
| errorMessage | string | false | 
| adAdsResponse | string | false | 
| adAdsRawResponse | string | false | 
| adAdsRequest | string | false | 
| adNumNewAvails | string | false | 
| generatedMediaPlaylist | string | false | 
| requestStartTime | string | false | 
| requestEndTime | string | false | 
| requestStartTimeEpochMillis | string | false | 
| requestEndTimeEpochMillis | string | false | 