

# Filtering AWS Elemental MediaTailor logs and events
<a name="logs-filter"></a>

Logs emitted from a playback configuration in MediaTailor include information about a variety of activities that happen during the playback session. These activities are identified in the event type of the logs. Many events are logged by default. To help control the cost of logs in Amazon CloudWatch, you can specify the logs that MediaTailor emits. 

MediaTailor provides you control over log filtering so you can do the following:
+ Specify the log events that you want to exclude from logs
+ Enable logging raw responses from the ad decision server (ADS)

You can set these log filtering preferences independently for each playback session, or as a default for all playback sessions for a playback configuration. 
+ To filter logs on a per-session basis, include query parameters in the playback session initialization request.
+ To filter logs on a per-playback configuration basis, use the MediaTailor console or API to indicate your preferences in the playback configuration settings. 

The following sections provide instruction for enabling log filtering on sessions and playback configurations.