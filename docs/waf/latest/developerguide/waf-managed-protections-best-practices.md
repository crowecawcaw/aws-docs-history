**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Best practices for intelligent

threat mitigation in AWS WAF

Follow the best practices in this section for the most efficient, cost-effective
implementation of the intelligent threat mitigation features.

- **Implement the JavaScript and mobile application integration
  SDKs** – Implement application integration to enable the
  full set of ACFP, ATP, or Bot Control functionality in the most effective
  way possible. The managed rule groups use the tokens provided by the SDKs to
  separate legitimate client traffic from unwanted traffic at the session level.
  The application integration SDKs ensure that these tokens are always available.
  For details, see the following:

      + [Using application integration SDKs with ACFP](waf-acfp-with-tokens.md "waf-acfp-with-tokens.md")
      + [Using application integration SDKs with ATP](waf-atp-with-tokens.md "waf-atp-with-tokens.md")
      + [Using application integration SDKs with Bot Control](waf-bot-with-tokens.md "waf-bot-with-tokens.md")

  Use the integrations to implement challenges in your client and, for JavaScript, to
  customize how CAPTCHA puzzles are presented to your end users. For details,
  see [Client application
  integrations in AWS WAF](waf-application-integration.md "waf-application-integration.md").

If you customize CAPTCHA puzzles using the JavaScript API and you use the
CAPTCHA rule action anywhere in your protection pack (web ACL), follow the guidance for
handling the AWS WAF CAPTCHA response in your client at [Handling a CAPTCHA
response from AWS WAF](waf-js-captcha-api-conditional.md "waf-js-captcha-api-conditional.md"). This guidance applies to
any rules that use the CAPTCHA action, including those in the ACFP managed
rule group and the targeted protection level of the Bot Control managed rule group.

- **Limit the requests that you send to the ACFP, ATP, and
  Bot Control rule groups** – You incur additional fees for using
  the intelligent threat mitigation AWS Managed Rules rule groups. The ACFP rule group
  inspects requests to the account registration and creation endpoints that you
  specify. The ATP rule group inspects requests to the login endpoint that
  you specify. The Bot Control rule group inspects every
  request that reaches it in the protection pack (web ACL) evaluation.

Consider the following approaches to reduce your use of these rule groups:

    + Exclude requests from inspection with a scope-down statement in the
     managed rule group statement. You can do this with any nestable
     statement. For information, see [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md "waf-rule-scope-down-statements.md").
    + Exclude requests from inspection by adding rules before the rule group. For rules that
     you can't use in a scope-down statement and for more complex situations,
     such as labeling followed by label matching, you might want to add rules
     that run before the rule groups. For information, see [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md "waf-rule-scope-down-statements.md") and [Using rule statements in AWS WAF](waf-rule-statements.md "waf-rule-statements.md").
    + Run the rule groups after less expensive rules. If you have other
     standard AWS WAF rules that block requests for any reason, run them before
     these paid rule groups. For more information about rules and rule
     management, see [Using rule statements in AWS WAF](waf-rule-statements.md "waf-rule-statements.md").
    + If you're using more than one of the intelligent threat mitigation managed rule groups, run them in the following order to keep costs down: Bot Control, ATP, ACFP.

For detailed pricing information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

- **Do not limit the requests that you send to the Anti-DDoS rule group** – This rule group operates best when you configure it in to monitor all web traffic that you
  aren't explicitly allowing through. Position it in your web ACL to be evaluated
  only after rules with the Allow rule action and before all other rules.
- **For distributed denial of service (DDoS) protection, use either
  Anti-DDoS or Shield Advanced automatic application layer DDoS mitigation** –
  The other intelligent threat mitigation rule groups don't provide DDoS protection. ACFP protects
  against fraudulent account creation attempts to your application's sign-up page. ATP protects
  against account takeover attempts to your login page. Bot Control focuses on enforcing
  human-like access patterns using tokens and dynamic rate limiting on client
  sessions.

Anti-DDoS allows you to monitor and control DDoS attacks, allowing for quick response and mitigation of threats. Shield Advanced with automatic application layer DDoS mitigation automatically responds to detected DDoS attacks by creating, evaluating, and
deploying custom AWS WAF mitigations on your behalf.

For more information about
Shield Advanced, see [AWS Shield Advanced overview](ddos-advanced-summary.md "ddos-advanced-summary.md"), and [Protecting the application layer (layer 7) with AWS Shield Advanced and AWS WAF](ddos-app-layer-protections.md "ddos-app-layer-protections.md").

