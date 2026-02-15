# Chatting about your costs

Amazon Q Developer is a generative artificial intelligence (AI) powered conversational assistant that can help you understand, build, extend, and operate AWS applications. Amazon Q Developer provides powerful capabilities to help you manage your AWS costs through natural conversation. You can analyze your historical and forecasted costs from Cost Explorer, discover cost-saving recommendations from Cost Optimization Hub and AWS Compute Optimizer, understand Savings Plans and reservation opportunities, and get instant answers about AWS product attributes or service pricing. Amazon Q Developer can both answer specific questions (e.g., "What were net unblended costs for EC2 instances last month?") or perform complex or open-ended analysis (e.g., "What were the biggest drivers of last week's cost decrease?"). Amazon Q Developer transforms how you interact with AWS cost data by letting you ask questions in your own words instead of learning query syntax or navigating multiple console pages, while providing precise answers backed by real data from your AWS account and showing exactly which APIs were called and where to find the information in the console.

For more information about the cost management capabilities in Amazon Q Developer, see [Managing your costs using generative AI with Amazon Q Developer](../../../cost-management/latest/userguide/ce-cost-analysis-q.md "../../../cost-management/latest/userguide/ce-cost-analysis-q.md") in the _AWS Cost Management User Guide_.

## What you can do

With Amazon Q Developer, you can:

- **Analyze your costs** – Ask questions about your historical spending patterns, cost trends, and forecasted costs. For example, "What were my EC2 costs last month?" or "Why did my costs increase last week?"
- **Find optimization opportunities** – Discover ways to reduce your AWS spending by asking about recommendations from Cost Optimization Hub, AWS Compute Optimizer, and Savings Plans. For example, "What are my top cost optimization opportunities?" or "Which EC2 instances are over-provisioned?"
- **Understand pricing** – Get instant answers about AWS service pricing. For example, "How much does a c8g.2xlarge instance cost in us-east-1?" or "What would it cost to store 1 PB in S3 in Dublin?"
- **Check payment status** – List recent invoices and check payment balance. For example, “List my invoices for the last 6 months” and “Do I have an outstanding payment balance?”
- **Visualize your costs** – Generate custom charts and graphs of historical costs and usage, service pricing, budgets, and more. For example, “Show me a graph of how much we’re spending in each region” or “Create a chart breaking down EC2-Other costs last month”.

Amazon Q Developer adapts to however you phrase your questions. You can ask specific questions when you know exactly what you want, or ask open-ended exploratory questions and let Q investigate on your behalf. Q maintains context throughout your conversation, so you can ask follow-up questions to dive deeper or guide the analysis in a specific direction.

## How it works

When you ask Amazon Q Developer about your costs, Q retrieves data from AWS Cost Explorer, Cost Optimization Hub, AWS Compute Optimizer, and other AWS services. Q performs calculations, analyzes patterns, and provides insights based on your actual usage and spending data. With each response, Q provides transparency into how it arrived at its answer by showing you the API calls it made, the parameters used, and links to matching views in the AWS Management Console where available. This helps you verify the data and explore further.

## Getting started

To chat about your AWS costs, you need:

- **Appropriate IAM permissions** – Your IAM identity must have permissions to chat with Amazon Q and access your billing data. For an IAM policy that grants the required permissions, see [Allow Amazon Q
  to access cost data and provide cost optimization recommendations](id-based-policy-examples-users.md#id-based-policy-examples-allow-cost-chat "id-based-policy-examples-users.md#id-based-policy-examples-allow-cost-chat").
- **Cost Explorer opt-in** – You must enable AWS Cost Explorer in your AWS account. To enable Cost Explorer, open the [Cost Explorer console](https://console.aws.amazon.com/costmanagement/home#/cost-explorer "https://console.aws.amazon.com/costmanagement/home#/cost-explorer"). For more information, see [Enabling Cost Explorer](../../../cost-management/latest/userguide/ce-enable.md "../../../cost-management/latest/userguide/ce-enable.md") in the _AWS Cost Management User Guide_.

To take advantage of the full range of Amazon Q Developer's cost management capabilities, you can also enable additional services such as AWS Cost Optimization Hub or AWS Budgets. To learn more, see [Overview of cost management capabilities in Amazon Q Developer](../../../cost-management/latest/userguide/ce-q-overview.md "../../../cost-management/latest/userguide/ce-q-overview.md") in the _AWS Cost Management User Guide_.

To get started:

1. Sign in to the AWS Management Console at [https://console.aws.amazon.com](https://console.aws.amazon.com "https://console.aws.amazon.com").
2. Choose the Amazon Q icon on the right side of the console navigation bar.
3. Ask a question about your costs, such as:
   - "What were my costs last month?"
   - "What are my top cost optimization opportunities?"
   - "How much does a c8g.2xlarge instance running Linux cost in us-east-1?"
   - “Show me a pie chart of my costs by region last week”

You can also configure Amazon Q Developer in chat applications such as Slack and Microsoft Teams. For more information about using Amazon Q Developer in chat applications, see [Chatting with Amazon Q Developer in chat applications](q-in-chat-applications.md "q-in-chat-applications.md").

## Example questions

Following are example questions about costs that you can ask Amazon Q Developer:

**Cost analysis**

- "What were my costs last month?"
- "Show me my EC2 spending trends for the past six months."
- "What are the top contributing services to my AWS bill in the eu-central-1 region?"
- "Why did my costs increase last week?"
- "Analyze my spending data for the last month and give me the most important insights."

**Cost optimization**

- "What are my top cost optimization opportunities?"
- "Which EC2 instances are over-provisioned?"
- "Do I have any idle resources?"
- "Which Savings Plans should I purchase?"

**Budget and anomaly monitoring**

- "Have any teams exceeded their budgets?"
- "Do I have any cost anomalies?"

**Pricing estimation**

- "How much does a c8g.2xlarge instance cost in us-east-1?"
- "What would it cost to store 1 PB in S3 in Dublin?"
- "What's the monthly cost of a t4g.xlarge RDS instance with Multi-AZ and 300 GB gp2 storage?"
- "What would be the price to build a basic three tier web app, with a small EC2 instance, API gateway, a ~5GB SQL database, and a basic JS front-end hosted in CloudFront?"

**Cost visualization**

- “Graph my support charges by month for the last 12 months”
- “Show me an area chart of EC2 costs by instance type by day this month”
- “Create a chart of S3 storage pricing by tier in us-east-1”"
- “Line chart of Savings Plans coverage and utilization % over the last 3 months”
- “Graph EC2 cost per vCPU hour over the last 3 weeks”
