

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Pricing configuration
<a name="waf-ai-traffic-monetization-pricing"></a>

## Base price
<a name="waf-ai-traffic-monetization-base-price"></a>

Set a base price per request in the MonetizationConfig. The price is specified as a decimal USD string with up to 3 decimal places. The minimum price per request is $0.001 USDC.

## Price multipliers
<a name="waf-ai-traffic-monetization-price-multipliers"></a>

Use the `PriceMultiplier` parameter on individual Monetize rule actions to adjust pricing per rule. The effective price is the base price multiplied by this value.

For example, if your base price is `"0.001"` ($0.001) and a rule has PriceMultiplier `"3"`, the effective price for requests matching that rule is $0.003.

## Configuring pricing by intent
<a name="waf-ai-traffic-monetization-pricing-intent"></a>

You can set different prices for each verification tier. Common patterns include:
+ Lower prices for verified AI search crawlers that drive referral traffic
+ Standard prices for known agents performing RAG or summarization
+ Higher prices for unknown or unverified agents
+ Blocking training crawlers entirely or pricing at a premium

**Important**  
To implement your AI traffic monetization policies, we use multiple detection techniques such as behavioral signals and risk-based systems to inspect and categorize inbound traffic. While these methods are designed to provide high-confidence classification, they are probabilistic and might not correctly identify or categorize all bot traffic in all cases. We continuously test and update our analysis methods to increase accuracy. We recommend using Test mode to validate that your policies produce the expected results before enabling live monetization.

## Configuring rule action
<a name="waf-ai-traffic-monetization-rule-action"></a>

For each tier, you can set one of the following actions:
+ **Monetize** – A terminating action. When a rule with the Monetize action matches, AWS WAF stops evaluating subsequent rules. If the request does not include a valid payment authorization, AWS WAF returns an HTTP 402 response directly and the request is blocked.
+ **Allow** – Grant free access (for example, verified search crawlers under a referral agreement).
+ **Block** – Deny access entirely.
+ **Count** – Allow access and log the request without charging.
+ **Captcha** – Requires the end user to solve a CAPTCHA puzzle to prove that a human being is sending the request.
+ **Challenge** – Runs a silent challenge that requires the client session to verify that it's a browser, and not a bot.

## Important: Monetize action and human traffic
<a name="waf-ai-traffic-monetization-human-traffic"></a>

The Monetize action is designed for automated AI agent traffic. When a request matches a Monetize rule, AWS WAF returns an HTTP 402 Payment Required response containing machine-readable payment instructions in the x402 protocol format. Standard web browsers and human users cannot interpret or complete this payment flow – the 402 response will effectively block access for non-automated clients.

To avoid inadvertently blocking human visitors, use the Monetize action only on traffic that has been identified as automated. We recommend combining the Monetize action with AWS WAF Bot Control labels so that only bot traffic receives the 402 challenge, while human users continue to access your content normally.

**Example: Monetize only bot traffic using Bot Control labels**  
The following rule configuration uses Bot Control to classify traffic first, then applies the Monetize action only to requests labeled as bots:

```
{
  "Name": "MonetizeBotTrafficOnly",
  "Priority": 5,
  "Statement": {
    "LabelMatchStatement": {
      "Scope": "LABEL",
      "Key": "awswaf:managed:aws:bot-control:bot"
    }
  },
  "Action": {
    "Monetize": {
    }
  },
  "VisibilityConfig": {
    "CloudWatchMetricsEnabled": true,
    "MetricName": "MonetizeBotTrafficOnly",
    "SampledRequestsEnabled": true
  }
}
```

In this example, requests from human users (which do not carry the `awswaf:managed:aws:bot-control:bot` label) pass through this rule without matching and continue to subsequent rules. Only requests classified as bots by Bot Control receive the 402 Payment Required Challenge.

You can further refine this pattern by creating separate rules for different bot tiers – for example, allowing verified search crawlers for free while monetizing unverified bots at a higher price multiplier.

**Latency characteristics**  
AI traffic monetization adds several seconds of additional latency to requests that require payment processing. This overhead covers payment authorization verification and on-chain settlement. The additional latency applies only to requests where a transaction is being attempted – requests that do not match the Monetize action or requests without a payment signature attached are unaffected.

The exact latency depends on blockchain network conditions at the time of settlement.

## Payment processing errors and throttling
<a name="waf-ai-traffic-monetization-errors-throttling"></a>

Because AI traffic monetization relies on third-party blockchain settlement services, payment processing may occasionally fail for reasons outside of our control. Possible causes include temporary unavailability of the Coinbase Developer Platform's x402 facilitator service, blockchain network congestion, or transient errors during on-chain settlement. When payment processing fails, content is not served to the client. The client receives a response indicating the failure and can retry the request.

Additionally, AWS might throttle excessively high volumes of payment traffic to protect the integrity of the payment processing infrastructure and prevent abuse. If throttled, payment requests receive an error response and should be retried after a brief backoff. Normal request volumes are not affected by throttling.