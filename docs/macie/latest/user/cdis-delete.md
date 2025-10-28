# Deleting a custom data identifier

After you create a custom data identifier, you can delete it. If you do this,
Amazon Macie soft deletes the custom data identifier. This means that a record of the
custom data identifier remains for your account, but it’s marked as deleted. If a custom
data identifier has this status, you can’t configure new sensitive data discovery jobs to use it or
add it to your settings for automated sensitive data discovery. In addition, you can no longer access it by
using the Amazon Macie console. You can, however, retrieve its settings by using the
Amazon Macie API. If you delete a custom data identifier, it doesn’t count against the
quota of custom data identifiers for your account.

If you configure a sensitive data discovery job to use a custom data identifier that you subsequently
delete, the job will run as scheduled and continue to use the custom data identifier.
This means that your job results, both sensitive data findings and sensitive data discovery results, will
report text that matches the identifier's criteria. This helps ensure that you have an immutable history of sensitive data findings and discovery results for data privacy and protection audits or investigations that you perform.

Similarly, if you configure automated sensitive data discovery to use a custom data identifier that you
subsequently delete, daily analysis cycles will proceed and continue to use the custom
data identifier. This means that sensitive data findings, statistics, and other types of
results will continue to report text that matches the identifier's criteria.

Before you delete a custom data identifier, do the following to prevent Macie from
using it during subsequent analysis cycles and job runs:

- Check your settings for automated sensitive data discovery. If you added the custom data identifier to
  these settings, remove it. For more information, see [Configuring settings for automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md").
- Review your job inventory to identify jobs that use the custom data identifier
  and are scheduled to run in the future. If you want a job to stop using the
  custom data identifier, you can cancel the job. Then create a copy of the job,
  adjust the settings for the copy, and save the copy as a new job. For more
  information, see [Managing sensitive data discovery jobs](discovery-jobs-manage.md "discovery-jobs-manage.md").
  It's also a good idea to note the unique identifier (ID) that Macie assigned to the
  custom data identifier. You'll need this ID if you later want to review the custom data
  identifier's settings.

After you complete the preceding tasks, delete the custom data identifier.

###### To delete a custom data identifier

You can delete a custom data identifier by using the Amazon Macie console or the
Amazon Macie API.

Console
Follow these steps to delete a custom data identifier by using the
Amazon Macie console.

###### To delete a custom data identifier

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, under **Settings**,
   choose **Custom data identifiers**.
3. To note the unique identifier (ID) for the custom data identifier
   that you want to delete, choose the custom data identifier's name.
   On the page that appears, the **Id** box displays
   this ID. After you note the ID, choose **Custom data
   identifiers** in the navigation pane again.
4. On the **Custom data identifiers** page, select the checkbox for the
   custom data identifier to delete.
5. On the **Actions** menu, choose
   **Delete**.
6. When prompted for confirmation, choose
   **Ok**.

API
To delete a custom data identifier programmatically, use the [DeleteCustomDataIdentifier](../APIReference/custom-data-identifiers-id.md "../APIReference/custom-data-identifiers-id.md") operation of the Amazon Macie API. Or,
if you're using the AWS Command Line Interface (AWS CLI), run the [delete-custom-data-identifier](../../../cli/latest/reference/macie2/delete-custom-data-identifier.md "../../../cli/latest/reference/macie2/delete-custom-data-identifier.md") command.

For the `id` parameter, specify the unique identifier (ID) for
the custom data identifier that you want to delete. You can get this ID by
using the [ListCustomDataIdentifiers](../APIReference/custom-data-identifiers-list.md "../APIReference/custom-data-identifiers-list.md") operation. This operation retrieves a
subset of information about the custom data identifiers for your account. If
you're using the AWS CLI, you can run the [list-custom-data-identifiers](../../../cli/latest/reference/macie2/list-custom-data-identifiers.md "../../../cli/latest/reference/macie2/list-custom-data-identifiers.md") command to retrieve this
information.

The following example shows how to delete a custom data identifier by
using the AWS CLI.

```
`$` `aws macie2 delete-custom-data-identifier --id `393950aa-82ea-4bdc-8f7b-e5be3example``
```

Where `393950aa-82ea-4bdc-8f7b-e5be3example` is
the ID for the custom data identifier to delete.

If the request succeeds, Macie returns an empty HTTP 200 response.
Otherwise, Macie returns an HTTP 4*xx* or
500 response indicating why the request failed.

To review a custom data identifier's settings after you delete it, use the [GetCustomDataIdentifier](../APIReference/custom-data-identifiers-id.md "../APIReference/custom-data-identifiers-id.md") operation of the Amazon Macie API. Or, if you're using
the AWS CLI, run the [get-custom-data-identifier](../../../cli/latest/reference/macie2/get-custom-data-identifier.md "../../../cli/latest/reference/macie2/get-custom-data-identifier.md") command. For the `id` parameter,
specify the custom data identifier's ID. After you delete a custom data identifier, you
can't access its settings by using the Amazon Macie console.
