

# Removing access to a Private Pricing contract
<a name="pp-remove-access"></a>

Your account can lose access to a Private Pricing contract automatically, or you can remove access yourself so that another eligible payer account can manage the contract. You can re-establish access later.

## When an account automatically loses access
<a name="pp-automatic-access-loss"></a>

Your account automatically loses access to a Private Pricing contract in the following situations:
+ Your payer account becomes a linked account (called a *member account* in AWS Organizations) under another payer account. Linked accounts cannot access Private Pricing contract pages. 
+ Your account is no longer an eligible payer account under the Private Pricing contract.

In these situations, you don't need to remove access manually. You can also remove access yourself to hand off management to another eligible payer account, as described in the following sections.

## When to remove access
<a name="pp-when-to-remove"></a>

You might remove access when:
+ You want to transfer management to a different payer account in your organization.
+ A different team with access to another payer account needs to manage the contract going forward.

## Removing access to a contract
<a name="pp-remove-procedure"></a>

**To remove access to a contract**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Private Pricing**.

1. In the **Your Private Pricing contracts** table, select the contract row whose **Access** is **Verified**.

1. Choose **Remove access**.

1. In the **Remove access** confirmation modal, confirm that you want to remove access. The modal states: "Are you sure you want to remove account access to this contract? You can re-establish access later." Choose **Remove**.

After you remove access, Private Pricing displays the message "You removed access to this Private Pricing contract. To manage it again, verify access."

## What happens after you remove access
<a name="pp-after-removal"></a>

After you remove access to the contract, the following changes take effect:
+ The contract is still visible on the Private Pricing page, but its access status changes to **Not verified**.
+ You can no longer perform any billing actions related to the contract, and account access to the contract is removed.
+ The contract becomes available for an eligible payer account to verify access.
+ If no other account verifies access, you can verify access again at any time. For more information, see [Getting started with Private Pricing pages](pp-getting-started.md).