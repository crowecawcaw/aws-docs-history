# Overview of cost management capabilities in Amazon Q Developer

Amazon Q Developer provides powerful capabilities to help you understand and optimize your AWS
costs. These capabilities include:

- **Cost analysis**: Analyze your historical and forecasted
  AWS cost data from Cost Explorer.
- **Cost optimization**: Identify and implement cost-saving
  opportunities from Cost Optimization Hub, AWS Compute Optimizer, and Savings Plans and reservation
  recommendations.
- **Pricing and cost estimation**: Understand AWS
  service pricing and estimate the cost of new workloads.
  These capabilities use generative AI and large language models (LLMs) to interpret your
  questions, retrieve relevant cost data, and provide easy-to-understand, conversational
  responses. With each response, Amazon Q Developer displays the specific API parameters that were
  used, so you can understand exactly how Amazon Q Developer retrieved your data. Where
  applicable, it also provides links to matching views in the AWS Management console. If
  the response isn’t immediately useful, you can ask follow-up questions to expand on the
  initial response. The cost management capabilities in Amazon Q Developer uses the
  context from your current conversation to create follow-up responses.

## Cost analysis

The cost analysis capability in Amazon Q Developer works with Cost Explorer. You
can ask questions about your AWS costs and receive answers in natural language
that reflect the actual costs of your AWS account. For example, if you ask
Amazon Q Developer a question such as _“What services did I spend the most on last
month?”_, it will provide a response similar to the following:

The AWS services with the highest costs for your account last month were:

1. Amazon Relational Database Service: $2,595.55 (36.65% of total cost)
2. EC2 - Other: $1,222.71 (17.26% of total cost)
3. Amazon QuickSight: $1,006.32 (14.21% of total cost)
4. Amazon OpenSearch Service: $695.07 (9.81% of total cost)
5. Amazon ElastiCache: $482.11 (6.81% of total cost)
6. Amazon Elastic Load Balancing: $269.05 (3.80% of total cost)
7. AWS Supply Chain: $208.32 (2.94% of total cost)
8. Amazon Elastic Container Service for Kubernetes: $148.80 (2.10% of total
   cost)
9. Amazon Virtual Private Cloud: $141.50 (2.00% of total cost)
10. AWS Glue: $67.57 (0.95% of total cost)

The cost analysis capability uses data from the following Cost Explorer APIs:
GetCostAndUsage, GetCostForecast, GetDimensionValues, GetCostCategories, and
GetTags.

## Cost optimization

The cost optimization capability in Amazon Q Developer works with Cost Optimization Hub, AWS Compute Optimizer, and
Savings Plans and reservation recommendations. You can ask questions about cost optimization
opportunities in your AWS account and receive answers in natural language that
reflect actual cost-saving recommendations. For example, if you ask Amazon Q Developer a
question such as _“What are my top cost optimization
opportunities?”_ it will provide a response similar to the
following:

You have substantial opportunities to optimize your AWS costs, with 374
recommendations, totaling $33,479.82, spanning multiple resource types.

1. EC2 Auto Scaling Groups: $19,412.63 (10 recommendations)
2. Compute Savings Plans: $8,788.76 (101 recommendations)
3. RDS DB Instances: $2,160.07 (4 recommendations)
4. RDS Reserved Instances: $1,666.73 (54 recommendations)
5. OpenSearch Reserved Instances: $335.95 (12 recommendations)
6. EBS Volumes: $293.48 (22 recommendations)
7. ElastiCache Reserved Instances: $259.62 (6 recommendations)
8. EC2 Instances: $153.28 (2 recommendations)
9. RDS DB Instance Storage: $150.00 (1 recommendation)
10. SageMaker Savings Plans: $137.20 (12 recommendations)
11. ECS Services: $65.71 (2 recommendations)
12. DynamoDB Reserved Capacity: $56.38 (148 recommendations)

The cost optimization capability uses data from the following APIs:

