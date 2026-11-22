

# Setting up electronic invoice delivery

Purchases and invoices travel in opposite directions, and they're configured separately.

The punchout carries purchases: your buyers reach the AWS Marketplace catalog from your procurement system, and a purchase order comes back. Electronic invoice delivery carries the result: AWS sends the resulting invoices to your procurement system, instead of leaving your team to enter them by hand.

Most organizations want both, because together they close the loop. A purchase that began as a requisition in your procurement system ends as an invoice in the same place, matched to the purchase order that authorized it.

## Where you configure it
<a name="procurement-system-invoicing-where"></a>

AWS Billing and Cost Management issues your invoices rather than AWS Marketplace, so you set up their delivery in the AWS Billing and Cost Management console, on the **Billing preferences** page, by adding the delivery details to the connection or preference you already created.

For the setup steps, see [Procurement portal preferences](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-pref.html#procurement-portal) in the *AWS Billing and Cost Management User Guide*.

**Note**  
You can add a new AWS Marketplace punchout together with its invoicing configuration in the AWS Billing and Cost Management console, without moving between pages. This works only when you already have an external system connected in AWS Marketplace.

## How invoices match your purchase order lines
<a name="procurement-system-invoicing-line-items"></a>

What arrives in your procurement system is an invoice your team has to reconcile against the requisition that authorized it. The matching is done for you, and it happens line by line.

When your approvers complete the approval, your procurement system returns a purchase order whose lines correspond to the charges AWS Marketplace sent for approval. AWS Marketplace records, for each charge, both the purchase order number and the line of that purchase order the charge belongs to. The invoices for that charge carry the same reference, which is what lets your procurement system post an invoice against the right line rather than against the purchase order as a whole.

So the shape of the purchase order decides the shape of the reconciliation.

Your buyer chooses that shape when they submit the purchase for approval, by deciding whether the purchase goes out as a single line item or is split into one line item for each charge. For more information about splitting a purchase into separate line items, see [How line item type is determined](procurement-system-supported-scenarios.md#procurement-integration-unspsc-line-item-type).

One line item for the whole purchase  
The charges are consolidated into a single line. Every invoice for the purchase posts against that one line, so your procurement system shows one commitment and the invoices that have landed against it.  
This keeps the requisition simple. It also means a purchase that mixes a contract charge with usage charges doesn't separate them, so your records don't distinguish the two on the purchase order.

A separate line item for each charge  
Each charge gets its own line, and the invoices for a charge post against that charge's line.  
This is what you want when a purchase carries charges your finance team treats differently. A contract charge and the usage charges that accompany it land on separate lines, each with its own invoices, so the committed amount and the consumption are attributed separately without anyone splitting them by hand afterwards.