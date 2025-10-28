# Logging and metrics for overlay ads in MediaTailor

This section explains logging and metrics for overlay ads in MediaTailor. For more information
about setting up logging, see [Monitoring and tagging AWS Elemental MediaTailor resources](monitoring.md "monitoring.md").

###### Topics

- [CloudWatch logs](#overlay-ads-logging-and-metrics-cloudwatch "#overlay-ads-logging-and-metrics-cloudwatch")
- [CloudWatch
  metrics](#overlay-ads-logging-and-metrics-cloudwatch-metrics "#overlay-ads-logging-and-metrics-cloudwatch-metrics")

## CloudWatch logs

CloudWatch collects the following log information about overlay ads:

- `VAST_RESPONSE` - Shows information about the non-linear ads
  list.
- `FILLED_PROVIDER_OVERLAY` - Shows information about the non-linear
  ads.

###### Note

The `RAW_ADS_RESPONSE` is an optional event that shows the original
response from the ADS. Using this event is especially helpful in a staging and
testing environment. To enable this event on a configuration or account, submit a
ticket to AWS Support.

## CloudWatch

metrics

MediaTailor collects overlay ad metrics separately from other ADS metrics. MediaTailor
collects these metrics after successfully fetching the ads from the ADS. You don't have
to poll the `GetTracking` API to collect the metrics.

The following table describes CloudWatch metrics for overlay ads:

| Metric                                         | Description                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `AdDecisionServer.OverlayAds`                  | The count of overlay ads included in the ADS responses within the CloudWatch time period that you specified.                                                                                                                                                                                                                         |
| `AdDecisionServer.OverlayErrors`               | The number of non-HTTP `200` status code responses, empty responses, and timed-out responses that MediaTailor received from the ADS within the CloudWatch time period that you specified.                                                                                                                                            |
| `AdDecisionServer.OverlayFilled`               | The number of avails that were successfully filled with at least one overlay ad: <br>• 1 - There's at least one valid ad. <br>• 0 - Either MediaTailor didn't get any overlay ads, or there was some other failure. `SampleCount` tracks the number of avails filled. `Sum` tracks the number of successfully filled overlay avails. |
| `AdDecisionServer.OverlayMinSuggestedDuration` | The sum of `minSuggestedDuration` durations, in milliseconds, of all ads that MediaTailor received from the ADS within the CloudWatch time period that you specified. If `minSuggestedDuration` isn't specified, the duration shown is the planned duration.                                                                         |
| `AdDecisionServer.OverlayLatency`              | The response time, in milliseconds, for requests that MediaTailor makes to the ADS.                                                                                                                                                                                                                                                  |
| `AdDecisionServer.OverlayTimeouts`             | The number of timed-out requests to the ADS in the CloudWatch time period that you specified.                                                                                                                                                                                                                                        |
| `AdsBilled`                                    | For more information about ads billed, see [Billing for overlay ads in MediaTailor](overlay-ads-billing.md "overlay-ads-billing.md").                                                                                                                                                                                                |
| `Avail.*`                                      | Because MediaTailor doesn't do any planning for overlay ads, CloudWatch doesn't show any `Avail.X` metrics.                                                                                                                                                                                                                          |
| `SkippedReason.*`                              | Because MediaTailor doesn't do any planning for overlay ads, CloudWatch doesn't show any `SkippedReason.X` metrics.                                                                                                                                                                                                                  |
