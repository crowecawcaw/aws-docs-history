

# ADVREL05-BP04 Monitor partner-facing bid gateway health independently per Region

 During a Regional impairment, you need visibility in each Region into gateway health to confirm the failure, watch the surviving Region absorb traffic, and judge when the impaired Region has recovered. Infrastructure metrics can't determine these aspects of an impairment. For example, a gateway can report healthy connections and sub-budget latency while bid responses arrive after the exchange's tmax and are discarded upstream. Region-specific monitoring must include auction-side signals, break down per exchange partner endpoint, and reconcile against the exchange's own view of your availability. 

 **Desired outcome:** 
+  All RTB Fabric gateway metrics carry a Region dimension, and auction-side signals (bid response rate inside tmax, timeout rate, invalid-response rate, no-bid rate, win rate, clearing price) are emitted per Region and per exchange partner endpoint, so each Region's and each partner's health is visible independently. 
+  Availability in each Region is reconciled against exchange-reported timeout and impression counts, so you notice a divergence between your view and the partner's view. 
+  Asymmetry alarms distinguish a Regional impairment (share shifts across all partners) from a partner-side routing change (share shifts for one partner), against a daypart baseline. 
+  Amazon Route 53 health-check status and DNS failover behavior are observable, confirming failover triggers as expected during an event. 
+  Failback readiness is a measured state, confirmed by auction-quality signals and restored QPS allocation, not by gateway health checks alone. 

 **Common anti-patterns:** 
+  Aggregating metrics across Regions, or across exchange partners within a Region, so a single degraded Region or one partner's endpoint disappears into healthy aggregate traffic. 
+  Monitoring only infrastructure signals per Region (connections, throughput, 5xx, latency), which stay healthy while bid responses miss tmax and are discarded by the exchange. 
+  Measuring bid latency at your own gateway rather than against each exchange's tmax, so a partner with a tighter timeout degrades. 
+  Treating your own telemetry as a single authoritative source, with no reconciliation against exchange-reported timeout rates or impression counts. 
+  Shipping bid logs through a pipeline that terminates in the Region being observed, so the auction-side signal is lost exactly when the event starts. 
+  Declaring the impaired Region recovered on infrastructure health alone, returning traffic to a fleet with cold targeting indexes and no restored QPS allocation. 

 **Benefits of establishing this best practice:** 
+  A regional impairment is detected quickly and unambiguously rather than being hidden in aggregate metrics. 
+  Auction-side signals detect commercially-important failure modes such as missed tmax, lost wins, and suppressed spend. 
+  Reconciliation against exchange-reported counts catches impairments that are visible only from the partner's side, including QPS throttling applied in response to your timeouts. 
+  Per-partner breakdown separates a Regional problem from a single partner's routing or integration change, avoiding a failover performed for the wrong reason. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Region-based monitoring during an event helps you confirm that the Region is truly failing, provides a way to watch the surviving Region take up the traffic, and helps you recognize when the impaired Region is healthy enough to resume. Signals gathered in each Region are the precondition for making data-backed decisions with confidence. 

 The exchange's deadline defines success: a bid response that arrives after tmax is discarded upstream and never appears as an error in your telemetry. A gateway can have connections, report throughput, and show a healthy p99 against your own latency budget while failing every auction it is involved in. The signals that indicate Regional impairment are the valid bid response rate inside each partner's timeout, the timeout and invalid-response rates, and the auction outcomes such as win rate, no-bid rate, and clearing price. 

 Partner-facing gateways terminate connections from distinct exchanges, each with its own timeout and network path. A fault in one partner's path is a Regional problem for that partner, invisible in the Region's aggregate. Monitor at the grain of Region combined with exchange partner endpoint. A consolidated view hosted in the Region that fails is useless. The data pipeline must also run outside the Region it observes, or the auction-side signal disappears when the event begins. Your own telemetry does not provide a complete understanding in this scenario, because exchanges measure your availability from their side and shape QPS down to bidders that time out. Reconciling your per-Region counts against partner-reported figures makes the measurement two-sided, and a persistent divergence is itself a finding. 

 Asymmetry between Regions is an early warning. Compare each Region's share against a baseline, not a static threshold, and verify that the baseline reflects partner-side routing, daypart, and live events. Break the comparison down for each partner, where a shift across all partners indicates a Regional problem, while a shift for one indicates a partner-side change. Infrastructure health returning does not confirm recovery. A recovered Region still has cold targeting and pacing state, and whatever reduced QPS allocation the exchange applied during the event. Measure readiness by matching the healthy Region on auction-quality signals under a ramped share of traffic. Confirm restored allocation against partner-reported figures before completing the ramp. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Add a Region dimension to all gateway metrics:** Instrument Amazon CloudWatch metrics with a Region dimension for all RTB Fabric gateway metrics (connection counts, bid request throughput, error rates, response latency). Use these as the baseline infrastructure layer rather than as the primary health signal. 

