# Update a budget in the AWS Billing and Cost Management console

###### Warning

We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

You can update a budget at any time. When you update a budget, your changes are saved
immediately, but budget calculations refresh up to three times a day. If you created a budget
using a template, you'll need to update the budget to change the default
configuration.

The following procedure shows how to update a zero spend budget to only create alerts for
costs associated with S3.

###### To update a budget

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Budgets**.
3. Choose your budget and then choose **Edit**.
4. For **Budget scope**, choose **Filter specific AWS cost
   dimensions**.
5. For **Filters**, choose **Add filter**.
6. For **Dimension**, select **Service**.
7. For **Values**, select **S3 (Simple Storage
   Service)**.
8. Choose **Apply Filter**.
9. Choose **Next**.
10. (Optional) Modify the alerts if necessary.
11. Choose **Next** and then choose
    **Next**.
12. Choose **Save**.
