

# Supported and unsupported procurement system scenarios

This topic lists what the procurement system integration does and does not support, and explains the reason for each limitation where it helps you plan around it.

Several of these boundaries affect how you write your approval rules. For the rules themselves, see [Routing purchases to your procurement system](procurement-system-routing.md).

## What the integration supports
<a name="procurement-system-scenarios-group-integration"></a>

These boundaries are about the integration itself: what it can carry between AWS Marketplace and your procurement system, and where a buyer can use it.

### What you can do in your procurement system
<a name="procurement-system-scenarios-in-your-system"></a>

The integration supports:
+ Starting a new punchout session and browsing the AWS Marketplace catalog
+ Returning a purchase order to settle an approval

It doesn't support editing or inspecting a cart you created earlier. Only new sessions are accepted.

It doesn't support changing or cancelling a purchase order through the integration. Only new purchase orders are accepted.

It doesn't support adding your own line items to the cart. What AWS Marketplace approves is a specific set of charges, and a returning purchase order is matched against them line by line. A line referring to a charge the approval doesn't contain can't be settled, because there is nothing to settle it against. The same applies to editing the charges on a line. Removing a line from the purchase order can prevent the approval from being accepted, or leave a charge without a purchase order to associate with.

Whether a buyer can begin a purchase in AWS Marketplace rather than in your procurement system depends on the system. Coupa supports Punchout Anywhere, which allows it. For more information, see [Letting buyers start in AWS Marketplace instead of Coupa](procurement-system-integration-coupa.md#procurement-system-coupa-direct-punchout).

### Using more than one procurement system
<a name="procurement-system-scenarios-one-system"></a>

Your organization can have one procurement system integrated at a time: Coupa or SAP Ariba, not both.

That limit is on the system, not on connections. You can have several connections to that one system, which is how you cover more than one AWS Billing entity. For more information about arranging connections, see [Create one connection per seller of record](procurement-system-best-practices.md#procurement-system-best-practices-connections).

You can integrate one procurement system at a time. To switch, remove the integration with the current one first, then set up the new one. For more information, see [Turning off a procurement system integration](procurement-integration-disabling.md).

### Where buyers can request approval
<a name="procurement-system-scenarios-where-buyers-request"></a>

Your buyers can find AWS Marketplace products in several places. They can browse the AWS Marketplace website, and they can also reach AWS Marketplace offers from the AWS Marketplace console and from the consoles of other AWS services, such as the Amazon Bedrock console and the Amazon EC2 console.

**Requesting approval works from the AWS Marketplace website only.** A purchase that needs approval has to be requested there, so that it can be sent to your procurement system.

Buyers don't have to know that in advance. If a buyer tries to request approval somewhere else, AWS Marketplace sends them to the right place to carry on:
+ From the AWS Marketplace console, the buyer is redirected to the AWS Marketplace website automatically.
+ From another service's console, the buyer is given a link to open so that they can continue the request on the AWS Marketplace website.

Either way the buyer's session isn't lost and they don't have to start again. They continue from where they were, on the website.

**Note**  
This affects where a purchase is *requested*, not what your rules govern. A purchase found through another service's console is still subject to the same approval rules.

## Products and purchase types
<a name="procurement-system-scenarios-group-purchases"></a>

Which kinds of purchase go through approval, and how each one behaves when it does.

### Upgrades, amendments, and renewals
<a name="procurement-system-scenarios-products"></a>

An upgrade raises a fresh approval against the upgraded terms.

An amendment is treated as a new purchase and goes through approval again. Only one amendment can be in progress against an agreement at a time, so cancel a pending one to unblock another.

An automatic renewal doesn't raise a new approval. The renewal term was approved when the original purchase was approved.

AWS Marketplace Vendor Insights and reseller agreements aren't governed by approval policies.

### Usage-based products and budget estimates
<a name="procurement-system-scenarios-usage-estimates"></a>

Products with usage-based pricing, such as contracts with consumption pricing, usage-based products, monthly recurring products, and annual agreements that combine usage with a contract, let you set a budget estimate for the usage you expect, and submit that estimate through your procurement system for approval.

The buyer provides the estimated usage, but that value is information sent to your procurement system only. Your approval rules aren't governed by it. Your actual charges are based on your real usage and billed monthly against the approved purchase order, whatever the estimate was. Your subscription doesn't stop if your usage exceeds the estimate.

### Offer Sets
<a name="procurement-system-scenarios-composable"></a>

In an Offer Set, each component is approved separately and the components are independent of one another. Some components may be auto-approved if your rules don't require approval for them.

This means partial outcomes are possible. If one component is approved and another is declined, the buyer ends up with part of what they asked for rather than none of it.

### Amazon Bedrock Foundational Models
<a name="procurement-system-scenarios-bedrock"></a>

Serverless models in the Amazon Bedrock model catalog (the models deployed as Serverless) don't go through the approval flow, so approval rules don't apply to them. Third-party models listed on AWS Marketplace (Bedrock Marketplace models) are governed by the approval flow and do require approval.

## Purchase orders and line items
<a name="procurement-system-scenarios-group-po"></a>

What AWS Marketplace sends on the purchase order, and what you can change about it afterwards.

### Purchase orders
<a name="procurement-system-scenarios-purchase-orders"></a>

A buyer can't supply a purchase order when they request approval from a procurement system, but they can add or correct one after approvals finish. Where the approver is in the AWS console or an email approver, the buyer can supply a purchase order with the request and it is recorded. A purchase order is procurement information rather than a term the approvers agreed to, so changing it doesn't invalidate their decisions or require approval again.

To correct one, open the agreement on the [**Manage subscriptions**](https://console.aws.amazon.com/marketplace/subscriptions?region=us-east-1) page and update the purchase order there.

A purchase order can't be added or corrected on an invoice that has already been issued. Purchase orders apply to future charges rather than past ones. To correct an invoice that has been issued, contact [AWS Support](https://console.aws.amazon.com/support/home).

### UNSPSC codes used by AWS Marketplace
<a name="procurement-integration-setup-unspsc-codes"></a>

AWS Marketplace uses United Nations Standard Products and Services codes (UNSPSC) to classify line items that are sent back to the procurement cart. The code assigned to each line item depends on the line item type.


| Line item type | UNSPSC code | Description | When used | 
| --- | --- | --- | --- | 
| Service (amount-based) | 81162000 | IT Service Delivery | An offer with a single, non-usage charge (for example, a contract upfront charge). Quantity is set to 1 and the unit price equals the full charge amount. Only one invoice can post against the purchase order line. | 
| Material (quantity-based) | 43232701 | Software | Any usage-based charge (for example, pay-as-you-go (PAYG)), or an offer with more than one charge (for example, multiple flexible payment schedule (FPS) installments). Quantity is calculated from the charge amount (the amount divided by 0.01) and the unit price is $0.01. Multiple invoices can post against the purchase order line. | 

#### How line item type is determined
<a name="procurement-integration-unspsc-line-item-type"></a>

AWS Marketplace classifies each line item based on the number of charges it contains. The Service and Material types are described in the table above.

If a buyer splits a purchase into separate line items, each charge gets its own line item. The one exception is pay-as-you-go (PAYG) usage: because usage can't be determined upfront, a PAYG charge is always classified as Material even when it has its own line.

## Approvals already in progress
<a name="procurement-system-scenarios-group-inflight"></a>

What happens to a purchase that has been submitted and is waiting for a decision.

### Changes while a purchase is waiting
<a name="procurement-system-scenarios-mid-flight"></a>

Your rules evaluate a purchase once, when the buyer submits it, and those rules stay with it. Changes you make afterwards apply to new purchases rather than to ones already waiting. That is deliberate, so that a buyer's purchase doesn't change course underneath them.

Some changes do affect a purchase that is already waiting.


| Change | Effect on a purchase already waiting | 
| --- | --- | 
| The seller changes the terms of the offer | The purchase can't complete, even if every approver has agreed to it. The buyer starts again against the new terms. | 
| The offer expires | The approval can still go through, but the agreement won't be created automatically. You receive a notification about this situation. The buyer needs to reach out to the seller to extend the offer expiration, and then can return to AWS Marketplace and accept the agreement from the product page without needing approval again. | 
| The time allowed for approval runs out | The purchase is declined and the buyer starts again. The offer itself is still valid. | 
| You disable the procurement connection | A purchase order returning for that purchase is rejected, because there is no longer an active connection to accept it. | 
| The buyer's account moves to a different organization or organizational unit | The purchase stops making progress. Approvers in the old place can no longer act on it, and approvers in the new place never see it. The buyer should cancel and submit again rather than wait. | 

### Overriding an approval
<a name="procurement-system-scenarios-override"></a>

An approval can get stuck in ways no approver in your procurement system can fix. The only approver at a level might have left the company, or their account might have moved out of your organization. Without a way out, the purchase simply waits until the time allowed for approval runs out.

Your organization's management account can resolve an approval directly in that situation. An override settles one level of one purchase, and you can apply only one override for each level.

An override is recorded with the identity that performed it, so overrides are the first entries to look at when you audit approvals. An override means a purchase completed without the approver you chose for it. For where those records are and how to find them, see [Security for procurement system integration](procurement-system-integration-security.md).

**Note**  
An override doesn't change your rules and doesn't apply to future purchases. If you find yourself overriding the same route repeatedly, the rule needs changing rather than the purchases.