

# ADVSUS03-BP06 Continuously measure fabric utilization and retire unjustified capacity

 RTB traffic volume, bid rates, and partner mix fluctuate over time, so resource consumption varies with them. Ongoing monitoring shows where you can reduce resources to lower environmental impact. 

 **Desired outcome:** 
+  RTB Fabric resource consumption is tracked continuously against defined KPIs. Efficiency metrics such as transaction volume, no-bid ratio, average payload size, and compute use are tracked alongside campaign metrics like win rate and CPM (plus click-through where meaningful). 
+  Resource allocation is adjusted in response to observed demand and partner-mix shifts, so provisioned capacity stays aligned with actual bidding workload. 
+  Sustainability and cost signals are visible to operators through dashboards, enabling data-driven allocation decisions rather than static over-provisioning. 

 **Common anti-patterns:** 
+  Provisioning RTB Fabric capacity for peak bidding volume once and leaving it fixed, so idle resources persist through low-traffic periods. 
+  Monitoring only campaign performance metrics while ignoring resource-efficiency proxies such as compute use per thousand bid requests or resource use per impression. 
+  Treating measurement as a one-time tuning exercise rather than an ongoing feedback loop tied to changing traffic and partner onboarding. 

 **Benefits of establishing this best practice:** 
+  Reduced energy and carbon footprint by retiring resources that are not justified by current bidding demand. 
+  Lower operating cost from right-sizing RTB Fabric capacity to observed usage. 
+  Faster detection of efficiency regressions as traffic patterns and partner mix evolve. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Transaction volume, no-bid ratios, payload sizes, and the balance of internal to external partner traffic all move over a campaign's life and as new partners onboard. The footprint that fit the workload at launch falls out of alignment. This is capacity drift: provisioned capacity stays constant while demand changes. Drift accumulates slowly and rarely shows up in a single snapshot, so keeping RTB Fabric efficient depends on ongoing measurement of actual use. 

 Efficiency signals and campaign signals can diverge, so track them separately. Campaign metrics like win rate and CPM (plus click-through where meaningful) can stay healthy while compute use per thousand bid requests degrades. Correlate the signals to distinguish a demand increase, which might justify more capacity, from an efficiency regression, which justifies investigation. Efficiency proxies such as resource consumed per impression expose waste that revenue metrics miss. 

 Infer energy for an RTB workload from resource metrics like compute use and data movement, and treat that estimate as a proxy. Reason from resource proxies, and use account-level carbon as a check against long-term drift. 

 An efficiency review needs a named owner and a rhythm tied to events that create demand, especially partner onboarding and traffic-mix shifts. Without a named owner, dashboards become stale, unread artifacts, and allocation reverts to static over-provisioning. The owner also decides how much short-term traffic volatility to absorb before adjusting capacity. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define resource and campaign KPIs:** Set KPIs for resource metrics (transaction volume, no-bid ratio, average payload size, and compute use) alongside campaign metrics like win rate and CPM, so efficiency can be evaluated against business outcomes. 

1.  **Visualize billed transaction volume with the CUDOS Dashboard:** Use the Cost and Usage Dashboards Operations Solution (CUDOS) Dashboard to visualize RTB Fabric spend and billed transaction volume over time, including the split between traffic routed inside and outside the fabric. CUDOS draws exclusively on the AWS Cost and Usage Report, so it shows billed usage rather than operational performance. Read latency and throughput from the CloudWatch metrics RTB Fabric publishes natively, alongside bid response rates. 

1.  **Analyze consumption patterns with Cost Explorer:** Use AWS Cost Explorer to understand resource consumption patterns and identify trends in spend that correlate with bidding demand. 

1.  **Build sustainability-focused dashboards:** Generate Quick dashboards for resource consumed per RTB impression and for compute-use metrics, and incorporate account-level carbon data from the AWS Sustainability service to expose efficiency signals not captured by campaign reporting. 

1.  **Evaluate traffic composition and onboarding:** Regularly evaluate the internal to external traffic ratio and partner onboarding progress to anticipate shifts in resource demand. 

1.  **Re-evaluate campaigns and adjust allocation:** As campaigns progress, continually re-evaluate them and adjust resource allocation to meet sustainability goals. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS03-BP01 Align partner connectivity capacity with bid activity to reduce idle energy draw](advsus03-bp01.md) 
+  [ADVSUS04-BP01 Continually measure resource consumption of agentic AI advertising workloads, and adjust model and agent allocation accordingly](advsus04-bp01.md) 

 **Related documents:** 
+  [Guidance for Deploying a Data Transfer Dashboard for AdTech on AWS](https://aws.amazon.com/solutions/guidance/deploying-a-data-transfer-dashboard-for-adtech-on-aws/) 
+  [Guidance for Capturing Advertising OpenRTB Events for Analytics on AWS](https://docs.aws.amazon.com/solutions/capturing-advertising-openrtb-real-time-bidding-events-for-analytics-on-aws/) 

 **Related services:** 
+  [Amazon Athena](https://aws.amazon.com/athena/) 
+  [AWS Data Exports](https://aws.amazon.com/aws-cost-management/aws-data-exports/) 
+  [AWS Sustainability service](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) 
+  [Quick](https://aws.amazon.com/quicksight/) 