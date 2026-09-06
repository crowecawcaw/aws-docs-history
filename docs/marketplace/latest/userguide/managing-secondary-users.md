

# Managing secondary users for Know Your Customer (KYC)
<a name="managing-secondary-users"></a>

After KYC verification is complete, the AWS account root user has access to financial functions such as processing refunds, changing bank account details, and managing disbursement frequency options. However, as a security best practice, we strongly recommend that you do not use the root user for everyday tasks. The root user has unrestricted access to all resources in your account and its credentials should be safeguarded for only the tasks that require them. Instead, create administrative users with appropriate permissions for day-to-day operations. For more information, see [Root user best practices for your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html).

All other users who need access to these financial functions are referred to as secondary users. Secondary users must complete their own KYC verification using their individual login credentials before they can amend KYC information, process refunds, or change financial information such as bank account details. These secondary users are subject to the same ongoing screening controls as the root account owner.

**Note**  
Users are required to enable multi-factor authentication (MFA) to update disbursement information. For more information about MFA, see [Multi-Factor Authentication (MFA) for IAM](https://aws.amazon.com/iam/features/mfa/).

To become KYC verified, secondary users must complete the same KYC process as described in [Complete the KYC process](complete-kyc-process.md). 

**To add secondary users for the Know Your Customer procedure**

1. Ask the user to sign in to AWS Partner Central at [https://us-east-1.console.aws.amazon.com/partnercentral/home](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. Navigate to the **Settings** tab.

1. Choose the **Know Your Customer (KYC)** tab and see the section for **Secondary user information**.

1. Choose **Complete secondary user information**.

   You are redirected to the **Secondary User** registration portal.

1. In the **Secondary User** registration portal, complete the required fields, and then choose **Next**.

1. On the **Review and Submit** page, upload a copy of the identity document (**Upload Passport**) and proof of address (**Upload Document**).

1. Choose **Submit for Verification**.

The status of the secondary user's KYC compliance will be reviewed (typically within 24 hours). You will be notified through an email message after the review is complete.