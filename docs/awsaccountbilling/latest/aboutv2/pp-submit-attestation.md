

# Submitting an attestation
<a name="pp-submit-attestation"></a>

When you achieve an outcome, you can submit an attestation to request disbursement of your outcome-based investment (also called a credit).

**Note**  
If your Private Pricing contract isn't eligible for self-service attestation, the console displays a message that you must follow the terms of your contract to attest by email. In that case, you can't submit an attestation from the console.

## Prerequisites
<a name="pp-attestation-prereqs"></a>

Before you submit an attestation, ensure the following requirements are met:
+ At least one outcome is selected on the investment detail page. The outcome must have a status of **Available**, or you must acknowledge the window warning for an outcome whose attestation window has expired or has not opened yet.
+ You have the contract document ID from your Private Pricing contract.
+ You have the name, title, and email address of a C-level executive who authorizes you to submit the attestation.

## Submitting an attestation
<a name="pp-attestation-procedure"></a>

Complete the following procedure to submit an attestation.

**To submit an attestation**

1. On the investment detail page, select at least one outcome checkbox for the outcomes that you want to attest to.

1. Choose **Attest ({{count}})**.

1. For each outcome card on the attestation form, enter the attestation quantity. Each card has one input field, which varies by outcome type (as listed in your contract).

1. Review the computed investment amounts, which are read-only.

1. If the contract has multiple investment accounts, adjust the investment distribution percentages. The percentages must sum to 100%. For more information, see [Understanding investment distribution](pp-investment-distribution.md).

1. (Optional) For **Investment disbursement date**, enter the date on which you want the investment disbursed. If you leave this field blank, the investment is disbursed upon validation.

1. In the C-level executive information section, enter the executive's name, title, and email address, confirm the email address, and enter the contract document ID. They receive an automatic click-to-accept email to authorize the attestation.

1. (Optional) Expand **Additional recipients** and enter comma-separated email addresses to copy on the executive approval request email.

1. Select the **I confirm** acknowledgement checkbox to accept the legal-entity attestation statement.

1. Choose **Submit**.

1. In the **Submit attestation** confirmation modal, review the details, and then choose **Submit**.

## Attestation window and maximum warnings
<a name="pp-attestation-warnings"></a>

The attestation form displays warnings in the following situations. These warnings do not block submission.
+ **Expired window** — If the attestation window for one or more selected outcomes has expired, the form warns you that the attestation will be automatically rejected.
+ **Future window** — If the attestation window for one or more selected outcomes has not opened yet, the form warns you that the attestation will be automatically rejected.
+ **Maximum exceeded** — If the attested total exceeds the outcome or investment maximum, the form displays a warning, but you can still submit.

## Submit attestation confirmation
<a name="pp-submit-confirmation"></a>

When you choose **Submit**, the **Submit attestation** confirmation modal explains that submitting the attestation does the following:
+ Initiates an AWS validation process, including your AWS account manager.
+ Sends your C-level executive a click-to-accept email. This email typically arrives within 5 minutes.

 To continue, choose **Submit**.

## Batch submission
<a name="pp-batch-submission"></a>

You can submit attestations for multiple outcomes at the same time. When you select multiple outcomes, the attestation form displays an outcome card for each outcome, each with its own input fields and computed amounts. If some outcomes in a batch fail to submit, the form keeps the failed cards so that you can retry them.

## What happens after submission?
<a name="pp-after-submission"></a>

After you submit an attestation, the following happens:
+ The attestation enters a pending state and appears in the attestation history with a status of **Processing** or **Pending C-level confirmation**.
+ AWS starts a validation process that sends a click-to-accept email to your C-level executive and verifies the attestation inputs and outcome completion.
+ AWS then either disburses the investments into your investment accounts or rejects the attestation.
+ You receive an email notification at your account's billing contact email address for each status change. For more information about managing billing contact email addresses, see [Adding additional billing contact email addresses](manage-payment-method.md#manage-billing-contact-emails). For questions about a rejected attestation, contact your AWS account manager or Support.

For more information about tracking status, see [Tracking attestation status](pp-tracking-status.md).