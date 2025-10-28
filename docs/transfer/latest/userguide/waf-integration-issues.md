# Troubleshoot Web Application Firewall integration issues

This section describes possible solutions for issues related to integrating AWS WAF with
Transfer Family.

###### Topics

- [Troubleshoot WAF blocking legitimate
  traffic](#waf-false-positives "#waf-false-positives")
- [Troubleshoot WAF integration with custom identity
  providers](#waf-custom-idp "#waf-custom-idp")

## Troubleshoot WAF blocking legitimate

traffic

Description

After configuring AWS WAF with your Transfer Family endpoint, legitimate users are unable to
connect or experience intermittent connection failures. You may see HTTP 403
(Forbidden) responses in your logs.

Cause

Your AWS WAF rules may be too restrictive or incorrectly configured, causing false
positives that block legitimate traffic. Common causes include:

- IP-based rules that inadvertently block corporate networks or VPNs
- Rate-based rules with thresholds that are too low for your normal traffic
  patterns
- Managed rule groups that are overly aggressive for your use case

Solution

To resolve false positive issues:

1. Enable AWS WAF logging to identify which rules are triggering the blocks.
   For instructions, see [Logging AWS WAF web ACL
   traffic](../../../waf/latest/developerguide/logging.md "../../../waf/latest/developerguide/logging.md").
2. Review your logs to identify patterns in the blocked requests.
3. Adjust your rules by:
   - Adding IP addresses or ranges to an allowlist
   - Increasing rate limits for rate-based rules
   - Setting specific rules to Count mode instead of Block mode to
     monitor without blocking
   - Creating exceptions for specific rules using rule group
     exclusions

4. Test the updated configuration with a representative sample of legitimate
   traffic before fully deploying.

## Troubleshoot WAF integration with custom identity

providers

Description

After configuring AWS WAF with your Transfer Family server that uses a custom identity
provider, authentication fails or users experience intermittent authentication
issues.

Cause

When using a custom identity provider with API Gateway, AWS WAF rules may interfere with
the API calls between Transfer Family and your identity provider. This can happen because AWS WAF
is inspecting and potentially blocking the API traffic based on its rule
sets.

Solution

To resolve issues with AWS WAF and custom identity providers:

- Ensure that your AWS WAF configuration includes exceptions for the API
  Gateway endpoints used by your custom identity provider.
- Add the Transfer Family service principal (transfer.amazonaws.com) to an allowlist in
  your AWS WAF rules.
- If using managed rule groups, review them for rules that might affect API
  authentication flows and consider disabling those specific rules.
- Test your identity provider directly using the
  `TestIdentityProvider` API operation to verify it works
  correctly without AWS WAF interference.
