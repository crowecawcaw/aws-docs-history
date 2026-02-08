# HNREL03-BP01 Monitor the bandwidth and scale the bandwidth as

needed

Regularly monitor the bandwidth usage of your dedicated connection.
If usage consistently approaches the connection limit, order
additional dedicated connections and aggregate them into a LAG to
increase bandwidth and resilience with minimal downtime.

**Desired outcome:** Avoid service
degradation or outages due to bandwidth limitations by proactively
scaling your hybrid connectivity.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Prevent performance bottlenecks and dropped traffic
- Enables cost-effective scaling of hybrid network connectivity
- Supports growth in hybrid workload demand
- Ensures seamless failover and aggregation

## Implementation guidance

- Monitor metrics for all dedicated connection and IPSec VPN
  links.
- Create alarms for sustained high utilization.
- Plan and implement LAG to aggregate bandwidth and connections.

## Resources

- [How
  can I migrate virtual Interfaces to Direct Connect connections
  or LAG bundles?](https://repost.aws/knowledge-center/migrate-virtual-interface-dx-lag "https://repost.aws/knowledge-center/migrate-virtual-interface-dx-lag")
- [Direct
  Connect link aggregation groups (LAGs)](../../../directconnect/latest/UserGuide/lags.md "../../../directconnect/latest/UserGuide/lags.md")
- [Monitoring
  Direct Connect with CloudWatch](../../../directconnect/latest/UserGuide/monitoring-cloudwatch.md "../../../directconnect/latest/UserGuide/monitoring-cloudwatch.md")
