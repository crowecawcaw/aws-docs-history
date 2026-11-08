

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Payment networks and settlement
<a name="waf-ai-traffic-monetization-payment"></a>

You choose how to receive payments in your MonetizationConfig. You have two settlement options: settle to your own crypto wallet addresses that you configure with `CryptoConfig`, or settle through a connected account with a third-party payment provider (such as Stripe) that you configure with `ConnectedAccountConfigs`. In either case, AWS is not a party to or in the flow of funds for any payment you receive. With self-managed wallets, payments settle directly to the wallet addresses you configure. With a connected account, per-network deposit addresses are provisioned on your behalf and you don't manage wallet addresses yourself.

## How settlement works
<a name="waf-ai-traffic-monetization-settlement"></a>

1. The client's payment authorization is verified before content is fetched from origin.

1. After origin returns a successful response, the payment is settled on the blockchain.

1. USDC is transferred from the client's wallet to your configured wallet address for self-managed wallets, or to the deposit address provisioned for your connected account.

1. Settlement confirmation is included in the response to the client.

Payment settlement is provided to you by Coinbase Developer Platform's x402 facilitator. You agree to Coinbase's [terms of service](https://www.coinbase.com/en-gb/legal/developer-platform/terms-of-service). You instruct us to share pricing and payment configuration information with Coinbase and the relevant client.

To open a Stripe Connected account, you must agree to the [Stripe Connected Account Agreement on the Stripe website](https://stripe.com/en-ca/legal/connect-account).