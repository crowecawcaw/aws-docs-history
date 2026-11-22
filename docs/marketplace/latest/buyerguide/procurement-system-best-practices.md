

# Best practices for procurement system integration

With this integration, you have several ways to arrange the same governance. These are the arrangements that work well in practice, and the reasoning behind each one, so that you can tell whether it applies to you.

## Create one connection per seller of record
<a name="procurement-system-best-practices-connections"></a>

A connection can be limited to particular AWS Billing entities, also called sellers of record. If your organization purchases through more than one, create a separate connection for each and limit it to the matching billing entity.

The reason is invoicing. Each seller of record invoices separately, and in your procurement system each one usually has its own supplier record, with its own cost centers, approval chains and budgets. A connection per seller of record keeps each requisition and purchase order with the supplier record it belongs to, so your finance team can reconcile an invoice against the purchase order that authorized it.

**Note**  
A connection that names no billing entities accepts purchases from all of them. That is convenient when you have only one, and a blunt instrument when you have several.

## Send only large purchases to your procurement system
<a name="procurement-system-best-practices-thresholds"></a>

Routing every purchase to your procurement system is rarely what you want. A punchout requisition for a small subscription costs your buyers and your approvers the same effort as one for a large contract.

A more usable arrangement is to send purchases above a value you choose to your procurement system, and handle the rest more lightly: an email approval, an approval in the AWS console, or no approval at all. Your procurement system then carries the purchases where its workflow, its records and its purchase orders are worth the effort.

For how to write a rule on total contract value, see [Routing purchases to your procurement system](procurement-system-routing.md).

## Decide deliberately what to do about usage-based purchases
<a name="procurement-system-best-practices-payg"></a>

Usage-based purchases don't have a value you can approve in advance, because the charge depends on what the buyer goes on to use. Sending them through a full approval gives your approvers a decision they can't really make.

Two arrangements work better than that:
+ **Have an administrator approve in the AWS console.** Someone in your organization sees the purchase and the estimate, and decides quickly, without a requisition going through your procurement system.
+ **No approval at all.** Write no rule that matches them, and control the risk somewhere more suitable: with Private Marketplace to limit which products can be used, and with purchase orders so that the spending is attributed on your invoice.

Choose between them according to your organization's policy for usage-based spending. What to avoid is requiring a procurement system approval for a usage-based purchase, because the figure your approvers agree to then bears no relation to the invoice that follows.

## Govern at the organization level, and make exceptions deliberately
<a name="procurement-system-best-practices-org-level"></a>

Assign your policy as high in your organization as the rules make sense, rather than account by account. A policy assigned to an organizational unit covers accounts added to it later, so new accounts are governed from the day they appear rather than from the day somebody remembers them.

**Important**  
A policy assigned closer to an account replaces one assigned further away rather than adding to it. So an exception for one account is a whole policy for that account, not a change to the organization's rules. Write the exception policy with that in mind, because anything you leave out of it no longer applies to that account.

For how account groups and the governance hierarchy work, see [Governance hierarchy](private-marketplace-concepts.md#governance-hierarchy).

## Require purchase orders as a second safeguard
<a name="procurement-system-best-practices-mpo"></a>

Approval rules decide who agrees to a purchase. Requiring a purchase order decides whether a purchase can be completed and invoiced without one. The two catch different mistakes, and using both means a purchase that slips past one is still caught by the other.

Requiring purchase orders is also what makes your invoices reconcilable, because every charge arrives attributed to something your finance team recognizes.

Be aware of one interaction before you turn it on. If a purchase has charges that weren't sent to your procurement system, those charges still need a purchase order and your buyer has to supply it after the approval comes back. For more information about the other governance settings, see [Using procurement system integration with other governance settings](procurement-system-governance-settings.md).

## Set a blanket purchase order for purchases that arrive without one
<a name="procurement-system-best-practices-blanket-po"></a>

If you want every charge attributed to a purchase order without obliging your buyers to supply one, set a blanket purchase order on the [**Purchase orders**](https://console.aws.amazon.com/costmanagement/home?region=us-east-1#/purchaseorders) page of the AWS Billing and Cost Management console. A blanket purchase order applies to AWS Marketplace transactions where no purchase order was provided, so those charges still arrive on your invoice attributed to something your finance team recognizes.

It also reaches spending your approval rules can't. Usage of Anthropic and OpenAI models through Amazon Bedrock isn't governed by approval rules or by a purchase order requirement, and you can set a blanket purchase order for those models specifically.

**Note**  
A blanket purchase order doesn't satisfy a purchase order requirement. Where you require purchase orders, your buyers still have to supply one explicitly for the purchases that requirement covers.

## Name every kind of purchase you want governed
<a name="procurement-system-best-practices-coverage"></a>

Anything your rules don't cover is approved automatically. That is the right default, because it means governance is something you add deliberately rather than something you have to remember to switch off. It also means a gap in your rules is silent: nothing warns you that a kind of purchase is completing without review.

So when you write a set of rules, work through the kinds of purchase your organization actually makes and confirm that at least one rule names each of the ones you want governed. Delivery method and pricing type are the two conditions worth checking against, because between them they describe most of what your buyers will buy.

Check the other direction too. Where rules send purchases to different approvers, confirm that they don't overlap unless you intend a purchase to need every one of those approvals, because each distinct approver adds one more decision the buyer waits for.

For the conditions you can match on, see [Routing purchases to your procurement system](procurement-system-routing.md).

## Review your rules when your organization changes
<a name="procurement-system-best-practices-review"></a>

Rules are written against the organization you had when you wrote them. Two changes are worth a review: new accounts or organizational units that your policies don't yet cover, and approvers who have changed role or left.

An approver who is no longer there doesn't cause an error. The purchase simply waits, until someone notices or the time allowed for approval runs out. For what to do about one that is already stuck, see [Overriding an approval](procurement-system-supported-scenarios.md#procurement-system-scenarios-override).