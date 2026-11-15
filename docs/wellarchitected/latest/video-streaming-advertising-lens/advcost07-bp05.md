

# ADVCOST07-BP05 Implement cross-platform yield optimization to maximize revenue per infrastructure dollar
<a name="advcost07-bp05"></a>

 Without unified inventory visibility, publishers can't shift demand to the highest-yielding channel in real time. When you over-allocate linear inventory, you owe makegoods, and the digital inventory you could have sold goes unused. 

 **Desired outcome:** 
+  Inventory is dynamically allocated across linear, digital, and CTV to maximize total yield. 
+  Makegoods from over-allocated linear inventory are reduced by 20–40% through better allocation. 
+  Total portfolio yield (revenue per total available impressions across all channels) is tracked as the primary yield KPI. 

 **Common anti-patterns:** 
+  Managing linear and digital inventory allocation independently with separate yield optimization teams and tools, which limits real-time demand shifting between channels and loses revenue when one channel has excess demand while another has unsold inventory. 
+  Measuring yield performance in siloed KPIs (linear delivery against GRP guarantees, digital fill rate and eCPM separately) rather than total portfolio yield, so cross-channel inefficiencies are masked where over-delivery on one channel coexists with under-monetization on another. 
+  Accepting makegoods as a normal cost of linear TV operations rather than treating them as a yield allocation failure. 
+  Defaulting unsold premium digital inventory to low-CPM programmatic backfill without first evaluating whether the audience segment could command higher value through linear or CTV allocation, which underprices inventory that cross-channel visibility would correctly value. 
+  Implementing cross-channel yield optimization as a manual, periodic review process (weekly or monthly reallocation meetings) rather than automated, real-time rules and ML-based recommendations that respond to demand signals as they shift throughout the day and across campaign flights. 

 **Benefits of establishing this best practice:** 
+  Increase revenue 10–30% by shifting demand to highest-yielding channels without adding infrastructure 
+  Reduce makegood costs (wasted linear inventory) by 20–40% through better allocation 
+  Reduce revenue loss from under-priced digital inventory that could command premium linear CPMs 
+  Improve advertiser ROI (retaining budgets) by delivering optimal cross-channel reach 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Cross-channel yield optimization means allocating advertising inventory across linear TV, digital, and CTV to maximize total revenue per available impression. Without unified visibility into inventory value across channels, publishers can't identify when demand exceeds supply on one channel while another has unsold inventory. The result is simultaneous over-delivery (triggering makegoods on linear) and under-monetization (defaulting premium digital inventory to low-CPM programmatic backfill). 

 Total portfolio yield unifies cross-channel performance as total revenue divided by total available impressions across all channels. Siloed KPIs (such as linear GRP delivery, digital fill rate, and digital eCPM) can all look healthy individually while the portfolio as a whole is underperforming. A linear team delivering 100% against GRP guarantees might be over-delivering to compensate for schedule compression, which triggers no-charge makegood impressions that could have been sold at full price on digital or CTV. 

 When linear inventory is over-allocated relative to available supply, the publisher owes additional no-charge impressions to make advertisers whole. Each makegood is demand that could have been redirected to digital or CTV at full CPM. Reducing makegoods by 20–40% through better allocation converts wasted impressions into revenue without additional infrastructure. 

 Real-time allocation requires real-time demand signals. Batch-based reallocation (weekly planning meetings where teams negotiate inventory shifts) can't respond to intraday demand fluctuations. Bid request volume, win rates, floor prices, and linear delivery pacing change throughout the day. Streaming data architecture ingests these signals continuously and produces allocation recommendations that respond to current conditions. 

 Linear sales, digital programmatic, and CTV operations often report to different leaders with different revenue targets. Optimizing portfolio yield sometimes means shifting inventory away from one team's quota to another's, which creates internal conflict. Executive sponsorship and a shared portfolio yield target (rather than per-channel targets) resolve this by aligning incentives. Without organizational alignment, technical capability alone can't produce optimal allocation because teams resist shifts that reduce their individual metrics. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Build a unified yield dashboard in Quick:** Connect Quick to the unified data lakehouse. Build dashboards showing real-time CPM, fill rate, and revenue by inventory type (linear, digital, and CTV) in a single cross-channel view. This visibility is the prerequisite for data-driven yield optimization decisions. 

1.  **Ingest real-time demand signals through Kinesis:** Collect real-time signals (bid request volume, win rates, floor prices, and linear delivery pacing) into Kinesis Data Streams. Feed these into a Flink streaming application that computes rolling yield optimization recommendations. 

1.  **Implement automated allocation rules for cross-channel yield:** Configure rules that automatically shift unsold premium digital inventory to programmatic exchanges when demand exists, and redirect overflow digital demand to available linear and CTV inventory when digital is sold out. Track these allocation decisions for revenue attribution. 

1.  **Define total portfolio yield as the primary KPI:** Define portfolio yield = total revenue / total available impressions across all channels. Track this metric daily in Quick. Set alerts when cross-channel yield gap exceeds 10% of theoretical maximum, triggering manual yield review. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [AWS Guidance for Advertising Agency Planning Management](https://aws.amazon.com/solutions/guidance/advertising-agency-planning-management-on-aws/) 

 **Related services:** 
+  [Quick](https://aws.amazon.com/quicksight/) 
+  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) 
+  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) 