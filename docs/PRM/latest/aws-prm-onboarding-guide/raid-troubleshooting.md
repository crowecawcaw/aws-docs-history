

# Troubleshooting Revenue Attribution IDs
<a name="raid-troubleshooting"></a>

This section describes common issues you might encounter when creating or managing Revenue Attribution IDs, and provides steps to resolve them.

## Revenue Attribution ID not created successfully
<a name="raid-troubleshooting-creation"></a>

If you are unable to create a Revenue Attribution ID:
+ Verify that you have migrated to AWS Partner Central in the AWS Console.
+ Confirm that you have at least one AWS Marketplace product listing.
+ Ensure that you are selecting a product from your own account or a connected subsidiary account.
+ Check that all required fields are completed (Marketplace product, at least one offer or opportunity association, billing month, and cost allocation percentage).

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

## Common implementation errors
<a name="raid-troubleshooting-common-errors"></a>

The following table describes common implementation errors for Revenue Attribution IDs.


| Method | Issue | Cause | Solution | 
| --- | --- | --- | --- | 
| Revenue Attribution ID | Cost allocation rejected | Total exceeds 100% for billing month | Ensure all entries for the same Revenue Attribution ID and billing month sum to 100% or less. | 
| Revenue Attribution ID | Prior month update rejected | Past the 7th of current month | Updates to the prior month's allocation are only accepted until the 7th. | 
| Revenue Attribution ID | Association fails validation | Offer or opportunity doesn't meet requirements | Verify that the offer has a buyer account ID or the opportunity is in Launched stage with a customer AWS Account ID. | 