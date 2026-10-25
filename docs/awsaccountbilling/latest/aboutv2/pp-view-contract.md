

# Viewing your Private Pricing contracts
<a name="pp-view-contract"></a>

After you verify access to a contract, its **Access** changes to **Verified** and you can open its details page. You can then view contract details and investment terms (also called credits in the API and SDKs).

## Navigating the contract view
<a name="pp-contract-navigation"></a>

Use the following procedure to open a contract that you can access.

**To view a contract**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Private Pricing**.

1. In the **Your Private Pricing contracts** table, choose the type of a contract whose **Access** is **Verified**.

Contracts whose **Access** is **Not verified** are not clickable. If you select an unverified contract, a popover prompts you to verify access first. For more information, see [Getting started with Private Pricing pages](pp-getting-started.md).

## Overview
<a name="pp-contract-overview"></a>

The **Overview** section displays the following information:
+ *Customer legal name* — Your organization's legal entity name, as is in the contract.
+ *Term* — The contract start and end dates.
+ *Eligible payer accounts* — The payer accounts (called *management accounts* in AWS Organizations) that are eligible in the contract.
+ *Investment accounts* — The accounts designated to receive investment disbursements, such as credits.

## Outcome-based investments
<a name="pp-outcome-based-investments"></a>

Outcome-based investments (also called credits) are awarded after you achieve certain outcomes. You must submit an attestation to trigger investment validation and disbursement. This section appears first on the details page.

The **Outcome-based investments** table displays the following columns:
+ *Investment name* — The investment name, as is in your contract.
+ *Max amount* — The maximum dollar amount you can earn for this investment.
+ *Disbursed* — The total amount already disbursed for this investment.

Choose an investment name to view its outcomes. For more information, see [Viewing outcome-based investment details](pp-investment-details.md).

## Milestone-based investments
<a name="pp-milestone-based-investments"></a>

Milestone-based investments are awarded on a fixed schedule according to the terms set out in your contract. No action is required from you.

The **Milestone-based investments** table displays the following columns:
+ *Investment name* — The name that identifies the investment.
+ *Amount* — The dollar amount of the investment.
+ *Effective date* — The date when the investment is applied to your account.

**Note**  
If your contract has no investment terms, the console displays the message "This contract has no investment terms."