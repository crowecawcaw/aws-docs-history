

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Getting started with AI traffic monetization
<a name="waf-ai-traffic-monetization-getting-started"></a>

## Prerequisites
<a name="waf-ai-traffic-monetization-prerequisites"></a>
+ An AWS WAF protection pack (web ACL) associated with an Amazon CloudFront distribution
+ One of the following to receive payments: a [USDC wallet address on Base, Solana, or both](https://www.coinbase.com/developer-platform/wallets), or a connected account with a supported payment provider that is enabled for settlement. To set up a connected account, see [Managing connected accounts](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-connected-accounts.html) in the AWS Billing and Cost Management User Guide.
+ (Recommended) AWS WAF Bot Control enabled to classify AI bot traffic by identity

## Quick start
<a name="waf-ai-traffic-monetization-quick-start"></a>

1. **Create a protection pack (webACL)** – In the AWS WAF console, navigate to Protection packs (webACL) and [create a new pack scoped to CloudFront](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-creating.html) with your pricing, bot and agent policies, and payment configuration. AI traffic monetization requires a web ACL with CloudFront (global) scope. [Associate with a CloudFront distribution](https://docs.aws.amazon.com/waf/latest/developerguide/cloudfront-features.html).

1. **Enable Bot Control** – If not already enabled, [add the AWS WAF Bot Control managed rule group to your web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/waf-using-managed-rule-group.html).

1. **Configure MonetizationConfig** – To use AI traffic monetization, you configure a `MonetizationConfig` on your web ACL. This configuration defines the payment networks you accept and the base price for monetized requests.

The MonetizationConfig contains:
+ **CurrencyMode** – `REAL` for production payments or `TEST` for test network payments. `TEST` is supported only with `CryptoConfig` (self-managed wallets); it is not supported with a connected account configuration.
+ **CryptoConfig** – Payment network configuration including chains, wallet addresses, and pricing.
+ **ConnectedAccountConfigs** – Configuration for settling payments through a connected account with a third-party payment provider (such as Stripe), as an alternative to managing your own wallet addresses. You reference the connected account by its ARN and set per-network pricing.

## MonetizationConfig structure
<a name="waf-ai-traffic-monetization-config-structure"></a>

```
{
  "MonetizationConfig": {
    "CryptoConfig": {
      "PaymentNetworks": [
        {
          "Chain": "BASE",
          "WalletAddress": "0x1234567890abcdef1234567890abcdef12345678",
          "Prices": [
            {
              "Amount": "0.001",
              "Currency": "USDC"
            }
          ]
        },
        {
          "Chain": "SOLANA",
          "WalletAddress": "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
          "Prices": [
            {
              "Amount": "0.001",
              "Currency": "USDC"
            }
          ]
        }
      ]
    }
  }
}
```

**Important**  
The `Amount` is specified in USDC as a decimal string with up to 3 decimal places (for example, `"0.001"` = $0.001 USDC per request).

A MonetizationConfig can also contain a `ConnectedAccountConfigs` entry, either on its own or alongside `CryptoConfig`. When you combine the two, a given chain (BASE or SOLANA) can be used by only one of them. The following example settles BASE payments to a self-managed wallet and SOLANA payments through a connected account:

```
{
  "MonetizationConfig": {
    "CryptoConfig": {
      "PaymentNetworks": [
        {
          "Chain": "BASE",
          "WalletAddress": "0x1234567890abcdef1234567890abcdef12345678",
          "Prices": [
            {
              "Amount": "0.001",
              "Currency": "USDC"
            }
          ]
        }
      ]
    },
    "ConnectedAccountConfigs": [
      {
        "ConnectedAccountArn": "arn:aws:payments::123456789012:connectedaccount/my-account-aB3d47",
        "PaymentNetworks": [
          {
            "Chain": "SOLANA",
            "Prices": [
              {
                "Amount": "0.01",
                "Currency": "USDC"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

## Settling payments with a connected account
<a name="waf-ai-traffic-monetization-connected-account"></a>

In addition to managing your own crypto wallet addresses, you can also settle payments through a connected account with a supported third-party payment provider (Stripe). A connected account is an account that you set up with a supported payment provider and reference in your MonetizationConfig by its ARN. When you use a connected account, the per-network deposit addresses are provisioned and managed on your behalf, so you don't configure or maintain wallet addresses yourself. You can set a `MonetizationConfig`, including a `ConnectedAccountConfigs` entry, on a web ACL or a rule group; the requirements and validation described in this section apply to both. Connected accounts are available only in the commercial AWS partition. In other partitions, the request fails with `WAFInvalidParameterException`.

You create and manage connected accounts in the AWS Billing and Cost Management console, under **Payment preferences**, **Connected accounts**. For the full setup procedure, see [Managing connected accounts](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-connected-accounts.html) in the AWS Billing and Cost Management User Guide.

This differs from self-managed wallets, where you provide a wallet address for each payment network in your `CryptoConfig` and payments settle directly to those addresses.

**Prerequisites**  
To settle payments with a connected account, you need the following:
+ An active connected account with a supported payment provider (Stripe) that is enabled for payment settlement.
+ Permission to use that connected account. The IAM permissions for creating and managing connected accounts are on the billing side; for those actions, see [Managing connected accounts](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-connected-accounts.html) in the AWS Billing and Cost Management User Guide. To reference a connected account in a web ACL or rule group, you need the `payments:GetConnectedAccount` permission on the connected account ARN. If you don't have this permission, the request fails with `AccessDeniedException`.
+ The ARN of the connected account. You create the connected account and obtain its ARN in the AWS Billing and Cost Management console, under **Payment preferences**, **Connected accounts** – not from the payment provider directly. The ARN has the format `arn:aws:payments::<account-id>:connectedaccount/<name>-<id>`.

To use a connected account, configure `ConnectedAccountConfigs` in your MonetizationConfig. Reference your connected account by its ARN and set per-network pricing for each chain you accept. The following example shows a MonetizationConfig that settles payments through a connected account:

```
{
  "MonetizationConfig": {
    "ConnectedAccountConfigs": [
      {
        "ConnectedAccountArn": "arn:aws:payments::123456789012:connectedaccount/my-account-aB3d47",
        "PaymentNetworks": [
          {
            "Chain": "BASE",
            "Prices": [
              {
                "Amount": "0.01",
                "Currency": "USDC"
              }
            ]
          },
          {
            "Chain": "SOLANA",
            "Prices": [
              {
                "Amount": "0.01",
                "Currency": "USDC"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

**Note**  
Unlike a `CryptoConfig` entry, a `ConnectedAccountConfigs` entry does not include a `WalletAddress`. The deposit addresses for each payment network are provisioned for your connected account.

The following rules apply when you use a connected account:

**Important**  
`CurrencyMode` `TEST` is not supported with a connected account configuration.
+ Connected accounts support production settlement only.
+ The supported chains are BASE and SOLANA.
+ Prices for a connected account range from `0.01` to `999999.99` USDC, with up to 2 decimal places. Sub-cent amounts are not supported. This differs from self-managed wallets, which support amounts as small as 0.001 USDC.
+ You can configure one connected account.
+ You can use `CryptoConfig` and `ConnectedAccountConfigs` together on the same web ACL. However, a given chain (BASE or SOLANA) can be used by only one of them, not both.
+ AWS WAF validates the connected account on every web ACL or rule group create or update request that references it, not only when you change the connected account configuration. The account is usable only when both its account status is **Active** and its crypto settlement capability is **Enabled**. If validation fails, AWS WAF rejects the request with one of the following errors:
  + Account or crypto settlement capability not active – `WAFInvalidOperationException`
  + The ARN no longer exists because the account was deleted and recreated – `WAFNonexistentItemException`
  + You don't have the `payments:GetConnectedAccount` permission – `AccessDeniedException`
  + Invalid ARN or unsupported partition – `WAFInvalidParameterException`

  The rejection error is actionable – it tells you to reconnect the account, or to enable crypto settlement for it.
+ Before you create or update a web ACL or rule group that references a connected account, verify in the AWS Billing and Cost Management console, under **Payment preferences**, **Connected accounts**, that **Account status** is **Active** and **Crypto settlement** is **Enabled**. If the status is `Pending` or `Inactive`, choose **Actions**, **Resume linking** to reactivate it; if crypto settlement needs attention, resolve it with your payment provider (for Stripe, in the Stripe Dashboard). For details, see the "Checking account status and crypto settlement capability" guidance in [Managing connected accounts](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-connected-accounts.html).

## Supported payment networks
<a name="waf-ai-traffic-monetization-supported-networks"></a>


| Chain | Network | Currency | Use Case | Connected account support | 
| --- | --- | --- | --- | --- | 
| BASE | Base mainnet (EVM L2) | USDC | Production Payments | Yes | 
| SOLANA | Solana mainnet | USDC | Production Payments | Yes | 
| BASE\_SEPOLIA | Base Sepolia testnet | USDC | Test Mode | No | 
| SOLANA\_DEVNET | Solana Devnet | USDC | Test Mode | No | 

## Test mode
<a name="waf-ai-traffic-monetization-test-mode"></a>

Test mode (`CurrencyMode: TEST`) enables you to validate your monetization configuration using test blockchain networks before going live with real payments. This configuration is applied to the entire protection pack (web ACL) (web ACL).

**Important**  
To implement your AI traffic monetization policies, we use multiple detection techniques such as behavioral signals and risk-based systems to inspect and categorize inbound traffic. While these methods are designed to provide high-confidence classification, they are probabilistic and might not correctly identify or categorize all bot traffic in all cases. We continuously test and update our analysis methods to increase accuracy. We recommend using Test mode to validate that your policies produce the expected results before enabling live monetization.

### Enabling test mode
<a name="waf-ai-traffic-monetization-enabling-test-mode"></a>

Set `CurrencyMode` to `TEST` in your MonetizationConfig and configure test network chains.

**Note**  
Test mode is supported only with `CryptoConfig` (self-managed wallets). Connected account configurations do not support `TEST` mode; they support production settlement only.

### Test mode behavior
<a name="waf-ai-traffic-monetization-test-behavior"></a>

In test mode:
+ Payments use test networks: **Base Sepolia** and **Solana Devnet**
+ You use test funds such as [Testnet Faucet](https://faucet.circle.com/) (available from public faucets) instead of real USDC
+ The full payment flow executes identically to production – verification, origin fetch, and settlement all occur on the test blockchain
+ All events are logged with `CurrencyMode: TEST`
+ Revenue analytics are queryable with the `CurrencyMode: ["TEST"]` filter

**Important**  
Use test mode only on non-production traffic for internal validation before enforcing monetization policies in production.

### Validating configuration
<a name="waf-ai-traffic-monetization-validating-config"></a>

Use test mode to verify:
+ Correct pricing for different rules and content paths
+ Payment flow end-to-end (402 → payment authorization → verification → settlement)
+ Wallet address correctness (funds arrive in your test wallet)
+ Analytics and log fields are populated correctly

When satisfied, update your MonetizationConfig to `CurrencyMode: REAL` and configure production chains (BASE, SOLANA) to begin processing real payments.
+ You can start with `CurrencyMode: TEST` for initial testing, or directly start monetizing using `CurrencyMode: REAL`.
+ **Add Monetize rules** – Create rules with the Monetize action. Use match statements to target specific paths, Bot Control labels, or other request characteristics.
+ **Test** – Send test requests to your CloudFront distribution. Requests matching your Monetize rules will receive Payment Required Challenges (402 responses). Use a compatible payment client to complete the flow.
+ **Go live** – Update `CurrencyMode` to `REAL` and configure production payment networks (BASE, SOLANA). Fund a test wallet and verify end-to-end before opening to production traffic.

## Next steps
<a name="waf-ai-traffic-monetization-next-steps"></a>
+ Review the AI traffic analysis dashboard to understand your current bot traffic before setting prices.
+ Configure differentiated pricing based on agent tier and content path.
+ Set up revenue analytics to monitor earnings.