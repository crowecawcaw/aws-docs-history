

# ADVCOST01-BP01 Continually measure costs of advertising workloads, and adjust resource and model allocation accordingly
<a name="advcost01-bp01"></a>

 With fluctuations in usage over time, the costs associated with advertising workloads can vary significantly. RTB infrastructure costs scale with bid volume and campaign mix. Agentic AI costs scale with agent invocations and token consumption. To keep both under control, monitor them continually with dashboards that correlate spending to business outcomes. 

 **Desired outcome:** 
+  You have full visibility into RTB infrastructure costs and agentic AI inference costs at the campaign level, with automated dashboards and alerts that enable data-driven allocation decisions. 
+  Stakeholders receive regular cost and performance reports without manual effort, and campaigns are continuously optimized for cost-to-revenue efficiency. 
+  Cost allocation tags and inference profiles attribute costs to specific campaigns and agents, enabling accurate ROI calculations. 
+  Regular review enables identification of agents where inference cost is disproportionate to business value produced. 

 **Common anti-patterns:** 
+  Running RTB infrastructure without cost allocation tags, which prevents attribution of costs to specific campaigns or business units. 
+  Running multi-agent orchestration workflows without tracking per-agent token consumption, so agents that drive disproportionate costs cannot be identified. 
+  Reviewing costs only at the end of a billing cycle rather than continuously. 
+  Tracking only technical metrics (CPU utilization, request latency) without correlating them to business outcomes such as cost-per-click or cost-per-acquisition. 
+  Measuring only aggregate Amazon Bedrock spend without correlating costs to business outcomes, which blocks cost-to-value analysis at the agent or campaign level. 
+  Using a single foundation model for all agent tasks regardless of complexity, when smaller or cheaper models would produce equivalent results for simpler subtasks. 

 **Benefits of establishing this best practice:** 
