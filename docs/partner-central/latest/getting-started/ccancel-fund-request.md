

# Canceling a fund request
<a name="ccancel-fund-request"></a>

## Canceling from the AWS Partner Central in AWS Console
<a name="w2aac35c15b3"></a>

Use the Cancel function when you need to cancel a Fund Request that will no longer be executed. After the Fund Request is canceled, the status changes from "Active" to "Canceled", but the stage does not change. The Fund Request continues to be visible in the funding dashboard. You can cancel a Fund Request at any point before it reaches the Completed Stage, including after it reaches the cash claim stage. After you cancel, any unclaimed funding amount automatically returns to your wallet.

**Important**  
By canceling, you can no longer edit or resubmit the Fund Request.

You can cancel a Fund Request in either of the following ways:

1. Choose the Fund Request ID from the funding dashboard, and then choose **Cancel fund request**.

1. Open the Fund Request detail page and choose **Cancel fund request**.

## Cancellation rules for API users
<a name="w2aac35c15b5"></a>

If you are using the `CancelBenefitApplication` API operation, the following rules apply:

### Funding Benefit Applications (Fund Requests)
<a name="w2aac35c15b5b5"></a>
+ Fund requests can be canceled before approval (`PENDING_SUBMISSION`, `IN_REVIEW`, `ACTION_REQUIRED`).
+ Fund requests can be canceled after approval (`APPROVED`, Cash fulfillment type only).
+ Post-approval cancellation triggers the following actions:
  + The system cancels associated claims that have not yet reached Invoice stage.
  + The system releases Purchase Order (PO) allocations.
  + The system releases SCA wallet funds back to your available balance.

### Claim Benefit Applications (Cash Claims)
<a name="w2aac35c15b5b7"></a>
+ Claims can be canceled before approval (`PENDING_SUBMISSION`, `IN_REVIEW`, `ACTION_REQUIRED`).
+ Claims cannot be canceled after approval.
+ After a claim is approved, it moves to Invoice stage and enters the payment process.

**Important**  
To withdraw from an approved fund request, cancel the funding benefit application (the fund request itself). This action automatically cancels eligible claims. Claims already at Invoice stage or beyond are not affected and continue through the payment process.