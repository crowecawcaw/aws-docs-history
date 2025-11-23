# Overview of cost management capabilities in Amazon Q Developer

Amazon Q Developer is a generative artificial intelligence (AI) powered conversational assistant that can help you understand, analyze, and optimize your AWS costs. With Amazon Q Developer, you can ask complex, open-ended questions about your costs and let Q perform the analysis on your behalf. Q explores your cost data, forms and tests hypotheses, gathers information from multiple sources, performs calculations, and provides actionable insights, all through a natural language conversation.

Amazon Q Developer helps you get deeper cost insights with less time and expertise. Instead of manually exploring data across multiple tools, adjusting filters, and performing offline calculations, you can delegate the analytical work to Q. This is particularly valuable for teams without dedicated FinOps expertise, as Q reduces the learning curve by handling the complexity of knowing which tools to use, which APIs to call, and how to structure queries.

For more information about Amazon Q Developer, see [What is Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/what-is.md "../../../amazonq/latest/qdeveloper-ug/what-is.md") in the _Amazon Q Developer User Guide_.

## What you can do

Amazon Q Developer provides powerful capabilities across a wide range of cost management use cases:

### Understand your costs

Analyze your historical spending patterns, view cost breakdowns by service or account, and track trends over time. For example, you can ask "What were my costs by service last month?" or "Show me my EC2 spending trends for the past six months."

### Investigate cost changes

Perform root cause analysis to understand why your costs changed. Q can explore your data, identify the drivers of cost increases or decreases, and help you understand period-over-period changes. For example, you can ask "Why did my costs increase last week?" and Q will investigate the underlying causes.

### Find savings opportunities

Identify cost optimization recommendations from Cost Optimization Hub, AWS Compute Optimizer, and Savings Plans and reservation recommendations. Q can help you find idle resources, rightsizing opportunities, and commitment-based discount opportunities. For example, you can ask "What are my top cost optimization opportunities?" or "Which EC2 instances are over-provisioned?". You can also ask detailed follow-up questions, such as "Tell me more about the second recommendation" or "Why was that EBS volume classified as idle?".

### Monitor cost health

Check your budget status, identify cost anomalies, and monitor your free tier usage. Q can alert you to unusual spending patterns and help you stay within your budget targets. For example, you can ask "Have any teams exceeded their budgets?" or "Do I have any cost anomalies?"

### Estimate future costs

Understand AWS service pricing and estimate the cost of new workloads you plan to build. Q can help you compare pricing across regions, calculate costs for specific configurations, and forecast future spending. For example, you can ask "How much would it cost to store 1 PB in S3 in Dublin?" or "What's my cost forecast for this month?"

### Analyze commitment performance

Review your Savings Plans and Reserved Instances coverage and utilization to understand how effectively you're using commitment-based discounts. Q can identify underutilized commitments and opportunities to improve your discount coverage. For example, you can ask "Analyze our Savings Plans performance over the last month."

## How to use it

Amazon Q Developer adapts to however you phrase your questions. You can ask specific, bounded questions when you know exactly what you want, or ask open-ended exploratory questions and let Q investigate on your behalf.

### Example questions

**Specific questions**

When you know what data you need, you can ask targeted questions:

- "What were my net amortized S3 costs last month?"
- "Show me EC2 rightsizing recommendations."
- "How much does a c8g.2xlarge instance cost in us-east-1?"

**Open-ended questions**

When you want Q to explore and analyze your costs, you can ask broader questions:

- "Why did my costs increase last week?"
- "Analyze my cost data and give me insights."
- "What are some easy ways to lower my costs?"

**Multi-step analytical questions**

Q can handle complex questions that require gathering data from multiple sources and performing calculations:

- "What's my effective cost per EC2 instance hour after Savings Plans discounts?"
- "Which accounts had the biggest cost increases and what drove them?"
- "Analyze our Savings Plans performance and identify optimization opportunities."

**Estimation questions**

Q can help you estimate costs for new workloads or compare pricing across regions:

