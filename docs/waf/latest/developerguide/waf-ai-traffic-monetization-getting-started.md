

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Getting started with AI traffic monetization
<a name="waf-ai-traffic-monetization-getting-started"></a>

## Prerequisites
<a name="waf-ai-traffic-monetization-prerequisites"></a>
+ An AWS WAF protection pack (web ACL) associated with an Amazon CloudFront distribution
+ A [USDC wallet address on Base, Solana, or both to receive payments](https://www.coinbase.com/developer-platform/wallets).
+ (Recommended) AWS WAF Bot Control enabled to classify AI bot traffic by identity

## Quick start
<a name="waf-ai-traffic-monetization-quick-start"></a>

1. **Enable Bot Control** – If not already enabled, [add the AWS WAF Bot Control managed rule group to your web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/waf-using-managed-rule-group.html).

1. **Create a protection pack (webACL)** – In the AWS WAF console, navigate to Protection packs (webACL) in the Cloudfront (Global) region, and [create a new pack](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-creating.html) with your pricing, bot and agent policies, and payment configuration. [Associate with a CloudFront distribution](https://docs.aws.amazon.com/waf/latest/developerguide/cloudfront-features.html).

1. **Configure MonetizationConfig** – To use AI traffic monetization, you configure a `MonetizationConfig` on your web ACL. This configuration defines the payment networks you accept and the base price for monetized requests.

The MonetizationConfig contains:
+ **CurrencyMode** – `REAL` for production payments or `TEST` for test network payments.
+ **CryptoConfig** – Payment network configuration including chains, wallet addresses, and pricing.

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

## Supported payment networks
<a name="waf-ai-traffic-monetization-supported-networks"></a>


| Chain | Network | Currency | Use Case | 
| --- | --- | --- | --- | 
| BASE | Base mainnet (EVM L2) | USDC | Production Payments | 
| SOLANA | Solana mainnet | USDC | Production Payments | 
| BASE\_SEPOLIA | Base Sepolia testnet | USDC | Test Mode | 
| SOLANA\_DEVNET | Solana Devnet | USDC | Test Mode | 

## Test mode
<a name="waf-ai-traffic-monetization-test-mode"></a>

Test mode (`CurrencyMode: TEST`) enables you to validate your monetization configuration using test blockchain networks before going live with real payments. This configuration is applied to the entire protection pack (web ACL) (web ACL).

**Important**  
To implement your AI traffic monetization policies, we use multiple detection techniques such as behavioral signals and risk-based systems to inspect and categorize inbound traffic. While these methods are designed to provide high-confidence classification, they are probabilistic and might not correctly identify or categorize all bot traffic in all cases. We continuously test and update our analysis methods to increase accuracy. We recommend using Test mode to validate that your policies produce the expected results before enabling live monetization.

### Enabling test mode
<a name="waf-ai-traffic-monetization-enabling-test-mode"></a>

Set `CurrencyMode` to `TEST` in your MonetizationConfig and configure test network chains.

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