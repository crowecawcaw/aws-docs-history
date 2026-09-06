

AWS FinOps Agent is in preview release and is subject to change.

# Investigating cost anomalies
<a name="cost-anomaly-detection"></a>

Ask the agent to investigate why [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) anomalies occurred and perform root-cause analysis. The agent retrieves the anomaly details, analyzes the root causes ranked by cost impact, and presents its findings directly in the conversation.

The agent determines whether cost increases were driven by higher usage, higher rates, or both. When CloudTrail permissions are enabled, the agent searches CloudTrail event history for API activity correlated with the cost change.

The depth of root-cause analysis depends on which permissions are enabled in the agent's IAM role:


| Permissions enabled | Investigation depth | 
| --- | --- | 
| Cost Explorer only | Anomaly details with affected services, accounts, cost impact, cost trends, and rate-vs-usage analysis. | 
| Cost Explorer and CloudTrail | Full investigation including the above, plus a search of CloudTrail event history for API activity correlated with the cost change. | 

You can ask the agent to save the investigation as a downloadable file, create a Jira ticket with the summary, or post the result to a Slack channel.

To investigate anomalies automatically whenever AWS Cost Anomaly Detection detects one, without starting a conversation each time, see [Event-triggered cost anomaly investigation](automated-anomaly-response.md).

Sample prompts:
+ “Have there been any cost anomalies in the past 7 days? Investigate them.”
+ “Why did our costs jump this week?”
+ “Tell me more about the MemoryDB anomaly. What happened?”
+ “When a cost anomaly is detected on my production monitor, investigate the root cause and post the summary to {{<slack-channel>}}.”
+ “Set up monitoring so I'm alerted if this happens again at the same threshold, and auto-investigate.”