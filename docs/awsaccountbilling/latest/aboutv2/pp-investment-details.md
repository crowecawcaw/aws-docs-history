

# Viewing outcome-based investment details
<a name="pp-investment-details"></a>

Outcome-based investments (also called credits) contain outcomes that you attest to earn investment disbursements. The investment detail page lists the individual outcomes in your contract.

## Accessing the investment detail page
<a name="pp-investment-detail-access"></a>

Use the following procedure to access the detail page for an outcome-based investment.

**To access the investment detail page**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Private Pricing**.

1. In the **Your Private Pricing contracts** table, choose the name of a contract whose **Access** is **Verified**.

1. In the **Outcome-based investments** section, choose the investment name.

## Outcomes table
<a name="pp-outcome-table"></a>

The **Outcomes** table lists one row for each outcome. To find an outcome, use the text filter to search by outcome description. The table has the following columns:
+ **Outcome** — The description of the outcome, sourced directly from your contract.
+ **Attestation window start** — The date when you can begin submitting attestations for this outcome.
+ **Attestation window end** — The last date you can submit attestations for this outcome.
+ **Max amount** — The maximum investment amount for this outcome.
+ **Disbursed** — The amount already disbursed for this outcome.
+ **Pending disbursement** — The amount from submitted attestations that is awaiting disbursement for this outcome.
+ **Remaining** — The amount that remains to be disbursed for this outcome, net of the disbursed and pending disbursement amount. The value is `-` when the outcome has no Max amount.
+ **Status** — The current outcome status.

## Understanding outcome statuses
<a name="pp-outcome-statuses"></a>

Each outcome displays one of the following statuses:
+ **Available** — The outcome can be attested to.
+ **Attestation in progress** — An attestation submitted is pending validation, so you cannot submit a new attestation for the outcome yet.
+ **Future** — The attestation window for the outcome has not opened yet.
+ **Unavailable** — The outcome cannot be attested to. The attestation window has closed, or the outcome was attested and the investment was disbursed this month.

## Selecting outcomes for attestation
<a name="pp-selecting-outcomes"></a>

Select one or more outcomes by using the checkboxes in the **Outcomes** table, and then choose **Attest ({{count}})** to begin the attestation process. The **Attest** button shows the number of selected outcomes (for example, **Attest (3)**). The button is enabled only when every selected outcome can be attested to.

For more information about submitting attestations, see [Submitting an attestation](pp-submit-attestation.md).

## Viewing attestation history
<a name="pp-view-attestation-history"></a>

To view the history of attestations for this investment, choose **Attestation history**. For more information, see [Tracking attestation status](pp-tracking-status.md).