

AWS FinOps Agent is in preview release and is subject to change.

# AWS FinOps Agent use cases
<a name="chatting-with-finops-agent"></a>

The chat area in the web application is the primary way to interact with AWS FinOps Agent. From a single conversation, you can ask cost questions in plain language and get answers using your cost and usage data, investigate cost anomalies to root cause, surface optimization recommendations, and generate reports. The agent reads your context files, applies what it has remembered from previous sessions, and uses connected integrations such as Jira and Slack to create a Jira ticket or post results to a Slack channel.

The following topics walk through each use case, with sample prompts. You can also turn any of these into recurring or event-driven work. For the task and automation model, see [Task management](task-management.md). For an end-to-end automation walkthrough, see [Event-triggered cost anomaly investigation](automated-anomaly-response.md).

**Note**  
**Pricing for underlying AWS API calls.** AWS FinOps Agent is offered at no charge during preview, but the agent calls AWS APIs on your behalf and you pay the standard per-request rate for those APIs. For details, see [ pricing](https://aws.amazon.com/aws-cost-management/pricing/). Other services the agent reads from, including Cost Anomaly Detection, Cost Optimization Hub, Compute Optimizer, and CloudTrail Event History, are available at no additional charge.