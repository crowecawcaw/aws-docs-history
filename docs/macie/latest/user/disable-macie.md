

# Disabling Macie for your AWS account
<a name="disable-macie"></a>

If you want to stop using Amazon Macie in a particular AWS Region, you can disable it for your AWS account in the Region.

When you disable Macie in a Region, Macie stops performing all activities for your account in the Region. The activities include: monitoring your Amazon Simple Storage Service (Amazon S3) data, performing automated sensitive data discovery, and running sensitive data discovery jobs that are currently in progress. Macie also deletes all existing settings, resources, and data that it stores or maintains for your account in the Region. For example, Macie deletes your findings and sensitive data discovery jobs. Data that you stored or published to other AWS services remains intact and isn't affected—for example, sensitive data discovery results in Amazon S3 and finding events in Amazon EventBridge.

If your account is part of an organization that centrally manages multiple Macie accounts, you must do the following before you disable Macie for your account:
+ If you have a member account, work with your Macie administrator to remove your account as a member account.
+ If you're the Macie administrator for the organization, remove all member accounts that are associated with your account. Also delete the associations between your account and those accounts. 

How you complete the preceding tasks depends on whether your account is associated with other accounts through AWS Organizations or by invitation. For more information, see [Managing multiple accounts](macie-accounts.md).

**To disable Macie for your account**

To disable Macie for your account, you can use the Amazon Macie console or the Amazon Macie API. Follow these steps to disable it by using the console. To disable it programmatically, use the [DisableMacie](https://docs.aws.amazon.com/macie/latest/APIReference/macie.html) operation of the Amazon Macie API.
**Warning**  
If you disable Macie in a Region, you also permanently delete all of your existing findings, sensitive data discovery jobs, custom data identifiers, and other resources and data that Macie stores or maintains for your account in the Region. The resources and data can't be recovered after they're deleted. To keep the resources and data, [suspend Macie](suspend-macie.md) instead of disabling it. 

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/).

1. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to disable Macie.

1. In the navigation pane, choose **Settings**.

1. In the **Disable Macie** section, choose **Disable Macie**.

1. When prompted for confirmation, enter **Disable**, and then choose **Disable**.

To disable Macie in additional Regions, repeat the preceding steps in each additional Region.