For more information about Distributed Denial of Service (DDoS) prevention, see [Anti-DDoS rule group](aws-managed-rule-groups-anti-ddos.md "aws-managed-rule-groups-anti-ddos.md") and [Distributed Denial of Service (DDoS) prevention](waf-anti-ddos.md "waf-anti-ddos.md").

- **Enable the Anti-DDoS rule group and the targeted protection level of the
  Bot Control rule group during normal web traffic** –
  These rule categories need time to establish baselines for normal traffic.

**Enable the targeted protection level of the Bot Control rule group during normal web traffic** –
Some rules of the targeted protection level need time to establish baselines for normal traffic patterns before they can recognize
and respond to irregular or malicious traffic patterns. For example, the `TGT_ML_*` rules need up to 24 hours to warm up.

Add these protections when you are not experiencing an attack and give them time to establish their baselines
before expecting them to respond appropriately. If you add these
rules during an attack, you will need to enable the Anti-DDoS rule group in count mode. After the attack subsides, the time to establish a
baseline is usually from double to triple the normal required time, because of the
skewing added by the attack traffic. For additional information about the rules and any
warm-up times that they require, see
[Rules listing](aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-rules "aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-rules").

- **For distributed denial of service (DDoS) protection, use
  Shield Advanced automatic application layer DDoS mitigation** – The intelligent
  threat mitigation rule groups don't provide DDoS protection. ACFP protects
  against fraudulent account creation attempts to your application's sign-up page. ATP protects
  against account takeover attempts to your login page. Bot Control focuses on enforcing
  human-like access patterns using tokens and dynamic rate limiting on client
  sessions.

When you use Shield Advanced with automatic application layer DDoS mitigation enabled, Shield Advanced
automatically responds to detected DDoS attacks by creating, evaluating, and
deploying custom AWS WAF mitigations on your behalf. For more information about
Shield Advanced, see [AWS Shield Advanced overview](ddos-advanced-summary.md "ddos-advanced-summary.md"), and [Protecting the application layer (layer 7) with AWS Shield Advanced and AWS WAF](ddos-app-layer-protections.md "ddos-app-layer-protections.md").

- **Use production traffic loads when you establish baselines for the Anti-DDoS rule group** – It is common practice to test other rule groups using artificial test traffic. However, when you test and establish baselines for the Anti-DDoS rule group, we recommend that you use traffic flows that reflect the loads in your production environment. Establishing Anti-DDoS baselines using typical traffic is the best way to ensure your resources will be protected when the rule group is enabled in a production environment.
- **Tune and configure token handling** – Adjust
  the protection pack (web ACL)'s token handling for the best user experience.
  - To reduce operating costs and improve your end user's experience,
    tune your token management immunity times to the longest that your
    security requirements permit. This keeps the use of CAPTCHA puzzles and
    silent challenges to a minimum. For information, see [Setting timestamp expiration and token immunity times in AWS WAF](waf-tokens-immunity-times.md "waf-tokens-immunity-times.md").
  - To enable token sharing between protected applications, configure a
    token domain list for your protection pack (web ACL). For information, see [Specifying token domains and domain lists in AWS WAF](waf-tokens-domains.md "waf-tokens-domains.md").

- **Reject requests with arbitrary host
  specifications** – Configure your protected resources to
  require that the `Host` headers in web requests match the targeted
  resource. You can accept one value or a specific set of values, for example
  `myExampleHost.com` and `www.myExampleHost.com`, but
  don’t accept arbitrary values for the host.
- **For Application Load Balancers that are origins for CloudFront distributions,
  configure CloudFront and AWS WAF for proper token handling** – If
  you associate your protection pack (web ACL) to an Application Load Balancer and you deploy the Application Load Balancer as the origin
  for a CloudFront distribution, see [Required configuration for Application Load Balancers that are CloudFront origins](waf-tokens-with-alb-and-cf.md "waf-tokens-with-alb-and-cf.md").
- **Test and tune before deploying** –
  Before you implement any changes to your protection pack (web ACL), follow the testing and tuning
  procedures in this guide to be sure that you're getting the behavior you expect.
  This is especially important for these paid features. For general guidance, see
  [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md"). For
  information specific to the paid managed rule groups, see [Testing and deploying ACFP](waf-acfp-deploying.md "waf-acfp-deploying.md"), [Testing and deploying ATP](waf-atp-deploying.md "waf-atp-deploying.md"), and [Testing and deploying AWS WAF Bot Control](waf-bot-control-deploying.md "waf-bot-control-deploying.md").
