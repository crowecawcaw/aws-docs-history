

AWS FinOps Agent is in preview release and is subject to change.

# What is AWS FinOps Agent (preview)?

**Note**  
**Powered by Amazon Bedrock**: AWS FinOps Agent is built on Amazon Bedrock and includes [automated abuse detection](https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html) implemented in Amazon Bedrock to enforce safety, security, and the responsible use of AI.

AWS FinOps Agent is a frontier agent that makes it easy for customers to continuously monitor costs, investigate anomalies, and surface optimization opportunities across their cloud environments.

AWS FinOps Agent provides:
+ **Event-triggered cost anomaly investigation.** Configure the agent to listen for AWS Cost Anomaly Detection events and produce a consolidated investigation report, delivered to Jira or Slack.
+ **Cost inquiry in natural language.** Ask cost questions about your workloads and get answers using your cost and usage data.
+ **Recurring cost reporting.** Schedule recurring cost reports (for example, daily, weekly, or monthly) rendered in a downloadable, presentation-ready format in HTML, PDF, or PPT.
+ **Optimization opportunities in one place.** Pull recommendations from AWS Cost Optimization Hub and AWS Compute Optimizer, and summarize them into a Jira ticket so the engineering team can pick up the work in the tool they already use.
+ **Organization-wide coverage.** Read cost and usage data across every account in your AWS organization from your management account or a delegated administrator account, including accounts added later. For more information, see [Setting up organization-wide access and a delegated administrator](setting-up-organization-access.md).
+ **Resource-level cost attribution with Data Hub.** Connect the agent to a Data Hub dataset to attribute cost to individual resources, charge spend back to the teams that own them, and track unit cost over time, without building a cost data pipeline. For more information about Data Hub, see [Data Hub](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-hub.html) in the *AWS Billing User Guide*.
+ **Context files and memory.** Upload organization-specific context files. The agent applies them to its answers and remembers your preferences across sessions.

For how to use each feature, see [Chatting with AWS FinOps Agent](chatting-with-finops-agent.md), [Task management](task-management.md), and [Context files and memory](context-files-and-memory.md).

## Related services
<a name="related-services"></a>

AWS FinOps Agent integrates with AWS services that you permit during the [agent creation](creating-an-agent.md) process, or through the service-linked role for organization-wide agents. For the full list of IAM actions, see the [AWS FinOps Agent IAM setup guide](setting-up.md).
+ **AWS Cost Explorer**. Cost and usage data retrieval, forecasting, Savings Plans and Reserved Instance analysis.
+ **AWS Cost Anomaly Detection**. Anomaly monitoring and detection.
+ **AWS Cost Optimization Hub**. Optimization recommendations and savings estimates.
+ **AWS Compute Optimizer**. Detailed rightsizing and resource recommendations.
+ **AWS CloudTrail**. API activity logs for identifying infrastructure changes during anomaly investigations.
+ **AWS Organizations**. Organization-wide access and delegated administrator registration.
+ **Data Hub**. A managed, SQL-based data layer over your cost and usage data that the agent queries for resource-level attribution, chargeback, and unit cost. For more information, see [Data Hub](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-hub.html) in the *AWS Billing User Guide*.

To get started, see [Creating an agent](creating-an-agent.md).