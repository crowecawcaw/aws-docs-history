

# ADVOPS01-BP03 Establish performance metrics by defining key performance indicators (KPIs) and service-level objectives (SLOs)
<a name="advops01-bp03"></a>

 Establishing a set of operational performance metrics helps organizations monitor and validate the performance of advertising operations. KPIs and SLOs must extend beyond infrastructure availability to cover publisher yield health (eCPM, fill rate, bids per auction, ad break completion, and identity-signal match rates) and tie operational health directly to revenue outcomes. 

 **Desired outcome:** 
+  Publisher workloads have defined KPIs covering yield health (eCPM, fill rate, and bids per auction), delivery quality (ad break completion, channel uptime, and engagement rates), and identity-signal performance across standardized frameworks (UID2, LiveRamp, and ID5). 
+  SLOs are tiered (critical, warning, and informational) with explicit revenue-impact correlation. 
+  Error budgets track SLO consumption and trigger change freezes when exhausted. 
+  For converged operations, cross-channel KPIs normalize linear metrics (GRPs and spot delivery) and digital metrics (impressions and fill rate) into unified fulfillment indicators. 

 **Common anti-patterns:** 
+  Defining SLOs only for infrastructure availability without yield-specific targets. Infrastructure SLOs can remain green while monetization suffers (for example, a Prebid auction completing within latency SLO but with reduced bid density because of adapter misconfiguration). 
+  Tracking publisher metrics in isolation without correlating them to revenue impact. 
+  Setting KPI thresholds without historical baseline analysis. 
+  Monitoring identity-signal match rates without distinguishing performance across different identity frameworks (UID2, LiveRamp, and ID5). 
+  Using static thresholds for campaign pacing alerts instead of anomaly detection based on historical patterns. 

 **Benefits of establishing this best practice:** 
+  Revenue-aligned operational targets that let teams prioritize incident response. 
+  Early detection of yield degradation through SLO breach alerting. 
+  Data-driven capacity planning informed by yield-correlated metrics. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Infrastructure-only SLOs miss yield failures that reduce revenue. A prebid auction can complete within its latency SLO while bid density drops 40% from an adapter misconfiguration, generating far less revenue. 

 Publisher yield KPIs form a hierarchy with eCPM at the top. eCPM is revenue per thousand impressions, so it reflects bid density and winning bid prices but not fill rate. An unfilled opportunity never enters the denominator, so eCPM can rise while revenue falls. For a single number that includes fill rate, use a request-based figure such as revenue per thousand ad requests. Fill rate measures the fraction of ad opportunities that are monetized. Bids per auction measures demand competition, while identity-signal match rates measure how effectively audience data passes through the programmatic supply chain. 

 SLO tiering reduces alert fatigue while giving critical issues an immediate response. A critical SLO breach triggers immediate incident response (for example, prebid auction p99 latency exceeding 80% of configured timeout, or fill rate dropping more than 10% below the 7-day average). A warning SLO breach triggers investigation within a defined window (for example, eCPM declining 5% from the 7-day rolling average). Informational KPIs feed trend analysis without triggering automated response. 

 Each SLO has an allowable error rate over a period. When that budget is exhausted, freeze non-critical changes to the affected workload until the SLO recovers. Teams with high error budget consumption must stabilize before shipping new features. 

 For converged linear and digital operations, add campaign delivery pacing as a unified fulfillment KPI. It measures the percentage of ordered delivery completed against the flight schedule, combining linear spot count against ordered spots with digital impression delivery against booked impressions. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory all publisher yield metrics across workload themes:** Catalog eCPM, fill rate, bids per auction, timeout rate, SGAI ad break completion rate, FAST channel uptime, ad pod fill rate, viewer hours, and innovative format engagement rates. For each metric, identify the data source, update frequency, and the team responsible for monitoring. 

1.  **Establish historical baselines:** Use a minimum of 4 weeks of production data to establish baselines for each metric. Calculate p50, p90, and p99 distributions, weekly seasonality patterns, and daypart patterns. These baselines give you the reference points for threshold setting, since a threshold set without one is only a guess. 

1.  **Define tiered SLOs with revenue-impact correlation:** Assign each metric to a tier (critical, warning, and informational) based on the revenue impact of a breach. Configure critical SLO breaches to trigger immediate incident response through PagerDuty, SNS, or equivalent alerting. Configure warning SLO breaches to trigger investigation tickets with a defined SLA for first response. Define the revenue impact formula for critical SLOs so that incident responders understand the business stakes. 

1.  **Configure error budgets and change-freeze policies:** For each critical SLO, define an error budget (for example, 99.5% fill rate SLO = 0.5% error budget per period). Configure automated monitoring of error budget consumption using Amazon CloudWatch. When error budget is exhausted (consumption rate projects full consumption before period end), automatically trigger a change freeze for the affected workload by using an AWS Systems Manager Automation document that blocks deployments. 

1.  **Review and refine SLO thresholds monthly:** Review SLO thresholds monthly based on operational experience. Adjust baselines as workload patterns evolve (new demand partners onboarded, seasonal audience shifts, new creative formats launched). Use the monthly review to identify KPIs where static thresholds generate excessive false positives and replace them with CloudWatch Anomaly Detection-based alarms. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS02-BP01 Implement monitoring across each layer of your advertising stack](advops02-bp01.md) 
+  [ADVOPS02-BP02 Collect and analyze detailed metrics for successful operations and ad campaigns](advops02-bp02.md) 

 **Related documents:** 
+  [Improve application reliability with effective SLOs](https://aws.amazon.com/blogs/mt/improve-application-reliability-with-effective-slos/) 
+  [Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon Managed Grafana](https://aws.amazon.com/grafana/) 
+  [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) 