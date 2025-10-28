# Filtering AWS Elemental MediaTailor logs and events

Logs emitted from a playback configuration in MediaTailor include information about a
variety of activities that happen during the playback session. These activities are
identified in the event type of the logs. Many events are logged by default. To help
control the cost of logs in Amazon CloudWatch, you can specify the logs that MediaTailor emits.

MediaTailor provides you control over log filtering so you can do the following:

- Specify the log events that you want to exclude from logs
- Enable logging raw responses from the ad decision server (ADS)
  You can set these log filtering preferences independently for each playback session,
  or as a default for all playback sessions for a playback configuration.

- To filter logs on a per-session basis, include query parameters in the
  playback session initialization request.
- To filter logs on a per-playback configuration basis, use the MediaTailor console or
  API to indicate your preferences in the playback configuration settings.
  The following sections provide instruction for enabling log filtering on sessions and
  playback configurations.

To define a customized level of log detail for each session, append the
following parameters to your initial server-side or client-side playback session
request. Add values to the parameters to represent the events that you want to
include or exclude, in a comma-delimited format:

- `aws.adsInteractionLogPublishOptInEventTypes` to receive
  logs for specific ad decision server (ADS) interactions.
- `aws.adsInteractionLogExcludeEventTypes` to stop receiving
  logs for specific ADS interactions.
- `aws.manifestServiceLogExcludeEventTypes` to stop receiving
  logs for specific manifest service interactions.
  For a list of log and event types that MediaTailor emits, see [Manifest logs](log-types.md "log-types.md"), [ADS logs](ads-log-format.md "ads-log-format.md"), and [Transcode logs](tm-log-format.md "tm-log-format.md").

If you don't pass through any query parameters for log filtering, MediaTailor writes
all logs to your delivery destination.

###### Example server-side session initialization with log filters

To exclude `GENERATED_MANIFEST` and `PARSING_ERROR`
events from your manifest logs and `MAKING_ADS_REQUEST` from the
ADS logs, the session initialization request would look like this:

```
GET `<mediatailorURL>`/v1/master/`<hashed-account-id>`/`<origin-id>`/index.m3u8?aws.logMode=DEBUG&aws.manifestServiceLogExcludeEventTypes=GENERATED_MANIFEST,PARSING_ERROR&aws.adsInteractionLogExcludeEventTypes=MAKING_ADS_REQUEST
```

To enable raw logs from your ADS, include the
`RAW_ADS_RESPONSE` value for the
`AdsInteractionPublishOptInEventType` parameter:

```
GET `<mediatailorURL>`/v1/master/`<hashed-account-id>`/`<origin-id>`/index.m3u8?aws.adsInteractionPublishOptInEventType=RAW_ADS_RESPONSE
```

###### Example client-side session initialization with log filters

To exclude log events during client-side session initialization, include
`availSuppression` and log-type parameters in your client's
POST request to MediaTailor. For more information about how to construct a
client-side playback session request, see [Client-side ad tracking](ad-reporting-client-side.md "ad-reporting-client-side.md"). The following example
excludes `CONFIG_SECURITY_ERROR` and `PARSING_ERROR`
events from your manifest logs and `MAKING_ADS_REQUEST` from the
ADS logs.

```
POST parent.m3u8
   {
       "adsInteractionLog": {
           ...
           "excludeEventTypes": [
               "MAKING_ADS_REQUEST"
           ]
       },
       "manifestServiceLog": {
           ...
           "excludeEventTypes": [
               "GENERATED_MANIFEST",
               "PARSING_ERROR"
           ]
       },
      "logMode": "DEBUG"
   }
```

To enable raw logs from your ADS, include the `RAW_ADS_RESPONSE` value for the `publishOptInEventTypes` parameter:

```
POST parent.m3u8
   {
       "adsInteractionLog": {
           "publishOptInEventTypes": ["RAW_ADS_RESPONSE"],
           "excludeEventTypes": [
               "MAKING_ADS_REQUEST"
           ]
       },
       "manifestServiceLog": {
           ...
           "excludeEventTypes": [
               "GENERATED_MANIFEST",
               "PARSING_ERROR"
           ]
       },
       "logMode": "DEBUG"
   }
```

Use the playback configuration's settings to define the log event types that
MediaTailor emits as a default from this playback configuration. MediaTailor uses these
default log filtering settings for all sessions that don't include filtering
query parameters on the session init request.

You can choose to do the following:

- Receive logs for specific ad decision server (ADS)
  interactions.
- Exclude logs for specific ADS interactions.
- Exclude logs for specific manifest service interactions.
  To set these settings from the MediaTailor console, see [Creating a
  configuration](configurations-create.md "configurations-create.md"). For the MediaTailor API, see [PutPlaybackConfiguration](../apireference/API_PutPlaybackConfiguration.md "../apireference/API_PutPlaybackConfiguration.md") in the
  _AWS Elemental MediaTailor API Reference_.

For a list of log and event types that MediaTailor emits, see [Manifest logs](log-types.md "log-types.md"), [ADS logs](ads-log-format.md "ads-log-format.md"), and [Transcode logs](tm-log-format.md "tm-log-format.md").
