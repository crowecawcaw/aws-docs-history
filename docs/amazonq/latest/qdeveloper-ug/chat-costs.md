# Chatting about your costs

You can ask Amazon Q about your historical and forecasted AWS cost data as well as how to
optimize your costs. Amazon Q can retrieve your cost data, explain costs, and analyze cost
trends, so you can understand your costs without referring to documentation or interrupting
your workflow. Amazon Q can also provide recommendations on how to optimize your AWS costs,
including rightsizing instances, stopping or deleting idle or unused resources, migrating EC2 instances to
AWS Graviton-based instances, and purchasing Savings Plans.

When you ask Amazon Q about your costs, its response includes the specific parameters used
to retrieve the data, as well as a link to learn more in the AWS Management Console.

For more information about cost analysis in Amazon Q, see
[Analyzing and optimizing
your costs using generative AI with Amazon Q Developer](../../../cost-management/latest/userguide/ce-cost-analysis-q.md "../../../cost-management/latest/userguide/ce-cost-analysis-q.md") in the _AWS Cost Management User Guide_.

## Prerequisites

You can chat about your AWS costs in the AWS Management Console and in [configured chat applications](q-in-chat-applications.md "q-in-chat-applications.md").

For Amazon Q to answer questions about your costs, the following prerequisites must
be met.

### Add permissions

To chat about your costs, your IAM identity must have permissions to chat with Amazon Q, access your
billing data, and retrieve cost optimization recommendations. For an IAM policy that grants the required
permissions, see [Allow Amazon Q
to access cost data and provide cost optimization recommendations](id-based-policy-examples-users.md#id-based-policy-examples-allow-cost-chat "id-based-policy-examples-users.md#id-based-policy-examples-allow-cost-chat").

### Enable AWS Cost Explorer and AWS Cost Optimization Hub

To chat about your costs with Amazon Q, you must enable AWS Cost Explorer in your AWS
account. To enable Cost Explorer, open the Cost Explorer console. For more information, see [Enabling
Cost Explorer](../../../cost-management/latest/userguide/ce-enable.md "../../../cost-management/latest/userguide/ce-enable.md") in the _AWS Cost Management User Guide_.

To receive cost optimization recommendations from Amazon Q, you must enable
AWS Cost Optimization Hub. For more information, see [Getting
started with Cost Optimization Hub](../../../cost-management/latest/userguide/cost-optimization-hub-getting-started.md "../../../cost-management/latest/userguide/cost-optimization-hub-getting-started.md") in the _AWS Cost
Management User Guide_.

## Example questions

Following are example questions about costs that you can ask Amazon Q:

- How much did we spend on SageMaker AI in January?
- What are the top contributing services to my AWS bill in the
  `'eu-central-1'` region?
- What were my Amazon EC2 costs by instance type last week?
- What was my cost breakdown by service for the past three
  months?
- How can I lower my AWS bill?
- What are my top cost optimization opportunities?
- Are any of my Amazon EC2 instances over-provisioned?
- Which Savings Plans should I purchase?
