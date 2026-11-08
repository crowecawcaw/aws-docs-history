

# Managing Connected accounts
<a name="manage-connected-accounts"></a>

A connected account links an external payment provider account to your AWS account so that payments can be settled to that account. You can create a connected account to receive payments from AI bots and agents through [AWS WAF AI traffic monetization](https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-traffic-monetization.html).

For this use case, connect a Stripe account that is registered to a company or other organization. These Stripe accounts are eligible to receive these payments.

**Note**  
To create or manage a connected account, ask your IAM administrator for the base permissions described in this topic.

## Preparing to create a connected account
<a name="connected-accounts-preparing"></a>

Before you create a connected account, make sure that you have:
+ A Stripe account registered to a company or other organization.
+ Access to the Stripe account that you want to connect.
+ Permission to create and manage connected accounts in the AWS account.

You need AWS Identity and Access Management (IAM) access to the AWS Billing and Cost Management console. The AWS account root user must activate IAM access first. For instructions on activating IAM access, see [Activating IAM access to the AWS Billing and Cost Management console](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-getting-started.html#activating-iam-access-to-billing-console).

AWS redirects you to Stripe to authorize the connection. We don't receive or store your Stripe credentials. You manage your bank account details in the Stripe Dashboard.

## Granting permissions to manage connected accounts
<a name="connected-accounts-granting-permissions"></a>

Your IAM administrator grants the role or user base permissions to create and manage connected accounts.

In the following policy, replace {{111122223333}} with your AWS account ID. The `payments:CreateConnectedAccount` and `payments:ListConnectedAccounts` actions don't support resource-level permissions. The wildcard resource is required for those actions. The policy scopes the `payments:GetConnectedAccount` and `payments:DeleteConnectedAccount` actions to connected accounts in your AWS account.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "payments:CreateConnectedAccount",
        "payments:ListConnectedAccounts"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "payments:GetConnectedAccount",
        "payments:DeleteConnectedAccount"
      ],
      "Resource": "arn:aws:payments::{{111122223333}}:connectedaccount/*"
    }
  ]
}
```

The policy includes the following elements:
+ `payments:CreateConnectedAccount` creates a connected account, and `payments:ListConnectedAccounts` lists connected accounts.
+ `payments:GetConnectedAccount` retrieves connected account details, and `payments:DeleteConnectedAccount` deletes a connected account.
+ The connected account ARN uses the format `arn:aws:payments::{{account-id}}:connectedaccount/*`.

To add user-defined tags during account creation, your IAM administrator must also grant `payments:TagResource` permission with conditions that allow only the tag keys and values your organization uses.

For more information about granting Billing permissions, see [Identity-based policy with AWS Billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html).

## Creating a connected account
<a name="connected-accounts-creating"></a><a name="connected-accounts-starting-connection"></a>

**To start a connected account connection**

1. Open the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing/home#/paymentpreferences).

1. In the navigation pane, choose **Payment preferences**.

1. On the **Connected accounts** tab, choose **Add connected account**. Individual Stripe accounts aren't supported.

1. For **Connected account name**, enter a name to identify the account in AWS. You can't change the name later. Use 1 to 64 characters. Start with a letter or number, and use only letters, numbers, hyphens, and underscores. For example, enter `my-connected-account-1`.

1. (Optional) Add tags to organize connected accounts and to specify IAM permissions.

1. In the **Add connected account** dialog box, choose **Continue**.<a name="connected-accounts-completing-authorization"></a>

**To complete connected account authorization**

1. When AWS opens the Stripe sign-in page, sign in to your Stripe account.

1. Review the access request. Select an eligible existing Stripe account, or create a company or organization account. Then choose **Connect**.

1. After the page displays **Authorization Complete**, close the tab and return to the AWS Billing and Cost Management console. It can take a few minutes for the account status to change.

1. On the **Connected accounts** tab, verify that the **Account status** column shows **Active** and the **Crypto settlement** column shows **Enabled**.

## Checking account status and crypto settlement capability
<a name="connected-account-status-and-crypto-settlement"></a>

**Account status** shows whether your Stripe account is linked to AWS. **Active** means that the connection succeeded. If the status is **Pending** or **Inactive**, select the account, choose **Actions**, and then choose **Resume linking**. An inactive connected account can only be relinked to the Stripe account it was previously linked to.

**Crypto settlement** shows the status of the crypto configuration in Stripe. **Enabled** means that the account is ready for crypto settlement. **Action required** means that the configuration in Stripe needs attention. If you see **Crypto settlement: Action required**, open the Stripe Dashboard and resolve pending requirements, such as business verification. Then follow Stripe's instructions to [enable stablecoin payments](https://docs.stripe.com/payments/accept-stablecoin-payments).

## Troubleshooting connected accounts
<a name="connected-accounts-troubleshooting"></a>

### I can't select my Stripe account
<a name="connected-accounts-cant-select-stripe-account"></a>

**Common cause:** Individual Stripe accounts aren't supported.

**Resolution:** Select or create a Stripe account registered to a company or other organization.

### Stripe displays a conflict when I connect an account
<a name="connected-accounts-stripe-conflict"></a>

**Common cause:** A Stripe account can be linked to only one connected account.

**Resolution:** Use a Stripe account that isn't already linked to another connected account.

### My connected account is active, but crypto settlement requires action
<a name="connected-accounts-crypto-settlement-action-required"></a>

**Common cause:** The AWS connection is complete, but the crypto configuration in Stripe isn't ready.

**Resolution:** Resolve the pending configuration in the Stripe Dashboard, then complete the stablecoin setup steps in [Accept stablecoin payments](https://docs.stripe.com/payments/accept-stablecoin-payments).

## Next steps
<a name="connected-accounts-next-steps"></a>

After your connected account is active and crypto settlement is enabled, configure it for your AWS WAF web ACL. For instructions, see [Getting started with AI traffic monetization](https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-traffic-monetization-getting-started.html).