

# Tracking attestation status
<a name="pp-tracking-status"></a>

After you submit an attestation, you can track its status on the attestation history page. This page shows all attestations for a Private Pricing contract with their current status.

## Accessing attestation history
<a name="pp-attestation-history-access"></a>

Use the following procedure to view your attestation history.

**To access attestation history**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Private Pricing**.

1. In the **Your Private Pricing contracts** table, choose the name of a contract whose **Access** is **Verified**.

1. In the **Outcome-based investments** section, choose the investment name.

1. Choose **Attestation history**.

## Attestation history table
<a name="pp-attestation-table"></a>

The attestation history table displays the following columns:
+ **Attestation ID** — The unique identifier for the attestation.
+ **Investment name** — The investment associated with the attestation.
+ **Outcome** — The specific outcome description that was attested.
+ **Attested amount** — The investment amount attested to for the attestation.
+ **Attestation date** — The date the attestation was submitted.
+ **Last updated** — The date the status was last changed.
+ **Status** — The current attestation status.
+ **Actions** — The actions available for the attestation, such as cancelling an in-flight attestation.

Use the property filter to filter the table by investment, outcome, status, or attestation ID. To reload the table, choose **Refresh**.

## Understanding attestation statuses
<a name="pp-attestation-statuses"></a>

Each attestation has one of the following statuses:
+ **Pending C-level confirmation** — The attestation is awaiting the C-level executive's click-to-accept email confirmation. If the executive does not confirm within 7 calendar days, AWS rejects the attestation. 
+ **Processing** — The attestation has been submitted, C-level confirmation received and is under AWS review. 
+ **Pending cancellation** — A user in your organization requested a cancellation, and AWS is processing it. For more information, see [Cancelling an attestation](pp-cancel-attestation.md).
+ **Cancelled** — The attestation was cancelled. A cancelled attestation cannot be resubmitted.
+ **Rejected** — The attestation did not pass AWS review. The **Status** cell shows a **Rejection reason** popover with the details.
+ **Disbursed** — The attestation was processed and the investment has been disbursed to the designated investment accounts.

## Viewing the rejection reason
<a name="pp-rejection-reasons"></a>

When an attestation has a status of **Rejected**, choose the **Rejected** status to open the **Rejection reason** popover. The popover lists one or more reasons that explain why AWS rejected the attestation.

An attestation can be rejected for one or more of the following reasons:
+ This contract is not eligible for automated investment disbursement processing. Follow the terms of the contract to submit the attestation via email.
+ Before the investment disbursement can be processed, the contract requires review. You will be contacted by your account team.
+ The attestation submitted is referencing a contract ARN that does not exist or has expired. Please re-try with the correct contract in the required field(s).
+ The investment for the attestation does not exist. Confirm you entered the correct information in the required fields, and re-submit the attestation.
+ The submitted attestation is missing an investment account. Enter the correct investment account in the required field(s), and re-submit the attestation.
+ Based on the terms of your contract, the attested investment amount (including prior disbursed investments) exceeds the contract maximum amount. Enter the correct information in the required fields and re-submit the attestation if appropriate.
+ Based on the terms of your contract, the attested investment amount (including prior disbursed investments) exceeds the contract maximum amount. Review the attestation history for the outcome and re-submit the attestation if appropriate.
+ Based on the terms of your contract, the attested investment amount (including prior disbursed investments) exceeds the contract maximum amount.
+ The attestation window for the investment closed. For help, contact your account team or customer support.
+ The investment for this outcome is already pending or disbursed. Review the attestation history for the outcome, and re-submit the attestation if needed.
+ This investment was already attested, and the investments were disbursed or are pending disbursement.
+ The submitted attestation needs more evidence of outcome completion. Your account team will follow up with you on next steps.
+ Your designated C-level executive did not confirm the attestation within 7 days of the submission date. Submit a new attestation, and ensure a timely C-level confirmation.

## Email notifications
<a name="pp-email-notifications"></a>

AWS sends email notifications to your account's billing contact email address on every attestation status change:
+ Attestation received (**Processing**)
+ Attestation approved and investment disbursed (**Disbursed**)
+ Attestation rejected (**Rejected**)
+ C-level approval requested — sent to the designated C-level approver and any additional recipients for any attestation submitted.

These notifications are automatic. You cannot opt out.