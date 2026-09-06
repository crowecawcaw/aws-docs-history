

# Unenroll an account in Service Catalog
<a name="unenroll-with-sc"></a>

 Unenrolling an account can be done in the Service Catalog console by an IAM Identity Center user in the `AWSAccountFactory` group, by terminating the Provisioned Product. For more information on IAM Identity Center users or groups, see [Manage users and access through AWS IAM Identity Center](https://docs.aws.amazon.com/controltower/latest/userguide/unmanage-account.html). The following procedure describes how to unenroll a member account in Service Catalog.

**To unenroll an enrolled account through Service Catalog**

1. Open the Service Catalog console in your web browser at [https://console.aws.amazon.com/servicecatalog](https://console.aws.amazon.com/servicecatalog).

1. In the left navigation pane, choose **Provisioned products list**.

1. From the list of provisioned accounts, choose the name of the account that you want AWS Control Tower no longer to manage.

1. On the **Provisioned product details** page, from the **Actions** menu, choose **Terminate**.

1. From the dialog box that appears, choose **Terminate**.
**Important**  
The word *terminate* is specific to Service Catalog. When you terminate an account in Service Catalog Account Factory, the account is not closed. This action removes the account from its OU and your landing zone.

1.  When the account has been unenrolled, its status changes to **Not Enabled**.

1. If you no longer need the account, close it. For more information about closing AWS accounts, see [Closing an account](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/close-account.html) in the *AWS Billing User Guide*

**Note**  
Wait for the account's status to show **Not Enabled**.