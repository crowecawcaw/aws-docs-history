

# Overview of cost management capabilities in AWS assistant

The AWS assistant is a generative artificial intelligence (AI) powered conversational assistant that can help you understand, analyze, and optimize your AWS costs. With the AWS assistant, you can ask complex, open-ended questions about your costs and let the AWS assistant perform the analysis on your behalf. The AWS assistant explores your cost data, forms and tests hypotheses, gathers information from multiple sources, performs calculations, and provides custom visualizations and actionable insights, all through a natural language conversation.

The AWS assistant helps you get deeper cost insights with less time and expertise. Instead of manually exploring data across multiple tools, adjusting filters, and performing offline calculations, you can delegate the analytical work to the AWS assistant. This is particularly valuable for teams without dedicated FinOps expertise, as the AWS assistant reduces the learning curve by handling the complexity of knowing which tools to use, which APIs to call, and how to structure queries.

For more information about the AWS assistant, see [What is AWS assistant](https://docs.aws.amazon.com/assistant/latest/userguide/what-is.html) in the *AWS assistant User Guide*.

## What you can do
<a name="q-what-you-can-do"></a>

The AWS assistant provides powerful capabilities across a wide range of cost management use cases:

**Understand your costs**

Analyze your historical spending patterns, view cost breakdowns by service or account, and track trends over time. For example, you can ask "What were my costs by service last month?" or "Show me my EC2 spending trends for the past six months."

**Investigate cost changes**

Perform root cause analysis to understand why your costs changed. The AWS assistant can explore your data, identify the drivers of cost increases or decreases, and help you understand period-over-period changes. For example, you can ask "Why did my costs increase last week?" and the AWS assistant will investigate the underlying causes.

**Find savings opportunities**

Identify cost optimization recommendations from Cost Optimization Hub, AWS Compute Optimizer, and Savings Plans and reservation recommendations. The AWS assistant can help you find idle resources, rightsizing opportunities, and commitment-based discount opportunities. For example, you can ask "What are my top cost optimization opportunities?" or "Which EC2 instances are over-provisioned?". You can also ask detailed follow-up questions, such as "Tell me more about the second recommendation" or "Why was that EBS volume classified as idle?".

**Monitor cost health**

Check your budget status, identify cost anomalies, and monitor your free tier usage. The AWS assistant can alert you to unusual spending patterns and help you stay within your budget targets. For example, you can ask "Have any teams exceeded their budgets?" or "Do I have any cost anomalies?"

**Estimate future costs**

Understand AWS service pricing and estimate the cost of new workloads you plan to build. The AWS assistant can help you compare pricing across regions, calculate costs for specific configurations, and forecast future spending. For example, you can ask "How much would it cost to store 1 PB in S3 in Dublin?" or "What's my cost forecast for this month?"

**Analyze commitment performance**

Review your Savings Plans and Reserved Instances coverage and utilization to understand how effectively you're using commitment-based discounts. The AWS assistant can identify underutilized commitments and opportunities to improve your discount coverage. For example, you can ask "Analyze our Savings Plans performance over the last month."

**Check payment status**

List previously-issued invoices, check whether you have an outstanding payment balance, and check which payment methods you have set up.

## How to use it
<a name="q-how-to-use"></a>

The AWS assistant adapts to however you phrase your questions. You can ask specific, bounded questions when you know exactly what you want, or ask open-ended exploratory questions and let the AWS assistant investigate on your behalf.

### Example questions
<a name="q-example-questions"></a>

**Specific questions**

When you know what data you need, you can ask targeted questions:
+ "What were my net amortized S3 costs last month?"
+ "Show me EC2 rightsizing recommendations."
+ "How much does a c8g.2xlarge instance cost in us-east-1?"

**Open-ended questions**

When you want the AWS assistant to explore and analyze your costs, you can ask broader questions:
+ "Why did my costs increase last week?"
+ "Analyze my cost data and give me insights."
+ "What are some easy ways to lower my costs?"

**Multi-step analytical questions**

The AWS assistant can handle complex questions that require gathering data from multiple sources and performing calculations:
+ "What's my effective cost per EC2 instance hour after Savings Plans discounts?"
+ "Which accounts had the biggest cost increases and what drove them?"
+ "Analyze our Savings Plans performance and identify optimization opportunities."

**Estimation questions**

The AWS assistant can help you estimate costs for new workloads or compare pricing across regions:
+ "How much would it cost to store 1 PB in S3 in Dublin?"
+ "What's the monthly cost of a t4g.xlarge RDS instance with Multi-AZ and 300 GB gp2 storage?"
+ "What would be the price to build a basic three tier web app, with a small EC2 instance, API gateway, a \~5GB SQL database, and a basic JS front-end hosted in CloudFront?"

**Visualizations**

You can create charts and graphs to visualize your cost data:
+ "Chart S3 costs by storage tier last week"
+ "Graph my DynamoDB costs by region by day for the last 30 days"
+ "Graph RDS costs by instance type for the last 6 months"
+ "Show me an area chart of EC2-Other costs over the last 12 months"

### Tips for getting the most value
<a name="q-tips-for-value"></a>

**Use follow-up questions to steer the analysis**

The AWS assistant maintains context within a conversation, so you can ask follow-up questions to dive deeper or guide the analysis in a specific direction:
+ Initial question: "Why did my costs increase last month?"
+ Follow-up: "Next, check if any Savings Plans expired."
+ Follow-up: "Focus on the EC2."

**Be specific when you know what you want**

While the AWS assistant can handle open-ended questions, being more specific helps you get answers faster if you know exactly what you are looking for:
+ Instead of: "Tell me about my costs"
+ Try: "What were my net amortized EC2 instance costs in us-east-1 last month?"

**Use key-value pairs for tags and cost categories**

When filtering by cost allocation tags or cost categories, if you know the specific keys and values you want to use, you can specify them:
+ Instead of: "How much did we spend in prod last month?"
+ Try: "What was last month's spend for tag key='Environment', value='Production'?"

## User experience
<a name="q-user-experience"></a>

### Transparency
<a name="q-transparency"></a>

With each response, the AWS assistant provides transparency into how it arrived at its answer:
+ **API calls displayed**: The AWS assistant shows you the details of each API call it makes, including the exact parameters used. This allows you to understand precisely what data the AWS assistant retrieved.
+ **Console deep-links**: Where available, the AWS assistant provides links to matching views in the AWS Management Console, so you can verify the data or explore further.

This transparency helps you build trust in the AWS assistant's responses and gives you the information you need to provide more specific instructions in follow-up questions.

### Conversational and iterative
<a name="q-conversational"></a>

The AWS assistant maintains context throughout your conversation, enabling a natural, iterative dialogue:
+ **Ask follow-up questions**: You can ask follow-up questions to dive deeper into specific aspects of the analysis. For example, after the AWS assistant identifies that EC2 costs increased, you can ask "Which accounts had the highest EC2 cost increases?". You can also ask questions about generated visualizations, such as "What drove that increase on Wednesday?"
+ **Steer the analysis**: You can guide the AWS assistant's investigation by providing specific directions. For example, "Next, check if any Savings Plans expired" or "Focus on the production environment." For visualizations, you can request changes with follow-up prompts like "Let's switch from a bar chart to a line chart."
+ **Refine your questions**: If a response isn't quite what you need, you can rephrase or add more details to get a more targeted answer.

### Actionable insights
<a name="q-actionable-insights"></a>

The AWS assistant goes beyond simple data retrieval to provide meaningful insights:
+ **Interprets findings**: The AWS assistant not only provides facts and data, it also identifies patterns, highlights anomalies, and explains what the data means.
+ **Identifies opportunities**: The AWS assistant proactively surfaces cost optimization opportunities and potential issues in your spending.
+ **Provides guidance**: For optimization recommendations, the AWS assistant can explain the steps needed to implement the changes.

## Multi-account cost management
<a name="q-multi-account"></a>

For customers logged into the management account of an AWS organization, the AWS assistant automatically aggregates cost data from all member accounts in the organization. You can filter or group costs by member account, just as you would in Cost Explorer.

You can also create custom billing views to define custom multi-account aggregations. Custom billing views allow you to aggregate data from multiple member accounts or even multiple organizations. Once you create a custom billing view, the aggregations are available in both Cost Explorer and the AWS assistant. For more information, see [Getting started with custom billing views](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-billing-views.html). To use a custom billing view in the AWS assistant, specify the name of the billing view you'd like to use for your conversation with a prompt like "I'd like you to use the cross-org-rollup billing view for the rest of this conversation." Custom billing views are supported for historical and forecasted cost data and budgets data.

## Getting started
<a name="ce-q-getting-started"></a>

**Prerequisites**

To use the cost management capabilities in the AWS assistant, you need:
+ **Appropriate IAM permissions**: You need permissions to use the AWS assistant and to access the underlying Billing and Cost Management services. For details, see [Security for cost management capabilities in AWS assistant](ce-q-security.md).
+ **Cost Explorer opt-in**: To analyze your historical and forecasted costs, you must first opt in to Cost Explorer. To opt in, open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/). After you opt in, it can take up to 24 hours for AWS to process your cost and usage data.

