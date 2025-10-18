# CloudWatch metrics published by canaries

Canaries publish the following metrics to CloudWatch in the `CloudWatchSynthetics` namespace. 

 For more information about viewing CloudWatch metrics, see 
 [View available metrics](viewing_metrics_with_cloudwatch.md "viewing_metrics_with_cloudwatch.md").

###### Note

For multi-browser canaries, browser-dimension metrics are enabled by default to provide visibility into performance across browsers like Chrome, Firefox and other browsers.
 To disable browser metrics, set `browserDimension` to `false`.

For single-browser canaries, browser-dimension metrics are disabled by default to avoid redundancy. To see metrics broken down by browser, set `browserDimension` to `true`.



| Metric | Description |
| --- | --- |
| `2xx` | The number of network requests performed by the canary that returned OK responses, with response codes between 200 and 299. This metric is reported for UI canaries that use runtime version `syn-nodejs-2.0` or later, and is reported for API canaries that use runtime version `syn-nodejs-2.2` or later. Valid Dimensions: CanaryName, Browser Valid Statistic: Sum Units: Count |
| `4xx` | The number of network requests performed by the canary that returned Error responses, with response codes between 400 and 499. This metric is reported for UI canaries that use runtime version `syn-nodejs-2.0` or later, and is reported for API canaries that use runtime version `syn-nodejs-2.2` or later. Valid Dimensions: CanaryName, Browser Valid Statistic: Sum Units: Count |
| `5xx` | The number of network requests performed by the canary that returned Fault responses, with response codes between 500 and 599. This metric is reported for UI canaries that use runtime version `syn-nodejs-2.0` or later, and is reported for API canaries that use runtime version `syn-nodejs-2.2` or later. Valid Dimensions: CanaryName, Browser Valid Statistic: Sum Units: Count |
| `Duration` | The duration in milliseconds of the canary run. Valid Dimensions: CanaryName, Browser Valid Statistic: Average Units: Milliseconds |
| `DurationDryRun` | The duration of DryRun executions. Valid Dimensions: CanaryName, Browser Valid Statistic: Average Units: Milliseconds |
| `Error` | The number of times the canary failed to run its full script. Valid Dimensions: CanaryName, Browser Valid Statistic: Sum |
| `EphemeralStorageUsagePercent` | The maximum percentage of ephemeral storage used compared to total ephemeral storage configured. This metric is collected at every 10 second interval. |
| `Failed` | The number of canary runs that failed to execute. These failures are related to the canary itself. Valid Dimensions: CanaryName, Browser Valid Statistic: Sum Units: Count |
| `Failed requests` | The number of HTTP requests executed by the canary on the target website that failed with no response. Valid Dimensions: CanaryName, Browser Valid Statistic: Sum Units: Count |
| `RetryCount` | The number of times your canary retried. This metric is only displayed when there are retries. Valid Dimensions: CanaryName, Browser Valid Statistic: Sum Units: Count |
| `SuccessPercent` | The percentage of the runs of this canary that succeed and find no failures. Valid Dimensions: CanaryName, Browser Valid Statistic: Average Units: Percent |
| `SuccessPercentDryRun` | The success percentage of DryRun executions. Valid Dimensions: CanaryName, Browser Valid Statistic: Average Units: Percent |
| `SuccessPercentWithRetries` | The percentage of the runs of this canary that succeed after all attempts. Valid Dimensions: CanaryName, Browser Valid Statistic: Average Units: Percent |
| `VisualMonitoringSuccessPercent` | The percentage of visual comparisons that successfully matched the baseline screenshots during a canary run. Valid Dimensions: CanaryName, Browser Valid Statistic: Average Units: Percent |
| `VisualMonitoringTotalComparisons` | The total number of visual comparisons that happened during a canary run. Valid Dimensions: CanaryName, Browser Units: Count | ###### Note Canaries that use either the `executeStep()` or `executeHttpStep()` methods from the Synthetics library also publish `SuccessPercent` and `Duration` metrics with the dimensions `CanaryName` and `StepName` for each step.
