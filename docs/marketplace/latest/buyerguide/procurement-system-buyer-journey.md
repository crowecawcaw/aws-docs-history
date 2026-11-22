

# Understanding what your buyers see

Once the integration is configured and your rules are in place, the purchases your rules cover are gated. A buyer can't complete one in AWS Marketplace and can't skip the approval. The purchase has to be sent to your procurement system and approved there before it completes, so the request a buyer creates and the approval they wait for both live in the system they already use.

This topic follows a purchase stage by stage, describing what the buyer sees at each one, so that you can tell where a purchase has reached when a buyer asks. To run the same sequence yourself as a test, see [Testing your procurement system integration](procurement-system-testing.md).

## A purchase stage by stage
<a name="procurement-system-buyer-journey-steps"></a>

**What the buyer does, and what they see at each stage**

1. The buyer signs in to your procurement system and starts a punchout session by choosing the AWS Marketplace supplier.

   They arrive in the AWS Marketplace catalog. With single sign-on configured, they go through your own sign-in page and aren't asked to sign in to AWS separately. For more information about single sign-on, see [Configuring single sign-on for procurement system integration](procurement-system-sso.md).

1. The buyer browses the catalog and opens the offer they want.

   On an offer your rules cover, the action reads **Request Approval** rather than one that completes the purchase. That is how the buyer knows the purchase is governed, and it's the first thing to check if a purchase you expected to be governed wasn't. For more information about approval rules, see [Routing purchases to your procurement system](procurement-system-routing.md).

