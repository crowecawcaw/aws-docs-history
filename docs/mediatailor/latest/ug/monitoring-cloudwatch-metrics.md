

# Monitoring AWS Elemental MediaTailor with Amazon CloudWatch metrics
<a name="monitoring-cloudwatch-metrics"></a>

You can monitor AWS Elemental MediaTailor metrics using CloudWatch. CloudWatch collects raw data about the performance of the service and processes that data into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

Metrics can be useful when you investigate stale manifests. For more information, see [Using metrics to diagnose stale manifests](stale-manifest-diagnose.md).

Metrics are grouped first by the service namespace, and then by the various dimension combinations within each namespace.

**To view metrics using the CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. Under **All metrics**, choose the **MediaTailor** namespace. 

1. Select the metric dimension to view the metrics (for example, **originID**).

1. Specify the time period that you want to view. 

**To view metrics using the AWS Command Line Interface (AWS CLI)**
+ At a command prompt, use the following command:

  ```
  aws cloudwatch list-metrics --namespace "AWS/MediaTailor"
  ```

## AWS Elemental MediaTailor CloudWatch metrics
<a name="metrics"></a>

The AWS Elemental MediaTailor namespace includes the following metrics. These metrics are published by default to your account. 

### Channel Assembly (CA) metrics
<a name="metrics.channel-assembly"></a>

In the following table, all metrics are available by channel or by channel output.


| Metric | Description | 
| --- | --- | 
|  4xxErrorCount  | The number of `4xx` errors. | 
|  5xxErrorCount  | The number of `5xx` errors. | 
|  RequestCount  | The total number of requests. The transaction count depends largely on how often players request updated manifests, and the number of players. Each player request counts as a transaction. | 
|  TotalTime  | The amount of time that the application server took to process the request, including the time used to receive bytes from and write bytes to the client and network.  | 

#### Server-side Ad-insertion (SSAI) metrics
<a name="metrics.server-side-ad-insertion"></a>

The following table lists server-side ad-insertion metrics.


