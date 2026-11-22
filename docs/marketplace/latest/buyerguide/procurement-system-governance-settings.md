

# Using procurement system integration with other governance settings

Private Marketplace is the umbrella for the governance you apply to AWS Marketplace purchasing, and the procurement system integration is one control within it. It doesn't replace the other controls, and it doesn't switch them off. A single purchase can be subject to all of them.

Three settings decide whether a purchase goes through. Catalog curation decides which products a buyer can purchase, transaction approvals decide who has to approve the purchase, and mandatory purchase orders decide whether a purchase order is needed before it completes. This topic explains each one, the order they are applied in, and how they work together.

## What each setting decides
<a name="procurement-system-governance-what-each-decides"></a>

The following list describes what each of the three settings decides.

Catalog curation  
Decides which products your buyers can see and purchase. A product you haven't approved doesn't appear in the catalog, so a buyer can't start a purchase for it. Where you allow product requests, a buyer can ask for a product to be added, and you approve it once, for the product, rather than for each purchase of it.  
For more information, see [Managing user requests](manage-user-requests.md) and [Requesting products for procurement](requesting-products-for-procurement.md).

Transaction approvals  
Decides who has to approve a particular purchase, and where that approval comes from. Your approval rules live here, and so do the approvals your procurement system returns: routing a purchase to your procurement system is a transaction approval. For more information, see [Routing purchases to your procurement system](procurement-system-routing.md).

Mandatory purchase orders  
Decides whether a purchase needs a purchase order before it can be completed and invoiced.

## The order the settings are applied
<a name="procurement-system-governance-order"></a>

The settings are applied in a fixed order:

1. **Catalog curation** – can this buyer purchase this product?

1. **Transaction approvals** – who has to approve this purchase?

1. **Mandatory purchase orders** – is a purchase order required before this purchase completes?

Each stage stops a purchase for a different reason, so the stage a purchase has reached tells you where to look. A purchase that can't get past the first stage needs a change to your catalog. One waiting at the second stage is waiting for an approver. One held at the third stage has every approval it needs and is waiting only for a purchase order.

## Using the settings together
<a name="procurement-system-governance-together"></a>

Most organizations use more than one of these settings, and each one decides something the others don't. Follow a purchase through an organization that curates its catalog to a list of approved products, routes purchases above a threshold to its procurement system, and requires a purchase order on every purchase.

A buyer who wants a product that isn't on the list requests it, and you approve the product once, for every buyer the account group covers. Granting that request didn't approve the purchase. The buyer starts one, it matches your approval rule, and it arrives in your procurement system as a requisition.

When the requisition is approved, your procurement system returns a purchase order, and that purchase order satisfies the purchase order requirement for the charges it covers. Where a purchase has charges that weren't sent to your procurement system, those charges still need a purchase order, and the buyer supplies it in AWS Marketplace before the purchase can complete.

Changing one setting doesn't relax another. Removing the approval rule leaves the catalog curation and the purchase order requirement in place, and granting a product request doesn't exempt a purchase of that product from either of the other two settings.

**Important**  
An approval arriving from your procurement system doesn't always mean the purchase is finished. If your buyers report that approved purchases aren't completing, a charge that your procurement system never saw, and that still needs a purchase order, is the first thing to check.

## Where each setting is configured
<a name="procurement-system-governance-where-configured"></a>

These settings don't all live in the same place, which is the most common reason someone concludes a setting doesn't exist.


| Setting | Where you configure it | 
| --- | --- | 
| Catalog curation | AWS Marketplace, on the [**Private Marketplace**](https://console.aws.amazon.com/marketplace/private-marketplace/dashboard?region=us-east-1) dashboard | 
| Transaction approvals | AWS Marketplace, on the [**Procurement approval rules**](https://console.aws.amazon.com/marketplace/buying-policies/procurement-approval-rules?region=us-east-1) page | 
| Mandatory purchase orders | AWS Marketplace, on the [**Buying policies**](https://console.aws.amazon.com/marketplace/buying-policies?region=us-east-1) page | 