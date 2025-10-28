# Reviewing and acting on insights in

Security Hub CSPM

For each insight, AWS Security Hub CSPM first determines the findings that match the filter criteria,
and then uses the grouping attribute to group the matching findings.

From the **Insights** page on the console, you can view and take action on the
results and findings.

If you enable cross-Region aggregation, the results for
managed insights (when you're signed in to the aggregation Region) include findings from the aggregation Region and linked Regions. The results for
custom insights, if the insight doesn't filter by Region, also include findings from the aggregation Region and linked
Regions (when you're signed in to the aggregation Region). In other Regions, the insight results are only for that Region.

For information about configuring cross-Region aggregation, see [Understanding cross-Region aggregation in Security Hub CSPM](finding-aggregation.md "finding-aggregation.md").

## Viewing and taking action on

insight results

The insight results consist of a grouped list of the results for the insight. For
example, if the insight is grouped by resource identifiers, then the insight results are
the list of resource identifiers. Each item in the results list indicates the number of
matching findings for that item.

If the findings are grouped by resource identifier or resource type,
the results include all of the resources in the matching findings. This includes
resources that have a different type from the resource type specified in the filter
criteria. For example, an insight identifies findings that are associated with S3
buckets. If a matching finding contains both an S3 bucket resource and an IAM access
key resource, the insight results include both resources.

On the Security Hub CSPM console, the results list is sorted from most to fewest matching findings.
Security Hub CSPM can only display 100 results. If there are more than 100 grouping values, you
only see the first 100.

In addition to the results list, the insight results display a set of charts
summarizing the number of matching findings for the following attributes.

- **Severity label** – Number of findings for each
  severity label
- **AWS account ID** – Top five account IDs for the
  matching findings
- **Resource type** – Top five resource types for the
  matching findings
- **Resource ID** – Top five resource IDs for the
  matching findings
- **Product name** - Top five finding providers for the
  matching findings

If you have configured custom actions, then you can send selected results to a custom
action. The action must be associated with an Amazon CloudWatch rule for the `Security Hub
 Insight Results` event type. For more information, see [Using EventBridge for automated response and remediation](securityhub-cloudwatch-events.md "securityhub-cloudwatch-events.md").
If you have not configured custom actions, the **Actions** menu is disabled.

Security Hub CSPM console

###### To view and take action on insight results (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose **Insights**.
3. To display the list of insight results, choose the insight name.
4. Select the check box for each result to send to the custom action.
5. From the **Actions** menu, choose the custom action.

Security Hub CSPM API, AWS CLI
**To view and take action on insight results (API, AWS CLI)**

To view insight results, use the [>GetInsightResults](../../1.0/APIReference/API_GetInsightResults.md "../../1.0/APIReference/API_GetInsightResults.md") operation of the Security Hub CSPM API. If you use the AWS CLI, run the
[get-insight-results](../../../cli/latest/reference/securityhub/get-insight-results.md "../../../cli/latest/reference/securityhub/get-insight-results.md")
command.

To identify the
insight to return results for, you need the insight ARN. To obtain the insight
ARNs for custom insights, use the [`GetInsights`](../../1.0/APIReference/API_GetInsights.md "../../1.0/APIReference/API_GetInsights.md") API operation or the [get-insight-results](../../../cli/latest/reference/securityhub/get-insight-results.md "../../../cli/latest/reference/securityhub/get-insight-results.md") command.

The following example retrieves the results for the specified insight. This example is formatted for Linux, macOS, or Unix,
and it uses the backslash (\) line-continuation character to improve
readability.

```
`$` `aws securityhub get-insight-results --insight-arn "`arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"`
```

For information about how to create custom actions programmatically, see [Using custom actions to send findings
and insight results to EventBridge](securityhub-cwe-custom-actions.md "securityhub-cwe-custom-actions.md").

## Viewing and taking action on insight

result findings (console)

From an insight results list on the Security Hub CSPM console, you can display the list of findings for each
result.

###### To display and take action on insight findings (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose **Insights**.
3. To display the list of insight results, choose the insight name.
4. To display the list of findings for an insight result, choose the item from
   the results list. The findings list shows the active findings for the selected insight result that have
   a workflow status of `NEW` or `NOTIFIED`.

From the findings list, you can perform the following actions:

- [Filtering findings in Security Hub CSPM](securityhub-findings-manage.md "securityhub-findings-manage.md")
- [Reviewing finding details and
  history](securityhub-findings-viewing.md#finding-view-details-console "securityhub-findings-viewing.md#finding-view-details-console")
- [Setting the workflow status of findings in
  Security Hub CSPM](findings-workflow-status.md "findings-workflow-status.md")
- [Sending findings to a custom Security Hub CSPM action](findings-custom-action.md "findings-custom-action.md")
