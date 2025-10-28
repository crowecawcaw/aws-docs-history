# Applying a filter rule to Macie findings

When you apply a filter rule, Amazon Macie uses the rule's criteria to determine which
findings to include or exclude from your view of findings on the console. Macie also displays
the criteria to help you determine which criteria you applied.

###### Tip

Although filter rules are designed for use with the Amazon Macie console, you can use a
rule's criteria to query findings data programmatically with the Amazon Macie API. To do this,
retrieve the filter criteria for the rule, and then add the criteria to your query. To
retrieve the criteria, use the [GetFindingsFilter](../APIReference/findingsfilters-id.md "../APIReference/findingsfilters-id.md") operation.
To then identify findings that match the criteria, use the [ListFindings](../APIReference/findings.md "../APIReference/findings.md") operation and specify the
criteria in your query. For information about specifying filter criteria in a query, see [Creating and applying filters to Macie
findings](findings-filter-procedure.md "findings-filter-procedure.md").

###### To apply a filter rule to findings

Follow these steps to filter findings on the Amazon Macie console by applying a filter
rule.

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **Findings**.
3. In the **Saved rules** list, choose the filter rule that you want to
   apply. Macie applies the rule's criteria and displays the criteria in the **Filter
   criteria** box.
4. To refine the criteria, use the **Filter criteria** box to add or
   remove filter conditions. If you do this, your changes won't affect the settings for the
   rule. Macie saves your changes only if you explicitly save them as a new rule.
5. To apply a different filter rule, repeat step 3.
   After you apply a filter rule, you can quickly remove all of its filter criteria from your
   view. To do this, choose the **X** in the **Filter
   criteria** box.
