

# Reviewing approval requests

How approvers review a request depends on the rule's approval routing:

Email approval chain  
When a request reaches their level, each approver on that level receives an email with the subject "AWS Marketplace purchase approval needed." The approver verifies their identity with a one-time passcode and reviews the request in their browser. They don't need an AWS account.

AWS Marketplace console  
Your AWS management account or delegated administrator reviews the request on the **Approval requests** page in the AWS Marketplace console. For more information, see [Managing approval requests as an administrator](buyer-approvals-requests-page.md). For the IAM permissions that approvers need, see [Permissions for approval requests in the AWS Marketplace console](buyer-approvals-console-permissions.md).

External system  
The request appears in your organization's procurement system, such as Coupa or SAP Ariba. Approvers review it there, following your organization's standard approval process, and the decision is returned to AWS Marketplace. For more information, see [Integrating AWS Marketplace with procurement systems](procurement-system-integration.md).

The approval request shows what the buyer selected in AWS Marketplace, whether a public offer or a private offer with custom pricing and terms. It includes the requester's AWS account ID, the buyer's note, the product, pricing, payment schedule, total cost, and terms and conditions. Approvers after level 1 also see the decisions and reasons from earlier levels.

**To review an approval request as an email approver**

1. In the approval request email from AWS Marketplace, choose **Review request**.

1. Choose **Get a One Time Passcode**. AWS Marketplace sends a 6-digit one-time passcode to your email address. Enter the passcode in **One-time passcode**, and then choose **Verify and continue**. The passcode expires in 15 minutes. If you didn't receive it, wait 30 seconds and choose **Resend code**.

1. Review the purchase details.

1. (Optional) Add a purchase order number. For more information, see [Adding purchase order numbers when you approve](#buyer-approvals-approver-po).

1. Choose **Approve purchase** or **Decline purchase**.

1. Enter an **Approval reason** or a **Decline reason**. A reason is required, can be up to 1,000 characters, and is shared with the buyer. Then choose **Approve** or **Decline**.

When you approve, the request moves to the next level. If you're the final approver, the request is approved. If the purchase has other approval requests, AWS Marketplace creates the agreement after all of them are approved. When you decline, the request ends at your level. It isn't sent to later approvers, and the purchase doesn't proceed. You can't undo a decline.

Your review session lasts 15 minutes after you verify the passcode. To renew it for another 15 minutes, choose the session timer at the top of the page, and then choose **Stay signed in**. AWS Marketplace also prompts you when 2 minutes remain. If the session expires, choose **Verify to continue** and enter a new passcode. Your in-progress review is restored after you verify.

## Adding purchase order numbers when you approve
<a name="buyer-approvals-approver-po"></a>

Email approvers can add purchase order (PO) numbers to a purchase when they approve it. If the buyer already assigned PO numbers, you can also change them, and your values replace the buyer's. The PO numbers are used on the invoices for this offer.

**To add purchase order numbers as an approver**

1. On the review page, under **Pricing details**, find **Purchase order (PO) number**.

1. Under **Purchase order number options**, choose one of the following:
   + **No PO number**
   + **One PO number for all charges** – Editing the purchase order number on any charge applies it to all charges on this offer.
   + **Individual PO numbers for each charge**

1. In the **Payment schedule** table, enter the **Purchase order number** and **Purchase order line number** for each charge.

1. Choose **Approve purchase**. The approval dialog shows the previous and new purchase order values. Your changes are saved only when you approve.