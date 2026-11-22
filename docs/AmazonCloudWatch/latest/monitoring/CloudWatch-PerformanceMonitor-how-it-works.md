

# How Performance Monitor works

This section provides information about how Performance Monitor works.

**How Performance Monitor measures network paths**

Performance Monitor uses AWS infrastructure telemetry to measure the health of network paths serving your workloads. Performance Monitor analyzes network telemetry from the AWS infrastructure itself.

When you create a monitor and select VPCs, Performance Monitor identifies the network paths used by traffic from those VPCs. It then continuously measures the health of those paths by evaluating packet loss and latency data from the infrastructure layer.

**How impact scores are calculated**

The impact score uses a dual-comparison approach:

1. **Global context** – Performance Monitor computes statistics (mean and standard deviation) of impact across all measured paths at the current time. It then determines whether your specific path is an outlier compared to the collection of all paths.

1. **Local context** – Performance Monitor computes statistics of impact for your specific path over a trailing time window. It then determines whether your path is behaving abnormally at the current time compared to its recent history.

Performance Monitor combines these two comparisons into a single score, which determines the impact level.

Performance Monitor reports impact only when degradation persists across consecutive data points.

This approach has the following properties:
+ A path that is always noisy doesn't cause false alarms, because its local baseline accounts for the noise.
+ A path that suddenly degrades receives a high score, because its local z-score spikes.
+ A path that degrades along with many other paths, indicating an AWS infrastructure event, receives a high score because of the global context.
+ The score is monotonic: higher internal impact always produces a higher score.

**How network paths are categorized**

Performance Monitor categorizes paths based on where traffic originates and terminates:
+ Availability Zone to Availability Zone paths (intra-Region or inter-Region)
+ Availability Zone to service paths (traffic to AWS managed services)

Each path is associated with one or more VPCs and accounts, based on the subnets that contribute traffic to that path.

**How scope determines visibility**

Your scope determines the granularity of path information that's available:
+ For paths where both the source and destination account-Region pairs are in scope, you see full Availability Zone to Availability Zone detail with subnet-level drill-down.
+ For paths where only the source is in scope, you see the source Availability Zone detail, but the destination resolves only to a Region name. Subnet-level drill-down on the destination side isn't available.

After your monitor is active, Performance Monitor can detect traffic flowing to account-Region pairs that aren't in your scope, and recommend adding them for full visibility.