- Cost Optimization Hub: GetRecommendation, ListRecommendations,
  ListRecommendationSummaries
- Compute Optimizer: GetAutoScalingGroupRecommendations, GetEBSVolumeRecommendations,
  GetEC2InstanceRecommendations, GetECSServiceRecommendations,
  GetRDSDatabaseRecommendations, GetLambdaFunctionRecommendations,
  GetIdleRecommendations, GetEffectiveRecommendationPreferences
- Cost Explorer: GetReservationPurchaseRecommendation,
  GetSavingsPlansPurchaseRecommendation

## Pricing and cost estimation

The pricing and cost estimation capability in Amazon Q Developer works with the AWS
Price List APIs. You can ask questions about the prices of AWS services or the
estimated cost of new workloads you plan to build on AWS. For example, you can ask
a question such as _“How much would it cost to store 200 TB of data in S3
in Dublin?”_, and receive an answer similar to the following:

Here’s the cost breakdown for storing 200 TB of data in Amazon S3 in Dublin
(eu-west-1 region):

Storage cost for 200 TB in S3 Dublin:

- **Monthly cost**: $4,556.80
- **Annual cost**: $54,681.60

Cost breakdown (S3 Standard storage):

- **First 50 TB (51,200 GB)**: $0.023 per GB =
  $1,177.60
- **Remaining 150 TB (153,600 GB)**: $0.022 per
  GB = $3,379.20

Important considerations: This pricing covers **storage
only** for S3 Standard class. Additional costs may include:

- Data transfer fees (ingress/egress)
- API requests (PUT, GET, DELETE operations)
- Data retrieval charges
- Cross-region replication (if used)
- Versioning storage (if enabled)

The S3 Standard storage class provides immediate access to your data with high
durability and availability. If you don't need immediate access to all your data,
you could consider other storage classes like S3 Intelligent-Tiering, S3
Standard-IA, or S3 Glacier for potential cost savings.

The pricing and cost estimation capability uses data from the following AWS
Price List APIs: DescribeServices, GetAttributeValues, GetProducts.

## Getting started

**Prerequisites**

- Ensure you have the appropriate permissions to use Amazon Q Developer, AWS Cost Explorer, AWS Cost Optimization Hub,
  AWS Compute Optimizer, AWS Savings Plans and reservation recommendations, and
  AWS Price List APIs. For details, see [Security and privacy](ce-q-security.md "ce-q-security.md").
- To use the cost analysis capability in Amazon Q Developer, you must first opt in
  to Cost Explorer. To opt in to Cost Explorer, open the Billing and Cost Management console at
  [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/"). Once you’ve opted in to
  Cost Explorer, it can take up to 24 hours for your cost data to be
  available.
- To use the cost optimization capability in Amazon Q Developer, you must first opt in to Cost Optimization Hub. To
  opt in to Cost Optimization Hub, open the Cost Optimization Hub console page at [https://console.aws.amazon.com/costmanagement/home#/cost-optimization-hub](https://console.aws.amazon.com/costmanagement/home#/cost-optimization-hub "https://console.aws.amazon.com/costmanagement/home#/cost-optimization-hub"), and
  then choose **Enroll**. Once you’ve opted in to Cost Optimization Hub, it
  can take up to 24 hours for recommendations to be calculated.

###### To start a conversation with Amazon Q Developer

1. Log in to the AWS Management console at [https://console.aws.amazon.com](https://console.aws.amazon.com "https://console.aws.amazon.com").
2. Choose the Amazon Q icon on the right side of the console.
3. Ask a question about your costs, such as _“What were my costs last
   month?”_, _“How can I lower my AWS
   bill?”_, or _“How much does a c8g.2xlarge instance
   running Linux cost in us-east-1?”_

## Pricing

The cost analysis and cost optimization capabilities are included with Amazon Q Developer. For
information about Amazon Q Developer pricing, see [Amazon Q Developer pricing](https://aws.amazon.com/q/developer/pricing/ "https://aws.amazon.com/q/developer/pricing/").
