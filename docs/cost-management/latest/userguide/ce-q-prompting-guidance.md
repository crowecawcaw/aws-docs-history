# Prompting guidance for Amazon Q Developer

The following content provides guidance on the types of cost management questions that
Amazon Q Developer supports, and how to structure your prompts to achieve the best
results.

## Supported question categories

With the cost management capabilities in Amazon Q Developer, you can ask a wide variety of
questions to understand your historical and forecasted costs, find savings
opportunities, and understand AWS service pricing. For best results, we recommend
phrasing your questions similarly to the following question categories.

| Capability                           | Question category                                                                                                                                                                                            | Example                                                               |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| Cost analysis                        | Total costs                                                                                                                                                                                                  | What were my costs last month?                                        |
| Costs for a specific dimension value | What were my costs for S3 last month?                                                                                                                                                                        |
| Costs broken down by a dimension     | What were my costs by service last month?                                                                                                                                                                    |
| Top filter or bottom filter          | What were my five most expensive services last month?                                                                                                                                                        |
| Costs by charge type                 | Did we receive any credits last month?                                                                                                                                                                       |
| Costs for a relative time period     | What were my costs last week?                                                                                                                                                                                |
| Costs for an absolute time period    | What were my costs from 10/1/2024 to 10/7/2024?                                                                                                                                                              |
| Time period aggregation              | What were my costs for Q1?                                                                                                                                                                                   |
| Usage types                          | How much did we spend on EBSVolumeUsage:io2 last month?                                                                                                                                                      |
| API operations                       | What was the spend on the NatGateway operation yesterday?                                                                                                                                                    |
| Total cost forecasts                 | What is our cost forecast for this month?                                                                                                                                                                    |
| Usage amounts                        | How many EC2 instance hours did we use last month?                                                                                                                                                           |
| Cost allocation tags                 | What was last month’s spend for tag key = “Application”, value =<br>“web-app-1”?                                                                                                                             |
| Cost categories                      | What was last month’s spend, broken down by cost category “cost<br>center”?                                                                                                                                  |
| Month-over-month changes             | What services increased the most between April and May?                                                                                                                                                      |
| List items                           | What instance types did we use last month?                                                                                                                                                                   |
| Cost metrics                         | What were my net amortized costs last month?                                                                                                                                                                 |
| Cost optimization                    | General optimization opportunities                                                                                                                                                                           | What cost optimization opportunities do I have?                       |
| Resource-specific opportunities      | Show me EC2 optimization recommendations                                                                                                                                                                     |
| Savings threshold                    | What recommendations save more than $100 per month?                                                                                                                                                          |
| Top recommendations                  | What are my top five cost optimization opportunities?                                                                                                                                                        |
| Specific optimization types          | Show me recommendations for purchasing reservations                                                                                                                                                          |
| Idle resource identification         | Which resources are idle and can be removed?                                                                                                                                                                 |
| Rightsizing opportunities            | Which of my RDS instances are over-provisioned?                                                                                                                                                              |
| Implementation guidance              | What are the steps to migrate this instance to Graviton?                                                                                                                                                     |
| Recommendation details               | Tell me more about that first recommendation                                                                                                                                                                 |
| Savings summary                      | How much could I save in total from all recommendations?                                                                                                                                                     |
| Effort prioritization                | What are some easy ways to lower costs?                                                                                                                                                                      |
| Pricing and cost estimation          | Instance pricing                                                                                                                                                                                             | How much does a c8g.2xlarge instance running Linux cost in us-east-1? |
| Service pricing                      | How much does AWS charge for RDS extended support?                                                                                                                                                           |
| Product attributes                   | How many vCPUs does a p3.16xlarge instance have?                                                                                                                                                             |
| Regional availability                | What Regions are p5en instances available in?                                                                                                                                                                |
| Workload estimates                   | I need to send 5 million notifications per month to various<br>endpoints: 3 million to mobile push, 1 million to email, and 1<br>million to HTTP/S endpoints. Estimate the monthly cost using Amazon<br>SNS. |
| Price comparisons between services   | What is the cost difference between an Application Load Balancer<br>and a Network Load Balancer?                                                                                                             |
| Price comparisons between Regions    | What’s the difference in pricing for S3 Glacier between<br>ap-southeast-1 and us-west-2?                                                                                                                     |

For questions about other areas of cost management (such as questions about your budgets,
Savings Plans utilization, or payments), Amazon Q Developer can provide general guidance that
doesn't consider your account's specific cost data.

## Prompting tips

The cost analysis and cost optimization capabilities in Amazon Q Developer work best when your
prompts are clear and specific. For best results when analyzing your costs with
Amazon Q Developer, we recommend that you follow these guidelines.

- For cost analysis questions, specify the date range you’re interested in. You can express
  a date range as either an absolute date range (for example, "October 2024")
  or a relative date range (for example, “last month”).
- Specify the dimension you’re interested in. For example, asking “How did
  last month’s costs break down by service?” will yield better results than
  “What am I being charged for?”.
- For cost analysis questions, you can filter or group your costs by cost categories or
  cost allocation tags. Cost categories and cost allocation tags are both
  key-value pairs. To request cost data by cost category or cost allocation
  tag, precisely specify the key and, if applicable, the values of interest.
  For example, ask questions such as “What was last month’s spend, broken down
  by cost category ‘cost center’?” or “What was last month’s spend for tag key
  = ‘Application’, value = ‘web-app-1’?”. Amazon Q Developer can best understand your
  tag data if you follow [Best Practices for Tagging AWS Resources](../../../whitepapers/latest/tagging-best-practices/defining-needs-and-use-cases.md "../../../whitepapers/latest/tagging-best-practices/defining-needs-and-use-cases.md").
  Filtering and grouping by cost category and cost allocation tag is not
  supported for cost optimization questions.
- You can phrase your prompts as questions, commands, or descriptions of the cost data you
  want. For example, “What are my EC2 recommendations?”, “Show me EC2
  recommendations”, and “Top EC2 cost optimization recommendations” are all
  valid prompts.
