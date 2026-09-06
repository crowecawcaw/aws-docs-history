

AWS FinOps Agent is in preview release and is subject to change.

# Asking about costs
<a name="cost-inquiry"></a>

Ask questions about your AWS spend in natural language. The agent retrieves data from services, processes the results, and responds with answers based on your account data. The agent can break down spend by service, account, Region, or tag, compare time periods, and summarize Savings Plans and Reserved Instance utilization.

The agent accesses the following services through its configured IAM role:


| Data source | What it provides | 
| --- | --- | 
| AWS Cost Explorer | Cost and usage data with flexible grouping and filtering, cost forecasts, usage forecasts, dimension values, tags, cost categories, Savings Plans coverage and utilization and purchase recommendations, Reserved Instance coverage and utilization and purchase recommendations. | 
| AWS Cost Anomaly Detection | Detected anomalies and anomaly monitors. | 
| AWS Cost Optimization Hub | Cost-saving recommendations and recommendation summaries across services. | 
| AWS Compute Optimizer | Rightsizing recommendations for EC2, Auto Scaling groups, EBS, Lambda, RDS, ECS, and idle resource detection. | 

The depth of the agent's responses depends on which IAM permissions are enabled. If a data source is not granted, the agent disables the tools that depend on it and notes the limitation in its response. For the full list of IAM actions, see the [AWS FinOps Agent IAM setup guide](setting-up.md).

You can ask follow-up questions within the same conversation to refine results or explore related topics. The agent retains context across sessions through memory and applies preferences you have explicitly recorded, such as preferred cost views or common breakdowns, in future interactions.

Sample prompts:
+ “Summarize our AWS costs for last month compared to the month before.”
+ “What were our top 5 cost drivers last month? Break it down by service.”
+ “Which services had the biggest increase?”
+ “Show me EC2 costs by Region for the last 3 months.”
+ “What's our month-over-month spend trend?”
+ “Show me spend by linked account.”
+ “Show me costs grouped by cost-center tag.”
+ “What's the cost forecast for next month?”