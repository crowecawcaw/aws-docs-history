

# Trusted Advisor recommendations for Event Functions

AWS Lambda provides cost optimization recommendations for Event Functions in [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html). These recommendations identify functions that you can run on Lambda Managed Instances to reduce costs. With these recommendations, you can lower your Lambda costs by focusing your migration efforts on the functions that deliver the greatest savings.

Customers with eligible [AWS Support plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html) can access them in the [Trusted Advisor console](https://console.aws.amazon.com/trustedadvisor/) alongside other [cost optimization checks](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#lambda-managed-instances-migration-cost-opt).

## How recommendations are calculated
<a name="lambda-managed-instances-trusted-advisor-calculation"></a>

Lambda automatically analyzes the invocation patterns, duration, and resource utilization of all high-volume Event Functions to identify candidates for cost savings. These estimated savings are based on a simulation of each function's invocation patterns. Your actual savings might differ from the estimated savings provided.

Lambda calculates the estimated savings for each function using public On-Demand pricing for both AWS Lambda and Amazon EC2 instances. Because the estimate uses On-Demand pricing, your actual savings also vary if you use Amazon EC2 Savings Plans, Reserved Instances, or other pricing agreements. These pricing options apply to the underlying Amazon EC2 compute for Lambda Managed Instances, so they can increase your savings beyond the estimate.

## What each recommendation includes
<a name="lambda-managed-instances-trusted-advisor-fields"></a>

Each candidate function appears as a row in the results table for the check. The following table describes the fields in each row.


| Field | Description | 
| --- | --- | 
| Function ARN and Region | The function Amazon Resource Name (ARN) and the AWS Region of the recommended function. | 
| Instance Type | The recommended Amazon EC2 instance type for running the function on Lambda Managed Instances. | 
| Memory to vCPU Ratio | The recommended memory-to-vCPU ratio for the function. | 
| Lambda On-Demand Cost | The current estimated cost of the function, calculated using On-Demand pricing for AWS Lambda. | 
| Expected LMI Cost | The expected cost of the function on Lambda Managed Instances, calculated using On-Demand pricing for Amazon EC2. | 
| Expected LMI to Current Cost Ratio | The ratio of the expected Lambda Managed Instances cost to the current Lambda On-Demand cost. | 
| Date Range | The date range of the usage data that the recommendation is based on. | 
| Last Refresh Timestamp | The time when Trusted Advisor last refreshed the recommendation. | 

## Viewing recommendations in the Trusted Advisor console
<a name="lambda-managed-instances-trusted-advisor-viewing"></a>

To view the Lambda Managed Instances cost optimization recommendations, use the Trusted Advisor console.

1. Open the Trusted Advisor console at [https://console.aws.amazon.com/trustedadvisor/](https://console.aws.amazon.com/trustedadvisor/).

1. In the navigation pane, under **Recommendations**, choose **Cost optimization**.

1. On the **Cost optimization** page, find the **Cost optimization checks** section.

1. Locate the check named [AWS Lambda Managed Instances migration cost optimization recommendation](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#lambda-managed-instances-migration-cost-opt).

1. To find the check quickly, enter a term such as `Lambda` in the **Search by keyword** box, or use the **View** filter, for example **Investigation recommended**.

1. Expand the check to see its description, **Alert Criteria**, **Recommended Action**, and **Additional Resources**. The results table shows the candidate functions and their fields.

The following screenshot shows the AWS Lambda Managed Instances migration cost optimization recommendation check expanded in the Trusted Advisor console. The check displays its description, **Alert Criteria**, **Recommended Action**, and **Additional Resources**, followed by the results table. Each row in the results table lists a candidate function with the fields described in the preceding table.

![Trusted Advisor checks for cost optimization](https://docs.aws.amazon.com/lambda/latest/dg/images/lambda-managed-instances-trusted-advisor-cost-check.png)
