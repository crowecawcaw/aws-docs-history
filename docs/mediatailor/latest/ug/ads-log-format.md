

# AWS Elemental MediaTailor ADS logs description and event types
<a name="ads-log-format"></a>

The following sections describe the logs that MediaTailor emits to describe events with the ad decision server (ADS). These are `AdDecisionServerInteractions` logs.

**Topics**
+ [AdDecisionServerInteractions events](#log-types-adsinteraction)
+ [ADS log description](#ads-log-description)
+ [ADS log JSON schema](#ads-log-json-schema)

## AdDecisionServerInteractions events
<a name="log-types-adsinteraction"></a>

The following events are emitted during MediaTailor interactions with the ad decision server (ADS). 


| Log | Description | 
| --- | --- | 
| AD\_MARKER\_FOUND | MediaTailor found an ad marker in the manifest. | 
| BEACON\_FIRED | A tracking beacon was fired to report ad events. In server-side reporting mode (default), MediaTailor fires the beacon. In client-side reporting mode, the playback device fires the beacon. | 
| EMPTY\_VAST\_RESPONSE | The ADS returned an empty VAST response containing zero ads. | 
| EMPTY\_VMAP\_RESPONSE | The ADS returned an empty VMAP response. | 
| ERROR\_ADS\_INVALID\_RESPONSE | The ADS returned a non-200 status code. | 
| ERROR\_ADS\_IO | MediaTailor encountered an error while trying to communicate with the ADS.  | 
| ERROR\_ADS\_RESPONSE\_PARSE | MediaTailor encountered an error while parsing the ADS response.  | 
| ERROR\_ADS\_RESPONSE\_UNKNOWN\_ROOT\_ELEMENT | The ADS response contains an invalid root element. | 
| ERROR\_ADS\_TIMEOUT | The MediaTailor request to the ADS timed out. | 
| ERROR\_DISALLOWED\_HOST | The ADS host is not allowed. | 
| ERROR\_FIRING\_BEACON\_FAILED | MediaTailor failed at firing the tracking beacon. | 
| ERROR\_PERSONALIZATION\_DISABLED | Ad insertion is disabled for this session. | 
| ERROR\_UNKNOWN | MediaTailor encountered an unknown error during the ADS request. | 
| ERROR\_UNKNOWN\_HOST | The ADS host is unknown. | 
| ERROR\_VAST\_INVALID\_MEDIA\_FILE | The VAST Ad has an invalid or missing MediaFile element. | 
| ERROR\_VAST\_INVALID\_VAST\_AD\_TAG\_URI | The VAST response contains an invalid VASTAdTagURI. | 
| ERROR\_VAST\_MISSING\_CREATIVES | The VAST Ad contains zero or multiple Creatives elements. Exactly one Creatives element is required. | 
| ERROR\_VAST\_MISSING\_IMPRESSION | The VAST Ad contains zero Impression elements. At least one Impression element is required.  | 
| ERROR\_VAST\_MISSING\_MEDIAFILES | The VAST Ad contains zero or multiple MediaFiles elements. Exactly one MediaFiles element is required. | 
| ERROR\_VAST\_MISSING\_OVERLAYS | MediaTailor didn't receive any non-linear creatives from the ad server.  | 
| ERROR\_VAST\_MULTIPLE\_LINEAR | The VAST Ad contains multiple Linear elements. | 
| ERROR\_VAST\_MULTIPLE\_TRACKING\_EVENTS | The VAST Ad contains multiple TrackingEvents elements. | 
| ERROR\_VAST\_REDIRECT\_EMPTY\_RESPONSE | The VAST redirect request returned an empty response. | 
| ERROR\_VAST\_REDIRECT\_FAILED | The VAST redirect request encountered an error. | 
| ERROR\_VAST\_REDIRECT\_MULTIPLE\_VAST | The VAST redirect request returned multiple ads. | 
| FILLED\_AVAIL | MediaTailor successfully filled the avail. | 
| FILLED\_OVERLAY\_AVAIL | MediaTailor successfully filled the overlay avail. | 
| INTERSTITIAL\_VOD\_FAILURE | The ADS request or response encountered a problem while filling interstitial avails for the VOD playlist. No ads will be inserted. | 
| INTERSTITIAL\_VOD\_SUCCESS | MediaTailor successfully filled interstitial avails for the VOD playlist. | 
| MAKING\_ADS\_REQUEST | MediaTailor is requesting advertisements from the ADS. | 
| MODIFIED\_TARGET\_URL | MediaTailor modified the outbound target URL. | 
| NON\_AD\_MARKER\_FOUND | MediaTailor found a non-actionable ad marker in the manifest. | 
| PRE\_ADS\_REQUEST\_FUNCTION\_COMPLETED | An individual function in the pre-ads request hook completed. This is an opt-in event type. | 
| PRE\_ADS\_REQUEST\_FUNCTION\_ERROR | An individual function in the pre-ads request hook failed. | 
| PRE\_ADS\_REQUEST\_HOOK\_ERROR | The pre-ads request hook execution failed. | 
| PRE\_ADS\_REQUEST\_HOOK\_SUMMARY | Summary of the pre-ads request hook execution, including success or error status. This is an opt-in event type. | 
| RAW\_ADS\_RESPONSE | MediaTailor received a raw ADS response. | 
| REDIRECTED\_VAST\_RESPONSE | MediaTailor received a VAST response after following the VAST redirect. | 
| VAST\_REDIRECT | The VAST ad response contains a redirect. | 
| VAST\_RESPONSE | MediaTailor received a VAST response. | 
| VOD\_TIME\_BASED\_AVAIL\_PLAN\_SUCCESS | MediaTailor successfully created a time-based avail plan for the VOD template. | 
| VOD\_TIME\_BASED\_AVAIL\_PLAN\_VAST\_RESPONSE\_FOR\_OFFSET | MediaTailor is creating a time-based avail plan for the VOD template. MediaTailor received a VAST response for the time offset. | 
| VOD\_TIME\_BASED\_AVAIL\_PLAN\_WARNING\_NO\_ADVERTISEMENTS | The ADS request or response encountered a problem while creating a time-based avail plan for the VOD template. No ads will be inserted. | 
| WARNING\_NO\_ADVERTISEMENTS | MediaTailor encountered a problem while filling the avail. No ads are inserted. | 
| WARNING\_URL\_VARIABLE\_SUBSTITUTION\_FAILED | MediaTailor can't substitute dynamic variables in the ADS URL. Check the URL configuration. | 
| WARNING\_VPAID\_AD\_DROPPED | A VPAID ad dropped due to a missing slate, or the session uses server-side reporting. | 

## ADS log description
<a name="ads-log-description"></a>

This section describes the structure and contents of the ADS log description. To explore on your own in a JSON editor, use the listing at [ADS log JSON schema](#ads-log-json-schema). 

Each event in the ADS log contains the standard fields that are generated by CloudWatch Logs. For information, see [Analyze log data with CloudWatch Logs insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html). 

### ADS logs properties
<a name="ads-logs-main"></a>

This section describes the properties of the ADS logs.


| Property | Type | Required | Description | 
| --- | --- | --- | --- | 
| adsRequestUrl | string | false | The full URL of the ADS request made by MediaTailor. | 
| avail | object of type [avail](#ads-logs-avail) | false | Information about an avail that MediaTailor fills with ads. Currently, for the FILLED\_AVAIL event type, this is the plan created by MediaTailor when it first encounters the avail. How the avail is eventually filled may vary from this plan, depending on how the content plays out.  | 
| awsAccountId | string | true | The AWS account ID for the MediaTailor configuration that was used for the session. | 
| customerId | string | true | The hashed version of the AWS account ID, which you can use to correlate multiple log entries. | 
| eventDescription | string | true | A short description of the event that triggered this log message, provided by the MediaTailor service. By default, this is empty. Example: Got VAST response. | 
| eventTimestamp | string | true | The date and time of the event. | 
| eventType | string | true | The code for the event that triggered this log message. Example: VAST\_RESPONSE. | 
| errorType | string | false | Structured error classification. Present on PRE\_ADS\_REQUEST\_HOOK\_ERROR and PRE\_ADS\_REQUEST\_FUNCTION\_ERROR events. Values: INTERNAL\_ERROR, SYNTAX\_ERROR, RESOURCE\_LIMIT\_ERROR, RESTRICTION\_ERROR, TIMEOUT\_ERROR, VALIDATION\_ERROR. | 
| cause | string | false | Error detail string describing the specific failure. Present on PRE\_ADS\_REQUEST\_HOOK\_ERROR and PRE\_ADS\_REQUEST\_FUNCTION\_ERROR events. | 
| eventId | string | false | Unique identifier per hook invocation. Use this field to correlate hook-level and function-level events for the same execution. Present on Functions events only. | 
| executionTimeMs | integer | false | Execution time in milliseconds. Present on Functions events only. | 
| functionId | string | false | The identifier of the function. On hook events, this is the function configured on the hook. On function events, this is the individual function within the executor. Present on Functions events only. | 
| functionType | string | false | The type of function: CUSTOM\_OUTPUT, HTTP\_REQUEST, SEQUENTIAL\_EXECUTOR, or CONCURRENT\_EXECUTOR. Present on function-level events only. | 
| http | object | false | HTTP request and response details. Present on function-level events for HTTP\_REQUEST functions only. Contains request (url, method, headers, body), responseTimeMs, response (statusCode, headers, body), and truncated (true when request or response body was truncated to fit within log event size limits). | 
| input | object | false | Before-values of variables targeted by output expressions. Present on function-level events only. | 
| output | object | false | Values produced by the function. Present on PRE\_ADS\_REQUEST\_FUNCTION\_COMPLETED events only. | 
| status | string | false | Hook execution outcome: SUCCESS or ERROR. Present on PRE\_ADS\_REQUEST\_HOOK\_SUMMARY events only. | 
| originId | string | true | The configuration name from the MediaTailor configuration. This is different from the video content source, which is also part of the configuration. | 
| prefetchScheduleName | string | false | The name of the prefetch schedule associated with this ad event. | 
| requestHeaders | array of type [requestheaders](#ads-logs-requestheaders) | false | The headers that MediaTailor included with the ADS request. Typically, the logs include these when a request to the ADS fails, to help with troubleshooting. | 
| requestId | string | true | The MediaTailor request ID, which you can use to correlate multiple log entries for the same request. | 
| sessionId | string | true | The unique numeric identifier that MediaTailor assigned to the player session. All requests that a player makes for a session have the same session ID. Example: e039fd39-09f0-46b2-aca9-9871cc116cde. | 
| sessionType | string (legal values: [DASH, HLS]) | true | The player's stream type. | 
| vastAd | object of type [vastAd](#ads-logs-vastAd) | false | Information about a single ad parsed from the VAST response. | 
| vastResponse | object of type [vastResponse](#ads-logs-vastResponse) | false | Information about the VAST response that MediaTailor received from the ADS. | 
| vodCreativeOffsets | object of type [vodCreativeOffsets](#ads-logs-vodCreativeOffsets) | false | A map that indicates the time offsets in the manifest where MediaTailor will insert avails, based on the VMAP response. | 
| vodVastResponseTimeOffset | number | false | The VMAP specific time offset for VOD ad insertion. | 

### adContent
<a name="ads-logs-adContent"></a>

This section describes the properties of the ADS logs adContent.


**ADS Logs adContent Properties**  

| Property | Type | Required | Description | 
| --- | --- | --- | --- | 
| adPlaylistUris | object of type [adPlaylistUris](#ads-logs-adPlaylistUris) | false | The mapping from the origin manifest for a variant to the ad manifest for the variant. For DASH, this contains a single entry, because all variants are represented in a single DASH manifest.  | 

### adPlaylistUris
<a name="ads-logs-adPlaylistUris"></a>

This section describes the properties of the ADS logs adPlaylistUris.


**ADS Logs adPlaylistUris Properties**  

| Property | Type | Required | Description | 
| --- | --- | --- | --- | 
| <any string> | string | false | The URL of the ad manifest for the specific variant. | 

### avail
<a name="ads-logs-avail"></a>

This section describes the properties of the ADS logs avail.


**ADS Logs avail Properties**  

| Property | Type | Required | Description | 
| --- | --- | --- | --- | 
| availId | string | true | The unique identifier for this avail. For HLS, this is the media sequence number where the avail begins. For DASH, this is the period ID. | 
| creativeAds | array of type [creativeAd](#ads-logs-creativeAd) | true | The ads that MediaTailor inserted into the avail. | 
| fillRate | number | true | The rate at which the ads fill the avail duration, from 0.0 (for 0%) to 1.0 (for 100%). | 
| filledDuration | number | true | The sum of the durations of all the ads inserted into the avail. | 
| numAds | number | true | The number of ads that MediaTailor inserted into the avail. | 
| originAvailDuration | number | true | The duration of the avail as specified in the content stream from the origin (CUE\_OUT or SCTE). | 
| skippedAds | array of type [skippedAd](#ads-logs-skippedAd) | false | The ads that MediaTailor didn't insert, for reasons like TRANSCODE\_IN\_PROGRESS and TRANSCODE\_ERROR. For a list of skipped ad reasons, see [Ad skipping troubleshooting](troubleshooting-ad-skipping-overview.md). | 
| slateAd | object of type [slateAd](#ads-logs-slateAd) | true | Information about the slate ad, which MediaTailor uses to fill any unfilled segments in the avail. | 

### creativeAd
<a name="ads-logs-creativeAd"></a>

This section describes the properties of the ADS logs creativeAd.


**ADS Logs creativeAd Properties**  

| Property | Type | Required | Description | 
| --- | --- | --- | --- | 
| adContent | object of type [adContent](#ads-logs-adContent) | true | Information about the content of the inserted ad. | 
| creativeUniqueId | string | true | The unique identifier for the ad, used as a key for transcoding. This is the ID field for the creative in the VAST response, if available. Otherwise, it's the mezzanine URL of the ad.  | 
| trackingEvents | object of type [trackingEvents](#ads-logs-trackingEvents) | true | The tracking beacon URLs for the various tracking events for the ad. The keys are the event names, and the values are a list of beacon URLs. | 
| transcodedAdDuration | number | true | The duration of the ad, calculated from the transcoded asset. | 
| uri | string | true | The URL of the mezzanine version of the ad, which is the input to the transcoder. | 
| vastDuration | number | true | The duration of the ad, as parsed from the VAST response. | 

### requestheaders
<a name="ads-logs-requestheaders"></a>

This section describes the properties of the ADS logs requestheaders.


**ADS Logs requestheaders Properties**  

| Property | Type | Required | Description | 
| --- | --- | --- | --- | 
| name | string | true | The name of the header. | 
| value | string | true | The value of the header. | 

### skippedAd
<a name="ads-logs-skippedAd"></a>

This section describes the properties of the ADS logs skippedAd.


**ADS Logs skippedAd Properties**  

| Property | Type | Required | Description | 
| --- | --- | --- | --- | 
| adMezzanineUrl | string | true | The mezzanine URL of the skipped ad. | 
| creativeUniqueId | string | true | The unique identifier for the ad, used as a key for transcoding. This is the ID field for the creative in the VAST response, if available. Otherwise, it's the mezzanine URL of the ad.  | 
| skippedReason | string | true | The code that indicates why the ad wasn't inserted. Example: TRANSCODE\_IN\_PROGRESS. For a list of skipped ad reasons, see [Ad skipping troubleshooting](troubleshooting-ad-skipping-overview.md). | 
| transcodedAdDuration | number | false | The duration of the ad, calculated from the transcoded asset. | 
| vastDuration | number | true | The duration of the ad, as parsed from the VAST response. | 

### slateAd
<a name="ads-logs-slateAd"></a>

This section describes the properties of the ADS logs slateAd.


**ADS Logs slateAd Properties**  

| Property | Type | Required | Description | 
| --- | --- | --- | --- | 
| adContent | object of type [adContent](#ads-logs-adContent) | true | Information about the content of the inserted ad. | 
| creativeUniqueId | string | true | The unique identifier for the ad, used as a key for transcoding. This is the ID field for the creative in the VAST response, if available. Otherwise, it's the mezzanine URL of the ad.  | 
| transcodedAdDuration | number | true | The duration of the ad, calculated from the transcoded asset. | 
| uri | string | true | The URL of the mezzanine version of the ad, which is the input to the transcoder. | 

### trackingEvents
<a name="ads-logs-trackingEvents"></a>

This section describes the properties of the ADS logs trackingEvents.


**ADS Logs trackingEvents Properties**  

| Property | Type | Required | Description | 
| --- | --- | --- | --- | 
| <any string> | array of type string | false | The list of beacon URLs for the specified tracking event (impression, complete, and so on) | 

### vastAd
<a name="ads-logs-vastAd"></a>

This section describes the properties of the ADS logs vastAd.


**ADS Logs vastAd Properties**  

| Property | Type | Required | Description | 
| --- | --- | --- | --- | 
| adSystem | string | true | The value of the AdSystem tag in the VAST response. | 
| adTitle | string | true | The media files that are available for the ad in the VAST response. | 
| creativeAdId | string | true | The value of the adId attribute of the Creative tag in the VAST response. | 
| creativeId | string | true | The value of the id attribute of the Creative tag in the VAST response. | 
| duration | number | true | The approximate duration of the ad, based on the duration tag in the linear element of the VAST response. | 
| trackingEvents | object of type [trackingEvents](#ads-logs-trackingEvents) | true | The tracking beacon URLs for the various tracking events for the ad. The keys are the event names, and the values are a list of beacon URLs. | 
| vastAdId | string | true | The value of the id attribute of the Ad tag in the VAST response | 
| vastAdTagUri | string | false | The VMAP-specific redirect URI for an ad. | 
| vastMediaFiles | array of type [vastMediaFile](#ads-logs-vastMediaFile) | true | The list of available media files for the ad in the VAST response. | 

### vastMediaFile
<a name="ads-logs-vastMediaFile"></a>

This section describes the properties of the ADS logs vastMediaFile.


**ADS Logs vastMediaFile Properties**  

| Property | Type | Required | Description | 
| --- | --- | --- | --- | 
| apiFramework | string | true | The API framework needed to manage the media file. Example: VPAID. | 
| bitrate | number | true | The bitrate of the media file. | 
| delivery | string | true | The protocol used for the media file, set to either progressive or streaming. | 
| height | number | true | The pixel height of the media file. | 
| id | string | true | The value of the id attribute of the MediaFile tag. | 
| type | string | true | The MIME type of the media file, taken from the type attribute of the MediaFile tag. | 
| uri | string | true | The URL of the mezzanine version of the ad, which is the input to the transcoder. | 
| width | number | true | The pixel width of the media file. | 

### vastResponse
<a name="ads-logs-vastResponse"></a>

This section describes the properties of the ADS logs vastResponse.


**ADS Logs vastResponse Properties**  

| Property | Type | Required | Description | 
| --- | --- | --- | --- | 
| errors | array of type string | true | The error URLs parsed from the Error tags in the VAST response. | 
| vastAds | array of type [vastAd](#ads-logs-vastAd) | true | The ads parsed from the VAST response. | 
| version | string | true | The VAST specification version, parsed from the version attribute of the VAST tag in the response. | 

### vodCreativeOffsets
<a name="ads-logs-vodCreativeOffsets"></a>

This section describes the properties of the ADS logs vodCreativeOffsets.


**ADS Logs vodCreativeOffsets Properties**  

| Property | Type | Required | Description | 
| --- | --- | --- | --- | 
| <any string> | array of type [vodCreativeOffset](#ads-logs-vodCreativeOffset) | false | A mapping from a time offset in the manifest to a list of ads to insert at this time. | 

### vodCreativeOffset
<a name="ads-logs-vodCreativeOffset"></a>

This section describes the properties of the ADS logs vodCreativeOffset.


**ADS Logs vodCreativeOffset Properties**  

| Property | Type | Required | Description | 
| --- | --- | --- | --- | 
| adContent | object of type [adContent](#ads-logs-adContent) | true | Information about the content of the inserted ad. | 
| creativeUniqueId | string | true | The unique identifier for the ad, used as a key for transcoding. This is the ID field for the creative in the VAST response, if available. Otherwise, it's the mezzanine URL of the ad.  | 
| trackingEvents | object of type [trackingEvents](#ads-logs-trackingEvents) | true | The tracking beacon URLs for the various tracking events for the ad. The keys are the event names, and the values are a list of beacon URLs. | 
| transcodedAdDuration | number | true | The duration of the ad, calculated from the transcoded asset. | 
| uri | string | true | The URL of the mezzanine version of the ad, which is the input to the transcoder. | 
| vastDuration | number | true | The duration of the ad, as parsed from the VAST response. | 

## ADS log JSON schema
<a name="ads-log-json-schema"></a>

The following lists the JSON schema for the AWS Elemental MediaTailor ADS log.

```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://amazon.com/elemental/midas/mms/adsLogSchema.json",
  "type": "object",
  "title": "AWS Elemental MediaTailor ADS Log JSON Schema",
  "required": [
    "eventType",
    "eventTimestamp",
    "requestId",
    "sessionType",
    "eventDescription",
    "awsAccountId",
    "customerId",
    "originId",
    "sessionId"
  ],
  "additionalProperties": false,
  "properties": {
    "eventType": {
      "$id": "#/properties/eventType",
      "type": "string",
      "description": "The code for the event that triggered this log message. Example: <code>VAST_RESPONSE</code>.",
      "examples": [
        "FILLED_AVAIL"
      ]
    },
    "eventTimestamp": {
      "$id": "#/properties/eventTimestamp",
      "type": "string",
      "description": "The date and time of the event.",
      "examples": [
        "1970-01-01T00:00:00Z"
      ],
      "format": "date-time"
    },
    "requestId": {
      "$id": "#/properties/requestId",
      "type": "string",
      "description": "The MediaTailor request ID, which you can use to correlate multiple log entries for the same request.",
      "examples": [
        "c7c7ae8c-a61e-44e0-8efd-7723995337a1"
      ],
      "pattern": "^(.*)$"
    },
    "sessionType": {
      "$id": "#/properties/sessionType",
      "type": "string",
      "enum": [
        "HLS",
        "DASH"
      ],
      "description": "The player's stream type."
    },
    "eventDescription": {
      "$id": "#/properties/eventDescription",
      "type": "string",
      "description": "A short description of the event that triggered this log message, provided by the MediaTailor service. By default, this is empty. Example: <code>Got VAST response</code>.",
      "default": "",
      "examples": [
        "Got VAST response"
      ],
      "pattern": "^(.*)$"
    },
    "awsAccountId": {
      "$id": "#/properties/awsAccountId",
      "type": "string",
      "description": "The AWS account ID for the MediaTailor configuration that was used for the session."
    },
    "customerId": {
      "$id": "#/properties/customerId",
      "type": "string",
      "description": "The hashed version of the AWS account ID, which you can use to correlate multiple log entries.",
      "pattern": "^(.*)$"
    },
    "originId": {
      "$id": "#/properties/originId",
      "type": "string",
      "description": "The configuration name from the MediaTailor configuration. This is different from the video content source, which is also part of the configuration.",
      "examples": [
        "external-canary-dash-serverside-reporting-onebox"
      ],
      "pattern": "^(.*)$"
    },
    "sessionId": {
      "$id": "#/properties/sessionId",
      "type": "string",
      "description": "The unique numeric identifier that MediaTailor assigned to the player session. All requests that a player makes for a session have the same session ID. Example: <code>e039fd39-09f0-46b2-aca9-9871cc116cde</code>.",
      "examples": [
        "120b9873-c007-40c8-b3db-0f1bd194970b"
      ],
      "pattern": "^(.*)$"
    },
    "avail": {
      "$id": "#/properties/avail",
      "type": "object",
      "title": "avail",
      "description": "Information about an avail that MediaTailor fills with ads. Currently, for the <code>FILLED_AVAIL</code> event type, this is the plan created by MediaTailor when it first encounters the avail. How the avail is eventually filled may vary from this plan, depending on how the content plays out.  ",
      "required": [
        "creativeAds",
        "originAvailDuration",
        "filledDuration",
        "fillRate",
        "driftMillisecondsAtAvailStart",
        "numAds",
        "slateAd",
        "availId"
      ],
      "additionalProperties":  false,
      "properties": {
        "originAvailDuration": {
          "$id": "#/properties/avail/originAvailDuration",
          "type": "number",
          "description": "The duration of the avail as specified in the content stream from the origin (<code>CUE_OUT</code> or <code>SCTE</code>)."
        },
        "filledDuration": {
          "$id": "#/properties/avail/filledDuration",
          "type": "number",
          "description": "The sum of the durations of all the ads inserted into the avail."
        },
        "fillRate": {
          "$id": "#/properties/avail/fillRate",
          "type": "number",
          "description": "The rate at which the ads fill the avail duration, from 0.0 (for 0%) to 1.0 (for 100%)."
        },
        "driftMillisecondsAtAvailStart": {
          "$id": "#/properties/avail/driftMillisecondsAtAvailStart",
          "type": "number",
          "description": "The cumulative drift at the beginning of this avail. A positive value implies that we are moving away from the live edge, a negative value implies that we are moving towards the live edge."
        },
        "creativeAds": {
          "$id": "#/properties/avail/creativeAds",
          "type": "array",
          "description": "The ads that MediaTailor inserted into the avail.",
          "items": {
            "type": "object",
            "title": "creativeAd",
            "description": "Information about a single inserted ad.",
            "required": [
              "uri",
              "creativeUniqueId",
              "adSystem",
              "adContent",
              "trackingEvents",
              "vastDuration",
              "transcodedAdDuration"
            ],
            "additionalProperties": false,
            "properties": {
              "uri": { "$ref": "#/definitions/adMezzanineUri" },
              "creativeUniqueId": { "$ref": "#/definitions/creativeUniqueId" },
              "adSystem": { "$ref": "#/definitions/adSystem" },
              "adContent": { "$ref": "#/definitions/adContent" },
              "trackingEvents": { "$ref": "#/definitions/trackingEvents" },
              "vastDuration": { "$ref": "#/definitions/vastDuration" },
              "transcodedAdDuration": { "$ref": "#/definitions/transcodedAdDuration" }
            }
          }
        },
        "numAds": {
          "$id": "#/properties/avail/numAds",
          "type": "number",
          "description": "The number of ads that MediaTailor inserted into the avail."
        },
        "slateAd": {
          "$id": "#/properties/avail/slateAd",
          "type": ["object", "null"],
          "title": "slateAd",
          "description": "Information about the slate ad, which MediaTailor uses to fill any unfilled segments in the avail.",
          "additionalProperties": false,
          "required": [
            "uri",
            "creativeUniqueId",
            "adContent",
            "transcodedAdDuration"
          ],
          "properties": {
            "uri": { "$ref": "#/definitions/adMezzanineUri" },
            "creativeUniqueId": { "$ref": "#/definitions/creativeUniqueId" },
            "adContent": { "$ref": "#/definitions/adContent" },
            "transcodedAdDuration": { "$ref": "#/definitions/transcodedAdDuration" }
          }
        },
        "availId": {
          "$id": "#/properties/avail/availId",
          "type": "string",
          "description": "The unique identifier for this avail. For HLS, this is the media sequence number where the avail begins. For DASH, this is the period ID."
        },
        "skippedAds": {
          "$id": "#/properties/avail/skippedAds",
          "type": "array",
          "description": "The ads that MediaTailor didn't insert, for reasons like <code>TRANSCODE_IN_PROGRESS</code> and <code>TRANSCODE_ERROR</code>.",
          "items": {
            "type": "object",
            "title": "skippedAd",
            "description": "Information about a single skipped ad.",
            "required": [
              "creativeUniqueId",
              "adMezzanineUrl",
              "skippedReason",
              "vastDuration"
            ],
            "additionalProperties": false,
            "properties": {
              "creativeUniqueId": { "$ref": "#/definitions/creativeUniqueId" },
              "adMezzanineUrl": {
                "type": "string",
                "description": "The mezzanine URL of the skipped ad."
              },
              "skippedReason": {
                "type": "string",
                "description": "The code that indicates why the ad wasn't inserted. Example: <code>TRANSCODE_IN_PROGRESS</code>."
              },
              "vastDuration": { "$ref": "#/definitions/vastDuration" },
              "transcodedAdDuration": { "$ref": "#/definitions/transcodedAdDuration" },
              "targetVariant": {
                "type": "object",
                "title": "targetVariant",
                "description": "The target variant of the source content. This key is present when an ad wasn't inserted due to the source content containing a variant that could not match to any variants present in this ad.",
                "required": [
                  "mediaProtocol",
                  "mediaType",
                  "bitrate",
                  "mediaResolution",
                  "codecs"
                ],
                "additionalProperties": false,
                "properties": {
                  "mediaProtocol": {
                    "type": "string",
                    "description": "The media protocol of this variant, such as HLS.",
                    "enum": [
                      "HLS",
                      "DASH"
                    ]
                  },
                  "mediaType": {
                    "type": "array",
                    "description": "The media type of this variant, such as VIDEO.",
                    "items": {
                      "type": "string",
                      "enum": [
                        "VIDEO",
                        "AUDIO",
                        "SUBTITLES",
                        "TRICK_PLAY"
                      ],
                      "description": "Media type, such as VIDEO."
                    }
                  },
                  "bitrate": {
                    "$ref": "#/definitions/bitrate"
                  },
                  "mediaResolution": {
                    "type": "object",
                    "title": "mediaResolution",
                    "description": "The media resolution of this variant.",
                    "required": [
                      "width",
                      "height"
                    ],
                    "additionalProperties": false,
                    "properties": {
                      "width": {
                        "$ref": "#/definitions/width"
                      },
                      "height": {
                        "$ref": "#/definitions/height"
                      }
                    }
                  },
                  "codecs": {
                    "type": "array",
                    "description": "The codecs of this variant.",
                    "items": {
                      "type": "string",
                      "description": "Codec, such as avc1."
                    }
                  }
                }
              }
            }
          }
        },
        "adBreakTrackingEvents": {
          "$id": "#properties/avail/adBreakTrackingEvents",
          "type": "object",
          "title": "adBreakTrackingEvents",
          "description": "VMAP/ad break tracking events and corresponding URL",
          "properties": {
            "items": {
              "$ref": "#/definitions/adBreakTrackingEvents"
            }
          }
        }
      }
    },

    "vastResponse": {
      "$id": "#/properties/vastResponse",
      "type": "object",
      "title": "vastResponse",
      "description": "Information about the VAST response that MediaTailor received from the ADS.",
      "required": [
        "version",
        "vastAds",
        "errors",
        "nonLinearAdsList"
      ],
      "additionalProperties":  false,
      "properties": {
        "version": {
          "$id": "#/properties/vastResponse/version",
          "type": "string",
          "description": "The VAST specification version, parsed from the <code>version</code> attribute of the <code>VAST</code> tag in the response.",
          "examples": [
            "3.0"
          ],
          "pattern": "^(.*)$"
        },
        "vastAds": {
          "$id": "#/properties/vastResponse/vastAds",
          "type": "array",
          "description": "The ads parsed from the VAST response.",
          "items": {
            "$ref": "#/definitions/vastAd"
          }
        },
        "errors": {
          "$id": "#/properties/vastResponse/errors",
          "type": "array",
          "description": "The error URLs parsed from the <code>Error</code> tags in the VAST response.",
          "items": {
            "type": "string",
            "description": "A single error URL."
          }
        },
        "nonLinearAdsList": {
          "$id": "#/properties/vastResponse/nonLinearAds",
          "type": "array",
          "description": "A list of NonLinearAds as they are read from the VAST response.",
          "items": {
            "$ref": "#/definitions/nonLinearAds"
          }
        }
      }
    },

    "vastAd": {
      "$ref": "#/definitions/vastAd"
    },

    "vodVastResponseTimeOffset": {
      "$id": "#/properties/vodVastResponseTimeOffset",
      "type": "number",
      "description": "The VMAP specific time offset for VOD ad insertion.",
      "examples": [
        5.0
      ]
    },

    "vodCreativeOffsets": {
      "$id": "#/properties/vodCreativeOffsets",
      "type": "object",
      "title": "vodCreativeOffsets",
      "description": "A map that indicates the time offsets in the manifest where MediaTailor will insert avails, based on the VMAP response.",
      "additionalProperties": {
        "type": "array",
        "$id": "#/properties/vodCreativeOffsets/entry",
        "description": "A mapping from a time offset in the manifest to a list of ads to insert at this time.",
        "items": {
          "type": "object",
          "$id": "#/properties/vodCreativeOffsets/entry/items",
          "title": "vodCreativeOffset",
          "description": "The list of ads to insert at the specified time offset.",
          "additionalProperties": false,
          "required": [
            "uri",
            "creativeUniqueId",
            "vastDuration",
            "transcodedAdDuration",
            "adContent",
            "trackingEvents"
          ],
          "properties": {
            "uri": { "$ref": "#/definitions/adMezzanineUri" },
            "creativeUniqueId": { "$ref": "#/definitions/creativeUniqueId" },
            "vastDuration": { "$ref": "#/definitions/vastDuration" },
            "transcodedAdDuration": { "$ref": "#/definitions/transcodedAdDuration" },
            "adContent": { "$ref": "#/definitions/adContent" },
            "trackingEvents": { "$ref": "#/definitions/trackingEvents" }
          }
        }
      }
    },

    "adsRequestUrl": {
      "$id": "#/properties/adsRequestUrl",
      "type": "string",
      "description": "The full URL of the ADS request made by MediaTailor."
    },
    "adMarkers": {
      "$id": "#/properties/adMarkers",
      "type": "string",
      "description": "Found Ad Marker in the Manifest."
    },
    "segmentationUpid": {
      "$id": "#/properties/segmentationUpid",
      "type": "string",
      "description": "Value of segmentation upid parsed from ad markers in manifest."
    },
    "segmentationTypeId": {
      "$id": "#/properties/segmentationTypeId",
      "type": "integer",
      "description": "Value of segmentation typeId parsed from ad markers in manifest."
    },
    "requestHeaders": {
      "$id": "#/properties/requestHeaders",
      "type": "array",
      "description": "The headers that MediaTailor included with the ADS request. Typically, the logs include these when a request to the ADS fails, to help with troubleshooting.",
      "items": {
        "type": "object",
        "title": "requestheaders",
        "description": "The name and value for a single header included in the ADS request.",
        "required": [
          "name",
          "value"
        ],
        "additionalProperties": false,
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the header."
          },
          "value": {
            "type": "string",
            "description": "The value of the header."
          }
        }
      }
    },

    "originalTargetUrl": {
      "$id": "#/properties/originalTargetUrl",
      "type": "string",
      "description": "The old URL to which MediaTailor was going to make a request."
    },
    "prefetchScheduleName": {
      "$id": "#/properties/prefetchScheduleName",
      "type": "string",
      "description": "The name of the prefetch schedule associated with this ad event.",
      "examples": [
        "PrefetchScheduleName"
      ],
      "pattern": "^(.*)$"
    },
    "updatedTargetUrl": {
      "$id": "#/properties/updatedTargetUrl",
      "type": "string",
      "description": "The new URL to which MediaTailor is making a request."
    },

    "rawAdsResponse": {
      "$id": "#/properties/rawAdsResponse",
      "type": "string",
      "description": "Paginated ADS response as it's exactly returned to MediaTailor."
    },
    "rawAdsResponseIndex": {
      "$id": "#/properties/rawAdsResponseIndex",
      "type": "integer",
      "description": "Integer value denoting this rawAdsResponse's index into the full ADS response. This value is used to order the paginated messages for this ADS response."
    },

    "eventId": {
      "$id": "#/properties/eventId",
      "type": "string",
      "description": "Unique identifier per hook invocation. Use this field to correlate hook-level and function-level events for the same execution.",
      "examples": [
        "5dc6f040-0f72-4e8c-a64e-25eeef62708c"
      ]
    },
    "functionId": {
      "$id": "#/properties/functionId",
      "type": "string",
      "description": "The identifier of the function. On hook events, this is the function configured on the hook. On function events, this is the individual function within the executor.",
      "examples": [
        "my_first_function"
      ]
    },
    "functionType": {
      "$id": "#/properties/functionType",
      "type": "string",
      "enum": [
        "CUSTOM_OUTPUT",
        "HTTP_REQUEST",
        "SEQUENTIAL_EXECUTOR",
        "CONCURRENT_EXECUTOR"
      ],
      "description": "The type of function."
    },
    "executionTimeMs": {
      "$id": "#/properties/executionTimeMs",
      "type": "integer",
      "description": "Execution time in milliseconds."
    },
    "status": {
      "$id": "#/properties/status",
      "type": "string",
      "enum": [
        "SUCCESS",
        "ERROR"
      ],
      "description": "Hook execution outcome. Present on HOOK_SUMMARY events only."
    },
    "errorType": {
      "$id": "#/properties/errorType",
      "type": "string",
      "enum": [
        "INTERNAL_ERROR",
        "SYNTAX_ERROR",
        "RESOURCE_LIMIT_ERROR",
        "RESTRICTION_ERROR",
        "TIMEOUT_ERROR",
        "VALIDATION_ERROR"
      ],
      "description": "Structured error classification. Present on error events only."
    },
    "cause": {
      "$id": "#/properties/cause",
      "type": "string",
      "description": "Error detail string describing the specific failure."
    },
    "input": {
      "$id": "#/properties/input",
      "type": "object",
      "description": "Before-values of variables targeted by output expressions."
    },
    "output": {
      "$id": "#/properties/output",
      "type": "object",
      "description": "Values produced by the function. Present on FUNCTION_COMPLETED events only."
    },
    "http": {
      "$id": "#/properties/http",
      "type": "object",
      "description": "HTTP request and response details for HTTP_REQUEST functions.",
      "properties": {
        "request": {
          "type": "object",
          "description": "The HTTP request details.",
          "properties": {
            "url": { "type": "string", "description": "The request URL." },
            "method": { "type": "string", "description": "The HTTP method." },
            "headers": {
              "type": "array",
              "description": "The request headers.",
              "items": {
                "type": "object",
                "properties": {
                  "name": { "type": "string" },
                  "value": { "type": "string" }
                }
              }
            },
            "body": { "type": ["string", "null"], "description": "The request body." }
          }
        },
        "responseTimeMs": { "type": ["integer", "null"], "description": "HTTP response time in milliseconds." },
        "response": {
          "type": ["object", "null"],
          "description": "The HTTP response details. Null when the server was never reached.",
          "properties": {
            "statusCode": { "type": ["integer", "null"], "description": "The HTTP status code. Null when the server was never reached." },
            "headers": {
              "type": ["array", "null"],
              "description": "The response headers.",
              "items": {
                "type": "object",
                "properties": {
                  "name": { "type": "string" },
                  "value": { "type": "string" }
                }
              }
            },
            "body": { "type": ["string", "null"], "description": "The response body." }
          }
        },
        "truncated": { "type": "boolean", "description": "True when request or response body was truncated to fit within log event size limits." }
      }
    }
  },

  "__COMMENT_oneOf": "The oneOf section defines subtypes for our events. Subtypes can have different rules, including which fields are required. For more information, see https://json-schema.org/understanding-json-schema/reference/combining.html#oneof ",

  "oneOf": [
    { "$ref": "#/definitions/eventAdMarkersFound" },
    { "$ref": "#/definitions/eventNonAdMarkerFound" },
    { "$ref": "#/definitions/eventMakingAdsRequest" },
    { "$ref": "#/definitions/eventModifiedTargetUrl" },
    { "$ref": "#/definitions/eventRawAdsResponse" },
    { "$ref": "#/definitions/eventVastResponse" },
    { "$ref": "#/definitions/eventFilledAvail" },
    { "$ref": "#/definitions/eventFilledOverlayAvail" },
    { "$ref": "#/definitions/eventErrorFiringBeaconFailed" },
    { "$ref": "#/definitions/eventWarningNoAdvertisements" },
    { "$ref": "#/definitions/eventUnknownHost" },
    { "$ref": "#/definitions/eventErrorAdsTimeout" },
    { "$ref": "#/definitions/eventErrorVastMissingOverlays" },
    { "$ref": "#/definitions/eventPlannedAvail" },
    { "$ref": "#/definitions/eventEmptyVastResponse" },
    { "$ref": "#/definitions/eventEmptyVmapResponse" },
    { "$ref": "#/definitions/eventErrorUnknown" },
    { "$ref": "#/definitions/eventVastRedirect" },
    { "$ref": "#/definitions/eventRedirectedVastResponse" },
    { "$ref": "#/definitions/eventErrorAdsMissingImpression" },
    { "$ref": "#/definitions/eventErrorAdsResponseParse" },
    { "$ref": "#/definitions/eventErrorAdsInvalidResponse" },
    { "$ref": "#/definitions/eventErrorDisallowedHost"},
    { "$ref": "#/definitions/eventPersonalizationDisabled"},
    { "$ref": "#/definitions/eventWarningDynamicVariableSubFailed"},
    { "$ref": "#/definitions/eventVodTimeBasedAvailPlanVastResponseForOffset" },
    { "$ref": "#/definitions/eventVodTimeBasedAvailPlanSuccess" },
    { "$ref": "#/definitions/eventPreAdsRequestHookSummary" },
    { "$ref": "#/definitions/eventPreAdsRequestHookError" },
    { "$ref": "#/definitions/eventPreAdsRequestFunctionCompleted" },
    { "$ref": "#/definitions/eventPreAdsRequestFunctionError" }
  ],

  "definitions": {
    "eventAdMarkersFound": {
      "$id": "#/definitions/eventAdMarkersFound",
      "required": [
        "eventType",
        "adMarkers"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "AD_MARKER_FOUND"
        }
      }
    },
    "eventNonAdMarkerFound": {
      "$id": "#/definitions/eventNonAdMarkerFound",
      "required": [
        "eventType",
        "adMarkers"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "NON_AD_MARKER_FOUND"
        }
      }
    },
    "eventMakingAdsRequest": {
      "$id": "#/definitions/eventMakingAdsRequest",
      "required": [
        "eventType",
        "adsRequestUrl"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "MAKING_ADS_REQUEST"
        }
      }
    },

    "eventModifiedTargetUrl": {
      "$id": "#/definitions/eventModifiedTargetUrl",
      "required": [
        "eventType",
        "originalTargetUrl",
        "updatedTargetUrl"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "MODIFIED_TARGET_URL"
        }
      }
    },

    "eventRawAdsResponse": {
      "$id": "#/definitions/eventRawAdsResponse",
      "required": [
        "eventType",
        "rawAdsResponse",
        "rawAdsResponseIndex"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "RAW_ADS_RESPONSE"
        }
      }
    },

    "eventVastResponse": {
      "$id": "#/definitions/eventVastResponse",
      "_comment": "NOTE: the vastResponse property should ideally be marked as a required field for this event, but unfortunately, in the case of an empty vast response, we currently emit an EMPTY_VAST_RESPONSE followed by a VAST_RESPONSE, and the vastResponse property is not present in the latter. We need to fix this so that we don't emit both of those events in the empty response case, and update this schema to flag vastResponse as required for VAST_RESPONSE.",
      "required": [
        "eventType"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "VAST_RESPONSE"
        }
      }
    },

    "eventFilledAvail": {
      "$id": "#/definitions/eventFilledAvail",
      "required": [
        "eventType",
        "avail"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "FILLED_AVAIL"
        }
      }
    },

    "eventFilledOverlayAvail": {
      "$id": "#/definitions/eventFilledOverlayAvail",
      "required": [
        "eventType",
        "avail"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "FILLED_OVERLAY_AVAIL"
        }
      }
    },

    "eventErrorVastMissingOverlays": {
      "$id": "#/definitions/eventErrorVastMissingOverlays",
      "required": [
        "eventType",
        "adsRequestUrl",
        "requestHeaders"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "ERROR_VAST_MISSING_OVERLAYS"
        }
      }
    },

    "eventErrorFiringBeaconFailed": {
      "$id": "#/definitions/eventErrorFiringBeaconFailed",
      "required": [
        "eventType",
        "error",
        "beaconInfo"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "ERROR_FIRING_BEACON_FAILED"
        }
      }
    },

    "eventWarningNoAdvertisements": {
      "$id": "#/definitions/eventWarningNoAdvertisements",
      "required": [
        "eventType"
      ],
      "_comment": "We should really have a more descriptive error field for these events",
      "properties": {
        "eventType": {
          "type": "string",
          "const": "WARNING_NO_ADVERTISEMENTS"
        }
      }
    },

    "eventUnknownHost": {
      "$id": "#/definitions/eventUnknownHost",
      "required": [
        "eventType",
        "requestHeaders"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "ERROR_UNKNOWN_HOST"
        }
      }
    },

    "eventErrorAdsTimeout": {
      "$id": "#/definitions/eventErrorAdsTimeout",
      "required": [
        "eventType",
        "adsRequestUrl",
        "requestHeaders"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "ERROR_ADS_TIMEOUT"
        }
      }
    },

    "eventPlannedAvail": {
      "$id": "#/definitions/eventPlannedAvail",
      "required": [
        "eventType"
      ],
      "_comment": "TODO: Flesh this out as we implement it",
      "properties": {
        "eventType": {
          "type": "string",
          "const": "PLANNED_AVAIL"
        }
      }
    },

    "eventEmptyVastResponse": {
      "$id": "#/definitions/eventEmptyVastResponse",
      "required": [
        "eventType"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "EMPTY_VAST_RESPONSE"
        }
      }
    },

    "eventEmptyVmapResponse": {
      "$id": "#/definitions/eventEmptyVmapResponse",
      "required": [
        "eventType"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "EMPTY_VMAP_RESPONSE"
        }
      }
    },

    "eventErrorUnknown": {
      "$id": "#/definitions/eventErrorUnknown",
      "required": [
        "eventType"
      ],
      "_comment": "TODO: we should have a field for the exception message or something",
      "properties": {
        "eventType": {
          "type": "string",
          "const": "ERROR_UNKNOWN"
        }
      }
    },

    "eventVastRedirect": {
      "$id": "#/definitions/eventVastRedirect",
      "required": [
        "eventType"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "VAST_REDIRECT"
        }
      }
    },

    "eventRedirectedVastResponse": {
      "$id": "#/definitions/eventRedirectedVastResponse",
      "required": [
        "eventType"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "REDIRECTED_VAST_RESPONSE"
        }
      },
      "_comment": "NOTE that the property vastResponse is not required because empty vast responses do not contain a vastResponse."
    },

    "eventErrorAdsResponseParse": {
      "$id": "#/definitions/eventErrorAdsResponseParse",
      "required": [
        "eventType"
      ],
      "_comment": "We should have a field with an error message here",
      "properties": {
        "eventType": {
          "type": "string",
          "const": "ERROR_ADS_RESPONSE_PARSE"
        }
      }
    },

    "eventErrorAdsInvalidResponse": {
      "$id": "#/definitions/eventErrorAdsInvalidResponse",
      "required": [
        "eventType",
        "additionalInfo"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "ERROR_ADS_INVALID_RESPONSE"
        }
      }
    },

    "eventErrorAdsMissingImpression": {
      "$id": "#/definitions/eventErrorAdsMissingImpression",
      "required": [
        "eventType"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "ERROR_VAST_MISSING_IMPRESSION"
        }
      }
    },

    "eventErrorDisallowedHost": {
      "$id": "#/definitions/eventErrorDisallowedHost",
      "required": [
        "eventType"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "ERROR_DISALLOWED_HOST"
        }
      }
    },

    "eventPersonalizationDisabled": {
      "$id": "#/definitions/eventPersonalizationDisabled",
      "required": [
        "eventType"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "ERROR_PERSONALIZATION_DISABLED"
        }
      }
    },

    "eventWarningDynamicVariableSubFailed": {
      "$id": "#/definitions/eventWarningDynamicVariableSubFailed",
      "required": [
        "eventType",
        "adsRequestUrl"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "WARNING_URL_VARIABLE_SUBSTITUTION_FAILED"
        }
      }
    },

    "eventVodTimeBasedAvailPlanVastResponseForOffset": {
      "$id": "#/definitions/eventVodTimeBasedAvailPlanVastResponseForOffset",
      "required": [
        "eventType",
        "vastResponse"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "VOD_TIME_BASED_AVAIL_PLAN_VAST_RESPONSE_FOR_OFFSET"
        }
      }
    },

    "eventVodTimeBasedAvailPlanSuccess": {
      "$id": "#/definitions/eventVodTimeBasedAvailPlanSuccess",
      "required": [
        "eventType",
        "vodCreativeOffsets"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "VOD_TIME_BASED_AVAIL_PLAN_SUCCESS"
        }
      }
    },

    "creativeUniqueId": {
      "type": "string",
      "description": "The unique identifier for the ad, used as a key for transcoding. This is the ID field for the creative in the VAST response, if available. Otherwise, it's the mezzanine URL of the ad. "
    },

    "adSystem": {
      "type": "string",
      "description": "The value of the <code>AdSystem</code> tag in the VAST response. "
    },

    "vastDuration": {
      "type": "number",
      "description": "The duration of the ad, as parsed from the VAST response."
    },

    "transcodedAdDuration": {
      "type": "number",
      "description": "The duration of the ad, calculated from the transcoded asset."
    },

    "adContent": {
      "$id": "#/properties/adContent",
      "type": ["object", "null"],
      "title": "adContent",
      "description": "Information about the content of the inserted ad.",
      "additionalProperties": false,
      "properties": {
        "adPlaylistUris": {
          "$id": "#/properties/adContent/adPlaylistUris",
          "type": "object",
          "title": "adPlaylistUris",
          "description": "The mapping from the origin manifest for a variant to the ad manifest for the variant. For DASH, this contains a single entry, because all variants are represented in a single DASH manifest. ",
          "additionalProperties": {
            "$id": "#/properties/adContent/adPlaylistUris/adPlaylistUri",
            "type": "string",
            "description": "The URL of the ad manifest for the specific variant."
          }
        }
      }
    },

    "adMezzanineUri": {
      "type": "string",
      "description": "The URL of the mezzanine version of the ad, which is the input to the transcoder."
    },

    "bitrate": {
      "type": "integer",
      "examples": [
        533
      ],
      "description": "The bitrate."
    },
    "width": {
      "type": "integer",
      "examples": [
        1280
      ],
      "description": "Width in pixels."
    },
    "height": {
      "type": "integer",
      "examples": [
        720
      ],
      "description": "Height in pixels."
    },

    "trackingEvents": {
      "type": "object",
      "title": "trackingEvents",
      "description": "The tracking beacon URLs for the various tracking events for the ad. The keys are the event names, and the values are a list of beacon URLs.",

      "additionalProperties":  {
        "type": "array",
        "description": "The list of beacon URLs for the specified tracking event (impression, complete, and so on)",
        "items": {
          "type": "string",
          "description": "The beacon URLs for this tracking event."
        }
      }
    },

    "nonLinearAds": {
      "$id": "#/properties/nonLinearAds",
      "type": "object",
      "title": "nonLinearAds",
      "description": "A NonLinearAds as it appears in the VAST response.",
      "required": [
        "nonLinearAdList",
        "nonLinearTrackingEvents"
      ],
      "properties": {
        "nonLinearAdList": {
          "type": "array",
          "description": "List of non linear ads as they exist within one NonLinearAds.",
          "items": {
            "type": "object",
            "title": "nonLinearAdList",
            "description": "List of NonLinearAd as they are parsed from its parent NonLinearAds.",
            "properties": {
              "nonLinearAdId": {
                "type": "string",
                "description": "Ad ID of this non linear ad."
              },
              "nonLinearAdSystem": {
                "type": "string",
                "description": "Ad system of this non linear ad's parent Inline ad."
              },
              "nonLinearAdTitle": {
                "type": "string",
                "description": "Ad title of this non linear ad's parent Inline ad."
              },
              "nonLinearCreativeId": {
                "type": "string",
                "description": "Creative ID of this non linear ad's parent Creative ad."
              },
              "nonLinearCreativeAdId": {
                "type": "string",
                "description": "Creative ad ID of this non linear ad."
              },
              "nonLinearCreativeSequence": {
                "type": "string",
                "description": "Creative sequence of this non linear ad."
              },
              "nonLinearWidth": {
                "type": "string",
                "description": "Width of this non linear ad."
              },
              "nonLinearHeight": {
                "type": "string",
                "description": "Height of this non linear ad."
              },
              "nonLinearExpandedWidth": {
                "type": "string",
                "description": "Expanded width of this non linear ad."
              },
              "nonLinearExpandedHeight": {
                "type": "string",
                "description": "Expanded height of this non linear ad."
              },
              "nonLinearScalable": {
                "type": "boolean",
                "description": "Boolean denoting if this non linear ad is scalable."
              },
              "nonLinearMaintainAspectRatio": {
                "type": "boolean",
                "description": "Boolean denoting if aspect ratio should be maintained for this non linear ad."
              },
              "nonLinearMinSuggestedDuration": {
                "type": "string",
                "description": "Min suggested duration for this non linear ad."
              },
              "nonLinearApiFramework": {
                "type": "string",
                "description": "API framework for this non linear ad's parent Inline ad."
              },
              "nonLinearStaticResource": {
                "type": "string",
                "description": "Static resource for this non linear ad."
              },
              "nonLinearStaticResourceCreativeType": {
                "type": "string",
                "description": "Static Resource creative type for this non linear ad."
              },
              "nonLinearIFrameResource": {
                "type": "string",
                "description": "I-Frame resource for this non linear ad."
              },
              "nonLinearHtmlResource": {
                "type": "string",
                "description": "HTML resource for this non linear ad."
              },
              "nonLinearAdParameters": {
                "type": "string",
                "description": "Ad parameters for this non linear ad."
              },
              "nonLinearClickThrough": {
                "type": "string",
                "description": "Click Through data for this non linear ad."
              },
              "nonLinearClickTracking": {
                "type": "string",
                "description": "Click Tracking data for this non linear ad."
              },
              "nonLinearClickTrackingId": {
                "type": "string",
                "description": "Click Tracking ID for this non linear ad."
              }
            }
          }
        },
        "nonLinearTrackingEvents": { "$ref": "#/definitions/trackingEvents" },
        "extensions": {
          "$id": "#/properties/nonLinearAds/extensions",
          "type": "array",
          "description": "Extensions that exist for this NonLinearAds.",
          "items": {
            "$id": "#/properties/nonLinearAds/extensions/items",
            "type": "object",
            "title": "Extensions",
            "description": "Extensions found in non linear ads",
            "additionalProperties":  false,
            "properties": {
              "extensionType": {
                "$id": "#/properties/nonLinearAds/extensions/extensionType",
                "type": "string",
                "description": "The value of the extension type attribute of the <code>Extensions</code> tag.",
                "examples": [
                  "FreeWheel"
                ]
              },
              "extensionContent": {
                "$id": "#/properties/nonLinearAds/extensions/extensionContent",
                "type": "string",
                "description": "The extension content attribute of the <code>Extensions</code> tag.",
                "examples": [
                  "progressive"
                ]
              }
            }
          }
        }
      }
    },
    "adBreakTrackingEvents": {
      "$id": "#/properites/adBreakTrackingEvents",
      "type": "object",
      "title": "adBreakTrackingEvents",
      "description": "These are all VMAP ad break tracking events.",
      "additionalProperties": {
        "type": "array",
        "description": "VMAP/ad break tracking events and corresponding URL",
        "items": {
          "type": "string",
          "description": "The beacon URLs for this tracking event."
        }
      }
    },
    "vastAd": {
      "$id": "#/properties/vastAd",
      "type": "object",
      "title": "vastAd",
      "description": "Information about a single ad parsed from the VAST response.",
      "required": [
        "vastAdId",
        "adSystem",
        "adTitle",
        "creativeId",
        "creativeAdId",
        "duration",
        "vastMediaFiles",
        "trackingEvents"
      ],
      "additionalProperties":  false,
      "properties": {
        "vastAdId": {
          "$id": "#/properties/vastAd/vastAdId",
          "type": "string",
          "description": "The value of the id attribute of the <code>Ad</code> tag in the VAST response",
          "examples": [
            "ad1"
          ]
        },
        "adSystem": {"$ref": "#/definitions/adSystem" } ,
        "adTitle": {
          "$id": "#/properties/vastAd/adTitle",
          "type": "string",
          "description": "The media files that are available for the ad in the VAST response.",
          "examples": [
            "External NCA1C1L1 LinearInlineSkippable"
          ]
        },
        "creativeId": {
          "$id": "#/properties/vastAd/creativeId",
          "type": "string",
          "description": "The value of the id attribute of the <code>Creative</code> tag in the VAST response.",
          "examples": [
            "creative1"
          ]
        },
        "creativeAdId": {
          "$id": "#/properties/vastAd/creativeAdId",
          "type": "string",
          "description": "The value of the adId attribute of the <code>Creative</code> tag in the VAST response."
        },
        "duration": {
          "$id": "#/properties/vastAd/duration",
          "type": "number",
          "description": "The approximate duration of the ad, based on the <code>duration</code> tag in the <code>linear</code> element of the VAST response.",
          "examples": [
            30,
            30.0
          ]
        },
        "vastMediaFiles": {
          "$id": "#/properties/vastAd/vastMediaFiles",
          "type": "array",
          "description": "The list of available media files for the ad in the VAST response.",
          "items": {
            "$id": "#/properties/vastAd/vastMediaFiles/items",
            "type": "object",
            "title": "vastMediaFile",
            "description": "Information about a media file for the ad.",
            "required": [
              "uri",
              "id",
              "delivery",
              "type",
              "apiFramework",
              "width",
              "height",
              "bitrate"
            ],
            "additionalProperties":  false,
            "properties": {
              "uri": { "$ref": "#/definitions/adMezzanineUri" },
              "id": {
                "$id": "#/properties/vastAd/vastMediaFiles/items/properties/id",
                "type": "string",
                "description": "The value of the id attribute of the <code>MediaFile</code> tag.",
                "examples": [
                  "GDFP"
                ]
              },
              "delivery": {
                "$id": "#/properties/vastAd/vastMediaFiles/items/properties/delivery",
                "type": "string",
                "description": "The protocol used for the media file, set to either progressive or streaming.",
                "examples": [
                  "progressive"
                ]
              },
              "type": {
                "$id": "#/properties/vastAd/vastMediaFiles/items/properties/type",
                "type": "string",
                "description": "The MIME type of the media file, taken from the type attribute of the <code>MediaFile</code> tag.",
                "examples": [
                  "video/mp4"
                ]
              },
              "apiFramework": {
                "$id": "#/properties/vastAd/vastMediaFiles/items/properties/apiFramework",
                "type": "string",
                "description": "The API framework needed to manage the media file. Example: <code>VPAID</code>."
              },
              "width": {
                "$ref": "#/definitions/width"
              },
              "height": {
                "$ref": "#/definitions/height"
              },
              "bitrate": {
                "$ref": "#/definitions/bitrate"
              }
            }
          }
        },
        "trackingEvents": { "$ref": "#/definitions/trackingEvents" },
        "vastAdTagUri": {
          "$id": "#/properties/vastAd/vastAdTagUri",
          "type": "string",
          "description": "The VMAP-specific redirect URI for an ad.",
          "examples": [
            "https://ads.redirect.com/redirect1"
          ]
        }
      }
    },

    "eventPreAdsRequestHookSummary": {
      "$id": "#/definitions/eventPreAdsRequestHookSummary",
      "required": [
        "eventType",
        "eventId",
        "functionId",
        "executionTimeMs",
        "status"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "PRE_ADS_REQUEST_HOOK_SUMMARY"
        }
      }
    },

    "eventPreAdsRequestHookError": {
      "$id": "#/definitions/eventPreAdsRequestHookError",
      "required": [
        "eventType",
        "eventId",
        "functionId",
        "executionTimeMs",
        "errorType",
        "cause"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "PRE_ADS_REQUEST_HOOK_ERROR"
        }
      }
    },

    "eventPreAdsRequestFunctionCompleted": {
      "$id": "#/definitions/eventPreAdsRequestFunctionCompleted",
      "required": [
        "eventType",
        "eventId",
        "functionId",
        "functionType",
        "executionTimeMs"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "PRE_ADS_REQUEST_FUNCTION_COMPLETED"
        }
      }
    },

    "eventPreAdsRequestFunctionError": {
      "$id": "#/definitions/eventPreAdsRequestFunctionError",
      "required": [
        "eventType",
        "eventId",
        "functionId",
        "functionType",
        "executionTimeMs",
        "errorType",
        "cause"
      ],
      "properties": {
        "eventType": {
          "type": "string",
          "const": "PRE_ADS_REQUEST_FUNCTION_ERROR"
        }
      }
    }
  }
}
```