# Using the Free Tier API

[AWS Free Tier](https://aws.amazon.com/free "https://aws.amazon.com/free") offers free usage each month for
AWS services and products. You can use the Free Tier API to programmatically track your
free tier usage against the monthly usage limits.

Use the API to understand when your free usage will change to pay-as-you-go pricing each
month. This helps you avoid unintended charges by comparing forecasted usage to the free
tier limit for each service throughout the month. For example, to know when your usage might
exceed the free offer limit for AWS Glue, you can use the API to track your AWS account
usage. You can then decide whether to keep the service or make any changes before the free
tier limit ends.

You can also use the API to create visualizations or write scripts to automate changes to
AWS resources based on your API responses.

###### Example: Find your free tier offers for AWS Glue

The following AWS Command Line Interface (AWS CLI) command uses the `GetFreeTierUsage` API
operation to filter by free tier usage for AWS Glue.

**Request**

```
aws freetier get-free-tier-usage --filter '{"Dimensions": {"Key": "SERVICE", "Values": ["Glue"], "MatchOptions": ["CONTAINS"]}}'
```

**Response**

The following response returns two `Always Free` offers from AWS Glue.

```
{
    "freeTierUsages": [
        {
            "actualUsageAmount": 287.0,
            "description": "1000000.0 Request are always free per month as part of AWS Free Usage Tier (Global-Catalog-Request)",
            "forecastedUsageAmount": 2224.25,
            "freeTierType": "Always Free",
            "limit": 1000000.0,
            "operation": "Request",
            "region": "global",
            "service": "AWS Glue",
            "unit": "Request",
            "usageType": "Catalog-Request"
        },
        {
            "actualUsageAmount": 176.36827958,
            "description": "1000000.0 Obj-Month are always free per month as part of AWS Free Usage Tier (Global-Catalog-Storage)",
            "forecastedUsageAmount": 1366.8541667450002,
            "freeTierType": "Always Free",
            "limit": 1000000.0,
            "operation": "Storage",
            "region": "global",
            "service": "AWS Glue",
            "unit": "Obj-Month",
            "usageType": "Catalog-Storage"
        }
    ]
}
```

## Related resources

The AWS CLI and the AWS Software Development Kits (SDKs) include support for the
Free Tier API. For a list of languages that support the Free Tier API, choose the
operation name, and in the **See Also** section, choose your preferred
language.

For more information about the Free Tier API, see the [AWS Billing and Cost Management API Reference](../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Free_Tier.md "../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Free_Tier.md").

To use the AWS Billing and Cost Management console to track your free tier usage, such as receiving email alerts,
see [Tracking your AWS Free Tier usage](tracking-free-tier-usage.md "tracking-free-tier-usage.md").

For more information about using Free Tier with Amazon EC2, see the [Tutorial: Get
started with Amazon EC2 Linux instances](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md") in the
_Amazon EC2 User Guide_.

You can also create budgets for your AWS costs and then set up notifications and alerts
when your budgets exceed or are forecasted to exceed your costs and usage. For more
information, see [Managing your costs with AWS Budgets](../../../cost-management/latest/userguide/budgets-managing-costs.md "../../../cost-management/latest/userguide/budgets-managing-costs.md") in the
_AWS Cost Management User Guide_.