| Metric | Description | 
| --- | --- | 
|  AdDecisionServer.Ads  | The count of ads included in ad decision server (ADS) responses within the CloudWatch time period that you specified.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  AdDecisionServer.Duration  | The total duration, in milliseconds, of all ads that MediaTailor received from the ADS within the CloudWatch time period that you specified. This duration can be greater than the `Avail.Duration` that you specified.<br />**Dimensions:** `ConfigurationName` | 
|  AdDecisionServer.Errors  | The number of non-HTTP 200 status code responses, empty responses, and timed-out responses that MediaTailor received from the ADS within the CloudWatch time period that you specified.<br />**Dimensions:** `ConfigurationName` | 
|  AdDecisionServer.FillRate  | The simple average of the rates at which the responses from the ADS filled the corresponding individual ad avails for the time period that you specified.<br />To get the weighted average, calculate the `AdDecisionServer.Duration` as a percentage of the `Avail.Duration`. For more information about simple and weighted averages, see [Simple and weighted averages](#metrics-simple-average).<br />**Dimensions:** `ConfigurationName` | 
|  AdDecisionServer.Latency  | The response time in milliseconds for requests made by MediaTailor to the ADS.<br />**Dimensions:** `ConfigurationName` | 
|  AdDecisionServer.Timeouts  | The number of timed-out requests to the ADS in the CloudWatch time period that you specified.<br />**Dimensions:** `ConfigurationName` | 
|  AdNotReady  | The number of times that the ADS pointed at an ad that wasn't yet transcoded by the internal transcoder service in the time period that you specified.<br />A high value for this metric might contribute to a low overall `Avail.FillRate`.<br />**Dimensions:** `ConfigurationName` | 
|  AdsBilled  | The number of ads for which MediaTailor bills customers based on insertion.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  Avail.Duration  | The planned total number of milliseconds of ad avails within the CloudWatch time period. The planned total is based on the ad avail durations in the origin manifest.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  Avail.FilledDuration  | The planned number of milliseconds of ad avail time that MediaTailor will fill with ads within the CloudWatch time period.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  Avail.FillRate  | The planned simple average of the rates at which MediaTailor will fill individual ad avails within the CloudWatch time period.<br />To get the weighted average, calculate the `Avail.FilledDuration` as a percentage of the `Avail.Duration`. For more information about simple and weighted averages, see [Simple and weighted averages](#metrics-simple-average).<br />The maximum `Avail.FillRate` that MediaTailor can attain is bounded by the `AdDecisionServer.FillRate`. If the `Avail.FillRate` is low, compare it to the `AdDecisionServer.FillRate`. If the `AdDecisionServer.FillRate` is low, your ADS might not be returning enough ads for the avail durations. <br />**Dimensions:** `ConfigurationName` | 
|  Avail.Impression  | The number of ads for which MediaTailor fired impression beacons during server-side reporting. MediaTailor emits one count for each ad that has at least one impression URI, regardless of whether those beacons were ultimately delivered. Use this metric as the denominator to calculate the video completion rate (VCR) (see `Avail.Complete`).<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  Avail.Impression.Fired  | The number of impression beacons that MediaTailor fired to a given ad tracking domain during server-side reporting, regardless of whether those beacons were ultimately delivered. An ad with multiple impression beacon URIs contributes one count per URI to each beacon's respective domain. This metric uses the same per-beacon, per-domain unit as `Avail.Impression.Retried` and `Avail.Impression.Recovered`, so you can combine the three per domain (for example, `Avail.Impression.Retried` / `Avail.Impression.Fired` gives the retry rate for a domain).<br />**Dimensions:**+ `AdTrackingDomain`<br />+ Account-level (no dimensions) | 
|  Avail.Impression.Retried  | The number of impression beacons that MediaTailor retried at least once for a given ad tracking domain during server-side reporting. Each beacon is counted once toward its domain, regardless of how many retry attempts were made. Compare this metric to `Avail.Impression.Recovered` to see how many retried impression beacons were ultimately delivered.<br />**Dimensions:**+ `AdTrackingDomain`<br />+ Account-level (no dimensions) | 
|  Avail.Impression.Recovered  | The number of impression beacons that were delivered successfully after being retried during server-side reporting. Each beacon is counted once toward its domain. These beacons would not have reached the ad tracking domain without retries. `Avail.Impression.Recovered` / `Avail.Impression.Retried` gives the retry success rate for impression beacons.<br />**Dimensions:**+ `AdTrackingDomain`<br />+ Account-level (no dimensions) | 
|  Avail.Complete  | The number of ads for which MediaTailor fired complete beacons during server-side reporting. MediaTailor emits one count for each ad that has at least one complete tracking URI, regardless of whether those beacons were ultimately delivered. To calculate the video completion rate (VCR), divide the sum of `Avail.Complete` by the sum of `Avail.Impression`.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  Avail.Complete.Fired  | The number of complete beacons that MediaTailor fired to a given ad tracking domain during server-side reporting, regardless of whether those beacons were ultimately delivered. An ad with multiple complete beacon URIs contributes one count per URI to each beacon's respective domain. This metric uses the same per-beacon, per-domain unit as `Avail.Complete.Retried` and `Avail.Complete.Recovered`, so you can combine the three per domain (for example, `Avail.Complete.Retried` / `Avail.Complete.Fired` gives the retry rate for a domain).<br />**Dimensions:**+ `AdTrackingDomain`<br />+ Account-level (no dimensions) | 
|  Avail.Complete.Retried  | The number of complete beacons that MediaTailor retried at least once for a given ad tracking domain during server-side reporting. Each beacon is counted once toward its domain, regardless of how many retry attempts were made. Compare this metric to `Avail.Complete.Recovered` to see how many retried complete beacons were ultimately delivered.<br />**Dimensions:**+ `AdTrackingDomain`<br />+ Account-level (no dimensions) | 
|  Avail.Complete.Recovered  | The number of complete beacons that were delivered successfully after being retried during server-side reporting. Each beacon is counted once toward its domain. These beacons would not have reached the ad tracking domain without retries. `Avail.Complete.Recovered` / `Avail.Complete.Retried` gives the retry success rate for complete beacons.<br />**Dimensions:**+ `AdTrackingDomain`<br />+ Account-level (no dimensions) | 
|  Avail.ObservedDuration  | The observed total number of milliseconds of ad avails that occurred within the CloudWatch time period. `Avail.ObservedDuration` is emitted at the end of the ad avail, and is based on the duration of the segments reported in the manifest during the ad avail.<br />**Dimensions:** `ConfigurationName` | 
|  Avail.ObservedFilledDuration  | The observed number of milliseconds of ad avail time that MediaTailor filled with ads within the CloudWatch time period.<br />**Dimensions:** `ConfigurationName` | 
|  Avail.ObservedFillRate  | The observed simple average of the rates at which MediaTailor filled individual ad avails within the CloudWatch time period.<br />Emitted only for HLS manifests, at the first `CUE-IN` tag. If there is no `CUE-IN` tag, MediaTailor doesn't emit this metric. <br />**Dimensions:** `ConfigurationName` | 
|  Avail.ObservedSlateDuration  | The observed total number of milliseconds of slate that was inserted within the CloudWatch period.<br />**Dimensions:** `ConfigurationName` | 
|  GetManifest.Age  | The total age of the manifest in milliseconds. Measured from when the origin creates the manifest, to when MediaTailor sends the personalized manifest. <br />For more information about metrics for measuring manifest age, see [Using metrics to diagnose stale manifests](stale-manifest-diagnose.md).<br />**Dimensions:** `ConfigurationName` | 
|  GetManifest.Errors  | The number of errors received while MediaTailor was generating manifests in the CloudWatch time period that you specified.<br />**Dimensions:** `ConfigurationName` | 
|  GetManifest.Latency  | The MediaTailor response time in milliseconds for the request to generate manifests.<br />For more information about metrics for measuring manifest age, see [Using metrics to diagnose stale manifests](stale-manifest-diagnose.md).<br />**Dimensions:** `ConfigurationName` | 
|  GetManifest.MediaTailorAge  | The amount of time that the manifest has been stored in MediaTailor in milliseconds. Measured from when MediaTailor receives an origin response, to when MediaTailor sends the personalized manifest. <br />For more information about metrics for measuring manifest age, see [Using metrics to diagnose stale manifests](stale-manifest-diagnose.md).<br />**Dimensions:** `ConfigurationName` | 
|  Origin.Age  | The amount of time that the origin has the manifest in milliseconds. Measured from when the origin creates the manifest, to when MediaTailor sends the origin request. <br />All `origin.*` metrics are emitted for requests that are fulfilled directly from the origin. They are not emitted for cached origin responses.<br />For more information about metrics for measuring manifest age, see [Using metrics to diagnose stale manifests](stale-manifest-diagnose.md).<br />**Dimensions:** `ConfigurationName` | 
|  Origin.Errors  | The number of non-HTTP 200 status code responses and timed-out responses that MediaTailor received from the origin server in the CloudWatch time period that you specified.<br />All `origin.*` metrics are emitted for requests that are fulfilled directly from the origin. They are not emitted for cached origin responses.<br />**Dimensions:** `ConfigurationName` | 
|  Origin.ManifestFileSizeBytes  | The file size of the origin manifest in bytes for both HLS and DASH. Typically this metric is used in conjunction with `Origin.ManifestFileSizeTooLarge`.<br />All `origin.*` metrics are emitted for requests that are fulfilled directly from the origin. They are not emitted for cached origin responses.<br />**Dimensions:** `ConfigurationName` | 
|  Origin.ManifestFileSizeTooLarge  | The number of responses from the origin that have a manifest size larger than the configured amount. Typically this metric is used in conjunction with `Origin.ManifestFileSizeBytes`.<br />All `origin.*` metrics are emitted for requests that are fulfilled directly from the origin. They are not emitted for cached origin responses.<br />**Dimensions:** `ConfigurationName` | 
|  Origin.Timeouts  | The number of timed-out requests to the origin server in the CloudWatch time period that you specified.<br />All `origin.*` metrics are emitted for requests that are fulfilled directly from the origin. They are not emitted for cached origin responses.<br />**Dimensions:** `ConfigurationName` | 
|  Requests  | The number of concurrent transactions per second across all request types. The transaction count depends mainly on the number of players and how often the players request updated manifests. Each player request counts as a transaction.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  SkippedReason.DurationExceeded  | The number of ads that were not inserted into an avail because the ADS returned a duration of ads that was greater than the specified avail duration. A high value for this metric might contribute to a discrepancy between the `AdsBilled` and `AdDecisionServer.Ads` metrics. For more information about ad skipped reasons, see [Ad skipping troubleshooting](troubleshooting-ad-skipping-overview.md).<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  SkippedReason.EarlyCueIn  | The number of ads skipped due to an early `CUE-IN`.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  SkippedReason.ImportError  | The number of ads skipped due to an error in the import job.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  SkippedReason.ImportInProgress  | The number of ads skipped due to an existing active import job.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  SkippedReason.InternalError  | The number of ads skipped due to a MediaTailor internal error.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  SkippedReason.NewCreative  | The number of ads that were not inserted into an avail because it was the first time the asset had been requested by a client. A high value for this metric might temporarily contribute to a low overall `Avail.FillRate`, until assets can be successfully transcoded.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  SkippedReason.NoVariantMatch  | The number of ads skipped due to there being no variant match between the ad and content.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  SkippedReason.PersonalizationThresholdExceeded  | The duration of ads exceeding the **Personalization Threshold** setting in this configuration.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  SkippedReason.ProfileNotFound  | The number of ads skipped due to the transcoding profile not being found.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  SkippedReason.TranscodeError  | The number of ads skipped due to a transcode error.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 
|  SkippedReason.TranscodeInProgress  | The count of the number of ads that were not inserted into an avail because the ad had not yet been transcoded. A high value for this metric might temporarily contribute to a low overall `Avail.FillRate`, until the assets can be successfully transcoded.<br />**Dimensions:**+ `ConfigurationName`<br />+ Account-level (no dimensions) | 

**Note**  
For HLS Interstitials sessions, some metrics behave differently due to the late-binding nature of ad decisioning:  
`Avail.ObservedFilledDuration` matches `Avail.FilledDuration` since MediaTailor cannot observe actual client-side playback behavior.
`Avail.ObservedSlateDuration` reports planned slate duration from Asset List responses rather than observed playback.
Metrics prefixed with "Observed" provide estimated values for HLS Interstitials sessions.

### Functions metrics
<a name="metrics.functions"></a>

The following metrics are published when you use [Functions](monetization-functions.html) with your playback configurations. These metrics are always emitted when a function is configured on a lifecycle hook. No opt-in or log configuration is required.

**Hook-level metrics** — one data point per lifecycle hook execution:


| Metric | Description | 
| --- | --- | 
|  PreSessionInitHook.Invocations  | The number of times the pre-session initialization hook was invoked.<br />**Dimensions:** `ConfigurationName` | 
|  PreSessionInitHook.Errors  | The number of pre-session initialization hook executions that resulted in an error.<br />**Dimensions:** `ConfigurationName` | 
|  PreSessionInitHook.Latency  | The execution time in milliseconds for the pre-session initialization hook.<br />**Dimensions:** `ConfigurationName` | 
|  PreAdsRequestHook.Invocations  | The number of times the pre-ads request hook was invoked.<br />**Dimensions:** `ConfigurationName` | 
|  PreAdsRequestHook.Errors  | The number of pre-ads request hook executions that resulted in an error.<br />**Dimensions:** `ConfigurationName` | 
|  PreAdsRequestHook.Latency  | The execution time in milliseconds for the pre-ads request hook.<br />**Dimensions:** `ConfigurationName` | 

**Function-level metrics** — one data point per individual function execution. These metrics include additional dimensions (`FunctionId`, `FunctionType`, `HookType`) so you can identify which specific function is slow or failing:


| Metric | Description | 
| --- | --- | 
|  Function.Invocations  | The number of times an individual function was executed.<br />**Dimensions:**+ `ConfigurationName`<br />+ `ConfigurationName`, `FunctionId`, `FunctionType`, `HookType` | 
|  Function.Errors  | The number of individual function executions that resulted in an error.<br />**Dimensions:**+ `ConfigurationName`<br />+ `ConfigurationName`, `FunctionId`, `FunctionType`, `HookType` | 
|  Function.Latency  | The execution time in milliseconds for an individual function.<br />**Dimensions:**+ `ConfigurationName`<br />+ `ConfigurationName`, `FunctionId`, `FunctionType`, `HookType` | 

### Simple and weighted averages
<a name="metrics-simple-average"></a>

You can retrieve the simple average and the weighted average for the responses from the ADS to ad requests from MediaTailor and for how MediaTailor fills ad avails: 
+ The *simple averages* are provided in the `AdDecisionServer.FillRate` and the `Avail.FillRate`. These are the averages of the fill rate percentages for the individual avails for the time period. The simple averages don't take into account any differences between the durations of the individual avails.
+ The *weighted averages* are the fill rate percentages for the sum of all avail durations. These are calculated as (`AdDecisionServer.Duration`\*100)/`Avail.Duration` and (`Avail.FilledDuration`\*100)/`Avail.Duration`. These averages reflect the differences in duration of each ad avail, giving more weight to those with longer duration. 

For a time period that contains just a single ad avail, the simple average provided by the `AdDecisionServer.FillRate` is equal to the weighted average provided by (`AdDecisionServer.Duration`\*100)/`Avail.Duration`. The simple average provided by the `Avail.FillRate` is equal to the weighted average provided by (`Avail.FilledDuration`\*100)/`Avail.Duration`. 

**Example**

Assume the time period that you specified has the following two ad avails:
+ The first ad avail has 90 seconds duration:
  + The ADS response for the avail provides 45 seconds of ads (50% filled). 
  + MediaTailor fills 45 seconds worth of the ad time available (50% filled).
+ The second ad avail has 120 seconds duration: 
  + The ADS response for the avail provides 120 seconds of ads (100% filled). 
  + MediaTailor fills 90 seconds worth of the ad time available (75% filled).

The metrics are as follows: 
+ `Avail.Duration` is 210, the sum of the two ad avail durations: 90 \+ 120.
+ `AdDecisionServer.Duration` is 165, the sum of the two response durations: 45 \+ 120.
+ `Avail.FilledDuration` is 135, the sum of the two filled durations: 45 \+ 90. 
+ `AdDecisionServer.FillRate` is 75%, the average of the percentages filled for each avail: (50% \+ 100%) / 2. This is the simple average.
+ The weighted average for the ADS fill rates is 78.57%, which is `AdDecisionServer.Duration` as a percentage of the `Avail.Duration`: (165\*100) / 210. This calculation accounts for the differences in the durations. 
+ `Avail.FillRate` is 62.5%, the average of the filled percentages for each avail: (50% \+ 75%) / 2. This is the simple average.
+ The weighted average for the MediaTailor avail fill rates is 64.29%, which is the `Avail.FilledDuration` as a percentage of the `Avail.Duration`: (135\*100) / 210. This calculation accounts for the differences in the durations. 

The highest `Avail.FillRate` that MediaTailor can attain for any ad avail is 100%. The ADS might return more ad time than is available in the avail, but MediaTailor can only fill the time available. 

## AWS Elemental MediaTailor CloudWatch dimensions
<a name="dimensions"></a>

You can filter the AWS Elemental MediaTailor data using the following dimensions.


| Dimension | Description | 
| --- | --- | 
| `ConfigurationName` | Indicates the configuration that the metric belongs to. Available on all metrics except the per-domain beacon metrics (`Avail.Impression.Fired`, `Avail.Impression.Retried`, `Avail.Impression.Recovered`, `Avail.Complete.Fired`, `Avail.Complete.Retried`, and `Avail.Complete.Recovered`). | 
| `AdTrackingDomain` | The registrable domain of the ad tracking beacon's destination, with subdomains removed. A host that cannot be resolved to a registrable domain is reported as `unknown`. Available on `Avail.Impression.Fired`, `Avail.Impression.Retried`, `Avail.Impression.Recovered`, `Avail.Complete.Fired`, `Avail.Complete.Retried`, and `Avail.Complete.Recovered`. | 
| `FunctionId` | The identifier of the function. Available on `Function.*` metrics only. | 
| `FunctionType` | The type of function: `CUSTOM_OUTPUT`, `HTTP_REQUEST`, `SEQUENTIAL_EXECUTOR`, or `CONCURRENT_EXECUTOR`. Available on `Function.*` metrics only. | 
| `HookType` | The lifecycle hook that triggered the function: `PRE_SESSION_INITIALIZATION` or `PRE_ADS_REQUEST`. Available on `Function.*` metrics only. | 