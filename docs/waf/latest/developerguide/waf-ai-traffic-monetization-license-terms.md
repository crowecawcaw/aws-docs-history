

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Communicating license terms to AI agents
<a name="waf-ai-traffic-monetization-license-terms"></a>

AI traffic monetization tells agents how much to pay but not what they're allowed to do with the content. To communicate machine-readable usage terms, you can use RSL (Really Simple Licensing) – an open standard for machine-readable content licensing.

RSL defines several discovery mechanisms for AI agents to find your license terms:
+ **robots.txt** – Add RSL directives to your existing robots.txt file. Agents discover terms during their standard crawl preflight.
+ **HTTP Link header** – Inject a `Link` header referencing your RSL license URL into HTTP responses. Can be configured with CloudFront (see below).
+ **HTML link element** – Embed a `<link rel="license">` tag in your HTML pages. Suitable for web content but not applicable to API or non-HTML responses.
+ **RSS/Atom module** – Attach licensing metadata to feed entries.

**Using CloudFront Response Header Policies for RSL**  
For HTTP `Link` header discovery, you can configure CloudFront to inject the RSL license reference into responses:

1. Create an RSL license XML file describing your usage terms and host it at a stable HTTPS URL (for example, `https://example.com/license.xml`). You can use a standard license from the [RSL Collective](https://rslstandard.org/rsl) or define custom terms.

1. Create a CloudFront Response Header Policy with a custom header:
   + Header name: `Link`
   + Value: `<https://example.com/license.xml>; rel="license"; type="application/rsl+xml"`

1. Associate this policy with the cache behaviors serving monetized content.

AI agents that support RSL will discover your terms automatically on every origin response.

**Note**  
CloudFront Response Header Policies apply to responses served from origin. The 402 Payment Required Challenge served by the Monetize action will not include this header.

For more information on response header policies, see [Adding HTTP response headers with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/adding-response-headers.html) in the *Amazon CloudFront Developer Guide*.

For the RSL specification, see [https://rslstandard.org/rsl](https://rslstandard.org/rsl).