To take advantage of the full range of cost management capabilities, you can also:
+ **Opt in to Cost Optimization Hub**: To receive personalized cost optimization recommendations, opt in to [Cost Optimization Hub](https://console.aws.amazon.com/costmanagement/home#/cost-optimization-hub), and then choose **Enroll**. After you opt in, it can take up to 24 hours for recommendations to be calculated.
+ **Opt in to Compute Optimizer**: To receive resource optimization recommendations, such as rightsizing EC2 instances or terminating idle EBS volumes, opt in to [Compute Optimizer](https://console.aws.amazon.com/compute-optimizer/).
+ **Create budgets**: To monitor your spending against budget targets, create budgets in [AWS Budgets](https://console.aws.amazon.com/billing/home#/budgets).
+ **Create a cost anomaly detection monitor**: To identify unusual spending patterns, create a cost anomaly detection monitor in [AWS Cost Anomaly Detection](https://console.aws.amazon.com/costmanagement/home#/anomaly-detection).
+ **Enable resource-level data, hourly data, and extended history**: To access resource-level cost data, hourly granularity, and up to 38 months of cost history, configure these settings on the [Cost Management Preferences page](https://console.aws.amazon.com/costmanagement/home#/settings?activeTabId=costExplorer).

**Start a conversation with AWS assistant**

1. Sign in to the AWS Management Console at [https://console.aws.amazon.com](https://console.aws.amazon.com).

1. Choose the AWS assistant icon on the right side of the console navigation bar.

1. Ask a question about your costs, such as:
   + "What were my costs last month?"
   + "What are my top cost optimization opportunities?"
   + "How much does a c8g.2xlarge instance running Linux cost in us-east-1?"
   + "Show me a pie chart of my costs by region last week"

### Use Amazon Q Developer in chat applications
<a name="q-chat-applications"></a>

You can also chat about your AWS costs in Microsoft Teams and Slack. Amazon Q Developer in chat applications allows you to ask cost questions directly from your team's chat channels, making it easy to collaborate on cost analysis and optimization without switching contexts. For example, you can ask "@Amazon Q what were my EC2 costs last month?" or "@Amazon Q what are my top cost optimization opportunities?" directly in your Slack or Teams channel.

To get started with Amazon Q Developer in chat applications, see [Chatting with Amazon Q Developer in chat applications](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-chat-applications.html) in the *Amazon Q Developer User Guide*.

## Next steps
<a name="q-next-steps"></a>

After you start using the AWS assistant for cost management, you can:
+ Learn more about [How the cost management capabilities in AWS assistant work](ce-q-how-it-works.md) to understand the agentic architecture and data sources
+ Review [Security for cost management capabilities in AWS assistant](ce-q-security.md) to ensure your team has appropriate access
+ Explore the full range of capabilities by asking open-ended questions like "Analyze my costs and give me insights"
+ Set up additional services like Cost Optimization Hub and Budgets to unlock more capabilities

## Pricing
<a name="ce-q-pricing"></a>

The cost management capabilities in the AWS assistant are included with the AWS assistant. Under the Amazon Q Developer Free Tier, you can ask up to 25 questions per account per month that require account or resource context to answer (including cost management questions). Beyond this free tier limit, an Amazon Q Developer Pro subscription is required.

For more information, see [Amazon Q Developer pricing](https://aws.amazon.com/q/developer/pricing/).