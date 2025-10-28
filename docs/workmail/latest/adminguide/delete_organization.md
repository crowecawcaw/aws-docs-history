# Deleting an organization

If you no longer want to use Amazon WorkMail for your organization's email, you can delete
your organization from Amazon WorkMail.

###### Note

This operation can't be undone. You won't be able to recover your mailbox data
after an organization is deleted.

###### To delete an organization

1. Open the Amazon WorkMail console at
   [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/ "https://console.aws.amazon.com/workmail/").

If necessary, change the AWS Region. In the bar at the top of the console
window, open the **Select a Region** list and choose a Region.
For more information, see [Regions and
endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the _Amazon Web Services General Reference_. 2. On the **Organizations** screen, in the list of
organizations, select the organization to delete and choose
**Delete**. 3. For **Delete organization**, choose whether to delete or keep
the existing user directory, and then enter the name of the organization. 4. Choose **Delete organization**.

###### Note

If you didn't provide your own directory for Amazon WorkMail, we'll create one for you. If
you keep this existing directory when you delete the organization, you will be
charged for it unless it is being used by Amazon WorkMail, WorkDocs, or WorkSpaces. For pricing
information, see [Other
directory types pricing](https://aws.amazon.com/directoryservice/other-directories-pricing/ "https://aws.amazon.com/directoryservice/other-directories-pricing/").

In order to delete the directory, it can't have any other AWS applications
enabled. For more information, see [Deleting a
Simple AD directory](../../../directoryservice/latest/admin-guide/simple_ad_delete.md "../../../directoryservice/latest/admin-guide/simple_ad_delete.md") or [Deleting an
AD Connector directory](../../../directoryservice/latest/admin-guide/ad_connector_delete.md "../../../directoryservice/latest/admin-guide/ad_connector_delete.md") in the
_AWS Directory Service Administration Guide_.

You may get an invalid Amazon Simple Email Service (Amazon SES) rule set error message when you attempt to
delete an organization. If you receive this error, edit the Amazon SES rule in the Amazon SES
console and remove the invalid rule set. The rule that you edit should have your Amazon WorkMail
organization ID in the rule name. For more information about editing Amazon SES rules, see
[Creating
receipt rules](../../../ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.md "../../../ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.md") in the _Amazon Simple Email Service Developer Guide_.

If you need to figure out which rule set is not valid, save the rule first. An error
message appears for the rule set.
