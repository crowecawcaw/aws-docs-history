**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Payment networks and settlement

You choose how to receive payments by configuring wallet addresses in your MonetizationConfig. Payments settle directly to your wallet. AWS is not a party to or in the flow of funds for any payment you receive.

## How settlement works

1. The client's payment authorization is verified before content is fetched from origin.
2. After origin returns a successful response, the payment is settled on the blockchain.
3. USDC is transferred from the client's wallet to your configured wallet address.
4. Settlement confirmation is included in the response to the client.

Payment settlement is provided to you by Coinbase Developer Platform's x402 facilitator. You agree to Coinbase's [terms of service](https://www.coinbase.com/en-gb/legal/developer-platform/terms-of-service "https://www.coinbase.com/en-gb/legal/developer-platform/terms-of-service"). You instruct us to share pricing and payment configuration information with Coinbase and the relevant client.
