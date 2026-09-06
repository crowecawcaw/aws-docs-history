

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Options for intelligent threat mitigation managed rule groups
<a name="waf-managed-protections-comparison-table-rg"></a>

This section compares managed rule group options.

The intelligent threat mitigation AWS Managed Rules rule groups provide management of basic bots, detection and mitigation of sophisticated, malicious bots, detection and mitigation of account takeover attempts, and detection and mitigation of fraudulent account creation attempts. These rule groups, combined with the application integration SDKs described in the prior section, provide the most advanced protections and secure coupling with your client applications. 


**Comparison of the managed rules group options**  

|  | ACFP  | ATP  | Bot Control common level | Bot Control targeted level | 
| --- | --- | --- | --- | --- | 
| What it is | Manages requests that might be part of fraudulent account creation attempts on an application's registration and sign-up pages.Does not manage bots. <br />See [AWS WAF Fraud Control account creation fraud prevention (ACFP) rule group](aws-managed-rule-groups-acfp.md). | Manages requests that might be part of malicious takeover attempts on an application's login page.Does not manage bots. <br />See [AWS WAF Fraud Control account takeover prevention (ATP) rule group](aws-managed-rule-groups-atp.md). | Manages common bots that self-identify, with signatures that are unique across applications.See [AWS WAF Bot Control rule group](aws-managed-rule-groups-bot.md). | Manages targeted bots that don't self-identify, with signatures that are specific to an application.See [AWS WAF Bot Control rule group](aws-managed-rule-groups-bot.md). | 
| Good choice for... | Inspection of account creation traffic for fraudulent account creation attacks such creation attempts with username traversal and many new accounts created from a single IP address. | Inspection of login traffic for account takeover attacks such login attempts with password traversal and many login attempts from the same IP address. When used with tokens, also provides aggregate protections such as rate limiting of IPs and client sessions for high volumes of failed login attempts. | Basic bot protection and labeling of common, automated bot traffic. | Targeted protection against sophisticated bots, including rate limiting at the client session level and detection and mitigation of browser automation tools such as Selenium and Puppeteer.  | 
| Adds labels that indicate evaluation results | Yes | Yes | Yes | Yes | 
| Adds token labels | Yes | Yes | Yes | Yes | 
| Blocking for requests that don't have a valid token | Not included. See [Blocking requests that don't have a valid AWS WAF token](waf-tokens-block-missing-tokens.md). | Not included. See [Blocking requests that don't have a valid AWS WAF token](waf-tokens-block-missing-tokens.md). | Not included. See [Blocking requests that don't have a valid AWS WAF token](waf-tokens-block-missing-tokens.md). | Blocks client sessions that send 5 requests without a token. | 
| Requires the AWS WAF token aws-waf-token | Required for all rules.See [Using application integration SDKs with ACFP](waf-acfp-with-tokens.md). | Required for many rules.See [Using application integration SDKs with ATP](waf-atp-with-tokens.md). | No | Yes | 
| Acquires the AWS WAF token aws-waf-token | Yes, enforced by the rule AllRequests | No | No | Some rules use Challenge or CAPTCHA rule actions, which acquire tokens. | 

For details about costs associated with these options, see the intelligent threat mitigation information at [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).

If your application faces bots that rotate IP addresses and mimic browser behavior, the common protection level alone won't detect them. These bots don't self-identify and require the behavioral analysis and machine learning that targeted protection provides. For guidance on choosing the right protection level for your specific application, see [Choosing and configuring Bot Control for your use case](waf-bot-control-use-cases.md).