

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# AI traffic monetization
<a name="waf-ai-traffic-monetization"></a>

AI traffic monetization enables content and API providers to charge AI bots and agents for access to protected resources directly at the edge. When a client requests a monetized resource, AWS WAF returns an HTTP 402 Payment Required response containing pricing and accepted payment networks. The client submits a signed payment authorization on their payment network of choice, AWS WAF verifies it, fetches the content, integrates with third-party facilitator services for settling the payment on-chain, and serves the response.

AI traffic monetization uses an open payment protocol for machine-to-machine payments. Any compatible client or agent runtime can complete payments.

**Note**  
AI traffic monetization is available globally with Amazon CloudFront at no additional charge beyond standard AWS WAF pricing.

**Topics**
+ [How AI traffic monetization works](waf-ai-traffic-monetization-how-it-works.md)
+ [Getting started with AI traffic monetization](waf-ai-traffic-monetization-getting-started.md)
+ [Pricing configuration](waf-ai-traffic-monetization-pricing.md)
+ [Payment networks and settlement](waf-ai-traffic-monetization-payment.md)
+ [Revenue analytics](waf-ai-traffic-monetization-analytics.md)
+ [Communicating license terms to AI agents](waf-ai-traffic-monetization-license-terms.md)