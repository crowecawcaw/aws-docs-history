

# Adding email approvers

Before you can add an approver who doesn't have an AWS account to an approval chain, you add them as an email approver. Email approvers don't receive requests until you add them to an approval chain and assign that chain to a rule.

**To add an email approver**

1. Using your AWS management account or a delegated administrator account, open [Approvers and routing](https://console.aws.amazon.com/marketplace/buying-policies/approvers-and-routing?tab=email-approvers) in the AWS Marketplace console. It's under **Buying policies** in the left navigation pane.

1. On the **Email approvers and chains** tab, choose **Add email approver**.

1. Enter the approver's **Email** and **Full name**. To add more approvers at the same time, choose **Add another**.

1. Choose **Add approver**.

Each approver receives a verification email with the subject "Verify your email address." The approver verifies by choosing the link in the email. The link expires after 7 days. In the **Email approvers** table, the approver's status is **Unverified** until they verify, and then **Verified**. You can add only verified approvers to approval chains.

If an approver didn't receive the email or the link expired, choose **Resend verification email** in the approver's row. After you resend, you must wait 10 minutes before you can resend again.

**Note**  
You can't edit an email approver after you add them. To change an approver's name or email address, delete the approver and then add a new one. If the approver is in an approval chain, remove them from the chain before you delete them, and then add the new approver to the chain.