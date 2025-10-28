**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Data protection exceptions

When enabled, data protection will apply to the fields it is enabled on, including `RuleMatchDetails` and `rateBasedRuleList`. However, there are instances when you may want to include the protected data and content in `RuleMatchDetails` and `rateBasedRuleList` for troubleshooting and visibility purposes. In these scenarios, you can specify exceptions to the data protection for that field.

- **`ExcludeRuleMatchDetails`**: If you specify this exception for a specific field, `RuleMatchDetails` will show the value of the field and won't be in scope for data protection.
- **`ExcludeRateBasedDetails`**: If you specify this exception for a specific field, `rateBasedRuleList` will show the value of the field and won't be in scope for data protection.

Example: The `ExcludeRateBasedDetails` rule is enabled on **SINGLE_HEADER** and **HEADER_NAME** for "dogname".

If an exception is not applied to the rule, the value for "dogname" will appear as `REDACTED`.

```
"rateBasedRuleList":[ {"rateBasedRuleId": ...,
                        "rateBasedRuleName":"RateBasedRule", "limitKey":"CUSTOMKEYS",
                        "maxRateAllowed":100, "evaluationWindowSec":"120", "customValues":[
                        {"key":"HEADER", "name":"dogname", "value":"REDACTED" } ] } ]
```

If an exception is enabled on the rule, the "dogname" value will appear in the log.

```
 "rateBasedRuleList":[ {"rateBasedRuleId": ...,
                        "rateBasedRuleName":"RateBasedRule", "limitKey":"CUSTOMKEYS",
                        "maxRateAllowed":100, "evaluationWindowSec":"120", "customValues":[
                        {"key":"HEADER", "name":"dogname", "value":"ELLA" } ] } ]
```

###### Warning

The data protection feature may potentially affect troubleshooting AWS WAF capabilities. These settings can cause unexpected detection and mitigation behaviors. Limit data protection for specific parameters to only those that are absolutely necessary.