- "How much would it cost to store 1 PB in S3 in Dublin?"
- "What's the monthly cost of a t4g.xlarge RDS instance with Multi-AZ and 300 GB gp2 storage?"
- "What would be the price to build a basic three tier web app, with a small EC2 instance, API gateway, a ~5GB SQL database, and a basic JS front-end hosted in CloudFront?"

### Tips for getting the most value

**Use follow-up questions to steer the analysis**

Amazon Q Developer maintains context within a conversation, so you can ask follow-up questions to dive deeper or guide the analysis in a specific direction:

- Initial question: "Why did my costs increase last month?"
- Follow-up: "Next, check if any Savings Plans expired."
- Follow-up: "Focus on the EC2."

**Be specific when you know what you want**

While Q can handle open-ended questions, being more specific helps you get answers faster if you know exactly what you are looking for:

- Instead of: "Tell me about my costs"
- Try: "What were my net amortized EC2 instance costs in us-east-1 last month?"

**Use key-value pairs for tags and cost categories**

When filtering by cost allocation tags or cost categories, if you know the specific keys and values you want to use, you can specify them:

- Instead of: "How much did we spend in prod last month?"
- Try: "What was last month's spend for tag key='Environment', value='Production'?"

## User experience

### Transparency

With each response, Amazon Q Developer provides transparency into how it arrived at its answer:

- **API calls displayed**: Q shows you the details of each API call it makes, including the exact parameters used. This allows you to understand precisely what data Q retrieved.
- **Console deep-links**: Where available, Q provides links to matching views in the AWS Management Console, so you can verify the data or explore further.

This transparency helps you build trust in Q's responses and gives you the information you need to provide more specific instructions in follow-up questions.

### Conversational and iterative

Amazon Q Developer maintains context throughout your conversation, enabling a natural, iterative dialogue:

- **Ask follow-up questions**: You can ask follow-up questions to dive deeper into specific aspects of the analysis. For example, after Q identifies that EC2 costs increased, you can ask "Which accounts had the highest EC2 cost increases?"
- **Steer the analysis**: You can guide Q's investigation by providing specific directions. For example, "Next, check if any Savings Plans expired" or "Focus on the production environment."
- **Refine your questions**: If a response isn't quite what you need, you can rephrase or add more details to get a more targeted answer.

### Actionable insights

Amazon Q Developer goes beyond simple data retrieval to provide meaningful insights:

- **Interprets findings**: Q doesn't just show you numbers—it identifies patterns, highlights anomalies, and explains what the data means.
- **Identifies opportunities**: Q proactively surfaces cost optimization opportunities and potential issues in your spending.
- **Provides guidance**: For optimization recommendations, Q can explain the steps needed to implement the changes.

## Multi-account cost management

For customers logged into the management account of an AWS organization, Amazon Q Developer automatically aggregates cost data from all member accounts in the organization. You can filter or group costs by member account, just as you would in Cost Explorer.

You can also create custom billing views to define custom multi-account aggregations. Custom billing views allow you to aggregate data from multiple member accounts or even multiple organizations. Once you create a custom billing view, the aggregations are available in both Cost Explorer and Amazon Q Developer. For more information, see [Getting started with custom billing views](../../../awsaccountbilling/latest/aboutv2/custom-billing-views.md "../../../awsaccountbilling/latest/aboutv2/custom-billing-views.md"). To use a custom billing view in Amazon Q Developer, specify the name of the billing view you'd like to use for your conversation with a prompt like "I'd like you to use the cross-org-rollup billing view for the rest of this conversation." Custom billing views are supported for historical and forecasted cost data and budgets data.

## Getting started

**Prerequisites**

To use the cost management capabilities in Amazon Q Developer, you need:

- **Appropriate IAM permissions**: You need permissions to use Amazon Q Developer and to access the underlying Billing and Cost Management services. For details, see [Security for cost management capabilities in Amazon Q
  Developer](ce-q-security.md "ce-q-security.md").
