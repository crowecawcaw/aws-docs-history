

# Routing purchases to your procurement system

When you connect a procurement system to AWS Marketplace, you can have purchases approved there. On its own, a connection doesn't initiate an approval. You decide which purchases go to your procurement system by writing approval rules, on the [**Procurement approval rules**](https://console.aws.amazon.com/marketplace/buying-policies/procurement-approval-rules?region=us-east-1) page in the AWS Marketplace console.

This topic explains how approval rules work, and ends with an example that sends different kinds of purchase approvals to different places.

## Approval concepts
<a name="procurement-system-routing-concepts"></a>

Six things work together to route a purchase. You will meet them in this order, from the widest container down to the person or system that decides.

Experience  
The container for the governance features AWS Marketplace offers you, including mandatory purchase orders, product policies, and approval policies.

Audience  
Defines which accounts an experience applies to. An audience can name individual AWS accounts, organizational units, or your entire organization. The console calls this an AWS account group.

Policy  
A container for your approval rules, held within an experience.

Rule  
A set of conditions, and what happens to a purchase that matches them. A rule is where you say that purchases like this need approval, or that they should be disapproved automatically.

Workflow  
Defines the sequence a purchase follows to reach a decision: an ordered set of levels, where each level has an approver.  
When the decision belongs to your procurement tool, the sequence and approval flow is the one you already maintain in that tool.

Approver  
There are three ways to route your AWS Marketplace purchase approval requests.  
+ **External system (procurement tool)** – the purchase approval request arrives in your procurement tool as a purchase requisition, and your own approval workflow inside that tool decides whether it goes ahead.
+ **An approver by email** – a named email address receives the request. The person approving doesn't need an AWS account.
+ **An approver in the AWS console** – your management account, or an account you have made a delegated administrator, receives the request and can approve it in AWS Marketplace.

For more information about these entities and how they fit together, see [Private Marketplace concepts](private-marketplace-concepts.md).

## Connecting your procurement system
<a name="procurement-system-routing-connecting"></a>

