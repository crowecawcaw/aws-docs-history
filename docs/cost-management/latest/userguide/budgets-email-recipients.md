

# Adding email recipients to a budget notification
<a name="budgets-email-recipients"></a>

To be notified about your budget's status, add email recipients to your budget notifications. When you add a new email address as a recipient, AWS Budgets sends a verification email to that address, and only verified addresses receive budget notifications. Email verification uses AWS User Notifications and follows the same recipient-confirm pattern used by other AWS services that rely on User Notifications. Email recipients on budgets created before AWS Budgets added verification continue to receive notifications without change. This topic describes how to add email recipients to a budget notification, how verification works, and how to troubleshoot verification issues.

You can add up to 10 email recipients per budget notification.

**Note**  
This topic covers email recipients added directly to a budget notification. If you send budget notifications through an Amazon SNS topic, see [Creating an Amazon SNS topic for budget notifications](budgets-sns-policy.md), which describes the Amazon SNS subscription confirmation flow separately.

## How verification works
<a name="budgets-email-recipients-how"></a>

When you add an email address as a recipient to a budget notification, AWS Budgets sends a verification email to that address. The verification email is sent from an `@aws.com` sender address. The recipient confirms the address by choosing the link in the verification email, which opens the AWS Management Console. The recipient must be signed in to the AWS account that added the email address to complete verification. Once verified, AWS Budgets begins sending budget notifications to the address. If the recipient does not verify the address, AWS Budgets does not send notifications to it.

If the recipient address is already verified for the same AWS account through another AWS service that uses User Notifications, adding it to a AWS Budgets recipient list activates it without a new verification email. The address appears with an Active status immediately.

Every email address is verified in an AWS account. If the same email address is a recipient on multiple budgets in the same account, one verification covers every budget. If the same email address is used across budgets in different AWS accounts (for example, a central FinOps address subscribed in linked accounts across an organization), each account requires its own verification, and the recipient must sign in to each account to complete verification. For scenarios where a single verification for many recipients is preferred, add an email distribution list as the recipient and manage list membership separately.

## Verification status
<a name="budgets-email-recipients-status"></a>

Verification status appears in the AWS Budgets console on the budget detail page. Each recipient row shows one of the following statuses:

**Active**  
The recipient confirmed the address, or the address was already verified for the AWS account through another AWS service that uses User Notifications. The address receives notifications.

**Pending**  
AWS Budgets sent a verification email and is waiting for the recipient to confirm.

**Expiring**  
The address was added to a budget notification before AWS Budgets introduced verification. The address continues to receive notifications during a grace period. Choose **Send Notification** to move it to Pending and preserve delivery after the grace period ends.

**Inactive**  
The address is not yet registered to receive notifications. Choose **Send Notification** to register the address and send a verification email. The status moves to Pending until the recipient confirms.

Each recipient row with a Pending status includes a **Resend verification** button that sends a fresh verification email. Rows with an Expiring or Inactive status include a **Send Notification** button that registers the address to receive notifications and sends a verification email.

## Adding an email recipient to a budget notification
<a name="budgets-email-recipients-add"></a>

Follow these steps when creating a new budget or adding a recipient to an existing budget.

**To add an email recipient**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management and Cost Management console at [https://console.aws.amazon.com/cost-management/](https://console.aws.amazon.com/cost-management/).

1. In the navigation pane, choose **Budgets**.

1. Create a new budget or open an existing budget, and add or edit an alert.

1. In the **Email recipients** field, enter one or more email addresses and save the alert.

1. AWS Budgets sends a verification email to each address that is not already verified in your account.

1. Each recipient must open the verification email, choose the link, and sign in to the AWS account that added the address. Verification completes in the AWS Management Console.

1. Refresh the budget detail page to see the updated verification status.

Verified recipients begin receiving budget notifications on the next scheduled evaluation.

## Troubleshooting
<a name="budgets-email-recipients-troubleshoot"></a>

**The recipient did not receive the verification email**  
Ask the recipient to check the spam folder. Verification emails come from an `@aws.com` sender address. If your organization uses an email allow list, add the `@aws.com` domain. If the email is not there, verify the address is correct in the AWS Budgets console. Choose **Resend verification** to try again. Verification emails are subject to a short cooldown between sends to protect email deliverability.

**The verification link has expired**  
Verification links expire 12 hours after send. Choose **Resend verification** to send a new link.

**The recipient's status is Inactive**  
An Inactive status means the address is not yet registered to receive notifications. Verify the address in the AWS Budgets console and correct any typos, then choose **Send Notification** to register the address.

**The recipient cannot complete verification**  
Verification requires the recipient to sign in to the AWS account that added the email address. If the recipient does not have access to that account, ask an administrator with access to that account to complete verification, or use a different recipient address. For scenarios where recipients cannot sign in to AWS, consider using an email distribution list as the recipient and managing list membership outside AWS.

**A recipient address is verified in one AWS account but not another**  
Verification is per email address per account. Each account requires its own verification, even for the same email address, and the recipient must sign in to each account to complete verification.