1.  **Emit auction-side signals for each Region and exchange partner endpoint:** Publish, with both a Region and a partner dimension, the valid bid response rate inside that partner's tmax, timeout rate, invalid-response rate (OpenRTB validation failures), no-bid rate, win rate, and clearing price. Measure response time against each partner's configured tmax rather than a single internal latency budget, so a partner with a tighter timeout cannot degrade without an alarm. 

1.  **Set independent alarms for each Region and partner, and reconcile against exchange-reported figures:** Alarm for each Region on both infrastructure and auction-side metrics, and add alarms for each Region and partner grain so degradation confined to one exchange endpoint is not absorbed by healthy aggregate traffic. Ingest partner-reported timeout rates and impression counts where exchanges expose them, alarm on sustained divergence, and treat a drop in shaped QPS as a high-severity signal. 

1.  **Alarm on cross-Region asymmetric distribution against a daypart baseline:** Compare each Region's share of bid requests against a baseline that accounts for time of day, day of week, and known live events rather than a static threshold. Evaluate the asymmetry per partner as well as in aggregate. A shift across all partners indicates Regional degradation, while a shift for a single partner indicates a partner-side routing or integration change. 

1.  **Keep telemetry and dashboards independent of the Region observed, and probe from partner-representative vantage points:** Verify that bid log and metric aggregation for a Region does not terminate in that Region, and deploy dashboards independently for each Region with a cross-Region consolidated view hosted in a separate operations Region. Monitor Route 53 health-check status using CloudWatch in us-east-1 (or AWS Global Accelerator endpoint health where that is the failover pattern), send synthetic OpenRTB bid probes that assert a valid response inside the relevant tmax, and track nurl and burl resolution failure rate in each Region so impressions won near failover are displayed as revenue at risk during the event. 

1.  **Gate failback on measured auction readiness:** Define failback as a ramp with explicit exit criteria. Return a small share of traffic to the recovered Region, require its bid response rate inside tmax, win rate, and clearing price to match the healthy Region before increasing the share, and confirm restored QPS allocation against partner-reported figures. Encode the readiness conditions as checks (for example, Amazon Route 53 Application Recovery Controller) so the decision is made based on automation and data. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL05-BP02 Monitor Availability Zone-level health and detect asymmetric failures](advrel05-bp02.md) 
+  [ADVREL05-BP03 Deploy partner-facing bid gateways in multiple AWS Regions](advrel05-bp03.md) 
+  [ADVREL05-BP05 Maintain independent operational readiness in each Region](advrel05-bp05.md) 

 **Related documents:** 
+  [Using Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_crossaccount_dashboard.html) 
+  [Amazon Route 53 health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html) 
+  [Amazon Route 53 Application Recovery Controller readiness checks](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.html) 
+  [Using synthetic monitoring with Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon Route 53](https://aws.amazon.com/route53/) 
+  [Amazon Route 53 Application Recovery Controller](https://aws.amazon.com/route53/application-recovery-controller/) 
+  [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 