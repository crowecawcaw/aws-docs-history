

# ADVREL06-BP01 Deploy Ad Decision Server infrastructure across multiple Availability Zones with automated failover

 The Ad Decision Server (ADS) receives personalized ad requests from the player during SCTE-35 signaled breaks. Single-AZ ADS deployment means Availability Zone failure removes personalized ad delivery for all viewers. 

 **Desired outcome:** 
+  ADS infrastructure spans at least 2 Availability Zones with active health checks. On Availability Zone failure, traffic redistributes automatically within the configured deregistration delay window. 
+  Your health checks exercise the ad decision path end to end rather than confirming process liveness, so an instance that can't produce a valid VAST response is removed from rotation. 
+  Ad decision latency is bounded by an explicit timeout budget, so a slow or unresponsive ADS produces a defined outcome for the break instead of an open-ended wait. 
+  You have verified what actually fills the break when ad decisioning fails, and the configuration that governs it is set deliberately rather than left at a default someone else chose. 
+  ADS capacity tracks concurrent VAST request volume, holding response latency inside the timeout budget through ad-break traffic spikes. 

 **Common anti-patterns:** 
+  Health checks that only validate container liveness, not full VAST response capability. 
+  Leaving ad decision timeouts at their defaults, so the time budget for a break is inherited rather than chosen. 
+  Treating the personalization threshold as a mechanism that triggers fallback content, when setting it below the break duration abandons personalization for the break instead. 
+  Manual capacity management for ADS means that you can't respond to traffic spikes around live event ad breaks. 

 **Benefits of establishing this best practice:** 
+  An Availability Zone-level impairment degrades ad decisioning capacity rather than removing personalized ad delivery entirely. 
+  A bounded ad decision keeps a failing ADS from stalling manifest generation, so an ad-serving problem stays an ad-serving problem instead of becoming a playback problem. 
+  Operators learn about ad decision failures from a metric rather than from viewer reports, and can separate error responses from timeouts during triage. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 In live and FAST streaming, an ad break arrives on a fixed schedule dictated by the content timeline. The player reaches that SCTE-35 splice point whether an ad decision is ready. ADS latency is therefore a hard constraint. A slow or unreachable ADS degrades fill rate and stalls manifest generation, pushing visible latency into the viewer session, because the origin can't emit the next segment until the ADS returns a decision. Unlike display or web-video advertising where an unfilled slot renders as blank space, a missed decision window in live streaming manifests as dead air or a frozen frame, which drives channel changes. 

 A time ceiling on the ad decision guards against ADS health that varies across Availability Zone failures, upstream demand-side platform timeouts, and campaign-database replication lag. Without that ceiling, the failure is silent. Viewers stall and session metrics degrade, but no alarm fires, because the ADS never returns an error and never responds. The ADS timeout parameters bound how long MediaTailor waits for a decision. PersonalizationThresholdSeconds does something different, close to the opposite. It caps how much *unfilled* ad time MediaTailor tolerates before abandoning personalization of the break. Setting it below a break's duration means an unfilled break exceeds the threshold. MediaTailor then shows the underlying content with no slate, even where a slate is configured. Treat it as a deliberate choice between showing content and showing slate on failure. 

 Health-checking an ad decision service differs from checking a typical HTTP microservice. A 200-status liveness probe confirms the process is running but does not determine whether the service can execute a complete VAST auction by reaching its campaign store, evaluating targeting rules, and returning a valid VAST document within the timing budget. The health check must exercise the decision path itself and confirm that the infrastructure behind the endpoint can produce a usable response under production-like conditions. 

 The ADS is frequently a third-party or separately-owned service, so the team that owns stream availability is often not the team that can fix a failing ad decision. Where the ADS is external, the timeout budget and the fallback behavior are the only controls the streaming team holds. Agree in advance who is paged for an ad decision failure, what the ADS owner's availability commitment is, and whether ad-serving degradation is permitted to page anyone outside revenue-critical events. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy the ADS across at least two Availability Zones:** Run the service on ECS or EKS behind an Application Load Balancer with cross-zone load balancing enabled. Tune the deregistration delay short enough that failover completes well inside an ad break rather than at the default, which is oriented toward draining long-lived connections. 

1.  **Make the health check exercise the decision path:** Point the [target-group health check](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html) at an endpoint that performs a representative decision end to end, rather than at a liveness route that returns a static 200. An instance that answers the probe but can't produce a valid VAST document should fail the check. Set the unhealthy threshold and interval so a failing instance leaves rotation within a single break. 

1.  **Set the ad decision timeout budget explicitly:** Configure MediaTailor's [ADS timeout parameters](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html) from your break structure and measured ADS latency rather than accepting defaults, and keep the per-request timeout inside the total personalization budget. Derive the value from the ADS latency distribution under peak load, not from a round number. 

1.  **Decide the personalization threshold against your break durations, then verify it:** Set PersonalizationThresholdSeconds knowing that a value below a break's duration suppresses slate on a total ad-decision failure. Confirm the intent in writing, then simulate an ADS timeout and an empty response and observe what fills the break. Trust what plays over what the configuration appears to promise. 

1.  **Alarm on ad decision failures and separate the failure types:** Alarm on AdDecisionServer.Errors, which the metrics reference defines as counting non-200 status responses, empty responses, and timed-out responses together, making it the single signal for ad decisioning being broken. Keep AdDecisionServer.Timeouts on the dashboard alongside it, because a shift toward timeouts points at capacity or upstream latency while error responses point at the service itself. Both are dimensioned by ConfigurationName. Route the alarm to a runbook that checks ADS health rather than to a human first. 

1.  **Watch fill rate as the leading indicator:** Alarm on AdDecisionServer.FillRate trending down, which exposes an ADS returning fewer ads per avail before it starts failing outright. Use fill rate as the degradation signal and the error metrics as the failure signal. 

1.  **Scale the ADS on a capacity-proportional signal:** Configure [Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html) against concurrent VAST request volume rather than a latency percentile, since latency stays flat until saturation and then spikes, which makes it a poor scaling input. Set the target so response latency stays inside the timeout budget from step 3, and pre-scale ahead of scheduled live events instead of waiting for reactive scale-out. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL03-BP01 Use a full regional deployment for compute resources through Auto Scaling groups and compute container orchestrators](advrel03-bp01.md) 
+  [ADVREL01-BP04 Implement chaos engineering practices](advrel01-bp04.md) 

 **Related documents:** 
+  [AWS Elemental MediaTailor Ad Behavior Configuration](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html) 
+  [Monitoring MediaTailor with Amazon CloudWatch metrics](https://docs.aws.amazon.com/mediatailor/latest/ug/monitoring-cloudwatch-metrics.html) 
+  [MediaTailor slate ad insertion](https://docs.aws.amazon.com/mediatailor/latest/ug/slate-management.html) 

 **Related services:** 
+  [Amazon ECS](https://aws.amazon.com/ecs/) 
+  [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 