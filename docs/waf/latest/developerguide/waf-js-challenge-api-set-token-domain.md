**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Providing domains for use in the

tokens

This section explains how to provide additional domains for tokens.

By default, when AWS WAF creates a token, it uses the host domain of the resource that’s
associated with the protection pack (web ACL). You can provide additional domains for the tokens that
AWS WAF creates for the JavaScript APIs. To do this, configure the global variable
`window.awsWafCookieDomainList`, with one or more token domains.

When AWS WAF creates a token, it uses the most appropriate, shortest domain from among the
combination of the domains in `window.awsWafCookieDomainList` and the
host domain of the resource that’s associated with the protection pack (web ACL).

Example settings:

```
window.awsWafCookieDomainList = ['.aws.amazon.com']
```

```
window.awsWafCookieDomainList = ['.aws.amazon.com', 'abc.aws.amazon.com']
```

You can't use public suffixes in this list. For example, you can't use
`gov.au` or `co.uk` as token domains in the list.

The domains that you specify in this list must be compatible with your other
domains and domain configurations:

- The domains must be ones that AWS WAF will accept, based on the protected
  host domain and the token domain list that's configured for the protection pack (web ACL). For
  more information, see [AWS WAF protection pack (web ACL) token domain list configuration](waf-tokens-domains.md#waf-tokens-domain-lists "waf-tokens-domains.md#waf-tokens-domain-lists").
- If you use the JavaScript CAPTCHA API, at least one domain in your
  CAPTCHA API key must be an exact match for one of the token domains in
  `window.awsWafCookieDomainList` or it must be the apex domain of
  one of those token domains.

For example, for the token domain `mySubdomain.myApex.com`,
the API key `mySubdomain.myApex.com`
is an exact match and the API key `myApex.com` is the apex domain. Either key
matches the token domain.

For more information about the
API keys, see [Managing API keys for the JS CAPTCHA API](waf-js-captcha-api-key.md "waf-js-captcha-api-key.md").
If you use the `AWSManagedRulesACFPRuleSet` managed rule group, you might
configure a domain that matches the one in the account creation path that you provided to
the rule group configuration. For more information about this configuration, see
[Adding the ACFP managed rule group to your web
ACL](waf-acfp-rg-using.md "waf-acfp-rg-using.md").

If you use the `AWSManagedRulesATPRuleSet` managed rule group, you might
configure a domain that matches the one in the login path that you provided to
the rule group configuration. For more information about this configuration, see
[Adding the ATP managed rule group to your protection pack (web ACL)](waf-atp-rg-using.md "waf-atp-rg-using.md").
