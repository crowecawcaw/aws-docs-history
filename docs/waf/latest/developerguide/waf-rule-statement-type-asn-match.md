**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Autonomous System Number (ASN) match rule statement

An ASN match rule statement in AWS WAF allows you to inspect web traffic based on the
Autonomous System Number (ASN) associated with the request's IP address. ASNs are
unique identifiers assigned to large internet networks managed by organizations such
as internet service providers, enterprises, universities, or government agencies. By
using ASN match statements, you can allow or block traffic from specific network
organizations without having to manage individual IP addresses. This approach offers
a more stable and efficient way to control access compared to IP-based rules, as
ASNs change less frequently than IP ranges.

ASN matching is particularly useful for scenarios such as blocking traffic from
known problematic networks or allowing access only from trusted partner networks.
The ASN match statement provides flexibility in determining the client IP address
through optional forwarded IP configuration, making it compatible with various
network setups including those using content delivery networks (CDNs) or reverse
proxies.

###### Note

ASN matching supplements, but doesn't replace, standard authentication and authorization controls.
We recommend that you implement authentication and authorization mechanisms, such as IAM,
to verify the identity of all requests in your applications.

## How the ASN match statement works

AWS WAF determines the ASN of a request based on its IP address. By default, AWS WAF uses the IP address of the web request's origin.
You can configure AWS WAF to use an IP address from an alternate request header,
like `X-Forwarded-For`, by enabling forwarded IP configuration in the rule statement settings.

The ASN match statement compares the request's ASN against the list of ASNs specified in
the rule. If the ASN matches one in the list, the statement evaluates to true,
and the associated rule action is applied.

### Handling unmapped ASNs

If AWS WAF cannot determine an ASN for a valid IP address, it assigns ASN 0. You can include ASN 0 in your rule to handle these cases explicitly.

### Fallback Behavior for Invalid IP Addresses

When you configure the ASN match statement to use forwarded IP addresses, you can specify a fallback behavior of _Match_ or _No match_ for requests with invalid or missing IP addresses in the designated header.

## Rule statement characteristics

**Nestable** – You can nest this statement
type.

**WCUs** – 1 WCU

This statement uses the following settings:

- **ASN list** – An array of ASN numbers to compare for an
  ASN match. Valid values range from 0 to 4294967295. You can specify up
  to 100 ASNs for each rule.
- **(Optional) Forwarded IP configuration** – By default, AWS WAF uses the IP address in the web request origin to determine the ASN. Alternatively, you can configure the rule to use a forwarded IP in an HTTP header like `X-Forwarded-For` instead. You specify whether to use the first, last, or any address in the header. With this configuration, you also specify a fallback behavior to apply to a web request with a malformed IP address in the header. The fallback behavior sets the matching result for the request, to match or no match. For more information, see [Using forwarded IP addresses](waf-rule-statement-forwarded-ip-address.md "waf-rule-statement-forwarded-ip-address.md").

## Where to find this rule statement

- **Rule builder** on the console – For **Request option**, choose **Originates from ASN in**.
- **API** – [AsnMatchStatement](../APIReference/API_AsnMatchStatement.md "../APIReference/API_AsnMatchStatement.md")

## Examples

This example blocks requests originating from two specific ASNs derived from an `X-Forwarded-For` header.
If the IP address in the header is malformed, the configured fallback behavior is `NO_MATCH`.

```
{
  "Action": {
    "Block": {}
  },
  "Name": "AsnMatchStatementRule",
  "Priority": 1,
  "Statement": {
    "AsnMatchStatement": {
      "AsnList": [64496, 64500]
    },
    "ForwardedIPConfig": {
      "FallbackBehavior": "NO_MATCH",
      "HeaderName": "X-Forwarded-For"
    }
  },
  "VisibilityConfig": {
    "CloudWatchMetricsEnabled": true,
    "MetricName": "AsnMatchRuleMetrics",
    "SampledRequestsEnabled": true
  }
},
"VisibilityConfig": {
  "CloudWatchMetricsEnabled": true,
  "MetricName": "WebAclMetrics",
  "SampledRequestsEnabled": true
}
}
```
