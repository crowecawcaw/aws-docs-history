

# Update a budget in the AWS Billing and Cost Management console
<a name="bcm-lite-update-a-budget"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

You can update a budget at any time. When you update a budget, your changes are saved immediately, but budget calculations refresh up to three times a day. If you created a budget using a template, you'll need to update the budget to change the default configuration.

The following procedure shows how to update a zero spend budget to only create alerts for costs associated with S3.

**To update a budget**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Budgets**.

1. Choose your budget and then choose **Edit**.

1. For **Budget scope**, choose **Filter specific AWS cost dimensions**.

1. For **Filters**, choose **Add filter**.

1. For **Dimension**, select **Service**.

1. For **Values**, select **S3 (Simple Storage Service)**.

1. Choose **Apply Filter**.

1. Choose **Next**.

1. (Optional) Modify the alerts if necessary.

1. Choose **Next** and then choose **Next**.

1. Choose **Save**.