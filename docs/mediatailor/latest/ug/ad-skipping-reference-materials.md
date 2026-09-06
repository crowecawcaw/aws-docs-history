

# MediaTailor ad skipping reference guide
<a name="ad-skipping-reference-materials"></a>

This section provides comprehensive reference information about ad skip reasons and links to related documentation for AWS Elemental MediaTailor. Use this reference guide to understand the specific meanings of different skip reasons and find additional troubleshooting resources.

## Complete ad skip reasons reference
<a name="complete-skip-reasons-reference"></a>

MediaTailor logs specific reasons why ads are skipped in the `FILLED_AVAIL` event log message from the `MediaTailor/AdDecisionServerInteractions` log group.


**Complete ad skip reasons**  

| Skip reason | Description | 
| --- | --- | 
| NEW\_CREATIVE | The ad has not been transcoded yet. This occurs when MediaTailor encounters a new ad creative that requires transcoding before insertion. | 
| PROFILE\_NOT\_FOUND | The MediaConvert transcode profile associated with the session's configuration does not exist, preventing ad preparation. | 
| TRANSCODE\_ERROR | The ad transcode process encountered an error and failed to complete. | 
| TRANSCODE\_IN\_PROGRESS | The ad transcode is still in progress and not yet ready for insertion. | 
| INTERNAL\_ERROR | An internal MediaTailor error occurred while handling the ad, preventing insertion. | 
| AVAIL\_DURATION\_EXCEEDED | The ad does not fit within the remaining duration of the ad break. | 
| LEFTOVER\_AVAIL\_EXCEEDED\_THRESHOLD | The cumulative duration of all ads that could have been inserted does not meet the personalization threshold configured for the session. | 
| VAST\_PARSING\_ERROR | The VAST response from the ad decision server contains errors or is malformed. | 
| ADS\_TIMEOUT | The ad decision server did not respond within the configured timeout period. | 
| MEDIA\_FILE\_UNAVAILABLE | The ad media files specified in the VAST response are not accessible. | 
| SESSION\_INITIALIZATION\_FAILED | The MediaTailor session failed to initialize properly, often due to incorrect session variables. | 
| EARLY\_CUE\_IN | The ad break ended earlier than expected due to an early cue-in signal, preventing the ad from being fully inserted. | 
| NO\_VARIANT\_MATCH | The ad creative does not have a variant that matches the content stream's encoding parameters (bitrate, resolution, codec). | 
| NO\_MODEL\_CREATIVE\_MATCH | The ad creative does not match the expected model or format requirements for the current playback configuration. | 
| REJECTED\_REPLICA\_VAST | The VAST response was rejected due to replica or duplicate content detection policies. | 
| INVALID\_VAST\_WRAPPER\_AD | The VAST wrapper ad contains invalid or malformed wrapper elements that prevent successful ad insertion. | 
| IMPORT\_ERROR | An error occurred during the ad import process, preventing the ad from being processed for insertion. | 
| IMPORT\_IN\_PROGRESS | The ad import process is currently in progress and has not completed yet. | 

## Related resources
<a name="related-resources"></a>

For more information on troubleshooting ad skipping issues, refer to these related topics:
+ [MediaTailor dynamic ad variables for ADS requests](variables.md) - Comprehensive guide to dynamic ad variables in MediaTailor
+ [Prefetching ads](prefetching-ads.md) - How to implement ad prefetching to prevent transcoding-related skipping
+ [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch metrics](monitoring-cloudwatch-metrics.md) - Monitoring MediaTailor with CloudWatch metrics
+ [Viewing AWS Elemental MediaTailor logs](monitoring-through-logs.md) - How to view and analyze MediaTailor logs
+ [Troubleshooting MediaTailor event flow issues](troubleshooting-event-flow.md) - Understanding the ad insertion event flow