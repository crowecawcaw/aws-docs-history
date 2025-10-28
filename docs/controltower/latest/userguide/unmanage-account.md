# Unenroll an account

If you created an account in Account Factory or enrolled an AWS account, and you no
longer want the account to be managed by AWS Control Tower in a landing zone, you can
_unenroll_ the account from the AWS Control Tower console.

When you unenroll an AWS Control Tower account, all resources provisioned by AWS Control Tower are
removed, including any controls and blueprints. The account is moved out of any AWS Control Tower
OU and into the **Root** area. The account is no longer part of a
registered OU, and it is no longer subject to AWS Control Tower SCPs. You can close the account
through AWS Organizations.

###### To unenroll an enrolled account from the AWS Control Tower console

1. Open the AWS Control Tower console in your web browser at [https://console.aws.amazon.com/controltower](https://console.aws.amazon.com/controltower "https://console.aws.amazon.com/controltower")
2. In the left navigation pane, choose **Organization**.
3. In the **Organization** page, expand the OU that contains the
   account, by selecting the **+** button near the OU.
4. Select the account and then choose **Unmanage**.

###### Note

Wait for the account's status to show **Not enrolled**.

If you no longer need the account, close it. For more information about closing AWS
accounts, see [Closing an account](../../../awsaccountbilling/latest/aboutv2/close-account.md "../../../awsaccountbilling/latest/aboutv2/close-account.md")
in the _AWS Billing User Guide_

###### Unenroll an account when auto-enroll is active

If the auto-enroll capability is active in your **Settings**
page, you also can unenroll an account by moving it into an OU that is not
registered in AWS Control Tower. All AWS Control Tower resources are removed. Be aware that you do not
unenroll the account accidentally in this manner. However, you can re-enroll the
account by returning it to the OU.

When you unenroll a customized account, AWS Control Tower removes the resources that the
landing zone has deployed, as well as any other resources that AWS Control Tower created within the
account. AWS Control Tower also removes the **AWSControlTowerExecution** role,
even if it was added manually. Removing this role aligns with the principle of least
privilege, because a service execution role should not stay in an unmanaged
account.

After you unenroll the account, you can close the account through AWS Organizations.

###### Note

An unenrolled account is not closed or deleted. When the account has been
unenrolled, the IAM Identity Center user that you selected when you created the account in
Account Factory still has administrative access to the account. If you do not want this
user to have administrative access, you must change this setting in IAM Identity Center by
updating the account in Account Factory and changing the IAM Identity Center user email address for the
account. For more information, see [Update and move accounts with AWS Control Tower](updating-account-factory-accounts.md "updating-account-factory-accounts.md").

## Video walkthrough

This video (3:25) describes how to remove an account from AWS Control Tower, gain root
access to the account, and finally close the AWS account. You also can close an
account with [an AWS Organizations
API](delete-account.md "delete-account.md"). For better viewing, select the icon at the lower right corner of the
video to enlarge it to full screen. Captioning is available.

You can view a list of AWS [YouTube videos](https://www.youtube.com/playlist?list=PLhr1KZpdzukdS9skEXbY0z67F-wrcpbjm "https://www.youtube.com/playlist?list=PLhr1KZpdzukdS9skEXbY0z67F-wrcpbjm") that explain common tasks in AWS Control Tower.
