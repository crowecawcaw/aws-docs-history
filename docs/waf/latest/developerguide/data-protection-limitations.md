**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Data protection limitations

The following are limitations to consider when using data protection.

## QueryString and SingleQueryArg

**QueryString Protection**

- Data protection on `QueryString` applies to all query arguments, substituting/hashing both keys and values according to the specified settings.

**QueryString in `RuleMatch` details and `RateBased` rule lists**

- If data protection is applied to a single-query argument, then the entire query string will be substituted/hashed in the `RuleMatchDetails` and `RateBasedRule` section in full logs.
- If different protection methods are specified (substitution and hashing) in multiple single-query arguments, the stricter method, substitution, will be applied to the entire query string in the `RuleMatchDetails` and `RateBasedRule` section in full logs.

## Cookies

###### Note

Data protection is only applied to the values of the cookie when the single header cookie is protected.

**Single cookie in `RuleMatchDetails` and `RateBasedRule` lists**

- If data protection is applied to a single cookie, then the entire cookie header will be substituted/hashed in the `RuleMatchDetails` and `RateBasedRule` section in full logs.
- If different protection methods are specified (substitution and hashing), the stricter method, substitution, will be applied to the entire cookie in the `RuleMatchDetails` and `RateBasedRule` section in full logs.
