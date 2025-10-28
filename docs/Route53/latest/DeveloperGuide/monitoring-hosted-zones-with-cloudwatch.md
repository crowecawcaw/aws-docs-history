# Monitoring hosted zones using Amazon CloudWatch

You can monitor your public hosted zones by using Amazon CloudWatch to collect and process raw data into readable, near real-time metrics.
Metrics are available shortly after Route 53 receives the DNS queries that the metrics are based on. CloudWatch metric data for
Route 53 hosted zones has a granularity of one minute.

For more information, see the following documentation

- For an overview and information about how to view metrics in the Amazon CloudWatch console and how to retrieve metrics using the
  AWS Command Line Interface (AWS CLI), see
  [Viewing DNS query metrics for a public hosted zone](hosted-zone-public-viewing-query-metrics.md "hosted-zone-public-viewing-query-metrics.md")
- For information about the retention period for metrics, see
  [GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") in the
  _Amazon CloudWatch API Reference_.
- For more information about CloudWatch, see
  [What is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md") in the _Amazon CloudWatch User Guide_.
- For more information about CloudWatch metrics, see
  [Using Amazon CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") in the _Amazon CloudWatch User Guide_.

###### Topics

- [CloudWatch metrics for Route 53 public hosted zones](#cloudwatch-metrics-route-53-hosted-zones "#cloudwatch-metrics-route-53-hosted-zones")
- [CloudWatch dimension for Route 53 public hosted zone metrics](#cloudwatch-dimensions-route-53-hosted-zones "#cloudwatch-dimensions-route-53-hosted-zones")

## CloudWatch metrics for Route 53 public hosted zones

The `AWS/Route53` namespace includes the following metrics for Route 53 hosted zones:

**DNSQueries**

For a hosted zone, the number of DNS queries that Route 53 responds to in a specified time period.

Valid statistics: Sum, SampleCount

Units: Count

Region: Route 53 is a global service. To get hosted zone metrics, you must specify US East (N. Virginia) for the Region.

**DNSSECInternalFailure**

Value is 1 if any object in the hosted zone is in an INTERNAL_FAILURE
state. Otherwise, value is 0.

Valid statistics: Sum

Units: Count

Volume: 1 per 4 hours per hosted zone

Region: Route 53 is a global service. To get hosted zone metrics, you
must specify US East (N. Virginia) for the Region.

**DNSSECKeySigningKeysNeedingAction**

Number of key signing keys (KSKs) that have an ACTION_NEEDED state
(due to KMS failure).

Valid statistics: Sum, SampleCount

Units: Count

Volume: 1 per 4 hours per hosted zone

Region: Route 53 is a global service. To get hosted zone metrics, you
must specify US East (N. Virginia) for the Region.

**DNSSECKeySigningKeyMaxNeedingActionAge**

Time elapsed since the key signing key (KSK) was set to the ACTION_NEEDED state.

Valid statistics: Maximum

Units: Seconds

Volume: 1 per 4 hours per hosted zone

Region: Route 53 is a global service. To get hosted zone metrics, you must specify US East (N. Virginia) for the Region.

**DNSSECKeySigningKeyAge**

The time elapsed since the key signing key (KSK) was created (not
since it was activated).

Valid statistics: Maximum

Units: Seconds

Volume: 1 per 4 hours per hosted zone

Region: Route 53 is a global service. To get hosted zone metrics, you
must specify US East (N. Virginia) for the Region.

## CloudWatch dimension for Route 53 public hosted zone metrics

Route 53 metrics for hosted zones use the `AWS/Route53` namespace and provide metrics for
`HostedZoneId`. To get the number of DNS queries, you must specify the ID of the hosted zone in the
`HostedZoneId` dimension.
