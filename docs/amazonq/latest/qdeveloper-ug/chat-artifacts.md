# Using Q artifacts in Amazon Q

Amazon Q artifacts enable Amazon Q to deliver responses enriched with table and chart visualizations. When you ask natural language questions
about your resources, Amazon Q may display an artifact that helps you quickly understand your resources at a glance.

The Q experience is now more usable and useful. Access Q easily from the navigation bar next to search. The Q chat panel opens on the left
and can expand to full screen. A new prompt library helps you discover useful example prompts.

To get started, ensure you have the required permissions, and then review the example prompts to get the most out of Amazon Q artifacts.
For more information, see [Prerequisites](#chat-artifacts-prereqs "#chat-artifacts-prereqs") and [Example prompts](#chat-artifacts-example-prompts "#chat-artifacts-example-prompts").

## Prerequisites

To view visualizations with Amazon Q see [Allow users to chat with Amazon Q](id-based-policy-examples-users.md#id-based-policy-examples-allow-chat "id-based-policy-examples-users.md#id-based-policy-examples-allow-chat") and [Chatting about your costs](chat-costs.md#cost-chat-getting-started "chat-costs.md#cost-chat-getting-started").

## How it works

###### Note

All data associated with Amazon Q visualizations is saved in us-east-1.

**To view Q artifacts in Amazon Q in the AWS management Console:**

1. Sign in to the AWS Management Console.
2. Access Amazon Q by choosing the Q icon in the Unified Navigation bar.
3. Describe your task to Amazon Q using natural language. For example:
   1. "List my running EC2 instances"
   2. "Create a chart of my costs by region last month"

4. If Amazon Q determines a visual interface would be helpful, it automatically displays an artifact in a new panel next to Q chat with either a table or chart visualization.
   1. If you are asking about resources, the panel will include:
      1. A table with the resources you asked about, categorized based on any properties you specify.
      2. Deep links to the resources that redirect you to the resource page in the service console.

   2. If you are asking about cost and billing information with chart visualization, the panel will include a chart widget.

## Example prompts

The following categories and associated prompts are examples of the types of tasks you can complete with Amazon Q artifacts.

- **View resource information** – Visualize resource information in table or chart format.
- **Get billing recommendations and forecasts** – Show me a line chart of my forecasted costs for the next 6 months, Graph RDS costs by instance type by month for the last 6 months.
- **Security and compliance** – Check traffic and internet accessibility to EC2 resources, verify internet connectivity for EC2 instances across regions.

For a list of suggested use cases, choose the Amazon Q prompt library icon in the top-right of the Q chat panel and filter by table or visualization response type.
