# Deleting an allow list

When you delete an allow list in Amazon Macie, you permanently delete all the list's settings.
These settings can't be recovered after they're deleted. If the settings specify a list of
predefined text that you store in Amazon Simple Storage Service (Amazon S3), Macie doesn't delete the S3 object that stores
the list. Only the settings in Macie are deleted.

If you configure sensitive data discovery jobs to use an allow list that you subsequently
delete, the jobs will run as scheduled. However, your job results, both sensitive data findings
and sensitive data discovery results, might report text that you previously specified in the
allow list. Similarly, if you configure automated sensitive data discovery to use a list that you subsequently delete,
daily analyses cycles will proceed. However, sensitive data findings, statistics, and other types
of results might report text that you previously specified in the allow list.

Before you delete an allow list, we recommend that you [review your job inventory](discovery-jobs-manage-view.md "discovery-jobs-manage-view.md") to identify jobs that use
the list and are scheduled to run in the future. In the inventory, the details panel indicates
whether a job is configured to use any allow lists and, if so, which ones. We recommend that you
also [check your settings for automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md"). You
might determine that it's best to change a list instead of deleting it.

As an additional safeguard, Macie checks the settings for all of your jobs when you try to
delete an allow list. If you configured jobs to use the list and any of those jobs have a
status other than **Complete** or **Cancelled**, Macie
doesn't delete the list unless you provide additional confirmation.

###### To delete an allow list

You can delete an allow list by using the Amazon Macie console or the Amazon Macie API.

Console
Follow these steps to delete an allow list by using the Amazon Macie console.

###### To delete an allow list by using the console

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, under **Settings**, choose
   **Allow lists**.
3. On the **Allow lists** page, select the checkbox for the allow
   list that you want to delete.
4. On the **Actions** menu, choose
   **Delete**.
5. When prompted for confirmation, enter `delete`, and then
   choose **Delete**.

API
To delete an allow list programmatically, use the [DeleteAllowList](../APIReference/allow-lists-id.md "../APIReference/allow-lists-id.md") operation
of the Amazon Macie API. For the `id` parameter, specify the unique identifier
for the allow list to delete. You can get this identifier by using the [ListAllowLists](../APIReference/allow-lists.md "../APIReference/allow-lists.md") operation. The **ListAllowLists** operation
retrieves information about all the allow lists for your account. If you're using the
AWS CLI, you can run the [list-allow-lists](../../../cli/latest/reference/macie2/list-allow-lists.md "../../../cli/latest/reference/macie2/list-allow-lists.md")
command to retrieve this information.

For the `ignoreJobChecks` parameter, specify whether to force deletion of
the list, even if sensitive data discovery jobs are configured to use the list:

- If you specify `false`, Macie checks the settings for all of your
  jobs that have a status other than `COMPLETE` or `CANCELLED`.
  If none of those jobs are configured to use the list, Macie deletes the list
  permanently. If any of those jobs are configured to use the list, Macie rejects your
  request and returns an HTTP 400 (`ValidationException`) error. The error
  message indicates the number of applicable jobs for up to 200 jobs.
- If you specify `true`, Macie deletes the list permanently without
  checking the settings for any of your jobs.

To delete an allow list by using the AWS CLI, run the [delete-allow-list](../../../cli/latest/reference/macie2/delete-allow-list.md "../../../cli/latest/reference/macie2/delete-allow-list.md")
command. For example:

```
`C:\>` `aws macie2 delete-allow-list --id `nkr81bmtu2542yyexample` --ignore-job-checks false`
```

Where `nkr81bmtu2542yyexample` is the unique identifier for
the allow list to delete.

If your request succeeds, Macie returns an empty HTTP 200 response. Otherwise, Macie
returns an HTTP 4*xx* or 500 response that indicates
why the operation failed.

If the allow list specified predefined text, you can optionally delete the S3 object that
stores the list. However, keeping this object can help ensure that you have an immutable
history of sensitive data findings and discovery results for data privacy and protection
audits or investigations.
