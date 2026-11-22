

# Requesting approval for a purchase

When a purchase needs approval, the purchase options page for the offer shows a **Purchase approval request** section. Under **Request sent to**, it shows who reviews the request: **Organization administrator**, the name of your organization's procurement system (for example, **Coupa**), or **Email approval chain**. For an email approval chain, the section also lists the approval levels and approvers. If the purchase needs more than one approval, the page shows **This purchase requires multiple approvals**.

**To request approval for a purchase**

1. On the purchase options page for the offer, review the offer details and the **Purchase approval request** section.

1. (Optional) Under **Purchase order (PO) number**, choose a **Purchase order number options** value and enter your purchase order numbers.

1. In **Notes for approvers**, add context for the approvers. A note is required and can be up to 1,000 characters.

1. Choose **Submit for approval**.

After you submit, the console opens the request details page. To return to it later, in the left navigation pane of the AWS Marketplace console, under **Private Marketplace**, choose **Approval requests**, and then choose the request. The request details page shows the request status, the approval levels and decisions, and any reason an approver gave. If the purchase matched more than one rule, the page also lists **Other requests for this purchase**.

Approvers have 30 days to complete a request. If the offer expires sooner, the **Request expires** date shows the offer expiration date instead, because AWS Marketplace can't create the agreement automatically after the offer expires. Approvers can still finish the review after that date. If they do, the request is approved, but the agreement isn't created. For what to do next, see **Approved** under the request outcomes that follow.

While a request is **Pending**, you can't submit another approval request for the same product. You can request to purchase the product again after the existing request is approved, declined, or cancelled.

**Request outcomes**  
While approvers review a request, its status is **Pending**. After a decision, the status is briefly **In progress** while AWS Marketplace processes it, and then changes to one of the following:

**Approved**  
Every required approval was granted. If the offer is still available, AWS Marketplace creates your agreement automatically. To view it, choose **View agreement**.  
If the offer expired before the last approval, AWS Marketplace doesn't create the agreement. You receive an email, and the request details page shows **Agreement creation failed**. Contact your seller to extend the offer expiration date, and then choose **Accept offer** to create the agreement. If you no longer want the purchase, cancel the request.

**Declined**  
An approver declined the request. The page shows who declined it and the reason. To submit again, address the reason and choose **Submit for approval**. The request starts again at level 1. If the purchase had more than one approval request, the purchase can't proceed after one is declined, even if the others are approved.

**Expired**  
The request wasn't completed within 30 days, so no agreement was created. To send the request again, choose **Submit for approval**.

**Cancelled**  
You cancelled the purchase request.

**To cancel a purchase request**

1. On the request details page, choose **Cancel request**.

1. Choose **Yes, cancel**.

Cancelling a purchase request cancels all of its approval requests and can't be undone. To buy the product later, submit a new request. You can also cancel an **Approved** request if its agreement wasn't created, for example after **Agreement creation failed**. You can cancel pending requests from the **Approval requests** list by selecting them and choosing **Cancel**.

For what happens in less common scenarios, such as an offer that expires during review or a purchase that requires a purchase order, see [Special cases for buyer approvals](buyer-approvals-special-cases.md).