

# Deleting a suppression rule for Macie findings
<a name="findings-suppression-rule-delete"></a>

You can delete a suppression rule at any time. If you delete a suppression rule, Amazon Macie stops suppressing new and subsequent occurrences of findings that match the rule's criteria and aren't suppressed by other rules. Note, however, that Macie might continue to suppress findings that it's currently processing and match the rule's criteria.

After you delete a suppression rule, new and subsequent occurrences of findings that match the rule's criteria have a status of *current* (not *archived*). This means that they appear by default on the Amazon Macie console. In addition, Macie publishes them to Amazon EventBridge as events. Depending on the [publication settings](findings-publish-frequency.md) for your account, Macie also publishes the findings to AWS Security Hub CSPM.

**To delete a suppression rule for findings**  
You can delete a suppression rule by using the Amazon Macie console or the Amazon Macie API.

------
#### [ Console ]

Follow these steps to delete a suppression rule by using the Amazon Macie console.

**To delete a suppression rule**

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/).

1. In the navigation pane, choose **Findings**.

1. In the **Saved rules** list, choose the edit icon (![The edit icon, which is a blue pencil.](http://docs.aws.amazon.com/macie/latest/user/images/icon-edit-resource-blue.png)) next to the suppression rule that you want to delete.

1. Under **Suppression rule**, choose **Delete**.

------
#### [ API ]

To delete a suppression rule programmatically, use the [DeleteFindingsFilter](https://docs.aws.amazon.com/macie/latest/APIReference/findingsfilters-id.html) operation of the Amazon Macie API. For the `id` parameter, specify the unique identifier for the suppression rule to delete. You can get this identifier by using the [ListFindingsFilter](https://docs.aws.amazon.com/macie/latest/APIReference/findingsfilters.html) operation to retrieve a list of suppression and filter rules for your account. If you're using the AWS Command Line Interface (AWS CLI), run the [list-findings-filters](https://docs.aws.amazon.com/cli/latest/reference/macie2/list-findings-filters.html) command to retrieve this list.

To delete a suppression rule by using the AWS CLI, run the [delete-findings-filter](https://docs.aws.amazon.com/cli/latest/reference/macie2/delete-findings-filter.html) command. For example:

```
C:\> aws macie2 delete-findings-filter --id {{8a3c5608-aa2f-4940-b347-d1451example}}
```

Where {{8a3c5608-aa2f-4940-b347-d1451example}} is the unique identifier for the suppression rule to delete.

If the command runs successfully, Macie returns an empty HTTP 200 response. Otherwise, Macie returns an HTTP 4*xx* or 500 response that indicates why the operation failed.

------