

# Managing approval requests as an administrator

Your AWS management account or delegated administrator can view every purchase approval request in your organization, regardless of how the request is routed. In the left navigation pane of the AWS Marketplace console, under **Private Marketplace**, choose **Approval requests**.

Before you begin, make sure that you have the required IAM permissions. For more information, see [Permissions for approval requests in the AWS Marketplace console](buyer-approvals-console-permissions.md).

Requests that are waiting for a decision have the status **Pending**. A purchase can have several approval requests, one for each **Require approval** rule that it matches. If more than one matching rule uses the same approval routing, such as the same approval chain, the AWS Marketplace console, or your external system, only one approval request is created for that routing. AWS Marketplace creates the agreement only after every request for the purchase is approved. If any approval request is declined, the purchase can't proceed, even if the other approval requests are approved. If the buyer cancels the purchase request, all of its approval requests are cancelled. For other scenarios, see [Special cases for buyer approvals](buyer-approvals-special-cases.md).

**To approve or decline a request routed to the AWS Marketplace console**

1. On the **Approval requests** page, open the request.

1. Review the request details, and then choose **Approve** or **Decline**.

1. Enter a **Reason for approving** or **Reason for declining**. The reason is saved with the approval request, so you can view it later on the request details page. A decline reason is also shared with the requester.

1. Choose **Approve** or **Decline**.

The request status is **In progress** while AWS Marketplace processes your decision, and then changes to **Approved** or **Declined**. AWS Marketplace notifies the requester of your decision and your reason.

## Overriding an approval request
<a name="buyer-approvals-override"></a>

If a request routed to an email approval chain or an external system is stuck or time-sensitive, an administrator can override it. Overriding approves or declines the request directly, on behalf of the assigned approver or external system, and bypasses the original approval routing. Every override requires a reason.

Overriding is the same action as approving or declining a request in the console, and it requires the same IAM permissions. Only your AWS management account or a delegated administrator can override a request. For more information, see [Permissions for approval requests in the AWS Marketplace console](buyer-approvals-console-permissions.md).

**To override an approval request**

1. On the **Approval requests** page, open a request with the status **Pending**.

1. (Optional) To change the purchase order numbers that the override uses, edit them under **Purchase order (PO) number** on the request details page.

1. Choose **Override**.

1. Under **Override action**, choose **Override to approve** or **Override to decline**.

1. For an email approval chain request that you're approving, choose an **Approval scope**:
   + **Approve current level only** – Clears the stuck level so the next approver in the chain can act.
   + **Approve all levels** – This is the default. Approves every remaining level of the chain. If every other request for the purchase is also approved, AWS Marketplace creates the agreement.

   An override of an external system request always approves the whole request.

1. Enter a **Reason for override** or a **Reason for declining**. A decline reason is shared with the requester.

1. Choose **Override and approve** or **Override and decline**.

Levels approved or declined by an override are marked **Approved (by admin)** or **Declined (by admin)** in the approval chain. When you override to decline, later levels are marked **Skipped**. AWS Marketplace notifies the requester of your decision and your reason. You can't undo an override.