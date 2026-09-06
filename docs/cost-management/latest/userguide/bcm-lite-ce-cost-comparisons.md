

# Cost comparisons in the AWS Billing and Cost Management console
<a name="bcm-lite-ce-cost-comparisons"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

You can create cost comparisons using Cost Explorer to understand changes in your AWS spending. Use Cost Comparisons to analyze cost variations between months and get cost comparison drivers. Cost comparison drivers explain the reason behind these variations. For instance, a cost comparison driver might be that there was a 5% increase in cost for DynamoDB due to an increase in ReadCapacity from 50,000 to 70,000. This means you read from your DynamoDB table more frequently that month. This might indicate an increase in customers for your service, or an issue in your service architecture. As a developer, it's your job to understand why these cost drivers occur.

## Use cost comparison
<a name="bcm-lite-ce-use-cost-comparison"></a>

Use Cost Comparison to compare two months, a baseline and comparison month, in the following two ways:

Query for any two months across any Cost Explorer dimension and cost metric. Cost Comparison analyzes your costs by:
+ Calculating the total cost for each selected dimension in the baseline month.
+ Comparing these with costs in the comparison month.
+ Ranking the dimension values by the absolute cost difference.
+ Returning the top 10 increases or decreases for each dimension.

The following procedure shows you how to create a cost comparison for Lambda, Amazon EC2, and DynamoDB over two months.

**To create a cost comparison**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the right pane, under **Report parameters**, choose **Compare**.

1. For **Date Range**, keep **Month over month**.

1. For **Group by**, choose **Service**.

1. For **Filters**, choose **Service**, and then choose **DynamoDB** and **Lambda**.

1. Choose **Apply**.

Request detailed cost drivers for the cost change associated with a specific dimension value. Cost Comparison gathers these cost drivers by:
+ Identifying the specific usage type driving the largest change.
+ Calculating the total cost for each charge type in the baseline and comparison months.
+ Ranking the results by absolute cost difference.
+ Returning a breakdown of cost changes for each charge type.