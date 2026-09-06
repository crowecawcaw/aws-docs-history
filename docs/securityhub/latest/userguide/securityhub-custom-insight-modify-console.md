

# Editing a custom insight
<a name="securityhub-custom-insight-modify-console"></a>

You can edit an existing custom insight to change the grouping value and filters. After you make the changes, you can save the updates to the original insight, or save the updated version as a new insight.

In AWS Security Hub CSPM, custom insights can be used to collect a specific set of findings and track issues that are unique to your environment. For background information about custom insights, see [Understanding custom insights in Security Hub CSPM](securityhub-custom-insights.md).

To edit a custom insight, choose your preferred method, and follow the instructions.

------
#### [ Security Hub CSPM console ]

**To edit a custom insight (console)**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

1. In the navigation pane, choose **Insights**.

1. Choose the custom insight to modify.

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

1. When you complete the updates, choose **Save insight**.

1. When prompted, do one of the following:
   + To update the existing insight to reflect your changes, choose **Update {{<Insight\_Name>}}** and then choose **Save insight**.
   + To create a new insight with the updates, choose **Save new insight**. Enter an **Insight name**, and then choose **Save insight**.

------
#### [ Security Hub CSPM API ]

**To edit a custom insight (API)**

1. Use the [`UpdateInsight`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateInsight.html) operation of the Security Hub CSPM API. If you use the AWS CLI run the [update-insight](https://docs.aws.amazon.com/cli/latest/reference/securityhub/update-insight.html) command.

1. To identify the custom insight that you want to update, provide the insight's Amazon Resource Name (ARN). To get the ARN of a custom insight, use the [`GetInsights`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetInsights.html) operation or the [get-insights](https://docs.aws.amazon.com/cli/latest/reference/securityhub/get-insights.html) command.

1. Update the `Name`, `Filters`, and `GroupByAttribute` parameters as needed.

The following example updates the specified insight. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\\) line-continuation character to improve readability.

```
$ aws securityhub update-insight --insight-arn "{{arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}" --filters '{"ResourceType": [{ "Comparison": "{{EQUALS}}", "Value": "{{AwsIamRole}}"}], "SeverityLabel": [{"Comparison": "{{EQUALS}}", "Value": "{{HIGH}}"}]}' --name "{{High severity role findings}}"
```

------
#### [ PowerShell ]

**To edit a custom insight (PowerShell)**

1. Use the `Update-SHUBInsight` cmdlet.

1. To identify the custom insight, provide the insight's Amazon Resource Name (ARN). To get the ARN of a custom insight, use the `Get-SHUBInsight` cmdlet.

1. Update the `Name`, `Filter`, and `GroupByAttribute` parameters as needed.

**Example**

```
$Filter = @{
    ResourceType = [Amazon.SecurityHub.Model.StringFilter]@{
        Comparison = "EQUALS"
        Value = "AwsIamRole"
    }
    SeverityLabel = [Amazon.SecurityHub.Model.StringFilter]@{
        Comparison = "EQUALS"
        Value = "HIGH"
    }
}

Update-SHUBInsight -InsightArn "arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" -Filter $Filter -Name "High severity role findings"
```

------