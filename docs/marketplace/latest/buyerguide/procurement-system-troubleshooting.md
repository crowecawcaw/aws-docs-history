

# Troubleshooting procurement system integration

A problem anywhere along the chain looks the same to a buyer: the purchase didn't go through. The tables in this topic start from what you can see and work back to the cause.

## Single sign-on
<a name="procurement-system-troubleshooting-sso"></a>


| Scenario | Details | 
| --- | --- | 
| Buyers sign in the default AWS way instead of through your identity provider | The session has no usable value for start\_url, so it sends the buyer to the AWS Marketplace home page, where they sign in the default way rather than on your sign-in page. Either the parameter is missing or wasn't saved, or its value wasn't accepted. Both produce exactly the same result, so you can't tell them apart from what the buyer sees. Check that the single sign-on address you supplied is correct. For the requirements and limitations, see [Requirements and limitations](procurement-system-sso.md#procurement-system-sso-requirements). | 
| Your sign-in page loads but authentication fails | The address is wrong, or the buyer isn't provisioned in your identity provider. Open the address directly in a browser to check it, then confirm the buyer is provisioned with the permissions they need. | 
| Buyers are asked to sign in again mid-session | Your identity provider's session is shorter than the punchout session. Review the session duration in your identity provider. For IAM Identity Center, check under Settings, Authentication. | 
| You can't configure or update single sign-on for SAP Ariba | The SAP Ariba punchout endpoint is managed on the AWS supplier account in the Ariba Network, so the parameter can't be self-configured. Contact [AWS Marketplace Support on the AWS website](https://aws.amazon.com/marketplace/help/contact-us) with your sign-in address. | 

## A purchase didn't reach your procurement system
<a name="procurement-system-troubleshooting-not-routed"></a>


| Scenario | Details | 
| --- | --- | 
| The purchase completed without any approval | No rule matched it. Rules describe what needs approval, and anything no rule names completes normally. Check that a rule covers this kind of purchase, and that you assigned the policy holding it to the account the buyer purchased from. For more information, see [Routing purchases to your procurement system](procurement-system-routing.md). | 
| The purchase needs approval, but it went somewhere else | More than one rule can match a purchase, and all matching rules apply. A purchase collects one approval for each distinct place it's sent. Check for a second rule that also matches. | 
| An account's purchases aren't governed by the rules you expect | A policy assigned closer to an account replaces one assigned further away rather than adding to it. If an account or organizational unit has its own policy, the organization's policy doesn't apply to it. Check which policy is assigned nearest to that account. | 
| The buyer says there was no option to request approval | Requesting approval works from the AWS Marketplace website only. A buyer who found the product in the AWS Marketplace console is redirected there automatically. From another service's console, they're given a link to open instead. For more information about where buyers can request approval, see [Where buyers can request approval](procurement-system-supported-scenarios.md#procurement-system-scenarios-where-buyers-request). | 
| AWS Marketplace tells the buyer the request can't be delivered | Enable the connection that covers the purchase, change the rule that requires approval, or have the buyer start a session from a supplier whose connection covers the AWS Billing entity they are purchasing through. A disabled connection doesn't remove the approval requirement, so the purchase still needs approval and still can't be delivered until one of those three is true. | 
| Purchases through one AWS Billing entity arrive, others don't | A connection can be limited to particular AWS Billing entities, also called sellers of record, and a purchase is only sent if a connection covers the billing entity it belongs to. Create a connection for each billing entity you purchase through. For more information about arranging connections, see [Create one connection per seller of record](procurement-system-best-practices.md#procurement-system-best-practices-connections). | 
| Connection details were changed on one side only | The punchout works because the same identifiers and credentials are held in both systems. A Buyer ID, Supplier ID or Shared secret changed in your procurement system but not in your connection, or changed in your connection but not in your procurement system, stops purchases reaching your procurement system. Compare the values your connection holds against the ones in your procurement system and correct whichever side was changed. For the Coupa connection fields, see [Managing your connections](procurement-system-integration-coupa.md#procurement-system-coupa-managing-connections). | 

## An approval doesn't complete
<a name="procurement-system-troubleshooting-approval-stuck"></a>


| Scenario | Details | 
| --- | --- | 
| The offer expired while the purchase was waiting | An offer has its own expiry, and approval time counts against it. If the offer expires, the approval can still go through, but the agreement isn't created automatically, and you receive a notification about it. This is the most common cause of a purchase that was approved but has no agreement. To resolve it:1.  Ask the seller to extend the offer expiry. <br />2.  Have the buyer accept the agreement from the product page in AWS Marketplace. No further approval is needed. <br />3.  If approvals in your organization routinely take a long time, ask for offers with expiry dates that allow for it.  | 
| The seller changed the terms of the offer | The purchase can't complete, even with every approval given, and the buyer starts again against the new terms. | 
| The time allowed for approval ran out | The purchase is declined and the buyer starts again. The offer itself is still valid, so this differs from offer expiry. | 
| Nobody in your procurement system can complete the approval | The requisition is waiting on an approval your workflow can't deliver, because the approver it routes to has left or the role is unfilled. Correct the workflow in your procurement system, or have your management account resolve the approval directly in AWS Marketplace. For more information about overriding an approval, see [Overriding an approval](procurement-system-supported-scenarios.md#procurement-system-scenarios-override). | 
| The purchase is waiting on more than one approval | A purchase collects one approval for each distinct approver your rules send it to, and all of them have to complete before the purchase does. The buyer can check for the others on the [**Approval requests**](https://console.aws.amazon.com/marketplace/private-marketplace/approval-requests?region=us-east-1) page, where a purchase still waiting has a request that isn't yet Approved. | 
| Part of a purchase was approved and part wasn't | In an Offer Set, each component is approved separately and independently, so partial outcomes are possible. | 
| Your procurement system approved the purchase, but the approval isn't recorded | AWS Marketplace matches a returning purchase order against the approved charges, line by line. A line naming a charge the approval doesn't contain can't be settled, so the approval isn't recorded. Added lines, edited charges and removed lines all cause this. | 
| Purchase orders from Coupa are rejected | Mutual TLS is required for Coupa, and AWS Marketplace rejects purchase orders sent without it. For the supplier settings that turn it on, see [Supplier settings](procurement-system-integration-coupa.md#procurement-system-coupa-supplier). | 
| The approval request shows Approved, but no agreement was created | If you require purchase orders and the purchase has charges that weren't sent to your procurement system, those charges still need one, and the buyer supplies it in AWS Marketplace before the purchase completes. An expired offer produces the same symptom, and is covered in the first row of this table. For more information about the other governance settings, see [Using procurement system integration with other governance settings](procurement-system-governance-settings.md). | 

## Purchase orders and invoices
<a name="procurement-system-troubleshooting-po"></a>


| Scenario | Details | 
| --- | --- | 
| A purchase order needs correcting | The buyer can update it themselves, on the agreement's details page from the [**Manage subscriptions**](https://console.aws.amazon.com/marketplace/subscriptions?region=us-east-1) page, because a purchase order is procurement information rather than a term the approvers agreed to. Once an invoice has been issued, it can no longer be corrected there. To correct an issued invoice, contact [AWS Support](https://console.aws.amazon.com/support/home). | 
| Invoices aren't arriving in your procurement system | Electronic invoice delivery is configured separately from the punchout, and setting up the punchout doesn't turn it on. For more information about electronic invoice delivery, see [Setting up electronic invoice delivery](procurement-system-invoicing.md). | 
| Line items map to the wrong category in your procurement system | AWS Marketplace classifies each line item with a UNSPSC code based on the pricing terms of the offer. Check the mapping in your procurement system against the codes AWS Marketplace sends. For more information about UNSPSC codes, see [UNSPSC codes used by AWS Marketplace](procurement-system-supported-scenarios.md#procurement-integration-setup-unspsc-codes). | 

## If none of these apply
<a name="procurement-system-troubleshooting-contact"></a>

If you haven't found a solution to your problem, contact [AWS Marketplace Support on the AWS website](https://aws.amazon.com/marketplace/help/contact-us).