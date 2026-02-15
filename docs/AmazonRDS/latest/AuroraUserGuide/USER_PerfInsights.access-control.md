# Creating a custom IAM

policy for Performance Insights

For users who don't have either the `AmazonRDSPerformanceInsightsReadOnly` or
`AmazonRDSPerformanceInsightsFullAccess` policy, you can grant access to Performance Insights
by creating or modifying a user-managed IAM policy. When you attach the policy to an IAM
permission set or role, the recipient can use Performance Insights.

###### To create a custom policy

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. On the **Create Policy** page, choose the
   **JSON** option.
5. Copy and paste the text provided in the _JSON policy
   document_ section in the _AWS Managed Policy Reference
   Guide_ for [AmazonRDSPerformanceInsightsReadOnly](../../../aws-managed-policy/latest/reference/AmazonRDSPerformanceInsightsReadOnly.md "../../../aws-managed-policy/latest/reference/AmazonRDSPerformanceInsightsReadOnly.md")
   or [AmazonRDSPerformanceInsightsFullAccess](../../../aws-managed-policy/latest/reference/AmazonRDSPerformanceInsightsFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonRDSPerformanceInsightsFullAccess.md")
   policy.
6. Choose **Review policy**.
7. Provide a name for the policy and optionally a description, and then choose
   **Create policy**.
   You can now attach the policy to a permission set or role. The following procedure
   assumes that you already have a user available for this purpose.

###### To attach the policy to a user

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. Choose an existing user from the list.

###### Important

To use Performance Insights, make sure that you have access to Amazon RDS in addition to the custom policy.
For example, the `AmazonRDSPerformanceInsightsReadOnly`
predefined policy provides read-only access to Amazon RDS. For more information,
see [Managing access using policies](UsingWithRDS.md#security_iam_access-manage "UsingWithRDS.md#security_iam_access-manage"). 4. On the **Summary** page, choose **Add
permissions**. 5. Choose **Attach existing policies directly**. For
**Search**, type the first few characters of your policy
name, as shown in the following image.

![Choose a Policy](images/perf_insights_attach_iam_policy.png) 6. Choose your policy, and then choose **Next: Review**. 7. Choose **Add permissions**.
