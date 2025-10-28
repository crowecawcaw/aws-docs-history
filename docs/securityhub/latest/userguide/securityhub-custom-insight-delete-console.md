# Deleting a custom insight

In AWS Security Hub CSPM, custom insights can be used to collect a specific set of findings and track issues that are unique
to your environment. For background information about custom insights, see [Understanding custom insights in Security Hub CSPM](securityhub-custom-insights.md "securityhub-custom-insights.md").

To delete a custom insight, choose your preferred method, and follow the instructions. You can't delete a managed insight.

Security Hub CSPM console

###### To delete a custom insight (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose **Insights**.
3. Locate the custom insight to delete.
4. For that insight, choose the more options icon (the three dots in the top-right corner
   of the card).
5. Choose **Delete**.

Security Hub CSPM API

###### To delete a custom insight (API)

1. Use the [`DeleteInsight`](../../1.0/APIReference/API_DeleteInsight.md "../../1.0/APIReference/API_DeleteInsight.md") operation of the Security Hub CSPM API. If you use the AWS CLI run the
   [delete-insight](../../../cli/latest/reference/securityhub/delete-insight.md "../../../cli/latest/reference/securityhub/delete-insight.md") command.
2. To identify the custom insight to delete, provide the insight's ARN. To get the ARN of a custom insight, use the
   [`GetInsights`](../../1.0/APIReference/API_GetInsights.md "../../1.0/APIReference/API_GetInsights.md") operation or [get-insights](../../../cli/latest/reference/securityhub/get-insights.md "../../../cli/latest/reference/securityhub/get-insights.md") command.

The following example deletes the specified insight. This example is formatted for Linux, macOS, or Unix,
and it uses the backslash (\) line-continuation character to improve
readability.

```
`$` `aws securityhub delete-insight --insight-arn "`arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"`
```

PowerShell

###### To delete a custom insight (PowerShell)

1. Use the `Remove-SHUBInsight` cmdlet.
2. To identify the custom insight, provide the insight's ARN. To get the ARN
   of a custom insight, use the `Get-SHUBInsight` cmdlet.

**Example**

```
-InsightArn "arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
```
