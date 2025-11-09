AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Creating OpsItems manually

(console)

You can manually create OpsItems using the AWS Systems Manager console. When you create an
OpsItem, it's displayed in your OpsCenter account. If you set up OpsCenter for
cross-account administration, OpsCenter provides the delegated administrator or
management account with the option to create OpsItems for selected member accounts.
For more information, see [(Optional)
Manually set up OpsCenter to centrally manage OpsItems across accounts](OpsCenter-getting-started-multiple-accounts.md "OpsCenter-getting-started-multiple-accounts.md").

###### To create an OpsItem using the AWS Systems Manager console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **OpsCenter**.
3. Choose **Create OpsItem**. If you don't see this button,
   choose the **OpsItems** tab, and then choose
   **Create OpsItem**.
4. (Optional) Choose **Other account**, and then choose
   the account where you want to create the OpsItem.

###### Note

This step is required if you're creating OpsItems for a member
account. 5. For **Title**, enter a descriptive name to help you
understand the purpose of the OpsItem. 6. For **Source**, enter the type of impacted AWS
resource or other source information to help users understand the origin
of the OpsItem.

###### Note

You can't edit the **Source** field after you
create the OpsItem. 7. (Optional) For **Priority**, choose the priority
level. 8. (Optional) For **Severity**, choose the severity
level. 9. (Optional) For **Category**, choose a
category. 10. For **Description**, enter information about this
OpsItem including (if applicable) steps for reproducing the issue.

###### Note

The console supports most markdown formatting in the OpsItem
description field. For more information, see [Using
Markdown in the Console](../../../awsconsolehelpdocs/latest/gsg/aws-markdown.md "../../../awsconsolehelpdocs/latest/gsg/aws-markdown.md") in the _Getting Started with the AWS Management Console
Getting Started Guide._ 11. For **Deduplication string**, enter words that the
system can use to check for duplicate OpsItems. For more information about
deduplication strings, see [Managing duplicate OpsItems](OpsCenter-working-deduplication.md "OpsCenter-working-deduplication.md"). 12. (Optional) For **Notifications**, specify the Amazon
Resource Name (ARN) of the Amazon SNS topic where you want notifications sent
when this OpsItem is updated. You must specify an Amazon SNS ARN that is in the
same AWS Region as the OpsItem. 13. (Optional) For **Related resources**, choose
**Add** to specify the ID or ARN of the impacted
resource and any related resources. 14. Choose **Create OpsItem**.
If successful, the page displays the OpsItem. When a delegated administrator or
management account creates an OpsItem for selected member accounts, the new OpsItems
are displayed in the OpsCenter of the administrator and members accounts. For
information about how to configure the options in an OpsItem, see [Manage OpsItems](OpsCenter-working-with-OpsItems.md "OpsCenter-working-with-OpsItems.md").
