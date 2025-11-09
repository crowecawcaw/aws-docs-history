# MediaTailor ad skipping reference

guide

This section provides comprehensive reference information about ad skip reasons and
links to related documentation for AWS Elemental MediaTailor. Use this reference guide to understand the
specific meanings of different skip reasons and find additional troubleshooting
resources.

## Complete ad skip reasons

reference

MediaTailor logs specific reasons why ads are skipped in the `FILLED_AVAIL`
event log message from the `MediaTailor/AdDecisionServerInteractions` log
group.

| Complete ad skip reasons            | Skip reason                                                                                                                                     | Description |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `NEW_CREATIVE`                      | The ad has not been transcoded yet. This occurs when MediaTailor<br>encounters a new ad creative that requires transcoding before<br>insertion. |
| `PROFILE_NOT_FOUND`                 | The MediaConvert transcode profile associated with the session's<br>configuration does not exist, preventing ad preparation.                    |
| `TRANSCODE_ERROR`                   | The ad transcode process encountered an error and failed to<br>complete.                                                                        |
| `TRANSCODE_IN_PROGRESS`             | The ad transcode is still in progress and not yet ready for<br>insertion.                                                                       |
| `INTERNAL_ERROR`                    | An internal MediaTailor error occurred while handling the ad,<br>preventing insertion.                                                          |
| `AVAIL_DURATION_EXCEEDED`           | The ad does not fit within the remaining duration of the ad<br>break.                                                                           |
| `LEFTOVER_AVAIL_EXCEEDED_THRESHOLD` | The cumulative duration of all ads that could have been inserted<br>does not meet the personalization threshold configured for the<br>session.  |
| `VAST_PARSING_ERROR`                | The VAST response from the ad decision server contains errors or<br>is malformed.                                                               |
| `ADS_TIMEOUT`                       | The ad decision server did not respond within the configured<br>timeout period.                                                                 |
| `MEDIA_FILE_UNAVAILABLE`            | The ad media files specified in the VAST response are not<br>accessible.                                                                        |
| `SESSION_INITIALIZATION_FAILED`     | The MediaTailor session failed to initialize properly, often due to<br>incorrect session variables.                                             |
| `EARLY_CUE_IN`                      | The ad break ended earlier than expected due to an early cue-in<br>signal, preventing the ad from being fully inserted.                         |
| `NO_VARIANT_MATCH`                  | The ad creative does not have a variant that matches the content<br>stream's encoding parameters (bitrate, resolution, codec).                  |
| `NO_MODEL_CREATIVE_MATCH`           | The ad creative does not match the expected model or format<br>requirements for the current playback configuration.                             |
| `REJECTED_REPLICA_VAST`             | The VAST response was rejected due to replica or duplicate<br>content detection policies.                                                       |
| `INVALID_VAST_WRAPPER_AD`           | The VAST wrapper ad contains invalid or malformed wrapper<br>elements that prevent successful ad insertion.                                     |
| `IMPORT_ERROR`                      | An error occurred during the ad import process, preventing the ad<br>from being processed for insertion.                                        |
| `IMPORT_IN_PROGRESS`                | The ad import process is currently in progress and has not<br>completed yet.                                                                    |

## Related resources

For more information on troubleshooting ad skipping issues, refer to these related
topics:

- [MediaTailor dynamic ad variables for ADS requests](variables.md "variables.md") - Comprehensive guide to dynamic ad variables
  in MediaTailor
- [Prefetching ads](prefetching-ads.md "prefetching-ads.md") - How to implement ad prefetching to
  prevent transcoding-related skipping
- [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch
  metrics](monitoring-cloudwatch-metrics.md "monitoring-cloudwatch-metrics.md") - Monitoring MediaTailor with
  CloudWatch metrics
- [Viewing AWS Elemental MediaTailor logs](monitoring-through-logs.md "monitoring-through-logs.md") - How to view and analyze MediaTailor
  logs
- [Troubleshooting MediaTailor event flow
  issues](troubleshooting-event-flow.md "troubleshooting-event-flow.md") - Understanding the ad
  insertion event flow
