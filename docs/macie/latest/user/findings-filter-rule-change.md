# Changing a filter rule for Macie

findings

After you create a filter rule, you can refine its criteria and change other settings for
the rule. A _filter rule_ is a set of filter criteria that
you create and save to use again when you review findings on the Amazon Macie console. Filter
rules can help you perform repeated, consistent analysis of findings that have specific
characteristics. Each rule consists of a set of filter criteria, a name, and, optionally, a
description.

In addition to changing the filter criteria or other settings for a rule, you can assign
tags to a rule. A *tag* is a label that you define and assign to certain types of AWS resources. Each tag consists of a required tag key and an optional tag value. Tags can help you identify, categorize, and manage resources in different ways, such as by purpose, owner, environment, or other criteria. To learn more, see [Tagging Macie resources](tagging-resources.md "tagging-resources.md").

###### To change a filter rule for findings

To assign tags or change the settings for a filter rule, you can use the Amazon Macie
console or the Amazon Macie API.

Console
Follow these steps to assign tags or change the settings for a filter rule by using
the Amazon Macie console.

###### To change a filter rule

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **Findings**.
3. In the **Saved rules** list, choose the edit icon
   (
   ![The edit icon, which is a blue pencil.](images/icon-edit-resource-blue.png)
   ) next to the filter rule that you want to change or
   assign tags to.
4. Do any of the following:
   - To change the filter criteria of the rule, use the **Filter
     criteria** box. In the box, enter conditions for the criteria that
     you want. To learn how, see [Creating and applying filters to Macie
     findings](findings-filter-procedure.md "findings-filter-procedure.md").
   - To change the name of the rule, enter a new name in the
     **Name** box under **Filter rule**.
   - To change the description of the rule, enter a new description in the
     **Description** box under **Filter rule**.
   - To assign tags to the rule, choose **Manage tags** under
     **Filter rule**. Then add, review, and change the tags as
     necessary. A rule can have as many as 50 tags.

5. When you finish making changes, choose **Save**.

API
To change a filter rule programmatically, use the [UpdateFindingsFilter](../APIReference/findingsfilters-id.md "../APIReference/findingsfilters-id.md")
operation of the Amazon Macie API. When you submit your request, use the supported
parameters to specify a new value for each setting that you want to change.

For the `id` parameter, specify the unique identifier for the rule to
change. You can get this identifier by using the [ListFindingsFilter](../APIReference/findingsfilters.md "../APIReference/findingsfilters.md")
operation to retrieve a list of filter and suppression rules for your account. If you're
using the AWS Command Line Interface (AWS CLI), run the [list-findings-filters](../../../cli/latest/reference/macie2/list-findings-filters.md "../../../cli/latest/reference/macie2/list-findings-filters.md") command to retrieve this list.

To change a filter rule by using the AWS CLI, run the [update-findings-filter](../../../cli/latest/reference/macie2/update-findings-filter.md "../../../cli/latest/reference/macie2/update-findings-filter.md") command and use the supported parameters to specify a
new value for each setting that you want to change. For example, the following command
changes the name of an existing filter rule.

```
`C:\>` `aws macie2 update-findings-filter --id `9b2b4508-aa2f-4940-b347-d1451example` --name `personal_information_only``

```

Where:

- `9b2b4508-aa2f-4940-b347-d1451example` is the unique
  identifier for the rule.
- `personal_information_only` is the new name for the
  rule.

If the command runs successfully, you receive output similar to the
following.

```
`{
 "arn": "arn:aws:macie2:us-west-2:123456789012:findings-filter/9b2b4508-aa2f-4940-b347-d1451example",
 "id": "9b2b4508-aa2f-4940-b347-d1451example"
}`
```

Where `arn` is the Amazon Resource Name (ARN) of the rule that was
changed, and `id` is the unique identifier for the rule.

Similarly, the following example converts a [suppression rule](findings-suppression.md "findings-suppression.md") to a filter rule by changing the value for the
`action` parameter from `ARCHIVE` to `NOOP`.

```
`C:\>` `aws macie2 update-findings-filter --id `8a1c3508-aa2f-4940-b347-d1451example` --action `NOOP``

```

Where:

- `8a1c3508-aa2f-4940-b347-d1451example` is the unique
  identifier for the rule.
- `NOOP` is the new action for Macie to perform on
  findings that match the criteria of the rule—perform no action (don't
  suppress the findings).

If the command runs successfully, you receive output similar to the
following:

```
`{
 "arn": "arn:aws:macie2:us-west-2:123456789012:findings-filter/8a1c3508-aa2f-4940-b347-d1451example",
 "id": "8a1c3508-aa2f-4940-b347-d1451example"
}`
```

Where `arn` is the Amazon Resource Name (ARN) of the rule that was
changed, and `id` is the unique identifier for the rule.
