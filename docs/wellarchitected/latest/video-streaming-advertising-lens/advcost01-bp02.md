

# ADVCOST01-BP02 Evaluate resiliency needs against the cost of downtime for ad delivery and bidding

 Compare the cost of running resilient infrastructure against the cost of going without it. With those numbers, you can choose Multi-Region deployments, backup strategies, and recovery approaches that balance cost against business continuity. 

 **Desired outcome:** 
+  You have a clear, quantified understanding of the financial impact of downtime for each campaign and can compare it directly against the cost of implementing resiliency measures. 
+  Investment in resiliency is proportional to the business value at risk, avoiding both over-spending and under-protection. 
+  Architecture decisions are justified with concrete financial data rather than assumptions. 

 **Common anti-patterns:** 
+  Assuming resiliency is too expensive without quantifying the actual cost of downtime. 
+  Applying the same level of resiliency to all campaigns regardless of their revenue potential or criticality. 
+  Evaluating resiliency costs in isolation without factoring in reputational damage, customer churn, or contractual penalties associated with downtime. 
+  Implementing resiliency measures reactively after a major outage rather than proactively as part of architecture planning. 

 **Benefits of establishing this best practice:** 
+  Investment in resiliency is proportional to the business value at risk. 
+  Stakeholders have a shared understanding of acceptable risk levels and the trade-offs involved. 
+  Reduced likelihood of catastrophic revenue loss during high-value campaign periods. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 RTB downtime economics differ from typical web applications because missed bid opportunities are gone permanently. An ecommerce customer might return after an outage. A bid request not answered within 100ms goes to a competitor and never comes back. This makes availability investment in RTB a direct function of opportunity cost per second. 

 Calculating that opportunity cost isn't straightforward because RTB revenue is probabilistic. You lose the expected value of bids you would have won. That value depends on your historical win rate, average clearing price, and traffic volume at that moment. Use this formula: 

 (bids per second) × (win rate) × (average revenue per win) × (seconds of downtime) = expected revenue loss 

 This number varies by orders of magnitude depending on time of day, day of week, and whether a high-value campaign is active. 

 Make-good obligations amplify downtime cost beyond missed revenue. Advertising contracts often require publishers to deliver a guaranteed number of impressions within a campaign window. If downtime interrupts delivery, the publisher owes no-cost impressions after the campaign ends. Those impressions could otherwise generate revenue from other advertisers. A 10-minute outage during a tentpole campaign can create make-good liability that exceeds the direct revenue loss by 2-3x. 

 Peak and off-peak value differ enough that you must tier resiliency. Live sporting events, season premieres, and holiday shopping peaks concentrate a disproportionate share of annual revenue into narrow windows. Year-round maximum resiliency is expensive and wasteful. Burst resiliency (scaling up redundancy for scheduled high-value windows and running leaner during off-peak) costs less overall but requires operational discipline to activate and deactivate correctly. This approach fails if operators forget to scale up before a tentpole event or scale down too early. 

 Multi-AZ active-active within a single Region handles the most common failure mode (single-AZ outage) at modest incremental cost, typically 10-30% above single-AZ deployment. Multi-region active-passive adds a warm standby in a second region for regional failure scenarios, roughly doubling infrastructure cost but covering a much rarer event. Multi-region active-active provides the lowest RTO but the highest cost and operational complexity, including the challenge of keeping bid-decision state synchronized across regions. The right choice depends on your downtime cost calculation. Choose active-passive when 5 minutes of regional failover costs less in lost revenue than the active-active premium. 

 Tier campaigns by contracted revenue (what you are obligated to deliver), reputational exposure (whether the advertiser's brand team will notice an outage), and time-concentration (whether the campaign's value is spread evenly or spiked around specific events). A campaign with high contracted revenue, a brand-sensitive advertiser, and value concentrated in a 3-hour live event window needs maximum resiliency during that window. A long-running programmatic campaign with no delivery guarantees and steady daily traffic can tolerate lower resiliency at significant cost savings. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Quantify the cost of downtime for each campaign tier:** For Tier 1 campaigns (high-value live events, tentpole campaigns), calculate expected revenue per minute of availability and multiply by realistic failure scenario durations. Include indirect costs: reputation damage, contractual SLA penalties, make-good obligations. Document these figures as the cost of downtime for each tier. 

1.  **Estimate the cost of resiliency measures for each tier:** Use the AWS Pricing Calculator to model costs of proposed resiliency configurations (multi-AZ, Multi-Region, backup and recovery). Compare the annualized cost of the resiliency investment against the expected value of prevented outages (probability of outage × cost per outage). Document the business case for each resiliency investment. 

1.  **Implement differentiated resiliency by campaign tier:** Deploy the highest resiliency tier (Multi-AZ active-active, automated failover) only for Tier 1 campaigns that justify the cost. Apply cost-appropriate resiliency to lower-tier campaigns (periodic snapshots, read replica failover). Document the resiliency tier and rationale for each campaign category. 

1.  **Review the analysis periodically as campaign revenue and AWS pricing evolve:** Revisit the downtime cost compared to resiliency cost analysis annually or when campaign revenue profiles change significantly. Update the analysis when AWS pricing changes, as new services may provide better cost-performance points for resiliency. Use AWS Resilience Hub to continuously validate that resiliency targets are being met at the documented investment level. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Establishing RPO and RTO Targets for Cloud Applications](https://aws.amazon.com/blogs/mt/establishing-rpo-and-rto-targets-for-cloud-applications/) 
+  [Stage 1: Set objectives](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/stage-1.html) 

 **Related services:** 
+  [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) 
+  [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/) 
+  [AWS Pricing Calculator](https://calculator.aws/#/) 