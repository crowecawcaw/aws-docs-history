

# Reopen an AWS account
<a name="manage-acct-reopening"></a>

If you closed your AWS account and do not have an outstanding balance, you can reopen it yourself during the [post-closure period](manage-acct-closing.md#post-closure-period).

You reopen your account by signing in as the root user and submitting the request from the Accounts page.

## What you need to know before reopening your account
<a name="reopen-account-considerations"></a>

Before you reopen your AWS account, note the following:
+ **Self-service requirements**: You can use this self-service process only if you closed the account yourself and your account had no outstanding balance at the time of account closure. You must sign in as the root user of the closed account; you can't reopen an account while signed in as an IAM user or role. You must submit your reopen request within 90 days of closing the account, during the post-closure period.
+ **Accounts closed by AWS**: If AWS closed your account, you can't reopen it yourself. Pay any outstanding balance within 30 days of the date your account was closed, and then contact [AWS Support](https://console.aws.amazon.com/support/home) to reopen your account.
+ **Payments and charges**: Your account must have a valid, unexpired payment method. Because your previous month's bill is finalized at the beginning of the following month, you might have an outstanding balance for usage before closure even if your account had no balance at closure. To review or pay a balance, see [Making payments](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-making-a-payment.html). When you reopen your account, charges resume for any services still running in it. If you didn't stop these services before closing the account, you might have incurred charges during the post-closure period as well.

## How to reopen your account
<a name="reopen-account-procedure"></a>

Follow these steps to reopen your closed account.

**Note**  
This task isn't supported in the AWS CLI or by an API operation from one of the AWS SDKs. You can perform this task only by using the AWS Management Console.<a name="reopening-the-account-proc"></a>

**To reopen your account from the Accounts page**

1. [Sign in to the AWS Management Console as the root user](https://docs.aws.amazon.com/signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.html) of the closed AWS account that you want to reopen. You can't reopen an account while signed in as an IAM user or role.

1. Open the Accounts page for the closed account, as follows: In the closed-account banner, choose **Reopen account**.

1. In the **Reopen account** dialog box, enter the account ID shown in the dialog box to confirm that you want to reopen the account.

1. Choose **Reopen account** to submit your request. A message confirms that account reopening has been initiated.

1. Wait for the reopen to complete. When your account is active again, a message confirms that the account has been successfully reopened and that your AWS services and billing have been restored.

If AWS can't reopen your account, you receive a console notification explaining why and how to resolve it.

## What to expect after you reopen your account
<a name="what-to-expect-after-reopening"></a>

After you submit a reopen request, the following occurs:
+ To check the status, refresh the Accounts page. When reopening is complete, the account shows as active and the closed-account banner no longer appears.
+ After the account is active, AWS restores access to its services and resources, and billing resumes.

## Prepare your account for use after reopening
<a name="prepare-account-after-reopening"></a>

Some resources and subscriptions are not restored to a running state automatically. After your account is reopened, you might need to do the following before you can resume normal operations:
+ Start any Amazon EC2 instances that were stopped at account closure. For more information, see [Start an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html#start-ec2-instance) in the *Amazon EC2 User Guide*.
+ Restore Amazon RDS databases from the snapshots created at account closure.
+ Cancel and re-subscribe to any AWS Marketplace subscriptions. Subscriptions aren't automatically restored on account reopening.

## Region availability
<a name="reopen-region-availability"></a>

Self-service account reopening is available in all commercial Regions.