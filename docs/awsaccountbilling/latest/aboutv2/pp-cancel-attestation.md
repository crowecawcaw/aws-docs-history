

# Cancelling an attestation
<a name="pp-cancel-attestation"></a>

You can cancel an in-flight attestation before its investment (also called a credit in the API and SDKs) is disbursed. Cancelling voids the attestation and its associated contract action.

**Important**  
Cancelled attestations cannot be resubmitted. To attest the outcome again, you must create a new attestation. For more information, see [Submitting an attestation](pp-submit-attestation.md).

## Which attestations you can cancel
<a name="pp-cancel-eligible"></a>

You can cancel an attestation only while it is still pending a decision. The console shows a **Cancel** action in the **Actions** column for these attestations.

After a cancellation is already in progress (**Pending cancellation**), or after an attestation reaches a terminal status (**Rejected**, **Cancelled**, or **Disbursed**), it can no longer be cancelled.

## Cancelling an attestation
<a name="pp-cancel-procedure"></a>

Use the following procedure to cancel an in-flight attestation from the attestation history page.

**To cancel an attestation**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Private Pricing**.

1. In the **Your Private Pricing contracts** table, choose the name of a contract whose **Access** is **Verified**, choose an outcome-based investment, and then choose **Attestation history**.

1. Find the attestation that you want to cancel, and then choose **Cancel** in the **Actions** column.

1. For the cancellation reason, enter 1–80 characters. A reason is required.

1. In the **Cancel attestation** modal, choose **Cancel attestation** to confirm. To dismiss the modal without cancelling, choose **Go back**.

**Note**  
The modal warns you that "Cancelled attestations cannot be resubmitted. You will need to create a new attestation."

## What happens after you cancel
<a name="pp-cancel-after"></a>

After you cancel an attestation, the following changes take effect:
+ The attestation moves to **Pending cancellation** while the cancellation is processed, and then to **Cancelled**.
+ No investment is disbursed for the cancelled attestation.
+ The cancelled attestation cannot be resubmitted. To attest the outcome again, create a new attestation.

For more information about tracking attestation status, see [Tracking attestation status](pp-tracking-status.md).