Before a rule can send purchases to your procurement system, the system has to be connected to AWS Marketplace. You set that connection up on the [**External system**](https://console.aws.amazon.com/marketplace/buying-policies/approvers-and-routing?region=us-east-1&tab=external-system) tab of the **Approvers and routing** page in the AWS Marketplace console.

 A connection holds the credentials and settings for one procurement system, and can be limited to particular AWS Billing entities (Seller of Record). A connection that names no billing entities accepts purchases from all of them.

If your organization purchases through more than one AWS Billing entity, and those arrangements use different credentials in your procurement system, create a connection for each and limit it to the matching billing entities. Your procurement system receives a purchase only if a connection covers the billing entity it belongs to.

For more information about the fields and the steps, see [Configuring AWS Marketplace to integrate with Coupa](procurement-system-integration-coupa.md) or [Configuring AWS Marketplace to integrate with SAP Ariba](procurement-system-integration-ariba.md).

## Workflows and approvers
<a name="procurement-system-routing-workflows"></a>

When you connect a procurement tool, AWS Marketplace creates the approver and a single-level workflow for it. You don't build either one yourself.

AWS Marketplace creates that workflow with a single level on purpose. Your approval sequence already exists in your procurement tool, with its own levels, approvers and thresholds. The single level hands the purchase over; your tool decides.

## How rules are evaluated
<a name="procurement-system-routing-combining"></a>

Rules describe what needs approval. By default, anything your rules don't cover is approved automatically and completes normally, so you build up governance by naming the cases you care about rather than by opening up the cases you don't. A rule can also reject a purchase outright instead of sending it for approval.

When a buyer submits a purchase, the rules in the governing policy are evaluated like this:
+ Within a single rule, every condition has to be true for the rule to match. The conditions are combined with AND.
+ Between rules, any rule that matches applies. The rules are combined with OR, so a purchase can match several of them at once.

When several matching rules point at the same approval chain, the purchase collects one approval, not one for each rule. The chain isn't duplicated.

When matching rules point at *different* approval chains, each chain produces its own approval and the purchase needs all of them. Those approvals run in parallel rather than one after another, so a purchase can be waiting on your procurement tool and on an email approver at the same time.

## What you can match on
<a name="procurement-system-routing-conditions"></a>

A condition compares one characteristic of the purchase against values you choose. The following table gives examples of the conditions you can match on. It isn't the complete set, and more conditions are added over time.


| Condition | What it matches | 
| --- | --- | 
| Total contract value | The total value of the agreement the buyer is creating, in the currency the purchase is priced in. | 
| Delivery method | How the product is delivered: software as a service (SaaS), Amazon Machine Image (AMI), container, professional services, or machine learning. | 
| Pricing type | The kind of charges on the offer: monthly recurring, usage-based (pay-as-you-go), contract pricing with a flexible payment schedule, contract pricing with an upfront payment, variable payments, free trial, or bring your own license (BYOL). | 
| Offer type | Whether the buyer is purchasing from a public listing or from a private offer. | 
| Publisher | The seller of the product. | 

## Example rules
<a name="procurement-system-routing-examples"></a>

Single-purpose rules are often all you need. Each of these is one rule with one or two conditions:
+ Require approval for every private offer, by matching on offer type.
+ Send every container purchase to an approver by email, by matching on delivery method.
+ Send large SaaS contracts to your procurement tool, by matching on delivery method, pricing type, and total contract value together.

And more complex rules let you handle different kinds of purchase differently. Suppose you want three things:
+ SaaS contracts over a threshold go to your procurement tool.
+ AMI and container contracts are approved in the AWS console, whatever they cost.
+ Everything else goes to an approver by email.


| Rule | Conditions | Approval comes from | 
| --- | --- | --- | 
| 1 | Delivery method is SaaS, pricing type is a contract, and total contract value is at or above your threshold | Your procurement tool | 
| 2 | Delivery method is SaaS, pricing type is a contract, and total contract value is below your threshold | An approver by email | 
| 3 | Delivery method is AMI or container, and pricing type is a contract | An approver in the AWS console | 
| 4 | Delivery method is professional services or machine learning | An approver by email | 
| 5 | Pricing type is usage-based | An approver by email | 

Two things in this example are worth noticing.

Rules 2, 4 and 5 all send purchases to the same email approver, so it doesn't matter that the rules overlap. A purchase matching two of them still collects one approval. Rules that send to *different* approvers are the ones to keep apart, because a purchase matching both waits for both.

There is no rule that means "everything else". Because rules describe what needs approval, you express "everything else" by naming the remaining cases, which is what rules 4 and 5 do in this example. Anything you don't name needs no approval and completes normally.

## Policies and the accounts they apply to
<a name="procurement-system-routing-policies"></a>

The accounts a policy governs are its audience: individual AWS accounts, organizational units, or your entire organization.

**Important**  
A single purchase is governed by one policy, the one whose audience sits closest to the account the buyer is purchasing from. Policies don't combine. A closer policy **replaces** a wider one, so any rule you leave out of the closer policy stops applying to those accounts.

That matters most when you are testing something out, because a policy assigned to a single test account takes the place of the policy that account would otherwise follow. As an example, you can create one policy and associate it with your entire organization, and another policy and associate it with one account you intend to use for testing. For a safe way to test, see [Testing your procurement system integration](procurement-system-testing.md).

## Where to go next
<a name="procurement-system-routing-checklist"></a>

These topics are worth reading before you settle on a set of rules:
+ For the arrangements that work well in practice, and the reasoning behind each one, see [Best practices for procurement system integration](procurement-system-best-practices.md).
+ For what your buyers experience after a rule sends their purchase to your procurement system, see [Understanding what your buyers see](procurement-system-buyer-journey.md).
+ For the boundaries of the integration, including the kinds of purchase that behave differently, see [Supported and unsupported procurement system scenarios](procurement-system-supported-scenarios.md).

Approval rules are one of three governance settings, and a purchase is evaluated against all three. For how they work together, see [Using procurement system integration with other governance settings](procurement-system-governance-settings.md).