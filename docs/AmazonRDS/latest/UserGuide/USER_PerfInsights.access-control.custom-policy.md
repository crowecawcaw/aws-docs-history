

# Creating a custom IAM policy for Database Insights
<a name="USER_PerfInsights.access-control.custom-policy"></a>

For users who don't have either the `AmazonRDSPerformanceInsightsReadOnly` or `AmazonRDSPerformanceInsightsFullAccess` policy, you can grant access to Database Insights by creating or modifying a user-managed IAM policy. When you attach the policy to an IAM permission set or role, the recipient can use Database Insights.

**To create a custom policy**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. On the **Create Policy** page, choose the **JSON** option.

1. Copy and paste the text provided in the *JSON policy document* section in the *AWS Managed Policy Reference Guide* for [AmazonRDSPerformanceInsightsReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRDSPerformanceInsightsReadOnly.html) or [AmazonRDSPerformanceInsightsFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRDSPerformanceInsightsFullAccess.html) policy.

1. Choose **Review policy**.

1. Provide a name for the policy and optionally a description, and then choose **Create policy**.

You can now attach the policy to a permission set or role. The following procedure assumes that you already have a user available for this purpose.

**To attach the policy to a user**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Users**.

1. Choose an existing user from the list.
**Important**  
To use Database Insights, make sure that you have access to Amazon RDS in addition to the custom policy. For example, the `AmazonRDSPerformanceInsightsReadOnly` predefined policy provides read-only access to Amazon RDS. For more information, see [Managing access using policies](UsingWithRDS.IAM.md#security_iam_access-manage).

1. On the **Summary** page, choose **Add permissions**.

1. Choose **Attach existing policies directly**. For **Search**, type the first few characters of your policy name, as shown in the following image.   
![The policy selection.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/perf_insights_attach_iam_policy.png)

1. Choose your policy, and then choose **Next: Review**.

1. Choose **Add permissions**.