- **Cost Explorer opt-in**: To analyze your historical and forecasted costs, you must first opt in to Cost Explorer. To opt in, open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/"). After you opt in, it can take up to 24 hours for AWS to process your cost and usage data.

To take advantage of the full range of cost management capabilities, you can also:

- **Opt in to Cost Optimization Hub**: To receive personalized cost optimization recommendations, opt in to [Cost Optimization Hub](https://console.aws.amazon.com/costmanagement/home#/cost-optimization-hub "https://console.aws.amazon.com/costmanagement/home#/cost-optimization-hub"), and then choose **Enroll**. After you opt in, it can take up to 24 hours for recommendations to be calculated.
- **Opt in to Compute Optimizer**: To receive resource optimization recommendations, such as rightsizing EC2 instances or terminating idle EBS volumes, opt in to [Compute Optimizer](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
- **Create budgets**: To monitor your spending against budget targets, create budgets in [AWS Budgets](https://console.aws.amazon.com/billing/home#/budgets "https://console.aws.amazon.com/billing/home#/budgets").
- **Create a cost anomaly detection monitor**: To identify unusual spending patterns, create a cost anomaly detection monitor in [AWS Cost Anomaly Detection](https://console.aws.amazon.com/costmanagement/home#/anomaly-detection "https://console.aws.amazon.com/costmanagement/home#/anomaly-detection").
- **Enable resource-level data, hourly data, and extended history**: To access resource-level cost data, hourly granularity, and up to 38 months of cost history, configure these settings on the [Cost Management Preferences page](https://console.aws.amazon.com/costmanagement/home#/settings?activeTabId=costExplorer "https://console.aws.amazon.com/costmanagement/home#/settings?activeTabId=costExplorer").

###### Start a conversation with Amazon Q Developer

1. Sign in to the AWS Management Console at [https://console.aws.amazon.com](https://console.aws.amazon.com "https://console.aws.amazon.com").
2. Choose the Amazon Q icon on the right side of the console navigation bar.
3. Ask a question about your costs, such as:
   - "What were my costs last month?"
   - "What are my top cost optimization opportunities?"
   - "How much does a c8g.2xlarge instance running Linux cost in us-east-1?"

### Use Amazon Q Developer in chat applications

You can also chat about your AWS costs in Microsoft Teams and Slack. Amazon Q Developer in chat applications allows you to ask cost questions directly from your team's chat channels, making it easy to collaborate on cost analysis and optimization without switching contexts. For example, you can ask "@Amazon Q what were my EC2 costs last month?" or "@Amazon Q what are my top cost optimization opportunities?" directly in your Slack or Teams channel.

To get started with Amazon Q Developer in chat applications, see [Chatting with Amazon Q Developer in chat applications](../../../amazonq/latest/qdeveloper-ug/q-in-chat-applications.md "../../../amazonq/latest/qdeveloper-ug/q-in-chat-applications.md") in the _Amazon Q Developer User Guide_.

## Next steps

After you start using Amazon Q Developer for cost management, you can:

- Learn more about [How the cost management capabilities in Amazon Q Developer work](ce-q-how-it-works.md "ce-q-how-it-works.md") to understand the agentic architecture and data sources
- Review [Security for cost management capabilities in Amazon Q
  Developer](ce-q-security.md "ce-q-security.md") to ensure your team has appropriate access
- Explore the full range of capabilities by asking open-ended questions like "Analyze my costs and give me insights"
- Set up additional services like Cost Optimization Hub and Budgets to unlock more capabilities

## Pricing

The cost management capabilities in Amazon Q Developer are included with Amazon Q Developer. Under the Amazon Q Developer Free Tier, you can ask up to 25 questions per account per month that require account or resource context to answer (including cost management questions). Beyond this free tier limit, an Amazon Q Developer Pro subscription is required.

For more information, see [Amazon Q Developer pricing](https://aws.amazon.com/q/developer/pricing/ "https://aws.amazon.com/q/developer/pricing/").
