

# Deleting a filter rule for Macie findings
<a name="findings-filter-rule-delete"></a>

If you create a filter rule, you can delete it at any time. A *filter rule* is a set of filter criteria that you create and save to use again when you review findings on the Amazon Macie console. If you delete a filter rule, your change doesn't affect findings that match the rule's criteria. A filter rule only determines which findings appear on the console after you apply the rule.

**To delete a filter rule for findings**  
You can delete a filter rule by using the Amazon Macie console or the Amazon Macie API.

------
#### [ Console ]

Follow these steps to delete a filter rule by using the Amazon Macie console.

**To delete a filter rule**

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/).

1. In the navigation pane, choose **Findings**.

1. In the **Saved rules** list, choose the edit icon (![The edit icon, which is a blue pencil.](http://docs.aws.amazon.com/macie/latest/user/images/icon-edit-resource-blue.png)) next to the filter rule that you want to delete.

1. Under **Filter rule**, choose **Delete**.

------
#### [ API ]

To delete a filter rule programmatically, use the [DeleteFindingsFilter](https://docs.aws.amazon.com/macie/latest/APIReference/findingsfilters-id.html) operation of the Amazon Macie API. For the `id` parameter, specify the unique identifier for the filter rule to delete. You can get this identifier by using the [ListFindingsFilter](https://docs.aws.amazon.com/macie/latest/APIReference/findingsfilters.html) operation to retrieve a list of filter and suppression rules for your account. If you're using the AWS Command Line Interface (AWS CLI), run the [list-findings-filters](https://docs.aws.amazon.com/cli/latest/reference/macie2/list-findings-filters.html) command to retrieve this list.

To delete a filter rule by using the AWS CLI, run the [delete-findings-filter](https://docs.aws.amazon.com/cli/latest/reference/macie2/delete-findings-filter.html) command. For example:

```
C:\> aws macie2 delete-findings-filter --id {{9b2b4508-aa2f-4940-b347-d1451example}}
```

Where {{9b2b4508-aa2f-4940-b347-d1451example}} is the unique identifier for the filter rule to delete.

If the command runs successfully, Macie returns an empty HTTP 200 response. Otherwise, Macie returns an HTTP 4*xx* or 500 response that indicates why the operation failed.

------