

# Creating a custom insight
<a name="securityhub-custom-insight-create-api"></a>

In AWS Security Hub CSPM, custom insights can be used to collect a specific set of findings and track issues that are unique to your environment. For background information about custom insights, see [Understanding custom insights in Security Hub CSPM](securityhub-custom-insights.md).

Choose your preferred method, and follow the steps to create a custom insight in Security Hub CSPM

------
#### [ Security Hub CSPM console ]

**To create a custom insight (console)**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

1. In the navigation pane, choose **Insights**.

1. Choose **Create insight**.

1. To select the grouping attribute for the insight:

   1. Choose the search box to display the filter options.

   1. Choose **Group by**.

   1. Select the attribute to use to group the findings that are associated with this insight.

   1. Choose **Apply**.

1. Optionally, choose any additional filters to use for this insight. For each filter, define the filter criteria, and then choose **Apply**.

1. Choose **Create insight**.

1. Enter an **Insight name**, and then choose **Create insight**.

------
#### [ Security Hub CSPM API ]

**To create a custom insight (API)**

1. To create a custom insight, use the [CreateInsight](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateInsight.html) operation of the Security Hub CSPM API. If you use the AWS CLI, run the [create-insight](https://docs.aws.amazon.com/cli/latest/reference/securityhub/create-insight.html) command.

1. Populate the `Name` parameter with a name for your custom insight.

1. Populate the `Filters` parameter to specify which findings to include in the insight.

1. Populate the `GroupByAttribute` parameter to specify which attribute is used to group the findings that are included in the insight.

1. Optionally, populate the `SortCriteria` parameter to sort the findings by a specific field.

The following example creates a custom insight that includes critical findings with the `AwsIamRole` resource type. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\\) line-continuation character to improve readability.

```
$ aws securityhub create-insight --name "{{Critical role findings}}" --filters '{"ResourceType": [{ "Comparison": "{{EQUALS}}", "Value": "{{AwsIamRole}}"}], "SeverityLabel": [{"Comparison": "{{EQUALS}}", "Value": "{{CRITICAL}}"}]}' --group-by-attribute "{{ResourceId}}"
```

------
#### [ PowerShell ]

**To create a custom insight (PowerShell)**

1. Use the `New-SHUBInsight` cmdlet.

1. Populate the `Name` parameter with a name for your custom insight.

1. Populate the `Filter` parameter to specify which findings to include in the insight.

1. Populate the `GroupByAttribute` parameter to specify which attribute is used to group the findings that are included in the insight.

If you've enabled [cross-region aggregation](finding-aggregation.md) and use this cmdlet from the aggregation Region, the insight applies to matching findings from the aggregation and linked Regions.

**Example**

```
$Filter = @{
    AwsAccountId = [Amazon.SecurityHub.Model.StringFilter]@{
        Comparison = "EQUALS"
        Value = "XXX"
    }
    ComplianceStatus = [Amazon.SecurityHub.Model.StringFilter]@{
        Comparison = "EQUALS"
        Value = 'FAILED'
    }
}
New-SHUBInsight -Filter $Filter -Name TestInsight -GroupByAttribute ResourceId
```

------

## Creating a custom insight from a managed insight (console only)
<a name="securityhub-custom-insight-frrom-managed"></a>

You can't save changes to or delete a managed insight. However, you can use a managed insight as the basis for a custom insight. This is an option on the Security Hub CSPM console only.

**To create a custom insight from a managed insight (console)**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

1. In the navigation pane, choose **Insights**.

1. Choose the managed insight to work from.

1. Edit the insight configuration as needed.
   + To change the attribute used to group findings in the insight:

     1. To remove the existing grouping, choose the **X** next to the **Group by** setting.

     1. Choose the search box.

     1. Select the attribute to use for grouping.

     1. Choose **Apply**.
   + To remove a filter from the insight, choose the circled **X** next to the filter.
   + To add a filter to the insight:

     1. Choose the search box.

     1. Select the attribute and value to use as a filter.

     1. Choose **Apply**.

1. When your updates are complete, choose **Create insight**.

1. When prompted, enter an **Insight name**, and then choose **Create insight**.