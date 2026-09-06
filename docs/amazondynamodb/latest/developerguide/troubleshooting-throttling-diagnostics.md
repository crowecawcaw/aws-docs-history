

# DynamoDB throttling resolution guide
<a name="troubleshooting-throttling-diagnostics"></a>

This section provides targeted resolution guidance for each specific throttling reason that DynamoDB might return. Each entry includes suggested resolution approaches based on best practices and corresponding CloudWatch metrics to monitor. 

DynamoDB implements 16 distinct throttling reasons across four main categories. Use the throttling reasons from your application's exception to navigate directly to the relevant guidance.

## Key range throughput exceeded (hot partitions)
<a name="partition-limits-throttling-reasons"></a>

These throttling reasons occur when individual partitions exceed their throughput limits, affecting both provisioned and on-demand modes:
+ [TableReadKeyRangeThroughputExceeded](throttling-key-range-limit-exceeded-mitigation.md#throttling-table-read-keyrange)
+ [TableWriteKeyRangeThroughputExceeded](throttling-key-range-limit-exceeded-mitigation.md#throttling-table-write-keyrange)
+ [IndexReadKeyRangeThroughputExceeded](throttling-key-range-limit-exceeded-mitigation.md#throttling-index-read-keyrange)
+ [IndexWriteKeyRangeThroughputExceeded](throttling-key-range-limit-exceeded-mitigation.md#throttling-index-write-keyrange)

## Provisioned throughput exceeded
<a name="provisioned-capacity-throttling-reasons"></a>

These throttling reasons occur when consumption rates exceed provisioned capacity limits in provisioned mode:
+ [TableReadProvisionedThroughputExceeded](throttling-provisioned-capacity-exceeded-mitigation.md#throttling-table-read-provisioned)
+ [TableWriteProvisionedThroughputExceeded](throttling-provisioned-capacity-exceeded-mitigation.md#throttling-table-write-provisioned)
+ [IndexReadProvisionedThroughputExceeded](throttling-provisioned-capacity-exceeded-mitigation.md#throttling-index-read-provisioned)
+ [IndexWriteProvisionedThroughputExceeded](throttling-provisioned-capacity-exceeded-mitigation.md#throttling-index-write-provisioned)

## Account limits exceeded
<a name="account-limits-throttling-reasons"></a>

These throttling reasons occur when consumption rates exceed account-level throughput quotas in your AWS Region:
+ [TableReadAccountLimitExceeded](throttling-account-limit-exceeded-mitigation.md#throttling-table-read-account-limit) 
+ [TableWriteAccountLimitExceeded](throttling-account-limit-exceeded-mitigation.md#throttling-table-write-account-limit)
+ [IndexReadAccountLimitExceeded](throttling-account-limit-exceeded-mitigation.md#throttling-index-read-account-limit)
+ [IndexWriteAccountLimitExceeded](throttling-account-limit-exceeded-mitigation.md#throttling-index-write-account-limit)

## On-demand maximum throughput exceeded
<a name="ondemand-maximum-throttling-reasons"></a>

These throttling reasons occur when consumption rates exceed configured maximum throughput limits in on-demand mode:
+ [TableReadMaxOnDemandThroughputExceeded](throttling-ondemand-capacity-exceeded-mitigation.md#throttling-diagnostic-table-read-max-ondemand)
+ [TableWriteMaxOnDemandThroughputExceeded](throttling-ondemand-capacity-exceeded-mitigation.md#throttling-diagnostic-table-write-max-ondemand)
+ [IndexReadMaxOnDemandThroughputExceeded](throttling-ondemand-capacity-exceeded-mitigation.md#throttling-diagnostic-index-read-max-ondemand)
+ [IndexWriteMaxOnDemandThroughputExceeded](throttling-ondemand-capacity-exceeded-mitigation.md#throttling-diagnostic-index-write-max-ondemand)