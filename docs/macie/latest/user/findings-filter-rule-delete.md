# Deleting a filter rule for Macie

findings

If you create a filter rule, you can delete it at any time. A _filter rule_ is a set of filter criteria that you create and save to use again
when you review findings on the Amazon Macie console. If you delete a filter rule, your change
doesn't affect findings that match the rule's criteria. A filter rule only determines which
findings appear on the console after you apply the rule.

###### To delete a filter rule for findings

You can delete a filter rule by using the Amazon Macie console or the Amazon Macie API.

Console
Follow these steps to delete a filter rule by using the Amazon Macie console.

###### To delete a filter rule

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **Findings**.
3. In the **Saved rules** list, choose the edit icon
   (
   ![The edit icon, which is a blue pencil.](images/icon-edit-resource-blue.png)
   ) next to the filter rule that you want to delete.
4. Under **Filter rule**, choose
   **Delete**.

API
To delete a filter rule programmatically, use the [DeleteFindingsFilter](../APIReference/findingsfilters-id.md "../APIReference/findingsfilters-id.md")
operation of the Amazon Macie API. For the `id` parameter, specify the unique
identifier for the filter rule to delete. You can get this identifier by using the
[ListFindingsFilter](../APIReference/findingsfilters.md "../APIReference/findingsfilters.md") operation to retrieve a list of filter and suppression
rules for your account. If you're using the AWS Command Line Interface (AWS CLI), run the [list-findings-filters](../../../cli/latest/reference/macie2/list-findings-filters.md "../../../cli/latest/reference/macie2/list-findings-filters.md") command to retrieve this list.

To delete a filter rule by using the AWS CLI, run the [delete-findings-filter](../../../cli/latest/reference/macie2/delete-findings-filter.md "../../../cli/latest/reference/macie2/delete-findings-filter.md") command. For example:

```
`C:\>` `aws macie2 delete-findings-filter --id `9b2b4508-aa2f-4940-b347-d1451example``

```

Where `9b2b4508-aa2f-4940-b347-d1451example` is the unique
identifier for the filter rule to delete.

If the command runs successfully, Macie returns an empty HTTP 200 response.
Otherwise, Macie returns an HTTP 4*xx* or 500 response
that indicates why the operation failed.
