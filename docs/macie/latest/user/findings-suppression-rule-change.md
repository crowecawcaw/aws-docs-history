# Changing a suppression rule for Macie

findings

After you create a suppression rule, you can change the settings for the rule. A
_suppression rule_ is a set of attribute-based
filter criteria that defines cases where you want Amazon Macie to archive findings
automatically. Suppression rules are helpful in situations where you've reviewed a class
of findings and don't want to be notified of them again. Each rule consists of a set of
filter criteria, a name, and, optionally, a description.

If you change the criteria of a suppression rule, findings that were previously suppressed
by the rule continue to be suppressed. The findings continue to have a status of
_archived_ and Macie doesn't publish them to
Amazon EventBridge or AWS Security Hub. Macie applies the new criteria only to new sensitive data
findings, new policy findings, and subsequent occurrences of existing policy
findings.

In addition to changing the criteria or other settings for a rule, you can assign tags to a
rule. A *tag* is a label that you define and assign to certain types of AWS resources. Each tag consists of a required tag key and an optional tag value. Tags can help you identify, categorize, and manage resources in different ways, such as by purpose, owner, environment, or other criteria. To learn more, see [Tagging Macie resources](tagging-resources.md "tagging-resources.md").

###### To change a suppression rule for findings

To assign tags or change the settings for a suppression rule, you can use the Amazon Macie
console or the Amazon Macie API.

Console
Follow these steps to assign tags or change the settings for a suppression rule by using
the Amazon Macie console.

###### To change a suppression rule

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose
   **Findings**.
3. In the **Saved rules** list, choose the edit icon
   (
   ![The edit icon, which is a blue pencil.](images/icon-edit-resource-blue.png)
   ) next to the suppression rule that you
   want to change or assign tags to.
4. Do any of the following:
   - To change the criteria of the rule, use the
     **Filter criteria** box. In the box,
     enter conditions that specify attributes of the findings
     that you want the rule to suppress. To learn how, see [Creating and applying filters to Macie
     findings](findings-filter-procedure.md "findings-filter-procedure.md").
   - To change the name of the rule, enter a new name in the
     **Name** box under
     **Suppression rule**.
   - To change the description of the rule, enter a new
     description in the **Description** box
     under **Suppression rule**.
   - To assign tags to the rule, choose **Manage tags** under
     **Suppression rule**. Then add, review,
     and change the tags as necessary. A rule can have as many as
     50 tags.

5. When you finish making changes, choose
   **Save**.

API
To change a suppression rule programmatically, use the [UpdateFindingsFilter](../APIReference/findingsfilters-id.md "../APIReference/findingsfilters-id.md") operation of the Amazon Macie API. When you
submit your request, use the supported parameters to specify a new value for
each setting that you want to change.

For the `id` parameter, specify the unique identifier for the
rule to change. You can get this identifier by using the [ListFindingsFilter](../APIReference/findingsfilters.md "../APIReference/findingsfilters.md") operation to retrieve a list of suppression
and filter rules for your account. If you're using the AWS Command Line Interface (AWS CLI),
run the [list-findings-filters](../../../cli/latest/reference/macie2/list-findings-filters.md "../../../cli/latest/reference/macie2/list-findings-filters.md") command to retrieve this list.

To change a suppression rule by using the AWS CLI, run the [update-findings-filter](../../../cli/latest/reference/macie2/update-findings-filter.md "../../../cli/latest/reference/macie2/update-findings-filter.md") command and use the supported parameters
to specify a new value for each setting that you want to change. For
example, the following command changes the name of an existing suppression
rule.

```
`C:\>` `aws macie2 update-findings-filter --id `8a3c5608-aa2f-4940-b347-d1451example` --name `mailing_addresses_only``

```

Where:

- `8a3c5608-aa2f-4940-b347-d1451example` is
  the unique identifier for the rule.
- `mailing_addresses_only` is the new name
  for the rule.

If the command runs successfully, you receive output similar to the
following.

```
`{
 "arn": "arn:aws:macie2:us-west-2:123456789012:findings-filter/8a3c5608-aa2f-4940-b347-d1451example",
 "id": "8a3c5608-aa2f-4940-b347-d1451example"
}`
```

Where `arn` is the Amazon Resource Name (ARN) of the rule that
was changed, and `id` is the unique identifier for the
rule.

Similarly, the following example converts a [filter rule](findings-filter-rule-procedures.md "findings-filter-rule-procedures.md") to a
suppression rule by changing the value for the `action` parameter
from `NOOP` to `ARCHIVE`.

```
`C:\>` `aws macie2 update-findings-filter --id `8a1c3508-aa2f-4940-b347-d1451example` --action `ARCHIVE``

```

Where:

- `8a1c3508-aa2f-4940-b347-d1451example` is
  the unique identifier for the rule.
- `ARCHIVE` is the new action for Macie to
  perform on findings that match the criteria of the
  rule—suppress the findings.

If the command runs successfully, you receive output similar to the
following:

```
`{
 "arn": "arn:aws:macie2:us-west-2:123456789012:findings-filter/8a1c3508-aa2f-4940-b347-d1451example",
 "id": "8a1c3508-aa2f-4940-b347-d1451example"
}`
```

Where `arn` is the Amazon Resource Name (ARN) of the rule that
was changed, and `id` is the unique identifier for the
rule.
