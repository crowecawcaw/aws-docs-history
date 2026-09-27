

# Grant DescribeStreamSummary permission to the KPL
<a name="service-managed-pk-kpl-permissions"></a>

The updated KPL calls the `DescribeStreamSummary` API to detect whether a stream uses service-managed record distribution (`AUTO`). Ensure that the IAM principal your producer uses has the `kinesis:DescribeStreamSummary` permission for the stream. This permission is included in the minimum-permissions policy for the KPL; if you follow that policy, no change is required.

**Important**  
If the KPL cannot call `DescribeStreamSummary`, it cannot reliably detect that a stream uses service-managed record distribution. This can happen, for example, if the `kinesis:DescribeStreamSummary` permission is not granted. In this case, the KPL falls back to aggregating records. Aggregation is not supported on service-managed streams, so the aggregated records that are written can be silently dropped by KCL consumers during de-aggregation, with no error surfaced by the producer or consumer. Grant the `kinesis:DescribeStreamSummary` permission before you enable service-managed record distribution on a stream that KPL producers write to.