1. The buyer chooses **Request Approval**.

   Before the request is submitted, the buyer makes any choices the purchase needs. For what those are, see [What the buyer decides before submitting](#procurement-system-buyer-journey-decisions).

1. The cart returns to your procurement system as a purchase requisition, with the charges as line items.

   From here the buyer works in your system rather than in AWS Marketplace.

1. The buyer submits the requisition, and your own approval workflow runs on it.

   This part is entirely yours. AWS Marketplace waits and plays no part in who approves or in what order.

1. When the requisition is approved, your procurement system sends a purchase order back to AWS Marketplace.

   On the [**Approval requests**](https://console.aws.amazon.com/marketplace/private-marketplace/approval-requests?region=us-east-1) page, the request now shows as **Approved**, and its details page shows the purchase order your procurement system returned.

1. AWS Marketplace matches the purchase order against the approval it answers, creates the agreement, and emails the buyer to tell them the subscription is ready.

   The agreement appears on the [**Manage subscriptions**](https://console.aws.amazon.com/marketplace/subscriptions?region=us-east-1) page, with the purchase order associated with a charge.

1. The buyer can now use the product.

   They might return to AWS Marketplace for instructions on how to deploy or configure it, but they don't have to come back to finish buying.

## What the buyer decides before submitting
<a name="procurement-system-buyer-journey-decisions"></a>

Two choices belong to the buyer rather than to you, and both change what your procurement system receives.

Which seller of record to purchase through  
If more than one of your connections covers the purchase, the buyer chooses which one to use. If exactly one covers it, that one is used and the buyer isn't asked. For how to arrange connections so that this choice is predictable, see [Create one connection per seller of record](procurement-system-best-practices.md#procurement-system-best-practices-connections).

Whether to split the purchase into separate line items  
The buyer decides whether the purchase arrives as a single line item or as one line item for each charge. This decides how your invoices reconcile against the purchase order afterwards, so it matters to your finance team even though it's the buyer's choice. For more information, see [How invoices match your purchase order lines](procurement-system-invoicing.md#procurement-system-invoicing-line-items).

## When a purchase can't be sent to your procurement system
<a name="procurement-system-buyer-journey-no-session"></a>

Sending an approval to your procurement system needs two things: a punchout session to return the cart to, and a connection covering the AWS Billing entity, also called the seller of record, that the purchase is billed through. Two situations leave one of them missing.
+ **The buyer opened the offer without a punchout session** – they reached AWS Marketplace some other way, such as from a bookmark, so there is no session and nowhere to return the cart.
+ **No connection covers the seller of record** – no connection names that billing entity, or your connections cover it in a way the buyer can't choose between.

In both cases AWS Marketplace shows the buyer a message explaining what's wrong, rather than letting the purchase fail later. The message asks them to start a punchout session, or to ask their administrator to configure the missing seller of record.

The buyer isn't fully blocked. The message also offers **Send to Procurement Admin**, which sends the approval request to a procurement administrator instead. The administrator can then override the approval in the AWS console and the purchase completes, or override and disapprove the approval request and give the buyer guidance. For more information about overriding an approval, see [Overriding an approval](procurement-system-supported-scenarios.md#procurement-system-scenarios-override).

**Important**  
A purchase settled this way never passes through your procurement system. No requisition is raised and no purchase order is returned, so it won't appear in your procurement records alongside the others. If buyers are sending requests to an administrator repeatedly, treat it as a configuration problem rather than a workflow: either a billing entity your buyers purchase through has no connection covering it, or your buyers are reaching AWS Marketplace without punching out.

Whether a buyer can begin in AWS Marketplace at all depends on your procurement system:
+ **Coupa with direct punchout turned on** – the buyer can begin in AWS Marketplace, without starting in Coupa to set the session up. Their cart is still returned to Coupa. For more information about direct punchout, see [Letting buyers start in AWS Marketplace instead of Coupa](procurement-system-integration-coupa.md#procurement-system-coupa-direct-punchout).
+ **SAP Ariba, or Coupa without direct punchout** – the buyer has to begin in the procurement system. Tell your buyers to start there rather than from a bookmark in AWS Marketplace.

Separately, a buyer can find a product somewhere other than the AWS Marketplace website, such as the console of another AWS service. Requesting approval works from the website only, so in that case AWS Marketplace sends them to the right place to carry on rather than leaving them stuck. For more information, see [Where buyers can request approval](procurement-system-supported-scenarios.md#procurement-system-scenarios-where-buyers-request).

## Purchase orders the buyer has to supply
<a name="procurement-system-buyer-journey-purchase-orders"></a>

When the purchase travels through your procurement system, the purchase order comes back with the approval and the buyer does nothing about it.

If you require purchase orders, there is one case where the buyer has to act. A purchase can carry charges that weren't sent to your procurement system, and those charges still need a purchase order. The buyer supplies it in AWS Marketplace after the approval comes back.

For the setting that requires purchase orders, and how it interacts with approval rules, see [Using procurement system integration with other governance settings](procurement-system-governance-settings.md).

## When a purchase needs more than one approval
<a name="procurement-system-buyer-journey-multiple-approvals"></a>

A purchase can need approval from more than one place. This happens when your rules send the same purchase to two different approvers, and it also happens with some kinds of agreement that are approved in stages.

From the buyer's side, the purchase isn't finished until every approval it needs has been given. They might be asked to act more than once, and the purchase isn't stuck in the meantime.

## Approval time counts against the offer
<a name="procurement-system-buyer-journey-offer-expiry"></a>

An offer has its own expiry date, set by the seller, and the time a purchase spends waiting for approval counts against it. Nothing pauses the offer while your approvers decide.

**Important**  
If the offer expires before the purchase completes, the approval can still go through, but the agreement isn't created automatically. You receive a notification when this happens. The buyer asks the seller to extend the offer expiry, and once that's done they return to AWS Marketplace and accept the agreement from the product page, without needing approval again.

This matters most for private offers, and most for organizations whose approvals take days rather than hours. Two things help. When you ask a seller for a private offer, ask for an expiry date that allows for how long approval actually takes in your organization. And where a purchase is time-critical, tell your approvers, because a decision that arrives after expiry turns a finished approval into further work: a request to the seller, and then a manual acceptance in AWS Marketplace.

For what to do when this happens, see [An approval doesn't complete](procurement-system-troubleshooting.md#procurement-system-troubleshooting-approval-stuck).