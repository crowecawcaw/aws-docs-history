

# Configuring buyer approvals

With buyer approvals, administrators can require approval before a purchase in AWS Marketplace is completed. You create procurement approval rules that decide which purchases need review and where each request is sent. When a buyer submits a purchase that matches a rule, AWS Marketplace sends an approval request to the rule's approvers. After every required approval is granted, AWS Marketplace creates the agreement. Purchases that don't match any rule are approved automatically.

The people who approve software purchases, such as finance controllers, procurement officers, and legal reviewers, often don't have access to an AWS account. Email approvers review and approve purchases through a secure link and a one-time passcode, without signing in to the AWS Management Console.

## How procurement approval rules work
<a name="buyer-approvals-concepts"></a>

Procurement approval rules work with the following building blocks. You configure them in the AWS Marketplace console under **Buying policies**.

Procurement approval rule  
Defines *which* purchases a rule applies to and what happens when a purchase matches. Each rule has approval criteria, such as purchase amount, pricing type, delivery method, offer type, or publisher. A purchase must match all of the rule's criteria for the rule to apply. Purchase amount criteria apply to one currency only. For example, a rule with amounts in USD doesn't match purchases in EUR or GBP, so create a separate rule for each currency. Each rule has one of the following actions:  
+ **Require approval** – Send the purchase to approvers for approval before the agreement is created.
+ **Decline purchase** – Block the purchase. Buyers can't complete the transaction.

Approval routing  
Defines *where* a **Require approval** rule sends its requests. Each rule uses exactly one of the following routings:  
+ **AWS Marketplace console** – Your AWS management account or delegated administrator reviews the request in the AWS Marketplace console. Buyers see this routing as **Organization administrator**.
+ **Email approval chain** – The request goes to the email approvers in an approval chain. Email approvers don't need an AWS account.
+ **External system** – The request goes to your organization's procurement system, such as Coupa or SAP Ariba. Buyers see the name of the system, for example **Coupa**. Your organization can connect one procurement system, and you can't remove it after you connect it. For more information, see [Integrating AWS Marketplace with procurement systems](procurement-system-integration.md).

Email approvers  
People who receive approval requests by email and act on them through a secure link. Each email approver must verify their email address before you can add them to an approval chain.

Approval chain  
A reusable, ordered group of verified email approvers, organized into one or more approval levels. You can assign the same approval chain to multiple rules. You can't delete an approval chain after you create it.

**Approval levels**  
An approval chain can have up to 6 approval levels, with up to 10 approvers at each level. In an email approval chain, each level reviews the request in order. The next level gets the request only after the current level approves it. If a level has more than one approver, only one of them needs to approve. The other approvers serve as backups.

Level 1 reviews every purchase that reaches the chain. For level 2 and later, you can optionally set a spend amount where the level starts reviewing, so that larger purchases escalate to more approvers. A level without an amount reviews after the previous level is complete. Spend amounts are saved on the chain, so every rule that uses the chain reviews purchases at the same amounts.

**When a purchase matches more than one rule**  
A purchase is checked against every rule that applies to the buyer's account. For more information, see [Where approval rules apply](#buyer-approvals-scope). Each **Require approval** rule that a purchase matches creates an approval request, sent to that rule's approval routing. If more than one matching rule uses the same approval routing, such as the same approval chain, the AWS Marketplace console, or your external system, only one approval request is created for that routing. Every required approval must be granted before the agreement is created. Reviews happen at the same time. If any approval request is declined, the purchase can't proceed, even if the other approval requests are approved. If the buyer cancels the purchase request, all of its approval requests are cancelled. If a purchase matches both a **Require approval** rule and a **Decline purchase** rule, the decline rule takes priority, and no approval requests are created.

**Rule limit**  
Your organization can have up to 10 rules in total. The limit includes require approval rules, decline purchase rules, and rules created in Private Marketplace experiences.

**Example: Rules for different kinds of purchases**  
You can create different rules for different kinds of purchases, matching the approval routing to the size and risk of each purchase. For example, an organization might set up the following rules. The amounts are illustrations, not recommendations.
+ Route all usage-based (pay-as-you-go) purchases to the **AWS Marketplace console**, where your organization administrator reviews them. Usage-based charges aren't known at the time of purchase, so this rule uses the pricing type instead of a purchase amount.
+ Route software as a service (SaaS) purchases from USD $10,000 to USD $100,000 to an email approval chain. A procurement manager reviews at level 1, and a finance director joins at level 2 for purchases of USD $50,000 and above. Approvers verify their identity with a one-time passcode and approve in their browser.
+ Route purchases of USD $100,000 and above to Coupa for financial approval and purchase order creation in your organization's system of record.

## Where approval rules apply
<a name="buyer-approvals-scope"></a>

Rules that you create on the **Procurement approval rules** page apply to purchases from all accounts in your organization, unless an account or its OU gets approval rules from a Private Marketplace experience. If your organization doesn't already have a Private Marketplace experience, AWS Marketplace creates one for you in the background when you configure buyer approvals.

To apply different rules to different parts of your organization, create rules from a Private Marketplace experience. Open the experience, choose the **Approval rules** tab, and then choose **Create approval rule** or **Create decline rule**. A rule created in an experience applies only to purchases from the AWS account groups (organizational units or accounts from AWS Organizations) associated with that experience. Approval rules from the most specific level apply. AWS Marketplace checks the account first, then its OU, and then the organization, and uses the approval rules from the first level that has them. If neither the account nor its OU has approval rules, the organization-wide rules apply. An account can be associated with only one experience at a time. Approval rules and product availability are inherited separately, so an account can get its approval rules from one experience and its product availability from another. If the experience has no AWS account groups, its rules don't apply to any purchases until you associate AWS account groups with it.

For example, you could configure the following:
+ A two-level email approval chain for purchases from your finance department's OU
+ A single-level email approval chain for purchases from your engineering OU
+ Organization-wide rules for every other OU, because those OUs have no approval rules of their own

For more information about experiences, see [Private Marketplace](private-marketplace-current.md).

For how buyer approvals work in less common scenarios, such as annual purchases, offer sets, and accounts that move to another organization, see [Special cases for buyer approvals](buyer-approvals-special-cases.md).

## Availability
<a name="buyer-approvals-availability"></a>

Buyer approvals are available in all AWS Marketplace commercial Regions.