+  Early detection of cost anomalies before they impact campaign profitability, including runaway agent loops and excessive orchestration depth. 
+  Clear attribution of both infrastructure costs and inference costs to individual campaigns, enabling accurate ROI calculations. 
+  Data-driven resource and model allocation decisions that align spending with value generation goals. 
+  Automated reporting reduces operational overhead and gives campaign managers and finance stakeholders consistent visibility. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 RTB cost attribution is harder than typical web-application cost accounting because infrastructure is shared at sub-millisecond granularity. A single bid-evaluation container processes requests for dozens of campaigns within the same second. You can't tag a CPU cycle to a specific campaign the way you tag an S3 object, so per-campaign cost measurement is an approximation. 

 Cost-to-revenue ratio combines infrastructure cost (from AWS billing data) with campaign revenue (from your DSP or SSP reporting). Infrastructure cost splits into directly attributable components (dedicated creative-serving buckets, campaign-specific pipelines) and shared components you must allocate proportionally (bid-evaluation compute, data transfer, caching). Allocating shared compute by bid volume treats all bids as equally expensive, which is wrong when some campaigns run complex ML models and others use rule-based bidding. Allocating by CPU-seconds-per-campaign is more accurate but requires instrumentation most organizations lack initially. Pick a method, document its assumptions, and refine as instrumentation matures. 

 Agentic AI advertising workloads present a different attribution challenge. A single campaign planning workflow might invoke multiple agents, each calling a foundation model several times, with costs distributed across inference, knowledge base retrieval, and action group execution. Without per-agent attribution, teams can't see which agent costs more than the business value it produces. A cost-per-business-outcome metric (total inference spend divided by completed deliverables like campaign plans or brand safety assessments) gives teams a ratio they can compare across agents and track over time. [Amazon Bedrock application inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-create.html) solve this by creating a named, taggable resource for each agent type, so every invocation appears as a distinct line item in Cost Explorer. 

 Teams tag at the account or service level, not the campaign or agent level. Cost reports then tell engineering how much DynamoDB or Bedrock costs but can't tell campaign managers whether Campaign X is profitable. Cost reviews happen monthly, which is too slow. RTB spend patterns shift daily with traffic fluctuations. Agentic AI costs can spike within hours when an agent enters a reasoning loop or a campaign launch triggers unexpectedly high invocation volumes. By the time a monthly review shows either anomaly, the overspend has already accumulated. Dashboards report cost without business context. 

 The [Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) provides line-item billing detail including resource IDs and cost allocation tags. Without tags activated and consistently applied, CUR data can't be grouped by campaign or agent type. 

 For smaller operations (fewer than 10 campaigns, uniform infrastructure), [Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) with tag-based grouping provides daily granularity and anomaly detection without additional infrastructure. For larger operations that need sub-daily granularity or dashboards combining billing data with campaign performance from non-AWS sources, a dedicated analytics layer built on the [CUDOS Dashboard](https://catalog.workshops.aws/awscid/en-US/dashboards/additional), Athena, and [Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) is appropriate. For agentic AI workloads specifically, Quick dashboards that join Bedrock cost data with application outcome logs provide the cost-per-business-outcome view that CUDOS alone can't deliver. 

 Ownership splits across engineering (which optimizes for performance and availability), campaign management (which optimizes for reach and conversion), and AI/ML teams (which optimize model selection and agent design), so no single team has visibility across all three concerns. When all stakeholders examine the same data in a joint weekly review, they reveal misalignments that any one team would miss. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define KPIs for each campaign that evaluate cost-to-revenue ratios:** Include both billing metrics (resource costs, data transfer costs, inference costs) and campaign metrics (click-through rate, cost per acquisition, fill rate, bid win rate). For agentic AI workloads, define cost-per-business-outcome metrics (cost per campaign plan, cost per brand safety assessment). Establish target ratios that define acceptable campaign economics. 

1.  **Implement cost allocation tags and inference profiles:** Apply a consistent tagging taxonomy: Campaign, Advertiser, WorkloadType (bid-evaluation, creative-serving, analytics, agent-planning, and agent-safety), and Environment (production, staging). Create [Amazon Bedrock application inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-create.html) for each agent type. Activate all tags in the AWS Billing and Cost Management console for cost allocation reporting. 

1.  **Deploy the CUDOS Dashboard to visualize billed cost and usage:** Deploy the Cost and Usage Dashboards Operations Solution from the AWS Solutions Library. CUDOS draws exclusively on the AWS Cost and Usage Report, so it reports billed cost and usage dimensions rather than operational performance, which comes from CloudWatch. Configure data exports and Athena integration to populate CUDOS with RTB-specific and Bedrock-specific cost dimensions. Use the Data Transfer tab to identify cross-AZ and cross-region transfer costs. 

1.  **Create Quick dashboards with user-configurable filters:** Build campaign-specific dashboards showing cost-per-bid, cost-per-win, fill rate, eCPM trends, and cost-per-agent-outcome. Join Bedrock cost data (from Cost Explorer exports) with application outcome logs to build cost-per-business-outcome views. Configure scheduled email delivery to campaign managers, finance, and engineering stakeholders. 

1.  **Establish a regular cadence to evaluate cost and adjust allocation:** Schedule weekly or biweekly reviews where engineering, campaign management, and AI/ML stakeholders jointly examine KPIs against cost targets. Reallocate compute between growing and declining campaigns. Adjust model assignments and agent configurations where cost-per-outcome is disproportionate. Use [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html) to alert on unexpected changes between reviews. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST01-BP02 Evaluate resiliency needs against the cost of downtime for ad delivery and bidding](advcost01-bp02.md) 

 **Related documents:** 
+  [Guidance for Deploying a Data Transfer Dashboard for AdTech on AWS](https://aws.amazon.com/solutions/guidance/deploying-a-data-transfer-dashboard-for-adtech-on-aws/) 
+  [Guidance for Capturing Advertising OpenRTB Real-Time Bidding Events for Analytics on AWS](https://docs.aws.amazon.com/solutions/capturing-advertising-openrtb-real-time-bidding-events-for-analytics-on-aws/) 
+  [Tracking, allocating, and managing your generative AI cost and usage with Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/track-allocate-and-manage-your-generative-ai-cost-and-usage-with-amazon-bedrock/) 
+  [Guidance for Advertising Agents on AWS](https://aws.amazon.com/solutions/guidance/advertising-agents-on-aws/) 
+  [Organizing costs using AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-categories.html) 
+  [Additional dashboards](https://catalog.workshops.aws/awscid/en-US/dashboards/additional) 

 **Related services:** 
+  [Amazon Athena](https://aws.amazon.com/athena/) 
+  [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) 
+  [Quick](https://aws.amazon.com/quicksight/) 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 