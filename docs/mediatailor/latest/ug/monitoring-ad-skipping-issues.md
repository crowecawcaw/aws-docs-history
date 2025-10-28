# MediaTailor ad skipping monitoring and

alerts

Proactive monitoring helps you detect and resolve ad skipping issues before they
significantly impact your revenue. AWS Elemental MediaTailor provides comprehensive metrics and logging
capabilities that enable effective monitoring of ad insertion performance. This guide
explains how to set up effective monitoring for ad skipping issues.

## Key CloudWatch metrics to monitor

Set up CloudWatch alarms for these key MediaTailor metrics:

- `AdDecisionServer.Ads.Skipped` - Count of skipped ads
- `AdDecisionServer.Timeouts` - Count of ADS timeouts
- `Avail.FilledDuration` - Duration of filled ad breaks
- `Avail.SlateOnly` - Count of ad breaks filled with slate
  only

## Advanced CloudWatch Logs Insights

queries

Use these specialized queries for detailed troubleshooting:

### Comprehensive session

analysis

For detailed analysis of ad insertion behavior for a specific session:

````

fields @timestamp, sessionId, eventType, creativeId, skipReason, adBreakIndex
| filter sessionId = "your-session-id-here"
| filter eventType in ["FILLED_AVAIL", "SKIPPED_AVAIL", "MAKING_ADS_REQUEST"]
| sort @timestamp asc
| limit 100 ``` ### Finding Creative IDs To identify Creative IDs from FILLED\_AVAIL events: ``` fields @timestamp, sessionId, eventType
| filter sessionId like /sessionId/ and eventType!='BEACON_FIRED'
| sort @timestamp desc ``` ###### Note Replace `sessionId` with the actual session ID you're investigating.
````
