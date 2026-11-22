

# Troubleshooting Revenue Attribution IDs

This section describes common issues you might encounter when creating or managing Revenue Attribution IDs, and provides steps to resolve them.

## Revenue Attribution ID not created successfully
<a name="raid-troubleshooting-creation"></a>

If you are unable to create a Revenue Attribution ID:
+ Verify that you have migrated to AWS Partner Central in the AWS Console.
+ Confirm that you have at least one AWS Marketplace product listing.
+ Ensure that you are selecting a product from your own account or a connected subsidiary account.
+ Check that all required fields are completed: at least one offer or opportunity association, billing month, and cost allocation percentage. A Marketplace product is required unless the Revenue Attribution ID covers products that share the same underlying AWS resources.

## Cost allocation percentage entry rejected
<a name="raid-troubleshooting-cost-allocation"></a>

If your cost allocation percentage entry is rejected:
+ Verify that the total cost allocation percentage across all entries for the same Revenue Attribution ID and billing month does not exceed 100%.
+ Confirm that each entry specifies a billing month and either an Offer ID or Opportunity ID.
+ Check that each (Offer ID or Opportunity ID, Billing Month) combination is unique. Duplicate monthly entries for the same association are not allowed.
+ Ensure that cost allocation percentages are between 0% and 100%.

## Unable to update a prior month's cost allocation
<a name="raid-troubleshooting-prior-month"></a>

If you cannot update a cost allocation entry for a prior billing month:
+ Updates to the prior billing month's cost allocation are only accepted until the 7th of the current month.
+ After the 7th, attribution for the prior billing month can no longer be modified.
+ Historical attribution for prior months is not retroactively recalculated.
+ To correct an error after the deadline, contact your AWS partner management team or APN Support (AWS Partner Central login required).

## Offer or opportunity association failing validation
<a name="raid-troubleshooting-association"></a>

If your offer or opportunity association fails:
+ For AWS Marketplace Offer associations, verify that the offer has a valid buyer account ID.
+ For ACE opportunity associations, confirm that the opportunity is in Launched stage with a customer AWS Account ID specified.
+ Verify that the Offer ID or Opportunity ID exists in AWS systems and belongs to your partner account.
+ If an AWS Marketplace Offer is already linked to an ACE opportunity, you only need to provide the Offer ID.

## Troubleshooting Marketplace Revenue Share
<a name="raid-troubleshooting-mrs"></a>

**No attributed revenue appears for an offer**

Confirm that:
+ The product has product-level AWS Revenue Measurement implemented (for example, Resource Tagging, User Agent String, AWS Marketplace Metering, Account Tagging for SaaS products, or Identity Tagging).
+ The product is generating revenue and has active offers.
+ The product is a SaaS listing, including a limited listing or a product in a seller account with an active Subsidiary Account Connection.
+ A Marketplace revenue share allocation is in effect for that month.
+ The offer was active that month.

Results appear in the deal-level table on the 17th of the following month.

**A product shows Action required**

No allocation is in effect for the current month or a future month. This includes when your last allocation's end month has passed. Open the product, choose Edit, add an allocation, and save.

**Calculated offer amounts look wrong**

Confirm that the offers belong to the product. To correct a specific offer, add it to the product's Revenue Attribution ID with a cost allocation percentage. You don't need to change offers that are already correct.

**You can't edit an allocation**

You can edit allocations on the Active allocations tab. After a month is processed on the 8th of the following month, its allocation moves to the Processed allocations tab and can't be changed. Make corrections in the current or a future month.

**A subsidiary product is missing or not attributed**

Confirm that the Subsidiary Account Connection is active. If the connection changed during the month, that product's revenue isn't attributed for that month. Re-establish the connection and add the product ID again if needed.

## Common implementation errors
<a name="raid-troubleshooting-common-errors"></a>

The following table describes common implementation errors for Revenue Attribution IDs.


| Method | Issue | Cause | Solution | 
| --- | --- | --- | --- | 
| Revenue Attribution ID | Cost allocation rejected | Total exceeds 100% for billing month | Ensure all entries for the same Revenue Attribution ID and billing month sum to 100% or less. | 
| Revenue Attribution ID | Prior month update rejected | Past the 7th of current month | Updates to the prior month's allocation are only accepted until the 7th. | 
| Revenue Attribution ID | Association fails validation | Offer or opportunity doesn't meet requirements | Verify that the offer has a buyer account ID or the opportunity is in Launched stage with a customer AWS Account ID. | 