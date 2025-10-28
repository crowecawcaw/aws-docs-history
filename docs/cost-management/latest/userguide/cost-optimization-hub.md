# Identifying opportunities with Cost Optimization Hub

Cost Optimization Hub is an AWS Billing and Cost Management feature that helps you consolidate and
prioritize cost optimization recommendations across your AWS accounts and AWS Regions, so that
you can get the most out of your AWS spend.

You can use Cost Optimization Hub to identify, filter, and aggregate AWS cost optimization recommendations
across your AWS accounts and AWS Regions. It makes recommendations on resource rightsizing,
idle resource deletion, Savings Plans, and Reserved Instances. With a single dashboard, you avoid having
to go to multiple AWS products to identify cost optimization opportunities.

Cost Optimization Hub helps you quantify and aggregate estimated savings when you implement cost optimization
recommendations. Cost Optimization Hub accounts for your specific commercial terms with AWS, such as Reserved
Instances and Savings Plans, so you can easily compare and prioritize recommendations.

After you enable Cost Optimization Hub, you can see estimated monthly savings in AWS Compute Optimizer,
consistent with the savings estimates in Cost Optimization Hub.

Cost Optimization Hub provides the following main benefits:

- Automatically identify and consolidate your AWS cost optimization opportunities.
- Quantify estimated savings that incorporate your AWS pricing and discounts.
- Aggregate and deduplicate savings across related cost optimization opportunities.
- Prioritize your cost optimization recommendations with filtering, sorting, and
  grouping.
- Measure and benchmark your cost efficiency.
  Cost Optimization Hub provides you with a console experience and a set of API operations that you can use to
  view the findings of the analysis and recommendations for your resources across multiple AWS
  Regions. You can also view findings and recommendations across multiple accounts within your
  organization when you opt in the management account of an organization. The findings from the
  feature are also reported in the consoles of the supported services, such as the Amazon EC2
  console.

###### Topics

- [Getting started with Cost Optimization Hub](coh-getting-started.md "coh-getting-started.md")
- [Customizing your Cost Optimization Hub preferences](coh-preferences.md "coh-preferences.md")
- [Viewing your cost optimization opportunities](coh-view-opportunities.md "coh-view-opportunities.md")
- [Prioritizing your cost optimization
  opportunities](coh-prioritize-opportunities.md "coh-prioritize-opportunities.md")
- [Understanding cost optimization strategies](coh-optimization-strategies.md "coh-optimization-strategies.md")
- [Viewing your savings opportunities](coh-savings-opportunities.md "coh-savings-opportunities.md")
- [Estimating monthly savings](coh-estimated-monthly-savings.md "coh-estimated-monthly-savings.md")
- [Supported resources](#coh-supported-resources "#coh-supported-resources")

## Supported resources

Cost Optimization Hub generates recommendations for the following resources:

- Amazon Elastic Compute Cloud (Amazon EC2) instances
- Amazon EC2 Auto Scaling groups
- Amazon Elastic Block Store (Amazon EBS) volumes
- AWS Lambda functions
- Amazon Elastic Container Service (Amazon ECS) tasks on AWS Fargate
- Compute Savings Plans
- EC2 Instance Savings Plans
- SageMaker Savings Plans
- EC2 Reserved Instances
- Amazon RDS Reserved Instances
- OpenSearch Reserved Instances
- Amazon Redshift reserved nodes
- ElastiCache reserved nodes
- Amazon RDS DB instances
- Amazon RDS DB instance storage
- MemoryDB reserved instances
- DynamoDB reserved capacity
- Amazon Aurora DB cluster storage
