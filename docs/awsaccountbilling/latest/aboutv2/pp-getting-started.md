

# Getting started with Private Pricing pages
<a name="pp-getting-started"></a>

This topic walks you through the prerequisites, how to access Private Pricing pages, and how to verify access to your contract.

## Prerequisites
<a name="pp-prerequisites"></a>

Before you get started with Private Pricing pages, ensure that you meet the following requirements:
+ **Eligible payer account** — You must sign in with a payer account (called a *management account* in AWS Organizations), or a standalone account, that is eligible under the contract. Linked accounts (called *member accounts* in AWS Organizations) cannot access the Private Pricing pages. Sign in with your payer account to view and manage your Private Pricing contracts.
+ **Contract document ID** — You need the contract document ID from your contract, formatted as `CC OTH 00000000 0000 TR`. You can find the contract document ID in the upper right corner of each page in your contract.
+ **IAM permissions** — Your IAM identity must have the following permissions:
  + `billing:AssociateContract`
  + `billing:DisassociateContract`
  + `billing:ListContracts`
  + `billing:GetContractInformation`
  + `billing:ListContractualInvestmentSummaries`
  + `billing:ListContractualInvestments`
  + `billing:CreateContractualInvestmentAttestation`
  + `billing:ListContractualInvestmentAttestations`
  + `billing:CancelContractualInvestmentAttestation`

## Accessing the Private Pricing pages
<a name="pp-accessing"></a>

You access Private Pricing from the AWS Billing and Cost Management console. The Private Pricing landing page is titled **Private Pricing** and described as "Access and manage your organization's contracts." It lists the contracts available to your account.

**To access Private Pricing pages**

1. Sign in to the AWS Management Console with your payer account.

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Private Pricing**.

 The page displays a single table that lists every contract available to your account, whether or not you have verified access to it. The table has the following columns:
+ **Contract type** — The type of contract.
+ **Term** — The start and end dates of the contract.
+ **Access** — Whether your account has verified access to the contract. The value is **Verified** or **Not verified**.

**Note**  
Linked accounts (called a *member account* in AWS Organizations) cannot access the Private Pricing pages. If you sign in with a linked account, sign in with your payer account instead.

If your account has no Private Pricing contracts, a **Join Private Pricing** panel appears instead of the table.

## Verifying access to your contract
<a name="pp-verifying-access"></a>

The first time you access Private Pricing contracts, you see the ones that your account is part of. To access a contract, you must "confirm access" to it first, through a one-time verification. Only one payer account can have access to manage a contract at a time. 

**To verify access to a contract**

1. On the **Private Pricing** landing page, select a contract row whose **Access** is **Not verified**.

1. Choose **Verify access**.

1. For **Contract document ID**, enter the contract document ID.

1. Choose **Verify**.

After you verify access, Private Pricing displays the message "Access verified successfully." and opens the contract's details page. The contract's **Access** value changes to **Verified**. Now your account has exclusive access to it.

**Note**  
If you select a contract whose **Access** is **Not verified** and try to open it, a popover explains that you must verify access first: "Access not verified — You must verify access to this contract before you can view its details or attest to its investments. Select the row and choose Verify access to continue."

## What you can do after verifying access
<a name="pp-after-verifying-access"></a>

After you verify access to a contract, you can perform the following tasks from the **Private Pricing** page:
+ View contract details, including the customer legal name, term, eligible payer accounts, and investment accounts. For more information, see [Viewing your Private Pricing contracts](pp-view-contract.md).
+ View milestone-based and outcome-based investments. For more information, see [Viewing outcome-based investment details](pp-investment-details.md).
+ Submit attestations for outcome-based investments. For more information, see [Submitting an attestation](pp-submit-attestation.md).
+ Track attestation status. For more information, see [Tracking attestation status](pp-tracking-status.md).
+ Remove access to the contract so that another eligible payer account can verify access and manage it. For more information, see [Removing access to a Private Pricing contract](pp-remove-access.md).