

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# How AI traffic monetization works
<a name="waf-ai-traffic-monetization-how-it-works"></a>

AI traffic monetization uses the [x402](https://docs.x402.org/introduction) open protocol for machine-to-machine payments. The following describes the request lifecycle for a monetized resource:

1. **Request** – A client (typically an AI agent) sends a request to a AWS WAF protected resource on your CloudFront distribution.

1. **Rule evaluation** – AWS WAF evaluates the request against your rules in priority order. If a rule with a Monetize action matches and the request does not include a valid payment authorization, AWS WAF returns an HTTP 402 Payment Required response. For more details, see [Rule actions](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-rule-actions.html).

1. **Payment Required Challenge** – AWS WAF returns an HTTP 402 response (the "Payment Required Challenge"). The response includes payment instructions containing:

   1. Content price (per request) in USDC

   1. Accepted payment networks (Base, Solana)

   1. Publisher wallet address (payTo)

   1. Maximum timeout

   1. Payment scheme

1. **Payment authorization** – The client signs a payment authorization using their wallet's private key or a server wallet API. The client resubmits the original request with a `payment-signature` header containing the signed authorization.

1. **Verification** – AWS WAF verifies the payment credentials, confirming transfer of sufficient funds and valid authorization. This occurs synchronously in the request path. If the verification fails, the client is served a 402 and the content is not served.

1. **Content fetch** – On successful verification, the request for content is allowed.

1. **Settlement** – If content fetch is successful (2xx status code), the payment is settled on the blockchain via Coinbase Developer Platform's x402 facilitator service. Settlement occurs synchronously – content is served after confirmed payment. If the payment settlement fails, the client is served a 402 and the content is not served.

1. **Response** – The content is served to the client with a `payment-response` header containing settlement confirmation details.

Key behaviors:
+ **No payment for failed origins** – If origin returns 4xx or 5xx, settlement is skipped and the client is not charged.
+ **Idempotency** – The x402 protocol supports a [payment-identifier extension](https://github.com/coinbase/x402/blob/main/specs/extensions/payment_identifier.md) that allows clients to retry requests without double-payment for up to 15 minutes, as long as the extension is used by the client.
+ **Replay protection** – Payment authorizations are single-use. Reusing a payment header without a valid payment-identifier results in a new 402 response.

For more details about the x402 open payment protocol, see [x402 documentation](https://docs.x402.org/introduction).

## Supported resource types
<a name="waf-ai-traffic-monetization-supported-resources"></a>

AI traffic monetization protects resources on Amazon CloudFront distributions. You can monetize any path or content zone served through CloudFront, including:
+ Web pages and articles
+ API endpoints
+ Data feeds
+ Media assets
+ Structured datasets