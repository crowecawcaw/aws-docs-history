# View your savings opportunities in the AWS Billing and Cost Management console

###### Warning

We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

Cost Optimization Hub is not supported for the Free Tier of our new AWS experience. When you
upgrade to the Paid Plan, Cost Optimization Hub is automatically turned on for your account.
For more information, see [Upgrade your account in AWS Settings](../../../accounts/latest/reference/upgrade-account.md "../../../accounts/latest/reference/upgrade-account.md").

Cost Optimization Hub shows idle resources that you can delete for savings opportunities.
You can choose individual resources to find more information or export your savings
opportunities.

Cost Optimization Hub provides information about the savings opportunity:

- **Estimated cost (before discounts)**: The
  savings estimate using AWS public (On-Demand) pricing without incorporating any
  discounts.
- **Estimated other discounts**: Estimated other
  discounts include all discounts that are not itemized, which includes Free Tier.
- **Estimated cost (after discounts)**: The
  savings estimate incorporating all discounts with AWS.
- **Estimated monthly savings**: The estimated
  monthly savings amount for the recommendation. This is calculated by dividing the
  aggregated estimated monthly savings of your cost optimization opportunities by your
  amortized monthly AWS costs, exclusive of credits and refunds. The estimated monthly
  savings is a quick approximation of your future savings. Any actual savings are
  dependent on your future AWS usage.
- **Estimated savings percentage**: The estimated
  savings percentage relative to the total cost.
  We also provide information such as the resource ID, usage, and any tags associated with
  the resource.

## Supported resources

The following resources are supported:

- Amazon Elastic Compute Cloud (Amazon EC2) instances
- Amazon EC2 Auto Scaling groups
- Amazon Elastic Block Store (Amazon EBS) volumes
- Amazon Elastic Container Service (Amazon ECS) tasks on AWS Fargate
- Amazon Relational Database Service DB instances
- NAT Gateway
- Amazon DynamoDB table
- ElastiCache cluster
- SageMaker endpoint
- MemoryDB cluster
- DocumentDB cluster

When you group related recommendations, Cost Optimization Hub identifies recommended
actions that interact with each other, and it reduces estimated aggregated savings based on
the degree of overlap. Cost Optimization Hub deduplicates amongst resource optimization
strategies and proposes the recommendation with the highest savings. It also considers the
reduction in usage by implementing the recommendations.

###### To find and delete an idle resource

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Optimization Hub**.

The cost optimization hub will show your savings opportunities. 3. Choose a resource.

The cost optimization hub will open a panel that provides more information about
your resource. 4. Under **Estimated savings**, choose **Open in Service
Console**.

You'll be directed to the service console where you can delete the
resource.
