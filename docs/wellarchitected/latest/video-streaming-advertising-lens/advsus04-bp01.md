

# ADVSUS04-BP01 Continually measure resource consumption of agentic AI advertising workloads, and adjust model and agent allocation accordingly
<a name="advsus04-bp01"></a>

 Agent invocation volumes fluctuate over time, so resource consumption for agentic AI advertising workloads varies with them. Foundation model inference uses compute for each token, and multi-agent orchestration compounds that usage. Ongoing monitoring shows where to reduce consumption. 

 **Desired outcome:** 
+  Resource consumption for every advertising agent is measured continuously and correlated with the business value it produces, so model and agent allocation can be tuned to sustainability goals as campaigns evolve. 
+  Resource metrics such as tokens and compute utilization are attributed to individual agents and campaigns. Energy is reported as a proxy estimate derived from those metrics. 
+  Resource consumption is expressed against business outcomes, such as compute per campaign plan or compute per brand safety assessment. 
+  Agent configurations, model assignments, and orchestration patterns are re-evaluated on a recurring basis and adjusted to reduce waste. 

 **Common anti-patterns:** 
+  Treating aggregate Amazon Bedrock spend or token counts as a single number, with no attribution to individual agents, campaigns, or workflows. 
+  Measuring resource consumption once at launch and never revisiting it as agent invocation volumes change. 
+  Tracking resource metrics in isolation, without relating them to the campaign plans, brand safety assessments, or ad load recommendations the agents deliver. 
+  Leaving over-provisioned models or redundant orchestration patterns in place because their cost-to-value ratio is never reviewed. 

 **Benefits of establishing this best practice:** 
+  Resource-intensive agents and workflows are identified relative to their business value, so optimization effort goes to the agents and workflows with the weakest resource-to-value ratio. 
+  Compute per business outcome, and the energy estimated from it, trend downward as allocation is tuned over the campaign lifecycle. 
+  Sustainability and advertising operations stakeholders share visibility into the resource footprint of agentic AI workloads. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Several agents collaborate to produce an outcome, such as a media planner, an inventory optimizer, an ad load optimizer, and a brand safety monitor. Their individual token consumption compounds into one number. A total Amazon Bedrock spend or token count can't distinguish a valuable but token-heavy agent from one that runs an over-provisioned model on a redundant orchestration path. To identify inefficiency, break the aggregate down by agent, model, and campaign. 

 Energy figures are proxies estimated from resource metrics such as tokens and compute utilization. Comparisons between agents and trends for one agent over time matter more than any single absolute figure. 

 Measure compute consumption as a ratio of resources used to business outcomes delivered (for example, compute per campaign plan or compute per brand safety assessment). A raw resource number climbs whenever a campaign scales up and can look like regression when it is only more work being done. 

 Do not measure against an outcome that is easy to manipulate, such as tokens processed. Shifting work to a cheaper model that produces worse plans improves your compute cost for each token, but does not reduce total cost. Measure against an outcome that has business value, like a completed campaign plan or a delivered brand safety assessment. An improvement in the ratio then reflects real efficiency, not displaced cost. 

 Re-measure the ratio on a recurring cadence. Invocation volumes and agent behavior drift as campaigns evolve, so a ratio measured once at launch no longer describes the live workload. The mechanisms that reduce the consumption measured here, such as prompt caching, knowledge base retrieval tuning, multi-agent orchestration patterns, and inference capacity options, are not specific to advertising and are covered by the Sustainability pillar of the Generative AI Lens and by the agentic AI cost practices in ADVCOST05. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define resource-to-value KPIs:** Set KPIs for each advertising agent to evaluate resource-to-value ratios. Track both resource metrics (tokens consumed, compute utilization per agent, and energy consumption) and business metrics (campaign plans generated, brand safety assessments completed, and ad load recommendations delivered). 

1.  **Tag Bedrock resources for attribution:** Implement resource allocation tags for all Amazon Bedrock resources (agents, knowledge bases, and model invocations) relevant to campaign and agent tracking. 

1.  **Attribute consumption per agent:** Use Amazon Bedrock application inference profiles to attribute resource consumption to individual agents (media planner, inventory optimizer, ad load optimizer, and brand safety monitor). 

1.  **Visualize billed consumption with CUDOS:** Use the Cost and Usage Dashboards Operations Solution (CUDOS) Dashboard to visualize billed Amazon Bedrock consumption over time, broken down by the tags and inference profiles you configured. CUDOS draws exclusively on the AWS Cost and Usage Report, so it reports billed usage rather than per-invocation behavior, which comes from agent traces and CloudWatch. 

1.  **Analyze patterns in Cost Explorer:** Use AWS Cost Explorer to understand resource consumption patterns, filtering by Amazon Bedrock-specific dimensions. 

1.  **Report resource per business outcome:** Generate Quick dashboards that track resource-per-business-outcome: energy per campaign plan, compute per brand safety assessment, and resources per ad load optimization recommendation. 

1.  **Scope dashboards to stakeholders:** Configure Quick with user-configurable filters to allow advertising operations teams to focus on the agents and campaigns most relevant to them. 

1.  **Distribute scheduled reports:** Configure Quick to email dashboard reports to campaign managers and sustainability stakeholders on a schedule. 

1.  **Review findings with the business:** Regularly evaluate the data and report findings back to the business. Identify which agents or workflows are disproportionately resource-intensive relative to their business value. 

1.  **Re-allocate as campaigns evolve:** As campaigns progress, continually re-evaluate agent configurations, model assignments, and orchestration patterns, and adjust resource allocation to meet sustainability goals. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS04-BP02 Match model capability to task complexity to reduce agent fleet energy use](advsus04-bp02.md) 
+  [ADVCOST05-BP03 Implement prompt caching and optimize prompt design to minimize token consumption](advcost05-bp03.md) 
+  [ADVCOST05-BP05 Design small, focused agents and use appropriate orchestration patterns to minimize multi-agent collaboration costs](advcost05-bp05.md) 
+  [GENSUS03-BP01 Leverage smaller models and optimized inference techniques to reduce carbon footprint](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensus03-bp01.html) 

 **Related documents:** 
+  [Guidance for Advertising Agents on AWS](https://docs.aws.amazon.com/solutions/advertising-agents-on-aws/) 
+  [Amazon Bedrock inference profiles for cost and usage attribution](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html) 
+  [Effective cost optimization strategies for Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effective-cost-optimization-strategies-for-amazon-bedrock/) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) (Application Inference Profiles) 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 
+  [AWS Data Exports](https://aws.amazon.com/aws-cost-management/aws-data-exports/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 
+  [Quick](https://aws.amazon.com/quicksight/) 
+  [AWS Sustainability service](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) 